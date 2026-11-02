#!/usr/bin/env python3
"""Consistency checks for v4 claims that use level-1 cheap neighbours (dense2_claude): cover-SAT
(paper Lemma lem:cover with D_v = l_v + 1).  UNSAT = good (consistent)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from levelsat_copy_claude import run, multigraph
tests = {
 "C4_2121_b3": (multigraph(4, {(0,1):3,(1,2):3,(2,3):3,(3,0):3}), [2,1,2,1]),
 "tri_122_b3": (multigraph(3, {(0,1):3,(1,2):3,(0,2):3}), [1,2,2]),
 "W4_level2_b2": (multigraph(5, {(0,1):2,(1,2):2,(2,3):2,(3,0):2,(0,4):2,(1,4):2,(2,4):2,(3,4):2}), [2]*5),
 "K4_level2_b3": (multigraph(4, {(0,1):3,(0,2):3,(0,3):3,(1,2):3,(1,3):3,(2,3):3}), [2]*4),
 "W5_level2_b2spokes": (multigraph(6, {(0,1):1,(1,2):1,(2,3):1,(3,4):1,(4,0):1,(0,5):2,(1,5):2,(2,5):2,(3,5):2,(4,5):2}), [2]*6),
}
for name in sys.argv[1:] or tests:
    items, levels = tests[name]
    r, data = run(items, levels, verbose=False, timeout=3600)
    print(name, "m=%d" % len(items), levels, "->", r, (data[1] if data else "")); sys.stdout.flush()
