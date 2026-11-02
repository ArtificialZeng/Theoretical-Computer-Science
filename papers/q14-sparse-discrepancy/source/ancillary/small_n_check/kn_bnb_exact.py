# Exact-arithmetic version of kn_bnb.py: box vertices are dyadic rationals; all comparisons in integers.
import itertools, numpy as np, sys
from fractions import Fraction as Fr
n = int(sys.argv[1]); j = int(sys.argv[2]); c = Fr(sys.argv[3]); maxdepth = int(sys.argv[4])
C = list(itertools.product([0, 1], repeat=j)); N = len(C)
Dm = np.array([[sum(a != b for a, b in zip(x, y)) for y in C] for x in C], dtype=np.int64)
M = 1 << N
masks = np.arange(M)
dT = np.full((M, N), 99, dtype=np.int64)
for i in range(N):
    sel = ((masks >> i) & 1) == 1
    dT[sel] = np.minimum(dT[sel], Dm[i][None, :])
dT = dT[1:]
anti = [(i, C.index(tuple(1 - b for b in C[i]))) for i in range(N)]
anti = [(a, b) for a, b in anti if a < b]
mixed_allowed = (j > c)
VERT = list(itertools.product([0, 1], repeat=j))
full = M - 1
def cleared(lo, hi, depth):
    # lo, hi: lists of Fractions with denominator dividing 2^(depth+1)
    den = 1 << (depth + 1)
    # integer weights scaled by den^j
    Wv = []
    for v in VERT:
        p = [lo[k] + v[k] * (hi[k] - lo[k]) for k in range(j)]
        pi = [int(pk * den) for pk in p]
        assert all(Fr(pi[k], den) == p[k] for k in range(j))
        w = []
        for y in C:
            prod = 1
            for k in range(j):
                prod *= pi[k] if y[k] else (den - pi[k])
            w.append(prod)
        Wv.append(w)
    Wv = np.array(Wv, dtype=object).astype(np.int64)      # values < den^j
    scale = den ** j
    E2 = Wv @ dT.T                                         # = scale * E[d]
    thr_num, thr_den = (c / 2).numerator, (c / 2).denominator
    # feasible if max E > c/2  <=>  max(E2)*thr_den > thr_num*scale
    feas = E2.max(axis=0) * thr_den > thr_num * scale
    sets = list((np.nonzero(feas)[0] + 1))
    if mixed_allowed:
        up_num = (Fr(j) - c / 2)
        for (a, b) in anti:
            e = Wv @ Dm[a]
            if e.max() * thr_den > thr_num * scale and e.min() * up_num.denominator < up_num.numerator * scale:
                sets.append((1 << a) | (1 << b))
    if not sets: return True
    sets = sorted(set(int(s) for s in sets), key=lambda m: -bin(m).count("1"))
    maxi = []
    for m in sets:
        if not any((m & Mx) == m for Mx in maxi):
            maxi.append(m)
    by_elem = [[m for m in maxi if (m >> e) & 1] for e in range(N)]
    def dfs(cov, k):
        if cov == full: return True
        if k == 0: return False
        u = (~cov) & full; e = (u & -u).bit_length() - 1
        for m in by_elem[e]:
            if dfs(cov | m, k - 1): return True
        return False
    return not dfs(0, n)
stack = [([Fr(0)] * j, [Fr(1, 2)] * j, 0)]
boxes = 0; fails = 0
while stack:
    lo, hi, d = stack.pop(); boxes += 1
    if cleared(lo, hi, d + 1): continue
    if d >= maxdepth:
        fails += 1; continue
    k = max(range(j), key=lambda i: hi[i] - lo[i]); mid = (lo[k] + hi[k]) / 2
    h1 = list(hi); h1[k] = mid; l2 = list(lo); l2[k] = mid
    stack.append((lo, h1, d + 1)); stack.append((l2, hi, d + 1))
print(f"EXACT n={n} j={j} c={c}: boxes={boxes} uncleared={fails}")
