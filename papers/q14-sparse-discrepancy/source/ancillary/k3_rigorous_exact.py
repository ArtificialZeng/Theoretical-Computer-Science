# Same as k3_rigorous.py but with exact rational arithmetic (fractions.Fraction) for the vertex tests.
import itertools
from fractions import Fraction as F
exec(open('k3_exact.py').read().split("bad = []")[0])  # C, d, dist_set
def rows_for(choice):
    R = []
    for ch in choice:
        if ch is None: continue
        typ, P = ch
        if typ == "one":
            R.append([d_ - 1 for d_ in (dist_set(y, P) for y in C)])
        else:
            x = P[0]
            R.append([d(y, x) - 1 for y in C])
            R.append([2 - d(y, x) for y in C])
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
    for r in R:
        if all(sum(ri * wi for ri, wi in zip(r, w)) <= 0 for w in Ws):
            return True
    return False
choices = []
for lab in itertools.product(range(3), repeat=8):
    parts = [[C[i] for i in range(8) if lab[i] == j] for j in range(3)]
    opts = []
    for P in parts:
        o = [None] if not P else [("one", P)] + ([("mixed", P)] if len(P) == 2 and d(P[0], P[1]) == 3 else [])
        opts.append(o)
    for choice in itertools.product(*opts):
        choices.append(choice)
boxes = 0; fails = 0
for choice in choices:
    R = rows_for(choice)
    stack = [([F(0)]*3, [F(1)]*3, 0)]
    while stack:
        lo, hi, depth = stack.pop(); boxes += 1
        if cleared(R, lo, hi): continue
        if depth > 16: fails += 1; print("FAIL", choice, lo, hi); break
        k = max(range(3), key=lambda i: hi[i] - lo[i]); mid = (lo[k] + hi[k]) / 2
        hi1 = list(hi); hi1[k] = mid; lo2 = list(lo); lo2[k] = mid
        stack.append((lo, hi1, depth + 1)); stack.append((lo2, hi, depth + 1))
print("choices", len(choices), "boxes", boxes, "fails", fails)
