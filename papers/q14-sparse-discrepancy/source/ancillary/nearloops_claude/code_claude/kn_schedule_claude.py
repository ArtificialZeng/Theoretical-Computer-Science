#!/usr/bin/env python3
"""Best uniform level C for K_n reachable with: cheap deletion (Lemma G: h exempts up to l_h>=2
neighbours, others pay one level, all neighbours need level>=2), and the base 'at most 5 vertices,
all levels >= 2' (paper Thm H) or 'K_2 with levels (>=1,>=2)' or a single vertex.  (dense2_claude)"""
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def good(state):
    m = len(state)
    if m <= 1:
        return all(l >= 1 for l in state)
    if m <= 5 and min(state) >= 2:
        return True
    if m == 2 and min(state) >= 1 and max(state) >= 2:
        return True
    for i in set(range(m)):
        lh = state[i]
        others = list(state[:i] + state[i+1:])
        if min(others) < 2:
            continue
        if lh < 1:
            continue
        k = min(lh, m - 1) if lh >= 2 else 0
        others.sort()
        # cheap: the k lowest; payers: the rest
        new = others[:k] + [l - 1 for l in others[k:]]
        if good(tuple(sorted(new))):
            return True
    return False

for n in range(2, 41):
    C = 1
    while not good(tuple([C] * n)):
        C += 1
    print(n, C, "(paper: %s)" % (str(n - 3) if n >= 6 else "2"))
