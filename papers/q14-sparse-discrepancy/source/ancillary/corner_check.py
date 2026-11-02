#!/usr/bin/env python3
"""
Corner analysis for K_n (n odd 2-Lipschitz functions on a common cube).
Lemma 9 of Hollender et al. gives a fractional point with <= n fractional coordinates at which
all multilinear extensions vanish.  The 2^n roundings of the fractional coordinates form a
subcube; each g_i restricted to it is 2-Lipschitz with weighted mean 0 (product weights).
If for every product weight vector there is no way for n such functions to make EVERY corner
'bad' (|g_i| > c for some i), then K_n <= c.

For a given weight vector w and a single function, the set of feasible bad patterns
(B+, B-) is decided by an LP.  We then test whether n feasible patterns can cover all corners.
"""
import itertools, sys
import numpy as np
from scipy.optimize import linprog

def cube(n):
    return list(itertools.product([0, 1], repeat=n))

def feasible(n, w, Bp, Bm, c, eps=1e-6):
    C = cube(n)
    N = len(C)
    idx = {x: i for i, x in enumerate(C)}
    A_ub, b_ub = [], []
    for x in C:
        for k in range(n):
            y = list(x); y[k] ^= 1; y = tuple(y)
            if idx[x] < idx[y]:
                r = np.zeros(N); r[idx[x]] = 1; r[idx[y]] = -1
                A_ub.append(r); b_ub.append(2)
                A_ub.append(-r); b_ub.append(2)
    for x in Bp:
        r = np.zeros(N); r[idx[x]] = -1
        A_ub.append(r); b_ub.append(-(c + eps))
    for x in Bm:
        r = np.zeros(N); r[idx[x]] = 1
        A_ub.append(r); b_ub.append(-(c + eps))
    A_eq = [np.array([w[idx[x]] for x in C])]
    res = linprog(np.zeros(N), A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=np.array(A_eq),
                  b_eq=[0.0], bounds=[(None, None)] * N, method="highs")
    return res.status == 0

def maximal_bad_sets(n, w, c):
    C = cube(n)
    N = len(C)
    feas = []
    # enumerate sign patterns in {-1,0,1}^N; prune by monotonicity (subsets of feasible are feasible)
    # simple approach: enumerate supports by decreasing size via DFS
    best = []
    def dfs(i, Bp, Bm):
        if i == N:
            if Bp or Bm:
                best.append((frozenset(Bp), frozenset(Bm)))
            return
        x = C[i]
        # try +, -, 0 ; prune infeasible
        for s in (1, -1, 0):
            if s == 1:
                nBp, nBm = Bp + [x], Bm
            elif s == -1:
                nBp, nBm = Bp, Bm + [x]
            else:
                nBp, nBm = Bp, Bm
            if s != 0 and not feasible(n, w, nBp, nBm, c):
                continue
            dfs(i + 1, nBp, nBm)
    dfs(0, [], [])
    supports = set(frozenset(a | b) for a, b in best)
    # keep maximal supports
    maxi = [s for s in supports if not any(s < t for t in supports)]
    return maxi

def covers(n, sets, k):
    full = frozenset(cube(n))
    for combo in itertools.combinations_with_replacement(sets, k):
        u = frozenset().union(*combo)
        if u == full:
            return combo
    return None

if __name__ == "__main__":
    n = int(sys.argv[1]); c = float(sys.argv[2])
    grid = [float(v) for v in sys.argv[3].split(",")]
    bad = []
    for ps in itertools.product(grid, repeat=n):
        if list(ps) != sorted(ps):
            continue
        # weights: product of Bernoulli(p_k) for coordinate value 1
        w = []
        for x in cube(n):
            pr = 1.0
            for k in range(n):
                pr *= ps[k] if x[k] else (1 - ps[k])
            w.append(pr)
        sets = maximal_bad_sets(n, w, c)
        cov = covers(n, sets, n)
        if cov:
            bad.append((ps, cov))
            print("BAD CONFIG at p=", ps, [sorted(s) for s in cov], flush=True)
    print("done; bad configs:", len(bad))
