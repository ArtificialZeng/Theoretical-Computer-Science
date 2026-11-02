# Search random CCRAs for "affine contexts" (the hypothesis of the affine-context theorem).
# The theorem predicts that NO series computed by a CCRA has one.  Positive controls: g, h, MPS Ex. 52 reversal.
# Run: python3 -I affine_context_search.py <seed> <trials>
import sys, os, random, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rand_ccra_base as base
import sympy as sp

def words(alph, n):
    for L in range(n + 1):
        for t in itertools.product(alph, repeat=L):
            yield ''.join(t)

def tofr(M):
    return [[F(int(sp.fraction(x)[0]), int(sp.fraction(x)[1])) for x in row] for row in M.tolist()]

def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m) if A[i][k]) for j in range(p)] for i in range(n)]

def vm(v, A):
    return [sum(v[k] * A[k][j] for k in range(len(v)) if v[k]) for j in range(len(A[0]))]

def eye(d):
    return [[F(int(i == j)) for j in range(d)] for i in range(d)]

def rank(rows):
    M = [list(r) for r in rows]
    if not M: return 0
    rk, cols = 0, len(M[0])
    for c in range(cols):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk

def nullspace_2(eqrows):
    # eqrows: list of (a,b) with a*s + b*t = 0; return list of basis vectors of solutions in (s,t)
    rk = rank(eqrows)
    if rk == 2: return []
    if rk == 0: return [(F(1), F(0)), (F(0), F(1))]
    for a, b in eqrows:
        if a != 0 or b != 0:
            return [(-b, a)]

def Mword(M, w, d):
    X = eye(d)
    for a in w:
        X = mm(X, M[a])
    return X

def finite_diff_poly(vals, maxdeg):
    # is the sequence a polynomial of degree <= maxdeg (on the sample)?  returns degree or None
    cur = list(vals)
    for deg in range(maxdeg + 2):
        if all(v == 0 for v in cur):
            return deg - 1
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        if len(cur) == 0:
            return None
    return None

def search(lam, M, alph, maxu=2, maxx=1, maxy=2, maxz=2, L=None, verbose=False):
    d = len(lam)
    if L is None: L = 2 * d + 4
    found = []
    Mw = {w: Mword(M, w, d) for w in words(alph, max(maxu, maxx, maxy, maxz))}
    for u in words(alph, maxu):
        v0 = vm(lam, Mw[u])
        if all(c == 0 for c in v0): continue
        for x in words(alph, maxx):
            for y in [w for w in words(alph, maxy) if w]:
                Y = Mw[y]
                for z in words(alph, maxz):
                    B, P = [], mm(Mw[x], eye(d))
                    for l in range(L + 1):
                        B.append(mm(P, Mw[z])); P = mm(P, Y)
                    # orbit closure of v0 under the B_l
                    basis = [v0]
                    changed = True
                    while changed and len(basis) <= 2:
                        changed = False
                        for v in list(basis):
                            for Bl in B:
                                w_ = vm(v, Bl)
                                if rank(basis + [w_]) > len(basis):
                                    basis.append(w_); changed = True
                                    if len(basis) > 2: break
                            if len(basis) > 2: break
                    if len(basis) != 2: continue
                    v1 = basis[1]
                    # fixed rows r = s v0 + t v1 with r B_l = r
                    eqs = []
                    for Bl in B:
                        a = [p - q for p, q in zip(vm(v0, Bl), v0)]
                        b = [p - q for p, q in zip(vm(v1, Bl), v1)]
                        for j in range(d):
                            eqs.append((a[j], b[j]))
                    ns = nullspace_2(eqs)
                    if len(ns) != 1: continue
                    s, t = ns[0]
                    if t == 0: continue          # r1 proportional to v0 = lambda M_u: excluded by (i)
                    r1 = [s * p + t * q for p, q in zip(v0, v1)]
                    # v0 B_l = beta r1 + alpha v0
                    alphas, betas, ok = [], [], True
                    for Bl in B:
                        img = vm(v0, Bl)
                        # solve img = beta r1 + alpha v0
                        sol = None
                        for j in range(d):
                            for k in range(d):
                                det = r1[j] * v0[k] - r1[k] * v0[j]
                                if det != 0:
                                    beta = (img[j] * v0[k] - img[k] * v0[j]) / det
                                    alpha = (r1[j] * img[k] - r1[k] * img[j]) / det
                                    sol = (alpha, beta); break
                            if sol: break
                        if sol is None or [beta * p + alpha * q for p, q in zip(r1, v0)] != img:
                            ok = False; break
                        alphas.append(sol[0]); betas.append(sol[1])
                    if not ok: continue
                    da = finite_diff_poly(alphas, L - 2)
                    if da is None or da < 1: continue                 # alpha must be a nonconstant polynomial
                    ratios = [b / (a - 1) for a, b in zip(alphas, betas) if a != 1]
                    if len(set(ratios)) <= 1: continue               # beta/(alpha-1) must be nonconstant
                    found.append((u, x, y, z, alphas[:5], betas[:5]))
                    if verbose: print('  affine context:', u, x, y, z, 'alpha', alphas[:5], 'beta', betas[:5])
                    return found
    return found

