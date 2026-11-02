"""Check of the sufficiency construction (Section 7 of manuscript_v2_claude), computed only from
a minimal representation.

Quasi-unipotent case: F = Gamma / Gamma_u is found by breadth-first search over words, two words
being identified when M_u^{-1} M_v is unipotent.  Cocycles c(g,a) = M_{r_g} M_a M_{r_{ga}}^{-1}
must be unipotent and pairwise commuting; then
    f(w) = lam * exp( sum_{g,a} n_{g,a}(w) N_{g,a} ) * M_{r_{phi(w)}} * gam,   N = log c,
where n_{g,a}(w) counts positions read in control state g with letter a.

Torus case (one-dimensional split torus): handled for explicitly given T, U decompositions.
"""
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import sys
from fractions import Fraction as Fr
from wa import *

def mlog_unipotent(A):
    d = len(A)
    N = madd(A, eye(d), Fr(-1))
    R = zeros(d, d)
    P = eye(d)
    for k in range(1, d + 1):
        P = mm(P, N)
        R = madd(R, P, Fr((-1) ** (k + 1), k))
    return R

def mexp_nilpotent(N):
    d = len(N)
    R = eye(d)
    P = eye(d)
    for k in range(1, d + 1):
        P = msc(mm(P, N), Fr(1, k))
        R = madd(R, P)
    return R

def quasi_unipotent_recipe(lam, Ms, gam, L=6, maxF=200):
    letters = list(Ms)
    reps = [()]
    mats = [eye(len(lam))]
    invs = [eye(len(lam))]
    trans = {}
    i = 0
    while i < len(reps):
        for a in letters:
            X = mm(mats[i], Ms[a])
            found = None
            for j in range(len(reps)):
                if is_unipotent(mm(invs[j], X)):
                    found = j
                    break
            if found is None:
                reps.append(reps[i] + (a,))
                mats.append(X)
                invs.append(inv(X))
                found = len(reps) - 1
                if len(reps) > maxF:
                    raise RuntimeError("finite quotient too large / not quasi-unipotent")
            trans[(i, a)] = found
        i += 1
    F = len(reps)
    coc = {}
    for g in range(F):
        for a in letters:
            c = mm(mm(mats[g], Ms[a]), invs[trans[(g, a)]])
            assert is_unipotent(c)
            coc[(g, a)] = mlog_unipotent(c)
    keys = list(coc)
    commuting = all(is_zero(comm(coc[k1], coc[k2])) for k1 in keys for k2 in keys)
    if not commuting:
        return F, False, None
    # verify formula
    for w in words(letters, L):
        g = 0
        Z = zeros(len(lam), len(lam))
        for a in w:
            Z = madd(Z, coc[(g, a)])
            g = trans[(g, a)]
        val = dot(vm(vm(lam, mexp_nilpotent(Z)), mats[g]), gam)
        if val != evalw(lam, Ms, gam, w):
            return F, True, ("formula fails", w)
    return F, True, "formula verified up to length %d" % L

if __name__ == "__main__":
    sys.path.insert(0, ".")
    import examples as E  # runs the example script, giving access to the representations
    for name, (lam, Ms, gam) in {"E1": ([Fr(0), Fr(1)], E.E1, [Fr(1), Fr(0)]),
                                 "E8": (E.l8, E.M8, E.g8),
                                 "E5": ([Fr(0), Fr(0), Fr(1)], E.E5, [Fr(1), Fr(0), Fr(0)])}.items():
        l2, M2, g2 = minimize(lam, Ms, gam)
        print(name, "dim", len(l2), "->", quasi_unipotent_recipe(l2, M2, g2))
