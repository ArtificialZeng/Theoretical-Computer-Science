#!/usr/bin/env python3
"""Fresh finite checks; no frozen implementation is imported or overwritten.

Compare the proposed ordering with synchronous finite-horizon Bellman DP.
All arithmetic is exact. Finite checks do not prove the general theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import random

JOB = 'c042-strongrsp-referee-5010e06f0ba2'
RHO, TOP = F(1, 32), F(33, 32)

def ceiling(x, bits):
    d = 1 << bits
    return F((x.numerator*d + x.denominator-1)//x.denominator, d)

def expectation(edge, i, j, table, q):
    u, _, law = edge
    return sum((p*(TOP if i+a >= q or j+b >= q else table[u,i+a,j+b])
                for a,b,p in law), F(0))

def synchronous(n, q, edges, active, boundary):
    states = [(v,i,j) for v in active for i in range(q) for j in range(q)]
    table = dict(boundary)
    table.update({x:TOP for x in states})
    horizon = (2*q+1)*(len(active)+1)
    for _ in range(horizon+2):
        nxt = dict(boundary)
        for v,i,j in states:
            options = [table.get((v,i+1,j),TOP), table.get((v,i,j+1),TOP)]
            options += [expectation(e,i,j,table,q) for e in edges if e[1] == v]
            nxt[v,i,j] = min(options)
        if nxt == table:
            return nxt
        table = nxt
    raise AssertionError('finite-rank claim did not stabilize')

def ordered(n, q, edges, active, boundary, bits=None):
    table, realized, ranks = dict(boundary), dict(boundary), {x:0 for x in boundary}
    for i in reversed(range(q)):
        for j in reversed(range(q)):
            keys, pointers = {}, {}
            for v in active:
                opts = [(table.get((v,i+1,j),TOP),('tick',v,i+1,j)),
                        (table.get((v,i,j+1),TOP),('tick',v,i,j+1))]
                keys[v], pointers[v] = min(opts, key=lambda x:x[0])
            def offer(ei):
                e = edges[ei]; v = e[1]
                raw = expectation(e,i,j,table,q)
                z = raw if bits is None else ceiling(raw,bits)
                if z < keys[v]:
                    keys[v], pointers[v] = z, ('edge',ei)
            for ei,e in enumerate(edges):
                if e[1] in active and e[0] not in active:
                    offer(ei)
            pending, last = set(active), RHO
            while pending:
                v = min(pending,key=lambda x:(keys[x],x))
                pending.remove(v)
                assert keys[v] >= last
                table[v,i,j] = last = keys[v]
                ptr = pointers[v]
                if ptr[0] == 'tick':
                    _,u,a,b = ptr
                    realized[v,i,j] = realized.get((u,a,b),TOP)
                    ranks[v,i,j] = 1+ranks.get((u,a,b),0)
                else:
                    e = edges[ptr[1]]
                    realized[v,i,j] = expectation(e,i,j,realized,q)
                    ranks[v,i,j] = 1+max([ranks.get((e[0],i+a,j+b),0)
                                         for a,b,p in e[2] if p] or [0])
                for ei,e in enumerate(edges):
                    if e[0] == v and e[1] in pending:
                        offer(ei)
    return table,realized,ranks

def offline_checks():
    # Full tables here are deliberately a finite reference test, not the
    # persistent production implementation or a running-time benchmark.
    n,q,T,D,bits = 4,2,8,3,20
    alpha = 1+F(1,16*(2*D+1))
    source = {(0,i,j):RHO for i in range(q) for j in range(q)}
    records, checks = [], 0
    for fixture in range(4):
        sequence = []
        for t in range(T+1):
            edges = []
            for k,(u,v) in enumerate([(0,1),(1,2),(2,3),(3,1),(0,3),(1,3),(2,2)]):
                p = F(max(0,min(8,t-(k+fixture)%3)),8)
                a,b = [(q,0),(0,q),(1,1),(0,0)][(k+fixture)%4]
                edges.append((u,v,[(0,0,p),(a,b,1-p)]))
            sequence.append(edges)
        truth = [synchronous(n,q,e,{1,2,3},source) for e in sequence]
        versions = {}
        versions[0] = ordered(n,q,sequence[0],{1,2,3},source,bits)[0]
        versions[T] = ordered(n,q,sequence[T],{1,2,3},source,bits)[0]
        versions[0] = {x:max(z,versions[T][x]) for x,z in versions[0].items()}
        activations = []
        def visit(l,r,parent):
            if r-l < 2:
                return
            left,right = versions[l],versions[r]
            active = {v for v in parent if any(left[v,i,j]>alpha*right[v,i,j]
                       for i in range(q) for j in range(q))}
            for v in {1,2,3}-parent:
                assert all(left[v,i,j]<=alpha*right[v,i,j]
                           for i in range(q) for j in range(q))
            t = (l+r)//2
            boundary = {x:z for x,z in left.items() if x[0] not in active}
            raw = ordered(n,q,sequence[t],active,boundary,bits)[0]
            mid = dict(left)
            for x in raw:
                if x[0] in active:
                    mid[x] = max(right[x],min(left[x],raw[x]))
            versions[t] = mid
            activations.append({'interval':[l,r],'active':sorted(active)})
            visit(l,t,active);visit(t,r,active)
        visit(0,T,{1,2,3})
        assert len(versions)==T+1
        for t in range(T+1):
            for x,z in versions[t].items():
                assert truth[t][x]<=z<=alpha**(2*D+1)*truth[t][x]
                if t:
                    assert z<=versions[t-1][x]
                v,i,j=x
                assert z<=versions[t].get((v,i+1,j),TOP)
                assert z<=versions[t].get((v,i,j+1),TOP)
                checks += 1
        records.append({'fixture':fixture,'activations':activations})
    return {'cases':len(records),'state_checks':checks,'records':records,
            'scope':'Four monotone finite two-clock sequences; fresh clipped rounded recursion compared to fresh synchronous Bellman reference; tests values, time/tick envelopes, and nested activity, not production persistence or total runtime.'}

def main():
    rng = random.Random(5010)
    records, count = [], 0
    for q in (2,3):
        n = 4
        for fixture in range(8):
            edges = []
            if fixture == 0:
                edges = [(1,2,[(0,0,F(1))]),(2,1,[(0,0,F(1))]),
                         (3,3,[(0,0,F(1))])]
            else:
                for v in (1,2,3):
                    for u in rng.sample(range(n),2):
                        bins = {}
                        for _ in range(4):
                            ab = (rng.randrange(q+1),rng.randrange(q+1))
                            bins[ab] = bins.get(ab,0)+1
                        edges.append((u,v,[(a,b,F(c,4)) for (a,b),c in sorted(bins.items())]))
                if fixture == 1:
                    edges += [(0,1,[(0,0,F(1,1<<40)),(q,0,1-F(1,1<<40))])]
            source = {(0,i,j):RHO for i in range(q) for j in range(q)}
            truth = synchronous(n,q,edges,{1,2,3},source)
            for mask in (0,1,3,7):
                active = {v for v in (1,2,3) if mask & (1<<(v-1))}
                boundary = dict(source)
                for v in {1,2,3}-active:
                    for i in range(q):
                        for j in range(q):
                            boundary[v,i,j] = min(TOP,ceiling(F(17,16)*truth[v,i,j],8))
                ref = synchronous(n,q,edges,active,boundary)
                exact,actual,rank = ordered(n,q,edges,active,boundary)
                assert exact == ref == actual
                rounded,actual,rank = ordered(n,q,edges,active,boundary,8)
                bound = (2*q+1)*(len(active)+1)
                for v in active:
                    for i in range(q):
                        for j in range(q):
                            x = (v,i,j)
                            assert ref[x] <= actual[x] <= rounded[x] <= ref[x]+F(bound,256)
                            assert rank[x] <= bound
                            assert rounded[x] <= rounded.get((v,i+1,j),TOP)
                            assert rounded[x] <= rounded.get((v,i,j+1),TOP)
                            for e in edges:
                                if e[1] == v:
                                    assert rounded[x] <= expectation(e,i,j,rounded,q)+F(1,256)
                            count += 1
                records.append({'q':q,'fixture':fixture,'active_mask':mask,
                                'max_rank':max(rank.values()),'rank_bound':bound})
    snap = json.loads(Path('audit/snapshot.json').read_text())
    assert all(hashlib.sha256(Path(f).read_bytes()).hexdigest()==h for f,h in snap['files'].items())
    offline = offline_checks()
    out = {'job_id':JOB,'snapshot_digest':snap['digest'],'all_checks_passed':True,
           'cases':len(records),'state_checks':count,'seed':5010,'records':records,
           'offline':offline,
           'scope':'Fresh exact synchronous finite-horizon DP versus fresh ordered oracle; q=2,3, n=4; arbitrary rational joint laws, zero closed classes, self loops, a 2^-40 mass, whole-vertex boundaries, rounded policy/payoff/rank/residual checks. No universal theorem or full production execution is certified.'}
    Path('audit/referee-checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'}))

if __name__ == '__main__':
    main()
