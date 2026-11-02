#!/usr/bin/env python3
"""Exact tests of the new geodesic, singleton-fault insertion-history lemma.
No prior exhaustive separator tests are rerun. No original-construction claim.
"""
from collections import deque
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]

def bfs(graph, source, target, deleted):
    assert source not in deleted and target not in deleted
    q = deque([source])
    dist = {source: 0}
    while q:
        u = q.popleft()
        if u == target:
            return dist[u]
        for v in graph[u]:
            if v not in deleted and v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return None

def test_history(core_size, edges, d, extra_core_edges=()):
    g = [set() for _ in range(core_size)]
    chains = []
    for a,b,length in edges:
        assert a != b and length > d
        chain = [a]
        for _ in range(length-1):
            chain.append(len(g)); g.append(set())
        chain.append(b)
        for u,v in zip(chain,chain[1:]):
            assert v not in g[u]
            g[u].add(v); g[v].add(u)
        chains.append(chain)
    target_edges = sum(map(len,g))//2
    for a,b in extra_core_edges:
        g[a].add(b); g[b].add(a)
    h = [set() for _ in g]
    calls = 0
    witness_histogram = {'delete_chain_end':0,'delete_chain_start':0}
    for chain in chains:
        length = len(chain)-1
        starts = list(range(0,length-d+1,d))
        if starts[-1] != length-d:
            starts.append(length-d)
        assert len(starts) == (length+d-1)//d
        for start in starts:
            p = chain[start:start+d+1]
            assert len(p)==d+1 and len(set(p))==d+1
            final = p[-1]==chain[-1]
            deleted = {chain[0] if final else chain[-1]}
            witness_histogram['delete_chain_start' if final else 'delete_chain_end']+=1
            assert not deleted.intersection(p)
            # Start BFS at the internal endpoint on the side of the removed core.
            s,t = (p[0],p[-1]) if final else (p[-1],p[0])
            assert bfs(g,s,t,deleted)==d
            assert bfs(h,s,t,deleted) is None
            new_edges = sum(v not in h[u] for u,v in zip(p,p[1:]))
            assert new_edges >= 1
            for u,v in zip(p,p[1:]):
                h[u].add(v); h[v].add(u)
            calls+=1
    assert sum(map(len,h))//2==target_edges
    assert all(h[u].issubset(g[u]) for u in range(len(g)))
    return {'d':d,'vertices':len(g),'bundle_paths':len(chains),
            'H_edges':target_edges,'ambient_extra_core_edges':len(extra_core_edges),
            'insertions_checked':calls,'exact_BFS_checks':2*calls,
            'fault_witnesses':witness_histogram,'failures':0}

def main():
    started=time.monotonic()
    cases=[]
    # Independent boundary suite: all d=1..8, all L=d+1..3d+2,
    # repeated bundles and an arbitrary complete ambient core shortcut graph.
    for d in range(1,9):
        for length in range(d+1,3*d+3):
            edges=[(0,1,length),(0,1,length),(1,2,length+1),(2,0,length+2)]
            cases.append(test_history(3,edges,d,list(itertools.combinations(range(3),2))))
    spec=importlib.util.spec_from_file_location('root_definition',ROOT/'intake/root-vft-joint-separator-check.py')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    expanded=[]
    for mask in (0,15):
        possible=[((0,v),(1,w)) for v,w in itertools.product((0,1),repeat=2)]
        allowed={edge for i,edge in enumerate(possible) if mask&(1<<i)}
        inst=module.make_instance(2,allowed)
        index={u:i for i,u in enumerate(inst['core'])}
        edges=[(index[u],index[v],length) for u,v,length in inst['bundles']
               for _ in range(inst['copies'])]
        spine=[(index[u],index[v]) for left,right in zip(inst['layers'],inst['layers'][1:])
               for u,v in itertools.product(left,right)]
        record=test_history(len(index),edges,inst['d'],spine)
        record.update(mask=mask,r=inst['r'],original_fault_budget=inst['f'],
                      inflated_output_budget=inst['budget'],copies=inst['copies'])
        expanded.append(record)
    result={'job_id':'c029-vftfast-research-36ff17e1eeb1',
        'kind':'exact_finite_tests_of_geodesic_singleton_fault_history_lemma',
        'boundary_cases':cases,'expanded_barrier_graphs':expanded,
        'total_history_insertions_checked':sum(c['insertions_checked'] for c in cases+expanded),
        'total_exact_BFS_checks':sum(c['exact_BFS_checks'] for c in cases+expanded),
        'failures':0,'elapsed_seconds':round(time.monotonic()-started,6),
        'source_sha256':hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
        'scope':'New history checks only. No exhaustive fault search, original resolution, novelty claim, or fresh referee audit.'}
    (ROOT/'evidence/research2-history-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='boundary_cases'},indent=2))

if __name__=='__main__':
    main()
