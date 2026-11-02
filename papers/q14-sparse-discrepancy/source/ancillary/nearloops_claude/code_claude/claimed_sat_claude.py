#!/usr/bin/env python3
"""Consistency checks (dense2_claude): leveled instances that the new cheap-deletion rule claims
to be good are tested with the cover SAT encoding (paper Lemma lem:cover, D_v = l_v + 1).
UNSAT = good (consistent with the claim); SAT = counterexample (would refute the claim)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from levelsat_copy_claude import run, multigraph

def inst(name):
    if name == "K4_3222_b2":
        E = {(0,1):2,(0,2):2,(0,3):2,(1,2):2,(1,3):2,(2,3):2}; return multigraph(4, E), [3,2,2,2]
    if name == "fan6_b2":   # apex 0, path 1-2-3-4-5; spokes size 2, path edges size 1
        E = {(0,i):2 for i in range(1,6)}; E.update({(i,i+1):1 for i in range(1,5)}); return multigraph(6, E), [2]*6
    if name == "fan6_b1p":  # spokes 1, path 2, private items on apex
        E = {(0,i):1 for i in range(1,6)}; E.update({(i,i+1):2 for i in range(1,5)}); return multigraph(6, E, {0:2}), [2]*6
    if name == "2tree7":    # 2-tree: triangles glued along edges
        E = {}
        edges = [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6)]
        for e in edges: E[e] = 1
        return multigraph(7, E, {0:1,6:1}), [2]*7
    if name == "K7_level3":
        E = {(i,j):1 for i in range(7) for j in range(i+1,7)}; return multigraph(7, E), [3]*7
    if name == "K6_33333_3":
        E = {(i,j):1 for i in range(6) for j in range(i+1,6)}; E[(0,1)] = 2; E[(2,3)] = 2; return multigraph(6, E), [3]*6
    if name == "octa_b1_level3":  # K_{2,2,2}
        V = range(6); E = {(i,j):1 for i in V for j in V if i<j and not (i//2 == j//2)}
        return multigraph(6, E, {0:1,2:1,4:1}), [3]*6
    raise SystemExit(name)

for name in sys.argv[1:]:
    items, levels = inst(name)
    r, data = run(items, levels, verbose=False, timeout=7200)
    print(name, "m=%d" % len(items), "levels", levels, "->", r, (data[1] if data else ""))
    sys.stdout.flush()
