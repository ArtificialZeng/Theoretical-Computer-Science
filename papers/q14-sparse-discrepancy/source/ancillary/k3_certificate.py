#!/usr/bin/env python3
"""Self-contained exact-arithmetic verification of the finite case analysis behind K_3 <= 2.

This is a dependency-free re-implementation of k3_rigorous_exact.py (same logic, no numpy,
no scipy, no exec).  Run with:  python3 -I k3_certificate.py

Setting (see Section 3 and Appendix A of the paper).  Suppose three odd 2-Lipschitz functions
had no common good corner on the 3-dimensional subcube {0,1}^3 produced by Lemma 9 of
Hollender-Manurangsi-Meka-Suksompong, where the product weights are
    w_y(p) = prod_k (p_k if y_k = 1 else 1 - p_k),   p in (0,1)^3,
and every function has w-weighted mean zero on the subcube.  Then the 8 corners can be
partitioned into parts T_1, T_2, T_3 (some possibly empty), T_i bad for function i, and each
nonempty part is either
  * "one":   one-signed, which forces          E_w[dist(X, T)] > 1,   or
  * "mixed": an antipodal pair {x, xbar}, forcing 1 < E_w[dist(X, x)] < 2.
Each condition reads  sum_y r_y w_y(p) > 0  for an integer row r, a multilinear polynomial in p.
For every one of the 7365 (labelling, type) choices we cover [0,1]^3 by dyadic boxes such that,
on each box, some row is <= 0 at all 8 vertices of the box; since a multilinear polynomial on a
box is a convex combination of its vertex values, that row is <= 0 on the whole box, so the
strict condition fails there.  All arithmetic is exact (fractions.Fraction).
"""
import itertools
from fractions import Fraction as F

C = list(itertools.product([0, 1], repeat=3))  # the 8 corners of the 3-cube


def d(x, y):
    return sum(a != b for a, b in zip(x, y))


def dist_set(y, T):
    return min(d(y, t) for t in T)


def rows_for(choice):
    R = []
    for ch in choice:
        if ch is None:
            continue
        typ, P = ch
        if typ == "one":
            R.append([dist_set(y, P) - 1 for y in C])        # E[dist(X,P)] - 1 > 0
        else:
            x = P[0]
            R.append([d(y, x) - 1 for y in C])               # E[dist(X,x)] - 1 > 0
            R.append([2 - d(y, x) for y in C])               # 2 - E[dist(X,x)] > 0
    return R


def wvec(p):
    out = []
    for y in C:
        v = F(1)
        for k in range(3):
            v *= p[k] if y[k] else (1 - p[k])
        out.append(v)
    return out


VERT = list(itertools.product([0, 1], repeat=3))


def cleared(R, lo, hi):
    Ws = [wvec([lo[k] + c[k] * (hi[k] - lo[k]) for k in range(3)]) for c in VERT]
    return any(all(sum(ri * wi for ri, wi in zip(r, w)) <= 0 for w in Ws) for r in R)


def all_choices():
    choices = []
    for lab in itertools.product(range(3), repeat=8):
        parts = [[C[i] for i in range(8) if lab[i] == j] for j in range(3)]
        opts = []
        for P in parts:
            if not P:
                opts.append([None])
            else:
                o = [("one", P)]
                if len(P) == 2 and d(P[0], P[1]) == 3:
                    o.append(("mixed", P))
                opts.append(o)
        choices.extend(itertools.product(*opts))
    return choices


def main():
    choices = all_choices()
    boxes = fails = maxdepth = 0
    for choice in choices:
        R = rows_for(choice)
        stack = [([F(0)] * 3, [F(1)] * 3, 0)]
        while stack:
            lo, hi, depth = stack.pop()
            boxes += 1
            maxdepth = max(maxdepth, depth)
            if cleared(R, lo, hi):
                continue
            if depth > 16:
                fails += 1
                print("FAIL", choice, lo, hi)
                break
            k = max(range(3), key=lambda i: hi[i] - lo[i])
            mid = (lo[k] + hi[k]) / 2
            hi1 = list(hi); hi1[k] = mid
            lo2 = list(lo); lo2[k] = mid
            stack.append((lo, hi1, depth + 1))
            stack.append((lo2, hi, depth + 1))
    print("choices", len(choices), "boxes", boxes, "max_depth", maxdepth, "fails", fails)
    print("VERIFIED: no product weight admits a bad cover" if fails == 0 else "NOT VERIFIED")


if __name__ == "__main__":
    main()
