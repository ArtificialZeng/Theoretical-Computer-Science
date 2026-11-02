#!/usr/bin/env python3
"""Lead's independent re-check (written from scratch): canonical 2-sparse patterns of j items on n
functions (each item read by 1 or 2 functions) up to S_n, by augmentation + brute-force canonical form;
counts compared with Burnside. usage: python3 -I lead_patterns_claude.py n jmax outprefix"""
import sys, itertools
from fractions import Fraction
from math import factorial
n=int(sys.argv[1]); jmax=int(sys.argv[2]); out=sys.argv[3]
types=[(a,a) for a in range(n)]+[(a,b) for a in range(n) for b in range(a+1,n)]
perms=list(itertools.permutations(range(n)))
def canon(ms):
    best=None
    for s in perms:
        t=tuple(sorted(tuple(sorted((s[a],s[b]))) for a,b in ms))
        if best is None or t<best: best=t
    return best
def burnside(j):
    tot=0
    for s in perms:
        idx={t:i for i,t in enumerate(types)}; seen=set(); lens=[]
        for t in types:
            if t in seen: continue
            L=0; u=t
            while u not in seen:
                seen.add(u); L+=1; u=tuple(sorted((s[u[0]],s[u[1]])))
            lens.append(L)
        poly=[1]+[0]*j
        for L in lens:
            new=poly[:]
            for d in range(L,j+1): new[d]+=new[d-L]
            poly=new
        tot+=poly[j]
    return Fraction(tot,len(perms))
level={()}
for j in range(1,jmax+1):
    nxt=set()
    for ms in level:
        for t in types: nxt.add(canon(ms+(t,)))
    level=nxt
    b=burnside(j)
    print(f"n={n} j={j}: {len(level)} patterns, Burnside {b}", flush=True)
    assert b==len(level)
    with open(f"{out}_j{j}.txt","w") as f:
        for ms in sorted(level):
            f.write(f"{j} "+" ".join(f"{a} {b}" for a,b in ms)+"\n")