def rep_from_function(f, alph, depth=4):
    # minimal representation via the Hankel code of rand_ccra_base (alphabet '01' there); generic version here
    P = list(words(alph, depth)); S = list(words(alph, depth))
    H = sp.Matrix([[f(p + s) for s in S] for p in P])
    rows = []; cur = sp.zeros(0, len(S))
    for i in range(len(P)):
        t = cur.col_join(H[i, :])
        if t.rank() > cur.rows: cur = t; rows.append(i)
    d = len(rows)
    if d == 0: return None
    Hr = H.extract(rows, list(range(len(S))))
    cols = []; cc = sp.zeros(d, 0)
    for j in range(len(S)):
        t = cc.row_join(Hr[:, j])
        if t.rank() > cc.cols: cc = t; cols.append(j)
    B = H.extract(rows, cols); Binv = B.inv()
    Pw = [P[i] for i in rows]; Sw = [S[j] for j in cols]
    lam = sp.Matrix([[f(s) for s in Sw]]) * Binv
    M = {a: sp.Matrix([[f(p + a + s) for s in Sw] for p in Pw]) * Binv for a in alph}
    gam = sp.Matrix([f(p) for p in Pw])
    return lam, M, gam, d

def check_rep(rep, f, alph, n):
    lam, M, gam, d = rep
    for w in words(alph, n):
        X = sp.eye(d)
        for a in w: X = X * M[a]
        if (lam * X * gam)[0, 0] != f(w): return False
    return True

if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    # ---- positive controls
    def g(w):  # over '01' with 0='a', 1='#'
        tot, prod = 0, 1
        for u in w.split('1'):
            tot += prod; prod *= len(u)
        return tot
    def h(w):
        tot, prod = 0, 1
        for u in w.split('1'):
            tot += prod; prod *= len(u) + 1
        return tot
    def mpsf(w):
        ms, ks, i = [], [], 0
        while True:
            j = i
            while j < len(w) and w[j] == '0': j += 1
            k0 = j
            while j < len(w) and w[j] == '1': j += 1
            ms.append(k0 - i); ks.append(j - k0); i = j
            if i >= len(w): break
        v = 1
        for m, k in zip(ms, ks): v = v * m + k
        return v
    controls = {'g': g, 'g^r': lambda w: g(w[::-1]), 'h': h, 'h^r': lambda w: h(w[::-1]),
                'mps f': mpsf, 'mps f^r': lambda w: mpsf(w[::-1])}
    for name, fn in controls.items():
        rep = rep_from_function(fn, '01', 4)
        assert check_rep(rep, fn, '01', 8)
        lam, M, gam, d = rep
        res = search(tofr(lam)[0], {a: tofr(M[a]) for a in '01'}, '01')
        print('control %-8s dim %d  affine context found: %s' % (name, d, res[0] if res else None), flush=True)
    # ---- random CCRAs (generator of indep_verify_claude/necessity_check.py, copied as rand_ccra_base.py)
    base.R = random.Random(seed)
    base.MODE['inv'] = 0.45          # more singular updates than the invertible-sector experiment
    stats = {}
    for t in range(trials):
        r = base.R.choice([1, 2, 2, 3]); c = base.R.choice([1, 2, 2, 3])
        A = base.rand_ccra(r, c)
        fn = lambda w, A=A: base.run(A, w)
        rep = rep_from_function(fn, '01', 4)
        if rep is None: stats['zero'] = stats.get('zero', 0) + 1; continue
        if not check_rep(rep, fn, '01', 7): stats['hankel-short'] = stats.get('hankel-short', 0) + 1; continue
        lam, M, gam, d = rep
        sing = any(M[a].det() == 0 for a in '01')
        key = ('singular' if sing else 'invertible') + '-d%d' % min(d, 9)
        res = search(tofr(lam)[0], {a: tofr(M[a]) for a in '01'}, '01')
        rres = None
        # also the reversal of the CCRA series (not necessarily CCRA): count contexts found there
        lamT = sp.Matrix(gam.T); MT = {a: M[a].T for a in '01'}
        rres = search(tofr(lamT)[0], {a: tofr(MT[a]) for a in '01'}, '01')
        stats[key] = stats.get(key, 0) + 1
        if res:
            stats['CONTEXT-IN-CCRA'] = stats.get('CONTEXT-IN-CCRA', 0) + 1
            print('!!! affine context in a CCRA series:', res, A, flush=True)
        if rres:
            stats['context-in-reversal'] = stats.get('context-in-reversal', 0) + 1
            print('reversal of a CCRA series has an affine context (so it is not CCRA):', rres, flush=True)
    print(stats)
