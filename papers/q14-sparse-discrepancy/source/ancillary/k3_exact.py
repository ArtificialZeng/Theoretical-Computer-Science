# Exact (LP) check that three functions cannot make every corner of the 3-cube bad (|v|>2),
# for ANY probability weights (not only product weights). See STATUS for the derivation:
# a one-signed bad set T is feasible iff E_w[d(X,T)] > 1; a mixed pair {x+, xbar-} is feasible
# iff 1 < E_w[d(X,x)] < 2.  Shrinking a cover to a partition preserves feasibility.
import itertools
import numpy as np
from scipy.optimize import linprog
C = list(itertools.product([0,1], repeat=3))
def d(x, y): return sum(a != b for a, b in zip(x, y))
def dist_set(y, T): return min(d(y, t) for t in T)
bad = []
count = 0
for lab in itertools.product(range(3), repeat=8):
    parts = [[C[i] for i in range(8) if lab[i] == j] for j in range(3)]
    if lab != min(tuple(sorted(range(3), key=lambda k: k)) and lab, lab):  # no-op placeholder
        pass
    # each part: options = one-signed (if nonempty) or mixed pair (if antipodal pair)
    opts = []
    for P in parts:
        o = []
        if not P:
            o.append(None)
        else:
            o.append(("one", P))
            if len(P) == 2 and d(P[0], P[1]) == 3:
                o.append(("mixed", P))
        opts.append(o)
    for choice in itertools.product(*opts):
        # variables: w (8), s (margin). maximize s subject to constraints
        A, b = [], []
        for ch in choice:
            if ch is None: continue
            typ, P = ch
            if typ == "one":
                # sum_y w_y (1 - d(y,P)) + s <= 0
                A.append([1 - dist_set(y, P) for y in C] + [1]); b.append(0)
            else:
                x = P[0]
                A.append([1 - d(y, x) for y in C] + [1]); b.append(0)          # E[d] > 1
                A.append([-(2 - d(y, x)) for y in C] + [1]); b.append(0)       # E[d] < 2
        count += 1
        res = linprog(c=[0]*8 + [-1], A_ub=A, b_ub=b, A_eq=[[1]*8 + [0]], b_eq=[1],
                      bounds=[(0, 1)]*8 + [(None, 1)], method="highs")
        if res.status == 0 and -res.fun > 1e-9:
            bad.append((lab, choice, res.x))
print("LPs:", count, "feasible covers:", len(bad))
for bb in bad[:5]: print(bb)
