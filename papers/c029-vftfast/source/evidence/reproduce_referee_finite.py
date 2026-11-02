#!/usr/bin/env python3
"""Offline reproduction of the accepted referee finite checks.

The mathematical test code below is copied unchanged from audit/referee_checks.py
(source SHA256 b30fbacf8e65e15bdbfc2aeb10dadcc6e22a19ef1056cba21b188c124044df39).
Only the final internal literature-cache snapshot check and audit-report writer
are replaced by a standalone JSON summary. This run is reproduction, not a new
referee review, mathematical acceptance, or a check of the omitted literature.
"""
import hashlib,json,time
from pathlib import Path
from itertools import combinations,permutations
from functools import lru_cache
from collections import deque

PRIME=11
JOB='c029-vftfast-referee-95ddbe77df2f'
counts=dict(graphs=0,representative_instances=0,avoidance_comparisons=0,
            scan_instances=0,insertion_witnesses=0,rejection_fault_tests=0,
            all_length_path_distance_tests=0,pendant_mixed_tests=0)

@lru_cache(None)
def coordinate(rank,support):
    # Leibniz expansion, independent of the frozen elimination determinant.
    h=len(support); perms=list(permutations(range(h)))
    signed=[(p,(-1)**sum(p[i]>p[j] for i in range(h) for j in range(i+1,h))) for p in perms]
    out=[]
    for rows in combinations(range(rank),h):
        total=0
        for perm,sign in signed:
            product=sign
            for j in range(h): product*=pow(support[perm[j]]+1,rows[j],PRIME)
            total+=product
        out.append(total%PRIME)
    return tuple(out)

def basis(paths,rank):
    selected=[]; pivots=[]; rows=[]
    for path in paths:
        v=list(coordinate(rank,tuple(sorted(path))))
        for p,row in zip(pivots,rows):
            a=v[p]
            v=[(x-a*y)%PRIME for x,y in zip(v,row)]
        p=next((j for j,x in enumerate(v) if x),None)
        if p is not None:
            inv=pow(v[p],PRIME-2,PRIME)
            rows.append([(x*inv)%PRIME for x in v]);pivots.append(p);selected.append(path)
    return selected

def dp(g,x,d,f):
    rank=min(len(g),f+d+1);table=[[] for _ in g];table[x]=[(x,)]
    for stage in range(d):
        nxt=[[] for _ in g]
        for u in range(len(g)):
            for path in table[u]:
                for v in sorted(g[u]):
                    if v not in path:nxt[v].append(path+(v,))
        table=[basis(a,rank) for a in nxt]
    return table

def paths(g,x,d):
    out=[[] for _ in g]
    def walk(path):
        if len(path)==d+1:out[path[-1]].append(path);return
        for v in sorted(g[path[-1]]):
            if v not in path:walk(path+(v,))
    walk((x,));return out

def faults(n,f,protected=()):
    available=sorted(set(range(n))-set(protected))
    for h in range(min(f,len(available))+1):
        for F in combinations(available,h):yield frozenset(F)

def bfs(g,x,y,F):
    if x in F or y in F:return None
    seen={x};queue=deque([(x,)])
    while queue:
        path=queue.popleft()
        if path[-1]==y:return path
        for v in sorted(g[path[-1]]):
            if v not in seen and v not in F:seen.add(v);queue.append(path+(v,))
    return None

def dist(g,x,y,F):
    p=bfs(g,x,y,F)
    return len(p)-1 if p is not None else 10**6

def scan(g,d,r,f):
    h=[set() for _ in g];counts['scan_instances']+=1
    for x in range(len(g)):
        tab=dp(g,x,d,f)
        for y in range(x+1,len(g)):
            for path in tab[y]:
                cut=set();accept=False
                for step in range(f+1):
                    route=bfs(h,x,y,cut)
                    if route is None or len(route)-1>r:accept=True;break
                    block=set(route)-set(path)
                    if not block or step==f:break
                    cut.update(block)
                if accept:
                    assert not cut.intersection(path) and len(cut)<=(r-1)*f
                    assert dist(h,x,y,cut)>r
                    assert any(v not in h[u] for u,v in zip(path,path[1:]))
                    counts['insertion_witnesses']+=1
                    for u,v in zip(path,path[1:]):h[u].add(v);h[v].add(u)
                else:
                    for F in faults(len(g),f,path):
                        assert dist(h,x,y,F)<=r
                        counts['rejection_fault_tests']+=1
    for F in faults(len(g),f):
        for x,y in combinations(sorted(set(range(len(g)))-F),2):
            if any(not F.intersection(p) for p in paths(g,x,d)[y]):
                assert dist(h,x,y,F)<=r
                counts['all_length_path_distance_tests']+=1
    return h

def pendant(g,ell):
    j=[set(a) for a in g]
    for v in range(len(g)):
        last=v
        for _ in range(ell):
            tip=len(j);j.append({last});j[last].add(tip);last=tip
    return j

def main():
    start=time.monotonic()
    for n in range(2,6):
        es=list(combinations(range(n),2))
        masks=range(1<<len(es)) if n<=4 else [0,1,7,31,127,341,682,777,1013,1023]
        for mask in masks:
            counts['graphs']+=1;g=[set() for _ in range(n)]
            for b,(u,v) in enumerate(es):
                if mask>>b&1:g[u].add(v);g[v].add(u)
            for d in range(1,min(3,n-1)+1):
                for f in range(min(2,n-d-1)+1):
                    for x in range(n):
                        tab=dp(g,x,d,f);full=paths(g,x,d)
                        counts['representative_instances']+=1
                        for y in range(n):
                            for F in faults(n,f,(x,y)):
                                a=any(not F.intersection(p) for p in full[y])
                                b=any(not F.intersection(p) for p in tab[y])
                                assert a==b
                                counts['avoidance_comparisons']+=1
                    for r in sorted({d,d+1,2*d+1}):scan(g,d,r,f)
            # Independent pendant projection for every original-budget fault.
            d=2 if n>=3 else 1;r=d+1;f=min(1,n-2)
            union=[set() for _ in g]
            for ell in range(d):
                out=scan(pendant(g,ell),d,r,f)
                for v in range(n):union[v].update(w for w in out[v] if w<n)
            for F in faults(n,f):
                for x,y in combinations(sorted(set(range(n))-F),2):
                    a=dist(g,x,y,F)
                    if a<10**6:
                        assert d*dist(union,x,y,F)<=r*a+d*r
                        counts['pendant_mixed_tests']+=1
    report=dict(source_referee_job=JOB, run_role='offline_reproduction_not_new_referee',
        exact_field_prime=PRIME, counts=counts, failures=0,
        elapsed_seconds=round(time.monotonic()-start,3),
        coverage='All labeled n=2,3,4 graphs and ten explicit n=5 masks; d<=3,f<=2 subject to f+d+1<=n; radii d,d+1,2d+1; independent pendant projection checks. Augmented N<=10.',
        limitations='Finite checks only; no literature-cache snapshot, new mathematical/novelty review or asymptotic sparsity verification.')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
