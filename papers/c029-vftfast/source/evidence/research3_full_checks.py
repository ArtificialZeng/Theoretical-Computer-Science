#!/usr/bin/env python3
"""Deterministic finite validation of the complete two-branch construction.

This tests code and exact finite guarantees, not asymptotic sparsity/novelty.
No subprocesses, external workers, or approximate distances are used.
"""
from collections import deque
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import random
import time

spec = importlib.util.spec_from_file_location('rep', Path(__file__).with_name('research2_representative_checks.py'))
rep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rep)
COUNTS = dict(d_to_r_runs=0, insertions=0, rejections=0, rejected_exact_fault_tests=0,
              insertion_witness_checks=0, distance_checks=0, fault_sets=0,
              mixed_runs=0, mixed_distance_checks=0, dr_runs=0, dr_distance_checks=0)

def shortest(g, x, y, forbidden=frozenset()):
    if x in forbidden or y in forbidden:
        return None
    parent = {x: None}
    queue = deque([x])
    while queue:
        u = queue.popleft()
        if u == y:
            path = [y]
            while parent[path[-1]] is not None:
                path.append(parent[path[-1]])
            return tuple(reversed(path))
        for v in sorted(g[u]):
            if v not in forbidden and v not in parent:
                parent[v] = u
                queue.append(v)
    return None

def distance(g, x, y, forbidden=frozenset()):
    p = shortest(g, x, y, forbidden)
    return len(g) * 10000 if p is None else len(p)-1

def fault_sets(n, f, protected=frozenset()):
    rest = [v for v in range(n) if v not in protected]
    for size in range(min(f,len(rest))+1):
        for ft in combinations(rest,size):
            yield frozenset(ft)

def protected_cut(h, path, r, f):
    protected = frozenset(path)
    x,y = path[0],path[-1]
    cut = set()
    for j in range(f+1):
        p = shortest(h,x,y,cut)
        if p is None or len(p)-1 > r:
            assert not protected.intersection(cut)
            assert len(cut) <= (r-1)*f
            return frozenset(cut)
        block = set(p)-protected
        if not block or j == f:
            return None
        cut.update(block)
    raise AssertionError('unreachable')

def d_to_r(g,d,r,f):
    h = [set() for _ in g]
    COUNTS['d_to_r_runs'] += 1
    for x in range(len(g)):
        families = rep.families(g,x,d,f)
        for y in range(x+1,len(g)):
            for path in sorted(families[y]):
                cut = protected_cut(h,path,r,f)
                if cut is None:
                    COUNTS['rejections'] += 1
                    # Independently verify the rejection against every admissible
                    # original-budget cut in this finite instance.
                    for ft in fault_sets(len(g),f,frozenset(path)):
                        assert distance(h,x,y,ft) <= r
                        COUNTS['rejected_exact_fault_tests'] += 1
                else:
                    assert distance(h,x,y,cut)>r
                    assert not set(path).intersection(cut)
                    assert all(v in g[u] for u,v in zip(path,path[1:]))
                    assert any(v not in h[u] for u,v in zip(path,path[1:]))
                    COUNTS['insertion_witness_checks'] += 1
                    for u,v in zip(path,path[1:]):
                        h[u].add(v);h[v].add(u)
                    COUNTS['insertions'] += 1
    for ft in fault_sets(len(g),f):
        COUNTS['fault_sets'] += 1
        for x,y in combinations([v for v in range(len(g)) if v not in ft],2):
            if distance(g,x,y,ft)==d:
                assert distance(h,x,y,ft)<=r
                COUNTS['distance_checks'] += 1
    return h

def pendants(g,ell):
    out=[set(a) for a in g]
    for v in range(len(g)):
        last=v
        for _ in range(ell):
            new=len(out);out.append({last});out[last].add(new);last=new
    return out

def mixed(g,d,r,f):
    h=[set() for _ in g]
    for ell in range(d):
        aug=pendants(g,ell)
        sub=d_to_r(aug,d,r,f)
        for u in range(len(g)):
            h[u].update(v for v in sub[u] if v<len(g))
    COUNTS['mixed_runs'] += 1
    for ft in fault_sets(len(g),f):
        for x,y in combinations([v for v in range(len(g)) if v not in ft],2):
            a=distance(g,x,y,ft);b=distance(h,x,y,ft)
            if a < len(g)*10000:
                assert d*b <= r*a+d*r
                COUNTS['mixed_distance_checks'] += 1
    return h

def dr(g,t,f):
    # Actual DR2020 modified multiplicative greedy, with protected endpoints.
    h=[set() for _ in g]
    for u in range(len(g)):
        for v in sorted(g[u]):
            if u<v and protected_cut(h,(u,v),2*t-1,f) is not None:
                h[u].add(v);h[v].add(u)
    COUNTS['dr_runs'] += 1
    for ft in fault_sets(len(g),f):
        for x,y in combinations([v for v in range(len(g)) if v not in ft],2):
            a=distance(g,x,y,ft);b=distance(h,x,y,ft)
            if a<len(g)*10000:
                assert b<=(2*t-1)*a
                COUNTS['dr_distance_checks'] += 1
    return h

def main():
    started=time.monotonic()
    coverage=[]; max_n=0; max_aug_n=0; cases=0; maximum_edges=0
    for n in range(2,7):
        edges=list(combinations(range(n),2));bound=1<<len(edges)
        masks=list(range(bound)) if n<=4 else sorted({0,bound-1,*[
            random.Random(290303+n*100+i).randrange(bound) for i in range(8)]})
        coverage.append(dict(n=n,graph_masks=len(masks),all_labeled_graphs=n<=4))
        for mask in masks:
            g=[set() for _ in range(n)]
            for i,(u,v) in enumerate(edges):
                if mask&(1<<i):g[u].add(v);g[v].add(u)
            max_n=max(max_n,n)
            # d=1..3 is deliberately tested beyond the small finite log cap.
            for d in range(1,min(3,n-1)+1):
                # The short radii stress cut decisions; 48d^2 is the eta=1/4,
                # k=d^2 target radius, and is often connectivity-only here.
                radii=sorted({d,d+1,2*d+1,48*d*d})
                for f in range(min(2,n-2)+1):
                    for r in radii:
                        out=mixed(g,d,r,f)
                        cases+=1;max_aug_n=max(max_aug_n,d*n)
                        maximum_edges=max(maximum_edges,sum(map(len,out))//2)
                    for t in sorted({1,d,3}):dr(g,t,f)
    result=dict(job_id='c029-vftfast-research-9df2f29ab673',field_prime=rep.P,
        coverage=coverage,small_branch_cases=cases,largest_base_n=max_n,
        largest_augmented_n=max_aug_n,max_output_edges_observed=maximum_edges,
        f_range='0..min(2,n-2)',d_range='1..min(3,n-1)',
        radii='d, d+1, 2d+1, 48*d*d (deduplicated)',
        counts=COUNTS,failures=0,elapsed_seconds=round(time.monotonic()-started,6),
        limitation='Exact finite tests; no finite check establishes asymptotic size, uniform runtime, novelty, or an infinite theorem. Small radii are stress tests beyond the packing theorem hypotheses.')
    Path('evidence/research3-full-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
