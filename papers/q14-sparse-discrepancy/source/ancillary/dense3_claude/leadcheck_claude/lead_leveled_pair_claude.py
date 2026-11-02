#!/usr/bin/env python3
"""Lead: the two six-item leveled patterns that timed out without coordinate sorting (two functions sharing
all j=6 fractional items, thresholds 1.99 and 2.99, or 1.99/1.99 vs 2.99): rerun with sort_coords=True,
valid because every item is read by the same two functions (all coordinate permutations are symmetries)."""
import sys, os
sys.argv=[sys.argv[0],'6','1']   # dummy to import the helpers without running the main loop
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'lead_leveled_claude.py')).read()
head=src.split("n=int(sys.argv[1])")[0]
exec(head)
import time
# the two timed-out patterns (s=1: ((0,1),)*6, s=2: ((0,2),)*6) are the same problem: a level-1 and a level-2
# function sharing all six fractional items; the other functions read no fractional item.
for name,cs,J in [("level-1 and level-2 function sharing 6 items (s=1 and s=2 cases)",[Fraction(199,100),Fraction(299,100)],[tuple(range(6))]*2)]:
    P=problem(6,J,cs); P.sort_coords=True
    t0=time.time(); r=cb.bnb(P,max_depth=30,time_limit=7200)
    print(name, r['status'], 'boxes',r['boxes'], f"{time.time()-t0:.1f}s", flush=True)
