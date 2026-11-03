#!/usr/bin/env python3
"""Exact finite offline-composition checks. Validation scans are counted separately.
Run from PROJECT_DIR. Uses prior policy enumerator as a non-heap reference.
No Poisson law construction, all-input RSP claim, or independent referee.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter, defaultdict
import importlib.util
import hashlib
import json
import random

spec = importlib.util.spec_from_file_location('boundary', 'evidence/check_boundary_oracle.py')
boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boundary)
RHO, TOP = boundary.RHO, boundary.TOP
JOB = 'c042-strongrsp-research-266844093669'


class PersistentBlocks:
    def __init__(self, blocks):
        self.n = len(blocks)
        self.stats = Counter()
        def build(l, r):
            if r-l == 1:
                return blocks[l]
            m = (l+r)//2
            return (build(l, m), build(m, r))
        self.root = build(0, self.n)

    def get(self, root, v):
        l, r = 0, self.n
        while r-l > 1:
            self.stats['read_nodes'] += 1
            m = (l+r)//2
            if v < m:
                root, r = root[0], m
            else:
                root, l = root[1], m
        self.stats['block_reads'] += 1
        return root

    def set(self, root, v, block):
        def put(node, l, r):
            self.stats['copied_nodes'] += 1
            if r-l == 1:
                return block
            m = (l+r)//2
            if v < m:
                return (put(node[0], l, m), node[1])
            return (node[0], put(node[1], m, r))
        self.stats['block_writes'] += 1
        return put(root, 0, self.n)


def local_solve(n, q, snapshot, incoming, outgoing, active, get_block, stats, bits=None):
    """No full n/m scan: indexed adjacency and lazy boundary retrieval only."""
    table = {}
    cache = {}
    def rounded(x):
        if bits is None:return x
        scale=1<<bits
        # Checker convenience; the proof uses charged binary comparisons.
        return F((x.numerator*scale+x.denominator-1)//x.denominator,scale)
    def value(v, i, j):
        if i >= q or j >= q:
            return TOP
        if v in active:
            return table[v, i, j]
        if v not in cache:
            cache[v] = get_block(v)
            stats['boundary_blocks'] += 1
        return cache[v][i*q+j]
    def transfer(edge_id, i, j):
        stats['edge_transfers'] += 1
        u, v, pl, pc = snapshot[edge_id]
        ans = F(0)
        for a, pa in enumerate(pl):
            for b, pb in enumerate(pc):
                if pa and pb:
                    ans += pa*pb*value(u, i+a, j+b)
        return rounded(ans)
    # A scan-min queue is used only in this tiny checker; the proof uses a heap.
    # It reads no inactive vertices. Queue work is not a runtime benchmark.
    for i in reversed(range(q)):
        for j in reversed(range(q)):
            keys = {v:min(value(v, i+1, j), value(v, i, j+1)) for v in active}
            for v in active:
                for edge_id in incoming[v]:
                    stats['incidence_inspections'] += 1
                    if snapshot[edge_id][0] not in active:
                        keys[v] = min(keys[v], transfer(edge_id, i, j))
            pending = set(active)
            last = RHO
            while pending:
                u = min(pending, key=lambda v:(keys[v],v))
                pending.remove(u)
                assert keys[u] >= last
                table[u, i, j] = last = keys[u]
                for edge_id in outgoing[u]:
                    stats['incidence_inspections'] += 1
                    v = snapshot[edge_id][1]
                    if v in pending:
                        z = transfer(edge_id, i, j)
                        assert z >= table[u, i, j]
                        keys[v] = min(keys[v], z)
    return {v:tuple(table[v,i,j] for i in range(q) for j in range(q)) for v in active}


def test_fixture(name, n, q, snapshots, rounded=False):
    T = len(snapshots)-1
    D = max(1, (max(1,T)-1).bit_length())
    alpha = 1+F(1,16*((2*D+1) if rounded else D))
    bits=None
    if rounded:
        bits=5
        while F(1,1<<bits)>((alpha-1)*RHO/((2*q+1)*(n+1))):bits+=1
    incoming, outgoing = [[] for _ in range(n)], [[] for _ in range(n)]
    for k, (u,v,*_) in enumerate(snapshots[0]):
        incoming[v].append(k)
        outgoing[u].append(k)
    degree = [len(incoming[v])+len(outgoing[v]) for v in range(n)]
    # Reference: enumerate every stationary policy at each layer, at every time.
    truth = []
    ref_stats = Counter()
    source = {0:{(i,j):RHO for i in range(q) for j in range(q)}}
    for edges in snapshots:
        tab, st = boundary.run(n,q,edges,set(range(1,n)),source,True)
        ref_stats.update(st)
        truth.append([tuple(tab[v,i,j] for i in range(q) for j in range(q)) for v in range(n)])
    for t in range(T):
        assert all(a>=b for x,y in zip(truth[t],truth[t+1]) for a,b in zip(x,y))
    # Two endpoint full solves, not n separate target solves.
    stats = Counter()
    get_source = lambda v: (RHO,)*(q*q) if v == 0 else (_ for _ in ()).throw(AssertionError(v))
    ends = []
    for t in (0,T):
        tab = local_solve(n,q,snapshots[t],incoming,outgoing,set(range(1,n)),get_source,stats,bits)
        blocks = [(RHO,)*(q*q)]+[tab[v] for v in range(1,n)]
        if not rounded:assert blocks == truth[t]
        else:assert all(x<=y<=alpha*x for a,b in zip(truth[t],blocks) for x,y in zip(a,b))
        ends.append(blocks)
    if rounded:
        ends[0]=[tuple(max(a,b) for a,b in zip(x,y)) for x,y in zip(ends[0],ends[1])]
    store = PersistentBlocks(ends[0])
    roots = {0:store.root}
    rt = store.root
    for v in range(n):
        rt = store.set(rt,v,ends[1][v])
    roots[T] = rt
    calls = []
    active_count = Counter()
    witness_intervals = defaultdict(list)
    creation_depth = {0:0,T:0}

    def recurse(l,r,h,parent_active):
        if r-l < 2:
            return
        stats['recursion_nodes'] += 1
        active = set()
        endpoint = {}
        for v in parent_active:
            stats['activation_vertex_tests'] += 1
            left, right = store.get(roots[l],v), store.get(roots[r],v)
            endpoint[v] = (left,right)
            witnesses = [k for k,(a,b) in enumerate(zip(left,right)) if a>alpha*b]
            if witnesses:
                active.add(v)
                for k in witnesses:
                    witness_intervals[h,v,k].append((l,r,left[k],right[k]))
        assert active <= parent_active
        # Validation only: a global scan checks that excluding parent-inactive
        # vertices never misses an active vertex. Not production algorithm work.
        for v in range(n):
            a,b = store.get(roots[l],v),store.get(roots[r],v)
            assert (any(x>alpha*y for x,y in zip(a,b))) == (v in active)
            stats['validation_global_vertex_checks'] += 1
        t = (l+r)//2
        before = stats['incidence_inspections']
        got = local_solve(n,q,snapshots[t],incoming,outgoing,active,
                          lambda v:store.get(roots[l],v),stats,bits)
        assert stats['incidence_inspections']-before == q*q*sum(degree[v] for v in active)
        rt = roots[l]
        for v in active:
            left,right = endpoint[v]
            raw = got[v]
            block = tuple(max(b,min(a,y)) for a,b,y in zip(left,right,raw))
            stats['upper_envelope_clips'] += sum(y>a for y,a in zip(raw,left))
            stats['lower_envelope_clips'] += sum(y<b for y,b in zip(raw,right))
            rt = store.set(rt,v,block)
            active_count[v] += 1
        roots[t] = rt
        creation_depth[t] = h+1
        calls.append({'l':l,'r':r,'depth':h,'active':sorted(active)})
        # Exact test of the documented recursion invariant at each new time.
        for v in range(n):
            block = store.get(rt,v)
            left,right = store.get(roots[l],v),store.get(roots[r],v)
            for k,z in enumerate(block):
                exponent=2*(h+1)+1 if rounded else h+1
                assert truth[t][v][k] <= z <= alpha**exponent*truth[t][v][k]
                assert right[k] <= z <= left[k]
                i,j = divmod(k,q)
                assert z <= (block[(i+1)*q+j] if i+1<q else TOP)
                assert z <= (block[i*q+j+1] if j+1<q else TOP)
                stats['validation_state_comparisons'] += 1
        recurse(l,t,h+1,active)
        recurse(t,r,h+1,active)
    recurse(0,T,0,set(range(1,n)))
    assert len(roots) == T+1
    # Verify fixed-depth multiplicative potentials exactly; no real logarithms.
    for key,intervals in witness_intervals.items():
        product = F(1)
        for l,r,a,b in sorted(intervals):
            product *= a/b
        assert alpha**len(intervals) < product <= TOP/RHO
        stats['validation_potential_checks'] += 1
    # An integer upper bound equivalent to ceil(log_alpha(M/rho)).
    Rint, power = 0,F(1)
    while power < TOP/RHO:
        Rint, power = Rint+1,power*alpha
    per_vertex_bound = q*q*D*Rint
    assert max(active_count.values(),default=0) <= per_vertex_bound
    weighted_work = sum((1+degree[v])*active_count[v] for v in range(n))
    assert weighted_work <= per_vertex_bound*sum(1+x for x in degree)
    assert stats['activation_vertex_tests'] <= n+2*sum(active_count.values())
    exponent=2*D+1 if rounded else D
    assert alpha**exponent <= F(16,15)
    exact, inflated = 0,0
    max_ratio = F(1)
    for t in range(T+1):
        for v in range(n):
            block = store.get(roots[t],v)
            for k,z in enumerate(block):
                x = truth[t][v][k]
                assert x <= z <= alpha**exponent*x
                if rounded:assert (z*(1<<bits)).denominator==1
                exact += z==x
                inflated += z>x
                max_ratio = max(max_ratio,z/x)
            if t<T:
                assert all(a>=b for a,b in zip(block,store.get(roots[t+1],v)))
    return {'name':name,'n':n,'q':q,'T':T,'alpha':str(alpha),'D':D,'rounded_bits':bits,
            'exact_entries':exact,'strictly_inflated_entries':inflated,
            'maximum_ratio':str(max_ratio),'active_calls_per_vertex':dict(active_count),
            'per_vertex_bound':per_vertex_bound,'weighted_active_work':weighted_work,
            'stats':dict(stats),'persistent_stats_including_validation_reads':dict(store.stats),
            'reference_stats':dict(ref_stats),'interval_calls':calls,
            'serialized_snapshots':[[[u,v,[str(x) for x in a],[str(x) for x in b]]
                                     for u,v,a,b in edges] for edges in snapshots]}


def law(q, atoms):
    return [F(atoms.count(k),len(atoms)) for k in range(q+1)]


def envelope_attacks():
    """Inherited approximate endpoints force both clipping directions.
    These are local induction tests, not new full-recursion endpoint solves.
    """
    q,n=1,3
    zero=[F(1),F(0)]
    alpha,beta=F(65,64),F(9,8)
    src={0:{(0,0):RHO}}
    records=[]
    for mode in ('upper','lower'):
        snapshots=[]
        for fail in ([F(3,4),F(3,4),F(1,4)] if mode=='upper'
                     else [F(3,4),F(1,4),F(1,4)]):
            edges=[(0,1,[F(1,2),F(1,2)],zero),
                   (0,2,[1-fail,fail],zero)]
            if mode=='upper':edges.append((1,2,zero,zero))
            snapshots.append(edges)
        truths=[]
        for edges in snapshots:
            tab,_=boundary.run(n,q,edges,{1,2},src,True)
            truths.append({v:tab[v,0,0] for v in range(n)})
        left,right=dict(truths[0]),dict(truths[2])
        if mode=='upper':left[1]*=beta;right[1]*=beta
        else:right[2]*=beta
        assert all(truths[0][v]<=left[v]<=beta*truths[0][v] and
                   truths[2][v]<=right[v]<=beta*truths[2][v] and
                   left[v]>=right[v] for v in range(n))
        active={v for v in range(1,n) if left[v]>alpha*right[v]}
        B={v:{(0,0):left[v]} for v in range(n) if v not in active}
        raw,_=boundary.run(n,q,snapshots[1],active,B)
        clipped={v:max(right[v],min(left[v],raw[v,0,0])) if v in active else left[v]
                 for v in range(n)}
        assert all(truths[1][v]<=clipped[v]<=alpha*beta*truths[1][v] for v in range(n))
        witness=[v for v in active if (raw[v,0,0]>left[v] if mode=='upper'
                                      else raw[v,0,0]<right[v])]
        assert witness
        records.append({'direction':mode,'active':sorted(active),'witness_vertices':witness,
                        'left':{v:str(x) for v,x in left.items()},
                        'right':{v:str(x) for v,x in right.items()},
                        'raw':{v:str(raw[v,0,0]) for v in active},
                        'clipped':{v:str(x) for v,x in clipped.items()}})
    return records


def fixtures():
    rng = random.Random(2026110302)
    out = []
    for case in range(10):
        n,q,T = 4,2,15+(case%3)
        edge_specs = [(rng.randrange(n),v) for v in range(1,n) for _ in range(2)]
        # Fixed nondecreasing event thresholds per atom yield a coordinatewise
        # nonincreasing sample-path coupling. Costs are fixed, length changes.
        specifications=[]
        for u,v in edge_specs:
            cost=law(q,[rng.randrange(q+1) for _ in range(4)])
            clocks=[]
            for _ in range(8):
                times=sorted(rng.sample(range(1,T+1),q))
                clocks.append(times)
            specifications.append((u,v,clocks,cost))
        snapshots=[]
        for t in range(T+1):
            edges=[]
            for u,v,clocks,cost in specifications:
                atoms=[sum(t<z for z in changes) for changes in clocks]
                edges.append((u,v,law(q,atoms),cost))
            snapshots.append(edges)
        out.append((f'coupled_seeded_{case}',n,q,snapshots))
    # Fine variation remains inactive; a large independent decrease activates
    # other blocks. Parallel edges, closed classes and no-op times are included.
    n,q,T=4,2,31
    zero=[F(1),F(0),F(0)]
    snapshots=[]
    for t in range(T+1):
        a=F(t,128*T)
        b=F(t//4,8)
        snapshots.append([(0,1,[a,F(0),1-a],zero),(1,2,zero,zero),
                          (0,2,[b,F(0),1-b],zero),(2,3,zero,zero),
                          (3,3,zero,zero),(2,3,zero,zero)])
    out.append(('fine_inactive_and_parallel',n,q,snapshots))
    # Held-out deterministic q=3 family, chosen structurally rather than by seed.
    n,q,T=3,3,11
    zero=[F(1),F(0),F(0),F(0)]
    snapshots=[]
    for t in range(T+1):
        a=F(t,16)
        snapshots.append([(0,1,[a,1-a,F(0),F(0)],zero),
                          (1,2,[a,F(0),1-a,F(0)],zero),
                          (2,1,zero,zero),(2,2,zero,zero)])
    out.append(('heldout_q3_zero_cycle',n,q,snapshots))
    # Degenerate roots and no events.
    for T in (0,1):
        q,n=2,3
        zero=[F(1),F(0),F(0)]
        out.append((f'degenerate_T{T}',n,q,[[(1,2,zero,zero),(2,1,zero,zero)]]*(T+1)))
    return out


def main():
    records=[]
    specified=fixtures()
    for name,n,q,snapshots in specified:
        records.append(test_fixture(name,n,q,snapshots))
    for name,n,q,snapshots in (specified[1],specified[7],specified[10],specified[11]):
        records.append(test_fixture(name+'_rounded',n,q,snapshots,True))
    totals=Counter()
    for r in records:
        totals.update({k:v for k,v in r['stats'].items()})
        totals['strictly_inflated_entries']+=r['strictly_inflated_entries']
        totals['reference_policy_evaluations']+=r['reference_stats']['policy_evaluations']
        totals['reference_nonterminating_policies']+=r['reference_stats']['nonterminating_policies']
    result={'job_id':JOB,'source_sha256':hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
            'seed':2026110302,'all_checks_passed':True,'fixtures':len(records),
            'totals':dict(totals),'records':records,'inherited_endpoint_clipping_attacks':envelope_attacks(),
            'scope':'Specified finite rational monotone two-clock sequences only; exact policy reference. '
                    'Not Poisson laws, a bit-complexity result, independent audit, or full RSP resolution. '
                    'Global scans occur only in separately marked validation/reference code; '
                    'the local production interface reads indexed active incidences. '
                    'Tiny checker uses scan-min queues; the algorithmic proof uses heaps.'}
    Path('evidence/offline-composition-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':
    main()
