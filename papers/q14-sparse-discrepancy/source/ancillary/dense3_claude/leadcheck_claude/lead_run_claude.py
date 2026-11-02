#!/usr/bin/env python3
"""Lead's re-run with the ORIGINAL paper checker q14paper_claude/ancillary/small_n_check/cover_bnb.py.
usage: lead_run_claude.py sparse n c file...  |  lead_run_claude.py full n c"""
import sys, os, time
ANC=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','q14paper_claude','ancillary','small_n_check'))
sys.path.insert(0, ANC)
from fractions import Fraction
import cover_bnb as cb
mode=sys.argv[1]; n=int(sys.argv[2]); c=Fraction(sys.argv[3])
print("checker:", cb.__file__, flush=True)
if mode=='full':
    for j in range(1,n+1):
        t0=time.time(); r=cb.bnb(cb.Problem(j,[tuple(range(j))]*n,c,sort_coords=True),max_depth=24,time_limit=900)
        print(f"full n={n} c={c} j={j}: {r['status']} boxes={r['boxes']} {time.time()-t0:.1f}s",flush=True)
        if r['status']!='PROVED': break
else:
    for fn in sys.argv[4:]:
        tot=nb=bad=0; t0=time.time()
        for line in open(fn):
            a=list(map(int,line.split()))
            if not a: continue
            j=a[0]; items=[(a[1+2*k],a[2+2*k]) for k in range(j)]
            Js=[tuple(k for k in range(j) if i in items[k]) for i in range(n)]
            r=cb.bnb(cb.Problem(j,Js,c),max_depth=24,time_limit=900)
            tot+=1; nb+=r['boxes']
            if r['status']!='PROVED':
                bad+=1; print("NOT PROVED",items,r['status'],flush=True)
                if bad>=3: break
        print(f"{fn}: {tot} patterns, {nb} boxes, not proved {bad}, {time.time()-t0:.1f}s",flush=True)
