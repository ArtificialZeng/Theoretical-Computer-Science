#!/usr/bin/env python3
"""Enumerate 2-sparse sparsity patterns (multisets of relevant sets of size 1 or 2 over n functions)
with j items, up to relabelling of the functions, by augmentation: every j-pattern minus one item
is a (j-1)-pattern, so adding one relevant set in all ways to all canonical (j-1)-patterns and
canonicalising gives all canonical j-patterns.

Canonical form: minimum over all n! relabellings of the multiplicity vector read as a base-8 number
(digit position = index of the relevant set), computed exactly as two base-8 halves in float64
BLAS matmuls (all partial sums are integers < 2^53, hence exact).

Completeness check (printed): sum of orbit sizes = number of labelled multisets C(R+j-1, j).
usage: python3 -I patterns_aug_claude.py n jmax outprefix
writes outprefix_j{j}.txt with lines "j a1 b1 ... " (b=-1 private), items sorted by relevant set.
"""
import itertools, sys
from math import comb
import numpy as np

n, jmax, outp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
rel = [(a,) for a in range(n)] + [(a, b) for a in range(n) for b in range(a + 1, n)]
R = len(rel)
idx = {r: k for k, r in enumerate(rel)}
perms = list(itertools.permutations(range(n)))
P = len(perms)
sigma = np.zeros((P, R), dtype=np.int64)
for pi, perm in enumerate(perms):
    for k, r in enumerate(rel):
        sigma[pi, k] = idx[tuple(sorted(perm[v] for v in r))]
H = (R + 1) // 2  # digit positions >= H go to the high half
assert jmax <= 7 and 8 ** (R - H) * 8 < 2 ** 52
Mhi = np.zeros((R, P)); Mlo = np.zeros((R, P))
for pi in range(P):
    for k in range(R):
        s = sigma[pi, k]
        if s >= H: Mhi[k, pi] = 8.0 ** (s - H)
        else: Mlo[k, pi] = 8.0 ** s

def canon(C):
    """C: B x R count matrix (float). returns list of (hi, lo) canonical codes."""
    hi = C @ Mhi; lo = C @ Mlo
    hmin = hi.min(axis=1)
    lo2 = np.where(hi == hmin[:, None], lo, np.inf)
    lmin = lo2.min(axis=1)
    return list(zip(hmin.astype(np.int64).tolist(), lmin.astype(np.int64).tolist()))

def decode(code):
    hi, lo = code
    c = np.zeros(R)
    for s in range(R):
        if s >= H: c[s] = (hi // 8 ** (s - H)) % 8
        else: c[s] = (lo // 8 ** s) % 8
    return c

cur = {(0, 0)}  # j = 0
for j in range(1, jmax + 1):
    base = [decode(cd) for cd in sorted(cur)]
    cands = []
    for c in base:
        for r in range(R):
            c2 = c.copy(); c2[r] += 1; cands.append(c2)
    new = set()
    B = 4096
    for s in range(0, len(cands), B):
        new.update(canon(np.array(cands[s:s + B])))
    cur = new
    # completeness check: orbit sizes
    orbit = 0
    codes = sorted(cur)
    for s in range(0, len(codes), 512):
        Cs = np.array([decode(cd) for cd in codes[s:s + 512]])
        hi = Cs @ Mhi; lo = Cs @ Mlo
        for t in range(len(Cs)):
            orbit += len(set(zip(hi[t].tolist(), lo[t].tolist())))
    ok = orbit == comb(R + j - 1, j)
    print(f"n={n} j={j}: {len(cur)} patterns; orbit sum {orbit} vs labelled {comb(R + j - 1, j)}: {ok}",
          file=sys.stderr, flush=True)
    assert ok
    with open(f"{outp}_j{j}.txt", "w") as f:
        for cd in codes:
            c = decode(cd)
            toks = [str(j)]
            for k in range(R):
                for _ in range(int(c[k])):
                    r = rel[k]
                    toks += [str(r[0]), str(r[1]) if len(r) == 2 else "-1"]
            f.write(" ".join(toks) + "\n")
