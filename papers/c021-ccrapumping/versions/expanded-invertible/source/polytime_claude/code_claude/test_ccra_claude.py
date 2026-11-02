# Random CCRA-derived invertible minimal representations must pass the polynomial-time test
# (necessity direction of the c021 main theorem).  The random CCRA generator and the Hankel
# minimisation are copied (not imported, not edited) from
#   c021_claude/indep_verify_claude/necessity_check.py
# Control: random invertible integer matrices; their verdict is compared with the finite
# proxies of that script (a proxy failure certifies "not (3)").
# usage: python3 test_ccra_claude.py SEED TRIALS
import sys, random, itertools, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fractions import Fraction as F
import sympy as sp
import flint
from linalg_claude import Q, unvec, vec, Subspace, is_zero_mat
from polyccra_claude import Setup, a_test, u_layers, decide
from groundtruth_claude import gt_general

R = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 40

# ---- copied from necessity_check.py (generator + minimisation) ----
COEF = [F(1), F(-1), F(2), F(-2), F(1, 2), F(3), F(-1, 3)]
def rand_expr(vars_):
    if not vars_:
        c = R.choice([F(0), F(0), F(1), F(-1), F(2), F(3)]); return ('c', c)
    e = ('v', vars_[0], R.choice(COEF))
    for v in vars_[1:]:
        e = ('add' if R.random() < 0.55 else 'mul', e, ('v', v, R.choice(COEF)))
    if R.random() < 0.6: e = ('add', e, ('c', R.choice(COEF)))
    return e
def ev(e, x):
    t = e[0]
    if t == 'c': return e[1]
    if t == 'v': return e[2] * x[e[1]]
    a, b = ev(e[1], x), ev(e[2], x)
    return a + b if t == 'add' else a * b
MODE = {'inv': 0.6}
def rand_update(r):
    if R.random() < MODE['inv']:
        perm = list(range(r)); R.shuffle(perm)
        groups = [[perm[i]] for i in range(r)]
        if r >= 2 and R.random() < 0.25:
            i, j = R.sample(range(r), 2); groups[i] = groups[i] + groups[j]; groups[j] = []
    else:
        used = [i for i in range(r) if R.random() < 0.85]; R.shuffle(used)
        groups = [[] for _ in range(r)]
        for v in used: groups[R.randrange(r)].append(v)
    return [rand_expr(g) for g in groups]
def rand_ccra(r, c):
    trans = {(q, a): (R.randrange(c), rand_update(r)) for q in range(c) for a in '01'}
    outs = [rand_expr([i for i in range(r) if R.random() < 0.7]) for _ in range(c)]
    x0 = [F(R.randint(-2, 3)) for _ in range(r)]
    return trans, outs, x0
def run(A, w):
    trans, outs, x = A; q = 0
    for a in w:
        q2, up = trans[(q, a)]; x = [ev(e, x) for e in up]; q = q2
    return ev(outs[q], x)
def words(n):
    for L in range(n + 1):
        for t in itertools.product('01', repeat=L): yield ''.join(t)
def minimal_rep(f, depth=4):
    P = list(words(depth)); S = list(words(depth))
    H = sp.Matrix([[f(p + s) for s in S] for p in P])
    rows = []; cur = sp.zeros(0, len(S))
    for i in range(len(P)):
        t = cur.col_join(H[i, :])
        if t.rank() > cur.rows: cur = t; rows.append(i)
    d = len(rows)
    if d == 0: return None
    cols = []; cc = sp.zeros(d, 0); Hr = H.extract(rows, list(range(len(S))))
    for j in range(len(S)):
        t = cc.row_join(Hr[:, j])
        if t.rank() > cc.cols: cc = t; cols.append(j)
    B = H.extract(rows, cols); Binv = B.inv()
    Pw = [P[i] for i in rows]; Sw = [S[j] for j in cols]
    lam = sp.Matrix([[f(s) for s in Sw]]) * Binv
    M = {a: sp.Matrix([[f(p + a + s) for s in Sw] for p in Pw]) * Binv for a in '01'}
    gam = sp.Matrix([f(p) for p in Pw])
    return lam, M, gam, d
