#!/usr/bin/env python3
"""
Independent slow brute-force cross-check of cover_bnb.find_cover.
Pure Python + Fractions, explicit enumeration of all possibly-bad (U+,U-) pairs,
maximal sets, then exhaustive cover search.  Shares no code with cover_bnb.
"""
import itertools
from fractions import Fraction
from math import floor


def hamming(a, b):
    return bin(a ^ b).count('1')


def exp_dist(U, r, pvec):
    """E_p d(X,U) for local cube of dim r with Pr[x_t=+1]=pvec[t], U a set of ints."""
    tot = Fraction(0)
    for y in range(1 << r):
        w = Fraction(1)
        for t in range(r):
            w *= pvec[t] if (y >> t) & 1 else 1 - pvec[t]
        tot += w * min(hamming(y, u) for u in U)
    return tot


def possibly_bad_sets(r, verts, c):
    """All U (frozensets) nonempty with max_vertex E d(X,U) > c/2  (down-closed family), plus empty."""
    res = [frozenset()]
    # DFS adding points in increasing order (down-closed so pruning is exact)
    def dfs(U, start):
        for u in range(start, 1 << r):
            V = U | {u}
            if any(exp_dist(V, r, pv) > c / 2 for pv in verts):
                res.append(frozenset(V))
                dfs(V, u + 1)
    dfs(frozenset(), 0)
    return res


def maximal(sets):
    sets = sorted(set(sets), key=lambda s: -len(s))
    out = []
    for s in sets:
        if not any(s <= t for t in out):
            out.append(s)
    return out


def brute_cover(j, Js, c, box):
    """box: list of (lo, hi) Fractions. Returns True iff a cover exists under the relaxation."""
    c = Fraction(c)
    dmin = floor(c) + 1
    N = 1 << j
    per_func = []
    for J in Js:
        r = len(J)
        if r == 0:
            per_func.append([])
            continue
        verts = [list(v) for v in itertools.product(*[sorted({box[k][0], box[k][1]}) for k in J])]
        pb = possibly_bad_sets(r, verts, c)
        Bs = []
        for Up in pb:
            for Um in pb:
                if Up & Um:
                    continue
                if Up and Um and min(hamming(a, b) for a in Up for b in Um) < dmin:
                    continue
                Bs.append(Up | Um)
        Bs = maximal(Bs)
        # lift
        lifted = []
        for B in Bs:
            m = 0
            for x in range(N):
                y = sum(((x >> k) & 1) << t for t, k in enumerate(J))
                if y in B:
                    m |= 1 << x
            lifted.append(m)
        per_func.append(sorted(set(lifted)))
    full = (1 << N) - 1
    # exhaustive with simple pruning by union of remaining maxima
    funcs = [L for L in per_func if L]
    def rec(idx, cov):
        if cov == full:
            return True
        if idx == len(funcs):
            return False
        rest = 0
        for L in funcs[idx:]:
            for m in L:
                rest |= m
        if cov | rest != full:
            return False
        for m in funcs[idx]:
            if rec(idx + 1, cov | m):
                return True
        return False
    return rec(0, 0)
