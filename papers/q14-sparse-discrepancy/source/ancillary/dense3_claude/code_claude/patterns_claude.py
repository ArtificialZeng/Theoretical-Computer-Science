#!/usr/bin/env python3
"""Enumerate all 2-sparse sparsity patterns of j items on n functions (each item relevant to a
set of 1 or 2 functions), up to relabelling of the functions (items are unordered: a pattern is a
multiset of relevant sets).  Canonical form = minimum over all n! relabellings of the base-(j+1)
encoding of the multiplicity vector over the relevant sets.

usage: python3 -I patterns_claude.py n j  > file      (one pattern per line: "j a1 b1 a2 b2 ..."
       with b = -1 for a private item)
A completeness check (sum of orbit sizes = number of labelled multisets) is printed to stderr.
"""
import itertools, sys
from math import comb
import numpy as np

n, j = int(sys.argv[1]), int(sys.argv[2])
rel = [(a,) for a in range(n)] + [(a, b) for a in range(n) for b in range(a + 1, n)]
R = len(rel)
idx = {r: k for k, r in enumerate(rel)}
perms = list(itertools.permutations(range(n)))
P = len(perms)
base = j + 1
# sigma[p][r] = index of the image of relevant set r under permutation p
sigma = np.zeros((P, R), dtype=np.int64)
for pi, perm in enumerate(perms):
    for k, r in enumerate(rel):
        sigma[pi, k] = idx[tuple(sorted(perm[v] for v in r))]
assert base ** R < 2 ** 62, "encoding overflow"
powr = np.array([base ** k for k in range(R)], dtype=np.int64)
M = powr[sigma].T  # R x P : M[r, p] = base^{sigma_p(r)}

combos = list(itertools.combinations_with_replacement(range(R), j))
total_labelled = len(combos)
assert total_labelled == comb(R + j - 1, j)
canon_codes = set()
B = 20000
for s in range(0, len(combos), B):
    chunk = combos[s:s + B]
    C = np.zeros((len(chunk), R), dtype=np.int64)
    for t, cmb in enumerate(chunk):
        for r in cmb:
            C[t, r] += 1
    codes = C @ M  # len x P
    canon_codes.update(codes.min(axis=1).tolist())

# completeness: orbit sizes
orbit_sum = 0
out = []
for code in sorted(canon_codes):
    cnt = []
    x = code
    for k in range(R):
        cnt.append(x % base); x //= base
    cnt = np.array(cnt, dtype=np.int64)
    orbit = set((cnt @ M).tolist())
    orbit_sum += len(orbit)
    items = []
    for k in range(R):
        items += [rel[k]] * int(cnt[k])
    out.append(items)
print(f"n={n} j={j}: {len(out)} patterns; orbit sum {orbit_sum} = labelled {total_labelled}: "
      f"{orbit_sum == total_labelled}", file=sys.stderr)
for items in out:
    toks = [str(j)]
    for r in items:
        toks += [str(r[0]), str(r[1]) if len(r) == 2 else "-1"]
    print(" ".join(toks))
