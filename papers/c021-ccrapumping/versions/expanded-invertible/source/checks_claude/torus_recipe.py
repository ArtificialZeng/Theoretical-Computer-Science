"""Sufficiency construction with a nontrivial split torus (connected case, T = diagonal part).
c = t u, Z_{i+1} = t^{-1} Z_i t + log u, f(w) = lam T_n exp(Z_n) gam.  Checked on E2 and E7."""
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import sys
from fractions import Fraction as Fr
sys.path.insert(0, ".")
from wa import *
from recipe import mlog_unipotent, mexp_nilpotent

def torus_check(lam, Ms, gam, L=7):
    d = len(lam)
    tu = {}
    for a, A in Ms.items():
        t = zeros(d, d)
        for i in range(d):
            t[i][i] = A[i][i]
        u = mm(inv(t), A)
        assert is_unipotent(u), "letter not in T.U with T diagonal"
        tu[a] = (t, inv(t), mlog_unipotent(u))
    logs = [v[2] for v in tu.values()]
    for w in words(list(Ms), L):
        T = eye(d); Z = zeros(d, d)
        for a in w:
            t, ti, X = tu[a]
            Z = madd(mm(mm(ti, Z), t), X)
            T = mm(T, t)
        if dot(vm(vm(lam, T), mexp_nilpotent(Z)), gam) != evalw(lam, Ms, gam, w):
            return False, w
    return True, "verified up to length %d" % L

def M(rows): return [[Fr(x) for x in r] for r in rows]
E2 = {"0": transpose(M([[1, 0], [0, 2]])), "1": transpose(M([[1, 2], [0, 2]]))}
print("E2", torus_check([Fr(0), Fr(1)], E2, [Fr(1), Fr(0)]))
# E7-type in minimal coordinates: pullback on span{1,x}: a: x->2x, b: x->x+1 ; basis (1,x)
E7 = {"a": M([[1, 0], [0, 2]]), "b": M([[1, 0], [1, 1]])}
print("E7", torus_check([Fr(1), Fr(0)], E7, [Fr(0), Fr(1)]))
# 3-dim: torus acting with two weights on a 2-dim commutative U (x -> 2x, y -> 4y ; translations)
E11 = {"a": M([[1, 0, 0], [0, 2, 0], [0, 0, 4]]), "b": M([[1, 0, 0], [1, 1, 0], [1, 0, 1]])}
print("E11", torus_check([Fr(1), Fr(0), Fr(0)], E11, [Fr(0), Fr(1), Fr(1)]))
