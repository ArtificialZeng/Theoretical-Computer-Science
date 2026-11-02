# Replay the random CCRAs of affine_context_search.py (same seed), find those whose REVERSAL has an
# affine context, print the machine, and verify the context symbolically in l (exact arithmetic).
# Run: python3 -I replay_reversal_hits.py <seed> <trials>
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rand_ccra_base as base
import affine_context_search as acs
import sympy as sp

seed = int(sys.argv[1]); trials = int(sys.argv[2])
base.R = random.Random(seed); base.MODE['inv'] = 0.45
l = sp.symbols('l', integer=True, nonnegative=True)
for t in range(trials):
    r = base.R.choice([1, 2, 2, 3]); c = base.R.choice([1, 2, 2, 3])
    A = base.rand_ccra(r, c)
    fn = lambda w, A=A: base.run(A, w)
    rep = acs.rep_from_function(fn, '01', 4)
    if rep is None or not acs.check_rep(rep, fn, '01', 7):
        continue
    lam, M, gam, d = rep
    lamT = sp.Matrix(gam.T); MT = {a: M[a].T for a in '01'}
    res = acs.search(acs.tofr(lamT)[0], {a: acs.tofr(MT[a]) for a in '01'}, '01')
    if not res:
        continue
    u, x, y, z, _, _ = res[0]
    print('trial', t, 'registers', r, 'states', c, 'minimal dim', d)
    print('machine (transitions, outputs, initial valuation):', A)
    # symbolic check on the reversed representation (row vector gam^T, matrices M^T)
    def W(w):
        X = sp.eye(d)
        for a in w: X = X * MT[a]
        return X
    Y = W(y); P, J = Y.jordan_form()
    Yl = sp.simplify(P * J ** l * P.inv())
    for tt in range(5): assert sp.simplify(Yl.subs(l, tt) - Y ** tt) == sp.zeros(d)
    B = sp.simplify(W(x) * Yl * W(z))
    v0 = lamT * W(u)
    # orbit plane X: v0 and v0*B(1)
    v1 = sp.simplify(v0 * B.subs(l, 1))
    cs = sp.symbols('s t')
    rr = cs[0] * v0 + cs[1] * v1
    eqs = []
    for tt in range(4):
        eqs += list(sp.simplify(rr * B.subs(l, tt) - rr))
    sol = sp.solve(eqs, cs, dict=True)
    s0 = sol[0]
    r1 = sp.simplify(rr.subs(s0).subs({cs[1]: 1, cs[0]: 1}))
    if all(e == 0 for e in r1):
        r1 = sp.simplify(rr.subs(s0).subs({cs[0]: 1}))
    a_, b_ = sp.symbols('a b')
    img = sp.simplify(v0 * B)
    sol2 = sp.solve(list(img - b_ * r1 - a_ * v0), [a_, b_], dict=True)
    al = sp.simplify(sol2[0][a_]); be = sp.simplify(sol2[0][b_])
    print('  context words u,x,y,z =', (u, x, y, z))
    print('  r1 fixed symbolically:', sp.simplify(r1 * B - r1) == sp.zeros(1, d))
    print('  alpha(l) =', sp.factor(al), '   beta(l) =', sp.factor(be))
    print('  beta/(alpha-1) =', sp.simplify(be / (al - 1)))
    print('  check v0*B(l) == beta r1 + alpha v0 symbolically:', sp.simplify(img - be * r1 - al * v0) == sp.zeros(1, d))
    sys.stdout.flush()
