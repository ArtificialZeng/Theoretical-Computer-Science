#!/usr/bin/env python3
"""K_n schedules if cheap neighbours may have level 1 (conditional on the level-1 near-loop
transfer).  Payers need level >= 2; h needs level >= 2 if J nonempty, else >= 1.
Bases: single vertex; K_2 with (>=1,>=2); with/without the five-vertex base (all >= 2)."""
import sys
from functools import lru_cache
USE_H = len(sys.argv) > 1 and sys.argv[1] == "H"
@lru_cache(maxsize=None)
def good(state):
    m = len(state)
    if m <= 1: return all(l >= 1 for l in state)
    if USE_H and m <= 5 and min(state) >= 2: return True
    if m == 2 and min(state) >= 1 and max(state) >= 2: return True
    for i in range(m):
        lh = state[i]
        others = sorted(state[:i] + state[i+1:])
        if lh < 1: continue
        k = min(lh, m - 1) if lh >= 2 else 0
        # payers = the m-1-k highest; they need level >= 2; cheap ones need >= 1
        cheap = others[:k]; pay = others[k:]
        if pay and min(pay) < 2: continue
        new = tuple(sorted(cheap + [l - 1 for l in pay]))
        if good(new): return True
    return False
for n in range(2, 31):
    C = 1
    while not good(tuple([C] * n)): C += 1
    print(n, C)
