"""Bounded exact diagnostic of a streaming generator using polynomial primitives.

No all-subsets oracle is used by the generator. Exhaustive subset recognition is
used ONLY as a finite independent expected-output oracle, for n<=10 here.
This script does not prove any asymptotic delay or universal correctness result.
"""
from pathlib import Path
from collections import deque, Counter
import sys, json, hashlib, datetime
import networkx as nx

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / 'intake'))
from pmc_atom_neighborhood import bits, components, component, neighborhood, is_pmc, neighbors
from pmc_streaming_finite import adjacency, extension


def separators(adj):
    """BBC queue scheme: return each separator on dequeue, once.

    Initialization and one queue expansion use polynomially many graph searches.
    Use a binary trie instead of Python's hash table for worst-case guarantees.
    """
    allv = (1 << len(adj)) - 1
    known, queue = set(), deque()
    def add_candidates(removed):
        for c in components(adj, allv & ~removed):
            s = neighborhood(adj, c)
            full = [d for d in components(adj, allv & ~s) if neighborhood(adj, d) == s]
            # Explicit validity check is polynomial and guards transcription errors.
            if len(full) >= 2 and s not in known:
                known.add(s)
                queue.append(s)
    for v in range(len(adj)):
        add_candidates(adj[v] | (1 << v))
    while queue:
        s = queue.popleft()
        yield s
        for x in bits(s):
            add_candidates(s | adj[x])


def generate(adj, trace):
    n = len(adj)
    allv = (1 << n) - 1
    cs = components(adj, allv)
    if len(cs) != 1:
        for c in cs:
            vs = list(bits(c))
            sub = tuple(sum(1 << j for j,w in enumerate(vs) if adj[v] >> w & 1) for v in vs)
            for z in generate(sub, trace):
                yield sum(1 << vs[j] for j in bits(z))
        return
    if all(adj[v] == (allv ^ (1 << v)) for v in range(n)):
        yield allv
        return
    a = next(v for v in range(n) if len(components(adj, allv ^ (1 << v))) == 1)
    vs = [v for v in range(n) if v != a]
    sub = tuple(sum(1 << j for j,w in enumerate(vs) if adj[v] >> w & 1) for v in vs)
    known, queue, fibers = set(), deque(), Counter()
    def add(z):
        if z in known:
            return False
        assert is_pmc(adj,z)
        known.add(z)
        queue.append(z)
        return True
    kc = 0
    for x in generate(sub, trace):
        kc += 1
        lift = sum(1 << vs[j] for j in bits(x))
        valid = [z for z in (lift, lift | (1 << a)) if is_pmc(adj,z)]
        assert valid
        for z in valid:
            if add(z):
                yield z
        assert len(known) >= kc
    sep_count = 0
    for s in separators(adj):
        sep_count += 1
        full = [c for c in components(adj, allv ^ s) if neighborhood(adj,c) == s]
        gamma, witness, _ = extension(adj,s,full)
        assert witness in components(adj, allv ^ gamma)
        assert neighborhood(adj,witness) == s
        fibers[gamma] += 1
        assert fibers[gamma] <= n
        if add(gamma):
            yield gamma
        assert sep_count <= n * len(known)
        z = s | (1 << a)
        if is_pmc(adj,z) and add(z):
            yield z
    popped = set()
    while queue:
        w = queue.popleft()
        assert w not in popped
        popped.add(w)
        # Root neighborhood function implements the same explicit endpoint-safe
        # graph-search formula. Candidate membership is the global criterion.
        candidates = set()
        for u in bits(w):
            x = w | adj[u]
            for b in bits(w & ~(1 << u)):
                aa = component(adj,b,allv & ~(x & ~(1 << b)))
                na = neighborhood(adj,aa)
                if (aa | na) >> u & 1:
                    continue
                uu = component(adj,u,allv & ~na)
                ss = neighborhood(adj,uu)
                assert not (ss >> b & 1) and not (ss >> u & 1)
                bb = component(adj,b,allv & ~ss)
                assert not (bb >> u & 1)
                z = x & (ss | bb)
                if is_pmc(adj,z):
                    candidates.add(z)
        # Compare endpoint implementations; this is not an independent PMC test.
        root_neighbors,_ = neighbors(adj,w,{z for z in candidates})
        assert candidates == root_neighbors
        for z in sorted(candidates):
            if add(z):
                yield z
    trace.append({'n':n, 'pmcs':len(known), 'separators':sep_count,
                  'max_fiber':max(fibers.values(),default=0),'popped':len(popped)})


def run():
    cases = [('empty',nx.empty_graph(0)),('isolated-5',nx.empty_graph(5))]
    for n in [1,2,4,7,10]:
        cases += [(f'complete-{n}',nx.complete_graph(n)),(f'path-{n}',nx.path_graph(n))]
    for n in [4,6,9,10]:
        cases += [(f'cycle-{n}',nx.cycle_graph(n))]
    cases += [('bipartite-4-5',nx.complete_bipartite_graph(4,5)),
              ('wheel-9',nx.wheel_graph(9)),('petersen',nx.petersen_graph()),
              ('disconnected-cycle-path',nx.disjoint_union(nx.cycle_graph(4),nx.path_graph(5))),
              ('disconnected-cliques',nx.disjoint_union(nx.complete_graph(3),nx.complete_graph(4)))]
    for i in range(8):
        cases.append((f'new-random-9-{i}',nx.gnp_random_graph(9,[.2,.4,.65,.85][i%4],seed=730051+i)))
    records=[]
    for label,g in cases:
        adj=adjacency(g); n=len(adj); allv=(1<<n)-1
        expected_seps={s for s in range(allv) if sum(neighborhood(adj,c)==s for c in components(adj,allv ^ s))>=2}
        got_seps=list(separators(adj))
        assert len(got_seps)==len(set(got_seps)) and set(got_seps)==expected_seps, label
        expected={s for s in range(1,1<<n) if is_pmc(adj,s)}
        trace=[]; outputs=list(generate(adj,trace))
        assert len(outputs)==len(set(outputs)) and set(outputs)==expected, label
        records.append({'label':label,'n':n,'edges':sorted(map(sorted,g.edges())),
                        'outputs':outputs,'separator_count':len(got_seps),'recursive_checks':trace})
    packet={'job_id':'c025-pmcdelay-research-338d67d18097',
            'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'case_count':len(records),'all_cases_passed':True,
            'generator_separator_oracle':'Polynomial graph-search BBC queue scheme; no subset enumeration.',
            'finite_expected_oracle':'All subsets using PMC criterion and full-component separator criterion, n<=10.',
            'limits':'Finite transcription diagnostics only; no universal delay/correctness or novelty certificate. Python hash sets are replaced by tries in the mathematical algorithm.',
            'records':records}
    dst=BASE/'evidence/pass1-targeted-streaming.json'
    dst.write_text(json.dumps(packet,indent=2)+'\n')
    print(json.dumps({'case_count':len(records),'all_cases_passed':True,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()}))

if __name__=='__main__':
    run()
