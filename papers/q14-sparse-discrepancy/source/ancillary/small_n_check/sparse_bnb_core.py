#!/usr/bin/env python3
"""
Sparse corner branch-and-bound with a DFS cover search (no subset enumeration), for larger
local cubes.  Same necessary conditions as sparse_bnb.py:
  bad part of g_i = U+ u U- (local patterns), d(U+,U-) >= floor(c)+1,
  for each nonempty part: max over box vertices of E_w[d_{J_i}(X,U)] > c/2  (downward closed).
A cover = one bad part per function whose lifts cover {0,1}^j.  If no cover exists in a box,
the box is cleared.  Exact integer arithmetic at dyadic box vertices.
usage: python3 -I -B sparse_bnb_dfs.py n t c maxdepth [j]
"""
import itertools, sys
from fractions import Fraction as Fr
n = t = maxdepth = dmix = thr_num = thr_den = None
c = None
def setup(n_, t_, c_, maxdepth_):
    global n, t, c, maxdepth, dmix, thr_num, thr_den
    n, t, c, maxdepth = n_, t_, Fr(c_), maxdepth_
    dmix = int(c) + 1
    thr_num, thr_den = (c / 2).numerator, (c / 2).denominator

def canon(pattern):
    best = None
    for perm in itertools.permutations(range(n)):
        key = tuple(sorted(tuple(sorted(perm[i] for i in R)) for R in pattern))
        if best is None or key < best: best = key
    return best

def run_pattern(pattern, j):
    J = [[k for k in range(j) if i in pattern[k]] for i in range(n)]
    Cj = list(itertools.product([0, 1], repeat=j)); Nj = len(Cj); full = (1 << Nj) - 1
    loc = []
    for i in range(n):
        d = len(J[i]); L = list(itertools.product([0, 1], repeat=d)); NL = len(L)
        D = [[sum(a != b for a, b in zip(x, y)) for y in L] for x in L]
        proj = [L.index(tuple(x[k] for k in J[i])) if d else 0 for x in Cj]
        lift = [0] * NL
        for gi in range(Nj): lift[proj[gi]] |= 1 << gi
        loc.append((d, NL, D, proj, lift))
    active = [i for i in range(n) if loc[i][0] > 0]
    def cleared(lo, hi, depth):
        den = 1 << (depth + 1)
        verts = list(itertools.product([0, 1], repeat=j))
        Pv = [[int((lo[k] + v[k] * (hi[k] - lo[k])) * den) for k in range(j)] for v in verts]
        Ws = {}; scales = {}
        for i in active:
            d, NL, D, proj, lift = loc[i]
            L = list(itertools.product([0, 1], repeat=d))
            W = []
            for pi in Pv:
                w = []
                for y in L:
                    prod = 1
                    for kk, k in enumerate(J[i]):
                        prod *= pi[k] if y[kk] else (den - pi[k])
                    w.append(prod)
                W.append(w)
            # deduplicate weight vectors
            Ws[i] = [list(x) for x in set(tuple(w) for w in W)]
            scales[i] = den ** d
        # state per function: (setmask+, dmin+, setmask-, dmin-)
        INF = 99
        def feasible(i, dmin):
            sc = scales[i]
            for w in Ws[i]:
                if sum(a * b for a, b in zip(w, dmin)) * thr_den > thr_num * sc: return True
            return False
        state = {i: [0, None, 0, None] for i in active}
        def try_add(i, y, sgn):
            d, NL, D, proj, lift = loc[i]
            st = state[i]
            mine = 0 if sgn > 0 else 2
            other = 2 if sgn > 0 else 0
            if (st[mine] >> y) & 1: return None
            # cross distance
            om = st[other]
            if om:
                for x in range(NL):
                    if (om >> x) & 1 and D[x][y] < dmix: return None
            old = st[mine + 1]
            new = [D[y][z] for z in range(NL)] if old is None else [min(a, D[y][z]) for z, a in enumerate(old)]
            if not feasible(i, new): return None
            saved = (st[mine], st[mine + 1])
            st[mine] |= 1 << y; st[mine + 1] = new
            return saved, mine
        def undo(i, saved, mine):
            state[i][mine], state[i][mine + 1] = saved
        def covered_by(i):
            d, NL, D, proj, lift = loc[i]
            m = state[i][0] | state[i][2]; g = 0
            for y in range(NL):
                if (m >> y) & 1: g |= lift[y]
            return g
        def dfs(cov):
            if cov == full: return True
            u = (~cov) & full; e = (u & -u).bit_length() - 1
            for i in active:
                y = loc[i][3][e]
                for sgn in (1, -1):
                    r = try_add(i, y, sgn)
                    if r is None: continue
                    saved, mine = r
                    newcov = cov | loc[i][4][y]
                    ok = dfs(newcov)
                    undo(i, saved, mine)
                    if ok: return True
            return False
        return not dfs(0)
    stack = [([Fr(0)] * j, [Fr(1, 2)] * j, 0)]
    boxes = 0; fails = 0
    while stack:
        lo, hi, dd = stack.pop(); boxes += 1
        if cleared(lo, hi, dd + 1): continue
        if dd >= maxdepth: fails += 1; continue
        k = max(range(j), key=lambda i: hi[i] - lo[i]); mid = (lo[k] + hi[k]) / 2
        h1 = list(hi); h1[k] = mid; l2 = list(lo); l2[k] = mid
        stack.append((lo, h1, dd + 1)); stack.append((l2, hi, dd + 1))
    return boxes, fails

