#!/usr/bin/env python3
"""Lead check: a pattern file (lines 'j a1 b1 ...', private item = (a,-1)) for n functions is a complete
list of pairwise non-isomorphic 2-sparse patterns of j items: all canonical forms distinct, count equal
to the Burnside orbit count. usage: n file j"""
import sys, itertools
from fractions import Fraction
n=int(sys.argv[1]); fn=sys.argv[2]; j=int(sys.argv[3])
types=[(a,a) for a in range(n)]+[(a,b) for a in range(n) for b in range(a+1,n)]
perms=list(itertools.permutations(range(n)))
def norm(a,b): return (a,a) if b<0 or a==b else (min(a,b),max(a,b))
pats=[]
for line in open(fn):
    v=list(map(int,line.split()))
    if not v: continue
    assert v[0]==j
    pats.append(tuple(norm(v[1+2*k],v[2+2*k]) for k in range(j)))
seen=set()
for ms in pats:
    c=min(tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in ms)) for p in perms)
    assert c not in seen, ("duplicate",ms); seen.add(c)
tot=0
for s in perms:
    sn=set(); lens=[]
    for t in types:
        if t in sn: continue
        L=0;u=t
        while u not in sn: sn.add(u); L+=1; u=tuple(sorted((s[u[0]],s[u[1]])))
        lens.append(L)
    poly=[1]+[0]*j
    for L in lens:
        new=poly[:]
        for d in range(L,j+1): new[d]+=new[d-L]
        poly=new
    tot+=poly[j]
B=Fraction(tot,len(perms))
print(f"{fn}: {len(pats)} patterns, all distinct, Burnside {B}: {'COMPLETE' if B==len(pats) else 'MISMATCH'}")
