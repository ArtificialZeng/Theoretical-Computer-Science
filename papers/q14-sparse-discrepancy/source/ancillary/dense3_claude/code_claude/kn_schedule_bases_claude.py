#!/usr/bin/env python3
"""Uniform level needed for K_n by cheap deletions (Lemma lem:cheap of the paper: delete h, keep the
levels of |J|<=l_h neighbours (l_h>=2 if J nonempty), lower the others, which need level >= 2)
ending in a base.  Bases: (a) paper: single vertex (level>=1), K_2 with max level >= 2, K_m (m<=5)
with all levels >= 2 [Thm H(b)]; (b) new: K_m (m<=7) all levels >= 2 [corner method, c=2.99],
K_m (m<=6) with one vertex of level 1 and the others >= 2 [leveled corner method].
usage: python3 -I kn_schedule_bases_claude.py {paper|new} nmax [m2 m1]
  new: bases K_m (m<=m2) all levels >= 2, K_m (m<=m1) with one level-1 vertex (defaults 7, 6)"""
import sys
from functools import lru_cache
MODE, NMAX = sys.argv[1], int(sys.argv[2])
M2, M1 = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (7, 6)
@lru_cache(maxsize=None)
def good(state):
    m = len(state)
    if m == 0: return True
    if min(state) < 1: return False
    if m == 1: return True
    if m == 2 and max(state) >= 2: return True
    if MODE == "paper" and m <= 5 and min(state) >= 2: return True
    if MODE == "new":
        if m <= M2 and min(state) >= 2: return True
        if m <= M1 and sorted(state)[1] >= 2: return True   # at most one level-1 vertex
    for i in range(m):
        lh = state[i]
        others = sorted(state[:i] + state[i + 1:])
        k = min(lh, m - 1) if lh >= 2 else 0
        cheap, pay = others[:k], others[k:]
        if pay and min(pay) < 2: continue
        if good(tuple(sorted(cheap + [l - 1 for l in pay]))): return True
    return False
for n in range(2, NMAX + 1):
    C = 1
    while not good(tuple([C] * n)): C += 1
    print(n, C, flush=True)
