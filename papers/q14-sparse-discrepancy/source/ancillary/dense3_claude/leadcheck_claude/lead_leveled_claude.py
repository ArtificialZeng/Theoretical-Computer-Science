#!/usr/bin/env python3
"""Lead's leveled re-check: the ORIGINAL paper checker (cover_bnb.py) patched textually to
per-function thresholds c_i (vertex_data threshold, distance condition dmin_i), and symmetry breaking
only between functions with equal J_i AND equal threshold.  Patterns: items on vertices/edges of
G = K_n - E(K_I), I = {0..s-1} of level 1 (threshold 1.99), others level 2 (threshold 2.99), up to
Aut = S_I x S_{rest}; counts checked by Burnside.  usage: lead_leveled_claude.py n s"""
import sys, os, itertools, time, types as _t
from fractions import Fraction
from math import floor
ANC=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','q14paper_claude','ancillary','small_n_check'))
src=open(os.path.join(ANC,'cover_bnb.py')).read()
a="thr = (self.cn * den ** r) // (2 * self.cd)"; b="thr = (self.cns[i] * den ** r) // (2 * self.cds[i])"
c="ok &= (o >= dmin)"; d="ok &= (o >= self.dmins[i])"
assert src.count(a)==1 and src.count(c)==1
src=src.replace(a,b).replace(c,d)
cb=_t.ModuleType('cb_lev'); exec(compile(src,'cover_bnb_leveled','exec'),cb.__dict__)
def problem(j,Js,cs):
    P=cb.Problem(j,Js,max(cs))
    P.cns=[Fraction(x).numerator for x in cs]; P.cds=[Fraction(x).denominator for x in cs]
    P.dmins=[floor(Fraction(x))+1 for x in cs]
    P.prev_same=[None]*P.n
    for i in range(P.n):
        for i2 in range(i-1,-1,-1):
            if P.Js[i2]==P.Js[i] and cs[i2]==cs[i]: P.prev_same[i]=i2; break
    return P
n=int(sys.argv[1]); s=int(sys.argv[2])
I=set(range(s)); cs=[Fraction(199,100) if v in I else Fraction(299,100) for v in range(n)]
types=[(v,v) for v in range(n)]+[(u,v) for u in range(n) for v in range(u+1,n) if not (u in I and v in I)]
auts=[p1+p2 for p1 in itertools.permutations(range(s)) for p2 in itertools.permutations(range(s,n))]
def canon(ms):
    return min(tuple(sorted(tuple(sorted((g[x],g[y]))) for x,y in ms)) for g in auts)
def burnside(j):
    tot=0
    for g in auts:
        seen=set(); lens=[]
        for t in types:
            if t in seen: continue
            L=0;u=t
            while u not in seen: seen.add(u); L+=1; u=tuple(sorted((g[u[0]],g[u[1]])))
            lens.append(L)
        poly=[1]+[0]*j
        for L in lens:
            new=poly[:]
            for dd in range(L,j+1): new[dd]+=new[dd-L]
            poly=new
        tot+=poly[j]
    return Fraction(tot,len(auts))
level={()}; grand=0; gb=0; bad=0
print(f"leveled n={n} |I|={s} thresholds {[str(x) for x in cs]}",flush=True)
for j in range(1,n+1):
    nxt=set()
    for ms in level:
        for t in types: nxt.add(canon(ms+(t,)))
    level=nxt; B=burnside(j); assert B==len(level)
    t0=time.time(); nb=0
    for ms in sorted(level):
        Js=[tuple(k for k in range(j) if v in ms[k]) for v in range(n)]
        r=cb.bnb(problem(j,Js,cs),max_depth=24,time_limit=900); nb+=r['boxes']
        if r['status']!='PROVED':
            bad+=1; print("NOT PROVED",ms,r['status'],flush=True)
            if bad>=3: break
    grand+=len(level); gb+=nb
    print(f"  j={j}: {len(level)} patterns (Burnside {B}), {nb} boxes, {time.time()-t0:.1f}s",flush=True)
    if bad>=3: break
print(f"TOTAL n={n} s={s}: {grand} patterns, {gb} boxes, not proved {bad}",flush=True)
