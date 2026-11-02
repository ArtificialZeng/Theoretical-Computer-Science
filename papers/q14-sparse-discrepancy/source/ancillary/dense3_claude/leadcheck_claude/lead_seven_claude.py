#!/usr/bin/env python3
"""Lead's independent schedule search for 7-vertex graphs (all levels 2): sequences of cheap deletions
(Lemma lem:cheap: delete h, exempt J subset N(h), |J| <= l_h, l_h >= 2 if J nonempty, vertices of
N(h)\\J need level >= 2 and drop by one) ending in a base: <= 5 vertices with level-1 set independent,
or 6 vertices with level-1 set independent of size <= 2.  Levels capped at 2 (monotonicity)."""
import itertools
from functools import lru_cache
def canon(n, edges, lev):
    best=None
    for p in itertools.permutations(range(n)):
        e=tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in edges))
        l=tuple(lev[p.index(i)] for i in range(n))
        key=(l,e)
        if best is None or key<best: best=key
    return best
@lru_cache(maxsize=None)
def good(n, lev, edges):
    E=set(edges); I=[v for v in range(n) if lev[v]==1]
    indep=all((min(a,b),max(a,b)) not in E for a in I for b in I if a<b)
    if indep and (n<=5 or (n==6 and len(I)<=2)): return True
    for h in range(n):
        N=[u for u in range(n) if (min(h,u),max(h,u)) in E]
        for k in range(0, min(len(N), lev[h])+1):
            if k>0 and lev[h]<2: continue
            for J in itertools.combinations(N,k):
                rest=[u for u in N if u not in J]
                if any(lev[u]<2 for u in rest): continue
                keep=[v for v in range(n) if v!=h]; idx={v:i for i,v in enumerate(keep)}
                nl=[min(2,lev[v]-(1 if v in rest else 0)) for v in keep]
                ne=[(idx[a],idx[b]) for a,b in E if h not in (a,b)]
                c=canon(n-1,ne,nl)
                if good(n-1,c[0],c[1]): return True
    return False
n=7; allE=[(a,b) for a in range(n) for b in range(a+1,n)]
# complements with <= 7 edges up to isomorphism (orderly augmentation)
def gcanon(edges):
    return min(tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in edges)) for p in itertools.permutations(range(n)))
classes=[{()}]
for k in range(1,8):
    nxt=set()
    for c in classes[-1]:
        for e in allE:
            if e not in c: nxt.add(gcanon(c+(e,)))
    classes.append(nxt)
tot=sum(len(c) for c in classes); print("complement classes with <=7 edges:", [len(c) for c in classes], "total", tot)
fails=[]
for c in classes:
    for comp in sorted(c):
        G=tuple(e for e in allE if e not in comp)
        cc=canon(n,G,(2,)*n)
        if not good(n,cc[0],cc[1]): fails.append(comp)
print("schedule search fails for", len(fails), "graphs; complements:")
for f in fails: print("  ", f)
