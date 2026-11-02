"""Randomized evidence for the necessity direction of Theorem A.

Random deterministic CCRAs (finite control, arbitrary copyless polynomial updates including
products, resets and permutations) are converted to weighted representations, minimized, and,
whenever the minimal letter matrices are invertible, the finite proxies (T1),(T2) of the group
criterion are evaluated.  Theorem A predicts that they never fail.
Control experiments: random invertible weighted automata (not built from CCRAs) usually fail.
"""
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import random, sys
import sympy
from fractions import Fraction as Fr
from wa import *
from groupcheck import criterion, letters_invertible

CONSTS = [Fr(-2), Fr(-1), Fr(1), Fr(2), Fr(3), Fr(1, 2), Fr(-1, 3)]
def rexpr(vs, rng):
    if not vs:
        return pconst(rng.choice([0, 1, 2, -1, 3]))
    if len(vs) == 1:
        a = rng.choice(CONSTS)
        b = rng.choice([0, 0, 1, -1, 2])
        return padd(pconst(b), pvar(vs[0]), a)
    k = rng.randint(1, len(vs) - 1)
    A, B = vs[:k], vs[k:]
    e1, e2 = rexpr(A, rng), rexpr(B, rng)
    if rng.random() < 0.5:
        return padd(e1, e2)
    e = pmul(e1, e2)
    if rng.random() < 0.5:
        e = padd(e, pconst(rng.choice([1, -1, 2])))
    return e

def rupdate(r, rng, p_acp):
    regs = list(range(r))
    rng.shuffle(regs)
    if rng.random() < p_acp:
        # affine coordinate permutation
        alphas = CONSTS if rng.random() < 0.5 else [Fr(1), Fr(1), Fr(1), Fr(-1), Fr(2)]
        return tuple(padd(pconst(rng.choice([0, 0, 1, -1, 2])), pvar(regs[i]), rng.choice(alphas)) for i in range(r))
    # general copyless: distribute a random subset of registers among outputs
    used = [v for v in regs if rng.random() < 0.85]
    buckets = [[] for _ in range(r)]
    for v in used:
        buckets[rng.randrange(r)].append(v)
    return tuple(rexpr(b, rng) for b in buckets)

def rccra(rng, nstates, r, alph, p_acp):
    states = list(range(nstates))
    delta = {}
    for q in states:
        for a in alph:
            delta[(q, a)] = (rng.choice(states), rupdate(r, rng, p_acp))
    out = {}
    for q in states:
        vs = [v for v in range(r) if rng.random() < 0.8]
        rng.shuffle(vs)
        out[q] = rexpr(vs, rng)
    x0 = [rng.choice([0, 1, 2, -1]) for _ in range(r)]
    return CCRA(states, 0, r, alph, delta, x0, out)

def all_roots_of_unity(A):
    x = sympy.Symbol('x')
    _, facs = sympy.factor_list(charpoly(A).as_expr(), x)
    for fpoly, _m in facs:
        P = sympy.Poly(fpoly, x).monic()
        if not all(c.is_integer for c in P.all_coeffs()) or not P.is_cyclotomic:
            return False
    return True

def lettersn_commute(Ms):
    ls = list(Ms)
    return all(is_zero(comm(Ms[a], Ms[b])) for a in ls for b in ls)

def main(trials=400, seed=7):
    rng = random.Random(seed)
    stats = dict(total=0, invertible=0, interesting=0, ok=0, fail=0, nonunip=0, finitepart=0)
    fails = []
    for t in range(trials):
        nstates = rng.choice([1, 1, 2, 3])
        r = rng.choice([1, 2, 2, 3])
        C = rccra(rng, nstates, r, ["a", "b"], p_acp=rng.choice([0.3, 0.6, 0.9]))
        assert C.is_copyless()
        lam, Ms, gam = C.representation()
        l2, M2, g2 = minimize(lam, Ms, gam)
        stats["total"] += 1
        if len(l2) == 0 or not letters_invertible(M2):
            continue
        stats["invertible"] += 1
        if len(l2) < 2 or lettersn_commute(M2):
            continue
        stats["interesting"] += 1
        if not all(is_unipotent(M2[a]) for a in M2):
            stats["nonunip"] += 1
        ok, info = criterion(M2, samples=15, seed=t)
        # non-vacuity statistics: nontrivial unipotent parts / non-unit eigenvalues
        A_, B_ = M2["a"], M2["b"]
        Ai, Bi = inv(A_), inv(B_)
        probe = [A_, B_, mm(A_, B_), mm(A_, Bi), mm(mm(A_, A_), B_), mm(B_, Ai), mm(mm(A_, B_), mm(Ai, Bi))]
        hasU = any(not meq(jordan_parts(g)[1], eye(len(l2))) for g in probe)
        hasT = any(not all_roots_of_unity(M2[a]) for a in M2)
        stats["has_unipotent_part"] = stats.get("has_unipotent_part", 0) + hasU
        stats["has_nonunit_eigenvalue"] = stats.get("has_nonunit_eigenvalue", 0) + hasT
        stats["both"] = stats.get("both", 0) + (hasU and hasT)
        stats["maxdim"] = max(stats.get("maxdim", 0), len(l2))
        if ok:
            stats["ok"] += 1
        else:
            stats["fail"] += 1
            fails.append((t, info))
            print("FAIL", t, info)
        sys.stdout.flush()
    print("CCRA trials:", stats)
    return fails

def control(trials=40, seed=3):
    rng = random.Random(seed)
    res = {"upper_tri_fail": 0, "upper_tri": 0, "general_fail": 0, "general": 0}
    for t in range(trials):
        d = rng.choice([2, 3])
        # upper triangular with rational diagonal: (T1) holds, (T2) typically fails
        Ms = {}
        for a in "ab":
            A = zeros(d, d)
            for i in range(d):
                A[i][i] = rng.choice([Fr(1), Fr(2), Fr(-1), Fr(1, 2)])
                for j in range(i + 1, d):
                    A[i][j] = Fr(rng.randint(-2, 2))
            Ms[a] = A
        lam = [Fr(rng.randint(-2, 2)) for _ in range(d)]
        gam = [Fr(rng.randint(-2, 2)) for _ in range(d)]
        l2, M2, g2 = minimize(lam, Ms, gam)
        if len(l2) >= 2 and not lettersn_commute(M2):
            res["upper_tri"] += 1
            ok, _ = criterion(M2, samples=10, seed=t)
            res["upper_tri_fail"] += (not ok)
        # general integer matrices
        Ms = {a: [[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(d)] for a in "ab"}
        if all(rank(M) == d for M in Ms.values()):
            l2, M2, g2 = minimize(lam, Ms, gam)
            if len(l2) >= 2 and letters_invertible(M2) and not lettersn_commute(M2):
                res["general"] += 1
                ok, _ = criterion(M2, samples=10, seed=t, kmax=12)
                res["general_fail"] += (not ok)
    print("control:", res)

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    main(n)
    control()