def Mw(M, w, d):
    X = sp.eye(d)
    for a in w: X = X * M[a]
    return X
# ---- end of copied part ----

def to_flint(A):
    d = A.rows
    return flint.fmpq_mat(d, d, [Q(int(sp.Rational(x).p), int(sp.Rational(x).q)) for x in A])

stats = {}
def bump(k):
    stats[k] = stats.get(k, 0) + 1

t0 = time.time()
for t in range(TRIALS):
    r = R.choice([1, 2, 2, 3]); c = R.choice([1, 2, 2, 3])
    A = rand_ccra(r, c); f = lambda w, A=A: run(A, w)
    rep = minimal_rep(f)
    if rep is None: bump('zero'); continue
    lam, M, gam, d = rep
    if any((lam * Mw(M, w, d) * gam)[0] != f(w) for w in words(7)): bump('hankel-too-short'); continue
    if any(M[a].det() == 0 for a in '01') or d < 2: bump('singular-or-trivial'); continue
    if d > 6: bump('too-large-for-test'); continue
    gens = [to_flint(M[a]) for a in '01']
    v, det = decide(gens, random.Random(t))
    key = 'CCRA:' + ('pass' if v else 'FAIL')
    bump(key)
    msg = ''
    # cross-check Lie(R_u G) with the exponential ground truth when feasible
    try:
        S = Setup(gens)
        ok_a, info = a_test(S, random.Random(t))
        if ok_a:
            Sgt, order = gt_general(S, info['_B'])
            rec = {}
            res = u_layers(S, record=rec)
            if res[0] == 'abelian':
                ours = Subspace([vec(X) for X in res[1]], d * d)
                same = (ours == Sgt)
                bump('GT-compare:' + ('same' if same else 'DIFFERENT'))
                msg = f' |quot|={order} dimU={Sgt.dim} GT-same={same}'
    except (RuntimeError, ValueError) as e:
        msg = f' GT skipped ({e})'
    print(f'[{t}] r={r} c={c} d={d} m={det["m"]} verdict={v}{msg}', flush=True)
    if not v:
        print('   COUNTEREXAMPLE?', det)

# control
def proxy_fail(Ms, d):
    """finite proxies of necessity_check: rational spectrum of N-th powers, unipotent commutators,
    commuting unipotent parts, on random short words.  Returns True if a proxy certifies failure."""
    Nn = 12
    ws = list({''.join(R.choice('01') for _ in range(R.randint(1, 3))) for _ in range(5)})
    pw = {w: Mw(Ms, w, d) ** Nn for w in ws}
    x = sp.symbols('x')
    for w, A in pw.items():
        _, fac = sp.factor_list(A.charpoly(x).as_expr())
        if not all(sp.degree(p, x) == 1 for p, _ in fac):
            return True
    for u, v in itertools.combinations(ws, 2):
        C = pw[u] * pw[v] * pw[u].inv() * pw[v].inv()
        if sp.expand(C.charpoly(x).as_expr() - (x - 1) ** d) != 0:
            return True
    return False

for t in range(15):
    d = R.choice([2, 3])
    Ms = {a: sp.Matrix(d, d, lambda i, j: R.randint(-2, 2)) for a in '01'}
    if any(Ms[a].det() == 0 for a in '01'): continue
    gens = [to_flint(Ms[a]) for a in '01']
    v, det = decide(gens, random.Random(100 + t))
    pf = proxy_fail(Ms, d)
    consistent = not (v and pf)
    bump('control:' + ('pass' if v else 'fail') + (':proxyfail' if pf else ':proxyok'))
    if not consistent:
        print('   INCONSISTENT control', det)
print(stats, f'time {time.time() - t0:.1f}s')
