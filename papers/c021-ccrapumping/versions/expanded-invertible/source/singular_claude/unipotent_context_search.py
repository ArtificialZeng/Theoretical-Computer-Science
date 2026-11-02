# Search for "unipotent contexts" (Theorem unipotentcontext): blocks b_l = x w^l z acting on a reachable plane
# X = span(r1, lambda M_u) by kappa(l) [[1,0],[s(l),1]] with s not a linear recurrence (tested on a sample).
# The theorem predicts that no CCRA series has one.  Controls: E (has one), the 2^n-analogue (s = 2^-l: no).
# Run: python3 -I unipotent_context_search.py <seed> <trials>
import sys, os, random, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import affine_context_search as acs
import rand_ccra_base as base
import sympy as sp

def is_lrs(vals, maxorder):
    # does the sequence satisfy a linear recurrence of order <= maxorder (checked on the sample)?
    n = len(vals)
    for k in range(0, maxorder + 1):
        if 2 * k + 2 > n: break
        rows = [vals[i:i + k + 1] for i in range(n - k)]
        if acs.rank(rows) <= k:
            return True
    return all(v == 0 for v in vals)

def search(lam, M, alph, L=26, maxu=2, maxx=1, maxy=2, maxz=2):
    d = len(lam)
    Mw = {w: acs.Mword(M, w, d) for w in acs.words(alph, max(maxu, maxx, maxy, maxz))}
    for u in acs.words(alph, maxu):
        v0 = acs.vm(lam, Mw[u])
        if all(c == 0 for c in v0): continue
        for x in acs.words(alph, maxx):
            for y in [w for w in acs.words(alph, maxy) if w]:
                for z in acs.words(alph, maxz):
                    B, P = [], acs.mm(Mw[x], acs.eye(d))
                    for l in range(L + 1):
                        B.append(acs.mm(P, Mw[z])); P = acs.mm(P, Mw[y])
                    w1 = acs.vm(v0, B[1])
                    if acs.rank([v0, w1]) < 2:
                        w1 = next((acs.vm(v0, Bl) for Bl in B if acs.rank([v0, acs.vm(v0, Bl)]) == 2), None)
                        if w1 is None: continue
                    basis = [v0, w1]
                    # check invariance of the plane and get 2x2 matrices in basis (v0, w1)
                    mats, ok = [], True
                    for Bl in B:
                        rowsimg = []
                        for v in basis:
                            img = acs.vm(v, Bl)
                            # solve img = c0 v0 + c1 w1
                            sol = None
                            for j in range(d):
                                for k in range(d):
                                    det = v0[j] * w1[k] - v0[k] * w1[j]
                                    if det != 0:
                                        c0 = (img[j] * w1[k] - img[k] * w1[j]) / det
                                        c1 = (v0[j] * img[k] - v0[k] * img[j]) / det
                                        sol = (c0, c1); break
                                if sol: break
                            if sol is None or [sol[0] * p + sol[1] * q for p, q in zip(v0, w1)] != img:
                                ok = False; break
                            rowsimg.append(sol)
                        if not ok: break
                        mats.append(rowsimg)      # row action matrix [[a,b],[c,e]]: v0->a v0+b w1, w1->c v0+e w1
                    if not ok: continue
                    # equal eigenvalues for all l and a common rational eigen-row r1 != v0 direction
                    good = True; r1 = None
                    for (a_, b_), (c_, e_) in mats:
                        if (a_ - e_) ** 2 + 4 * b_ * c_ != 0: good = False; break
                    if not good: continue
                    # eigen-row of a non-scalar member
                    for (a_, b_), (c_, e_) in mats:
                        if b_ != 0 or c_ != 0 or a_ != e_:
                            lamb = (a_ + e_) / 2
                            # row (s,t) with (s,t)[[a,b],[c,e]] = lamb (s,t)
                            # solve directly
                            Mx = sp.Matrix([[a_ - lamb, b_], [c_, e_ - lamb]])
                            ns = Mx.T.nullspace()
                            if not ns: good = False; break
                            r1 = (F(str(ns[0][0])), F(str(ns[0][1])))
                            break
                    if not good or r1 is None: continue
                    if r1[1] == 0 and r1[0] != 0:
                        continue   # r1 proportional to v0: excluded
                    # common eigen-row check and s(l)
                    svals = []
                    for (a_, b_), (c_, e_) in mats:
                        img = (r1[0] * a_ + r1[1] * c_, r1[0] * b_ + r1[1] * e_)
                        kap = (a_ + e_) / 2
                        if img != (kap * r1[0], kap * r1[1]) or kap == 0: good = False; break
                        # v0 = (1,0): v0 B = (a_, b_) = kap*(s r1 + v0)  ->  s r1 = (a_/kap - 1, b_/kap)
                        if r1[1] != 0: s = (b_ / kap) / r1[1]
                        else: good = False; break
                        if (a_ / kap - 1) != s * r1[0]: good = False; break
                        svals.append(s)
                    if not good: continue
                    if all(v == 0 for v in svals): continue
                    if not is_lrs(svals, 10):
                        return (u, x, y, z, svals[:5])
    return None

if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    def E(w):   # over '01': 0 = a, 1 = #
        ms = [len(u) + 1 for u in w.split('1')]; tot = 0
        for i in range(len(ms)):
            p = 1
            for j, m in enumerate(ms):
                if j != i: p *= m
            tot += p
        return tot
    def E2(w):
        ms = [2 ** len(u) for u in w.split('1')]; tot = 0
        for i in range(len(ms)):
            p = 1
            for j, m in enumerate(ms):
                if j != i: p *= m
            tot += p
        return tot
    for name, fn in {'E': E, 'E^r': lambda w: E(w[::-1]), 'E_2 (2^n blocks, CCRA)': E2}.items():
        rep = acs.rep_from_function(fn, '01', 4); lam, M, gam, d = rep
        assert acs.check_rep(rep, fn, '01', 8)
        res = search(acs.tofr(lam)[0], {a: acs.tofr(M[a]) for a in '01'}, '01')
        print('control %-24s dim %d  unipotent context: %s' % (name, d, res), flush=True)
    base.R = random.Random(seed); base.MODE['inv'] = 0.45
    stats = {}
    for t in range(trials):
        r = base.R.choice([1, 2, 2, 3]); c = base.R.choice([1, 2, 2, 3])
        A = base.rand_ccra(r, c); fn = lambda w, A=A: base.run(A, w)
        rep = acs.rep_from_function(fn, '01', 4)
        if rep is None or not acs.check_rep(rep, fn, '01', 7): stats['skip'] = stats.get('skip', 0) + 1; continue
        lam, M, gam, d = rep
        res = search(acs.tofr(lam)[0], {a: acs.tofr(M[a]) for a in '01'}, '01')
        stats['tested'] = stats.get('tested', 0) + 1
        if res:
            stats['CONTEXT-IN-CCRA'] = stats.get('CONTEXT-IN-CCRA', 0) + 1
            print('!!! unipotent context in a CCRA series:', res, A, flush=True)
    print(stats)
