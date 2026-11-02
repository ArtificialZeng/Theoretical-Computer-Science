# Sanity check of the Horner normal form in the proof of Theorem onereset (sufficiency, unipotent case).
# T(n) = R M_a^n C = [[2^n, n 2^n],[0, 3^n]]:  d/a = (3/2)^n and b/a = n are linear recurrence sequences.
import itertools
from fractions import Fraction as Fr
import sympy as sp
Ma = sp.Matrix([[2, 1, 0], [0, 2, 0], [0, 0, 3]])
R = sp.Matrix([[1, 0, 0], [0, 0, 1]]); C = sp.Matrix([[1, 0], [0, 2], [0, 1]])
Mh = C * R
lam = sp.Matrix([[1, -1, 2]]); gam = sp.Matrix([3, 1, -2])
def f_rep(w):
    X = sp.eye(3)
    for ch in w: X = X * (Ma if ch == 'a' else Mh)
    return (lam * X * gam)[0, 0]
def T(n): return R * Ma ** n * C
for n in range(6): assert T(n) == sp.Matrix([[2 ** n, n * 2 ** n], [0, 3 ** n]])
def machine(w):
    # simulate the copyless block machine: registers hold block values; Horner for V
    blocks = [len(u) for u in w.split('#')]
    if len(blocks) == 1:
        return (lam * Ma ** blocks[0] * gam)[0, 0]
    s = lam * Ma ** blocks[0] * C          # first block: s(n0), stored
    t = R * Ma ** blocks[-1] * gam          # last block: t(nk)
    A1 = A2 = D = Fr(1); V = Fr(0)
    for n in blocks[1:-1]:                  # middle blocks, combined at each '#'
        a, b, d = Fr(2) ** n, Fr(n) * 2 ** n, Fr(3) ** n
        A1, A2, D, V = A1 * a, A2 * a, D * d, V * (d / a) + (b / a)   # V := V*(d/a) + b/a
    s1, s2 = s[0, 0], s[0, 1]; t1, t2 = t[0, 0], t[1, 0]
    return s1 * t1 * A1 + s1 * t2 * A2 * V + s2 * t2 * D
ok = all(machine(w) == f_rep(w) for L in range(9) for w in map(''.join, itertools.product('a#', repeat=L)))
print('Horner block normal form agrees with the representation on all words of length <= 8:', ok)
