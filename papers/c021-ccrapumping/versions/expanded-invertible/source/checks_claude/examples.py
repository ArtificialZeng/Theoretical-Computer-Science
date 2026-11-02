"""Explicit examples for the invertible-sector characterization.

For each example: build a (possibly non-minimal) weighted representation, minimize it,
check invertibility, run the group criterion, and for YES examples verify an explicit
diagonal-affine group-controlled CCRA (registers never interact) on all words up to length L.
"""
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import sys
from fractions import Fraction as Fr
from wa import *
from groupcheck import criterion, letters_invertible

L = 7
def M(rows):
    return [[Fr(x) for x in r] for r in rows]

def check_equal(f, g, alph, L=L):
    for w in words(alph, L):
        if f(w) != g(w):
            return False, w
    return True, None

def report(name, lam, Ms, gam, expect, ccra=None, func=None):
    lam2, Ms2, gam2 = minimize(lam, Ms, gam)
    d = len(lam2)
    inv_ok = letters_invertible(Ms2)
    ok, info = criterion(Ms2) if inv_ok else (None, "singular")
    line = f"[{name}] minimal dim {d}, invertible={inv_ok}, criterion={ok} ({info}), expected={expect}"
    if func is not None:
        e, w = check_equal(lambda w: evalw(lam, Ms, gam, w), func, list(Ms))
        line += f"; WA==closed form up to len {L}: {e}" + ("" if e else f" (fails at {w})")
    if ccra is not None:
        assert ccra.is_copyless()
        e, w = check_equal(lambda w: evalw(lam, Ms, gam, w), ccra.run, list(Ms))
        line += f"; WA==CCRA up to len {L}: {e}" + ("" if e else f" (fails at {w})")
        # exact equivalence via minimization of the difference
        l1, M1, g1 = ccra.representation()
        n0, n1 = len(lam), len(l1)
        Md = {a: [[Ms[a][i][j] if i < n0 and j < n0 else (M1[a][i - n0][j - n0] if i >= n0 and j >= n0 else Fr(0))
                   for j in range(n0 + n1)] for i in range(n0 + n1)] for a in Ms}
        ld = list(lam) + list(l1)
        gd = list(gam) + [-x for x in g1]
        lz, _, _ = minimize(ld, Md, gd)
        line += f"; exact equivalence (difference has minimal dim {len(lz)})"
    print(line)
    sys.stdout.flush()
    return ok

results = {}

# E1 alternating sum f = sum_i (-1)^i b_i ; state (f, s), s=(-1)^j.  Row convention.
# column update for appending b:  f' = f - s b, s' = -s.  f(w) = e_f^T A_{w_n}...A_{w_1} (0,1)^T.
# Use transposed row representation: lam = (0,1), M_b = A_b^T, gam = e_f.
def Acol(b):
    return M([[1, -b], [0, -1]])
E1 = {str(b): transpose(Acol(b)) for b in (0, 1)}
def f1(w):
    return sum(((-1) ** (i + 1)) * int(c) for i, c in enumerate(w))
# CCRA: one register x, control parity p in {0,1}: on '1' at position i (1-based): x += (-1)^i.
def P(*polys):
    return tuple(polys)
x = pvar(0)
d1 = {}
for p in (0, 1):
    for b in ("0", "1"):
        sign = -1 if p == 0 else 1  # next position index i = (#read)+1; parity p = (#read) mod 2; (-1)^i = -1 if p==0
        upd = padd(x, pconst(sign * int(b)))
        d1[(p, b)] = (1 - p, P(upd))
C1 = CCRA([0, 1], 0, 1, ["0", "1"], d1, [0], {0: x, 1: x})
results["E1"] = report("E1 alternating sum", [Fr(0), Fr(1)], E1, [Fr(1), Fr(0)], True, ccra=C1, func=f1)

# E2 MPS Example 27: g(w) = sum_i 2^{k_i} over positions of 1's.  column (g, p): g' = g + 2 b p, p' = 2p
def A2(b):
    return M([[1, 2 * b], [0, 2]])
E2 = {str(b): transpose(A2(b)) for b in (0, 1)}
def f2(w):
    return sum(2 ** (i + 1) for i, c in enumerate(w) if c == "1")
# normal form: h := h/2 + b (h = g/2^j), p := 2p, output h*p   (registers never interact)
h, p_ = pvar(0), pvar(1)
d2 = {(0, "0"): (0, P(padd({}, h, Fr(1, 2)), padd({}, p_, Fr(2)))),
      (0, "1"): (0, P(padd(pconst(1), h, Fr(1, 2)), padd({}, p_, Fr(2))))}
C2 = CCRA([0], 0, 2, ["0", "1"], d2, [0, 1], {0: pmul(h, p_)})
results["E2"] = report("E2 MPS Ex.27 sum 2^k_i", [Fr(0), Fr(1)], E2, [Fr(1), Fr(0)], True, ccra=C2, func=f2)

# E3 position sum (MPS Example 26 / original witness): NO
def A3(b):
    return M([[1, b, b], [0, 1, 1], [0, 0, 1]])
E3 = {str(b): transpose(A3(b)) for b in (0, 1)}
def f3(w):
    return sum((i + 1) * int(c) for i, c in enumerate(w))
results["E3"] = report("E3 position sum", [Fr(0), Fr(0), Fr(1)], E3, [Fr(1), Fr(0), Fr(0)], False, func=f3)

