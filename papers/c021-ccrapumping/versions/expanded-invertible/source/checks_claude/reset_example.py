"""Corollary (local necessary condition) example: position sum of the suffix after the last '#'."""
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from fractions import Fraction as Fr
from wa import *
from groupcheck import criterion, letters_invertible
def M(r): return [[Fr(x) for x in row] for row in r]
A = {"0": transpose(M([[1,0,0],[0,1,1],[0,0,1]])), "1": transpose(M([[1,1,1],[0,1,1],[0,0,1]])),
     "#": transpose(M([[0,0,0],[0,0,0],[0,0,1]]))}
lam, gam = [Fr(0),Fr(0),Fr(1)], [Fr(1),Fr(0),Fr(0)]
def f(w):
    k = w.rfind("#") if "#" in w else -1
    return sum((i+1)*int(c) for i,c in enumerate(w[k+1:]))
ok = all(evalw(lam, A, gam, w) == f("".join(w)) for w in words(list(A), 6))
l2, M2, g2 = minimize(lam, A, gam)
print("closed form ok:", ok, "minimal dim:", len(l2), "ranks:", {a: rank(M2[a]) for a in M2})
sub = {a: M2[a] for a in "01"}
print("invertible sub-alphabet criterion:", criterion(sub))
