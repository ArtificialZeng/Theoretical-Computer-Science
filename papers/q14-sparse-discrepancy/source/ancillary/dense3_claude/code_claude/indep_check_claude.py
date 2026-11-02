#!/usr/bin/env python3
"""Independent re-check of the corner method with the paper's own Python checker
(cover_bnb_paper_copy_claude.py = verbatim copy of q14paper_claude/ancillary/small_n_check/cover_bnb.py),
on the patterns produced by patterns_claude.py.  usage: python3 -I indep_check_claude.py n c patternfile
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
import numpy as np
import cover_bnb_paper_copy_claude as cb
from cover_bnb_paper_copy_claude import Problem, bnb
# the paper's checker tabulates local distance matrices only for |J_v| <= 6; extend (same formula) to 7
for r in range(7, 9):
    if r not in cb.DT:
        cb.DT[r] = np.array([[cb.POP[u ^ y] for y in range(1 << r)] for u in range(1 << r)], dtype=np.int64)
n = int(sys.argv[1]); c = Fraction(sys.argv[2]); fn = sys.argv[3]
tot = 0; fails = 0; nb = 0; t0 = time.time()
for line in open(fn):
    a = list(map(int, line.split()))
    if not a: continue
    j = a[0]
    items = [(a[1 + 2 * k], a[2 + 2 * k]) for k in range(j)]
    Js = [tuple(k for k in range(j) if i in items[k]) for i in range(n)]
    prob = Problem(j, Js, c)
    r = bnb(prob, max_depth=24, time_limit=3600)
    tot += 1; nb += r['boxes']
    if r['status'] != 'PROVED':
        fails += 1
        print("NOT PROVED", items, r['status'], r.get('box'), flush=True)
print(f"file {fn}: {tot} patterns, {nb} boxes, not proved {fails}, {time.time()-t0:.1f}s", flush=True)