# E4 MPS Example 17 (polynomially ambiguous, invertible, not CCRA): states 1,2,3
E4 = {"a": M([[2, 2, 0], [0, 2, 0], [0, 0, 1]]), "b": M([[1, 0, 0], [0, 1, 1], [0, 0, 1]])}
results["E4"] = report("E4 MPS Ex.17", [Fr(1), Fr(0), Fr(0)], E4, [Fr(0), Fr(0), Fr(1)], False)

# E5 alternating position sum sum_i (-1)^i i b_i : NO
# column (f, q, s): q = s*j, s = (-1)^j ; f' = f - b(q+s), q' = -q - s, s' = -s
def A5(b):
    return M([[1, -b, -b], [0, -1, -1], [0, 0, -1]])
E5 = {str(b): transpose(A5(b)) for b in (0, 1)}
def f5(w):
    return sum(((-1) ** (i + 1)) * (i + 1) * int(c) for i, c in enumerate(w))
results["E5"] = report("E5 alternating position sum", [Fr(0), Fr(0), Fr(1)], E5, [Fr(1), Fr(0), Fr(0)], False, func=f5)

# E6 scaled Heisenberg: M_a = 2(I+E12), M_b = 3(I+E23).  Unipotent elements of the group commute
# (they lie in the centre), but unipotent parts of M_a, M_b do not: NO.
E6 = {"a": M([[2, 2, 0], [0, 2, 0], [0, 0, 2]]), "b": M([[3, 0, 0], [0, 3, 3], [0, 0, 3]])}
results["E6"] = report("E6 scaled Heisenberg", [Fr(1), Fr(0), Fr(0)], E6, [Fr(0), Fr(0), Fr(1)], False)

# E7 Baumslag-Solitar type: one register x, a: x:=2x, b: x:=x+1, output x, x0=0 (YES)
x = pvar(0)
d7 = {(0, "a"): (0, P(padd({}, x, Fr(2)))), (0, "b"): (0, P(padd(x, pconst(1))))}
C7 = CCRA([0], 0, 1, ["a", "b"], d7, [0], {0: x})
l7, M7, g7 = C7.representation()
results["E7"] = report("E7 BS(1,2) type", l7, M7, g7, True, ccra=C7)

# E8 S3-twisted counters (quasi-unipotent, YES).  Control: S3 acting on {0,1,2}; a = transposition (0 1),
# b = 3-cycle.  Registers count n_{g,a}; output depends on sign of control state.
import itertools as it
S3 = list(it.permutations(range(3)))
def compose(p, q):  # first p then q
    return tuple(q[p[i]] for i in range(3))
gen = {"a": (1, 0, 2), "b": (1, 2, 0)}
def sign(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s
# registers: r0 counts a read in states of sign +1, r1 counts b read in states with p[0]==0,
# r2 counts a read in states with p[2]==2 (copy), r3 = copy of r0
nr = 4
xs = [pvar(i) for i in range(nr)]
d8 = {}
for q in S3:
    for a in "ab":
        inc = [0] * nr
        if a == "a" and sign(q) == 1:
            inc[0] = inc[3] = 1
        if a == "b" and q[0] == 0:
            inc[1] = 1
        if a == "a" and q[2] == 2:
            inc[2] = 1
        d8[(q, a)] = (compose(q, gen[a]), P(*[padd(xs[i], pconst(inc[i])) for i in range(nr)]))
out8 = {}
for q in S3:
    if sign(q) == 1:
        out8[q] = padd(pmul(xs[0], xs[1]), pconst(q[0]))
    else:
        out8[q] = padd(pmul(pmul(xs[0], xs[3]), xs[2]), xs[1], Fr(-2))
C8 = CCRA(S3, (0, 1, 2), nr, ["a", "b"], d8, [0] * nr, out8)
l8, M8, g8 = C8.representation()
results["E8"] = report("E8 S3-twisted counters", l8, M8, g8, True, ccra=C8)

# E9 group-controlled torus + translations: Z/2 control, register x: in state 0, a: x:=2x+1, b: x:=x;
# in state 1, a: x:=x/3, b: x:=x-1 ; register y: y:=-y on a. output x*y in state 0, x in state 1.
x, y = pvar(0), pvar(1)
d9 = {(0, "a"): (1, P(padd(pconst(1), x, Fr(2)), padd({}, y, Fr(-1)))),
      (0, "b"): (0, P(x, y)),
      (1, "a"): (0, P(padd({}, x, Fr(1, 3)), padd({}, y, Fr(-1)))),
      (1, "b"): (1, P(padd(x, pconst(-1)), y))}
C9 = CCRA([0, 1], 0, 2, ["a", "b"], d9, [1, 1], {0: pmul(x, y), 1: x})
l9, M9, g9 = C9.representation()
results["E9"] = report("E9 Z2-controlled affine", l9, M9, g9, True, ccra=C9)

# E10 a CCRA with multiplicative / reset updates whose minimal representation is invertible:
# registers x,y,z: a: x := x*y + z, y := 1, z := 0 ; b: x := x + 1, y := 2, z := 3.  Singular pullbacks.
x, y, z = pvar(0), pvar(1), pvar(2)
d10 = {(0, "a"): (0, P(padd(pmul(x, y), z), pconst(1), {})),
       (0, "b"): (0, P(padd(x, pconst(1)), pconst(2), pconst(3)))}
C10 = CCRA([0], 0, 3, ["a", "b"], d10, [0, 1, 0], {0: x})
l10, M10, g10 = C10.representation()
results["E10"] = report("E10 singular physical updates", l10, M10, g10, True, ccra=C10)

print("summary:", results)
