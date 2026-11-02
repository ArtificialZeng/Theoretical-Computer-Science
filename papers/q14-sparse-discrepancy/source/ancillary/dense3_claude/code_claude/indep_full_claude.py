#!/usr/bin/env python3
"""Independent check of K_n <= floor(c) via the paper's own Python checker (verbatim copy
cover_bnb_paper_copy_claude.py): n functions all reading all j <= n fractional items, threshold c.
usage: python3 -I indep_full_claude.py n c"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
import numpy as np
import cover_bnb_paper_copy_claude as cb
from cover_bnb_paper_copy_claude import Problem, bnb
for r in range(7, 9):
    if r not in cb.DT:
        cb.DT[r] = np.array([[cb.POP[u ^ y] for y in range(1 << r)] for u in range(1 << r)], dtype=np.int64)
n = int(sys.argv[1]); c = Fraction(sys.argv[2])
for j in range(1, n + 1):
    t0 = time.time()
    prob = Problem(j, [tuple(range(j))] * n, c, sort_coords=True)
    r = bnb(prob, max_depth=24, time_limit=36000)
    print(f"n={n} c={c} j={j}: {r['status']} boxes={r['boxes']} time={time.time()-t0:.1f}s", flush=True)
