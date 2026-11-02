# Exact checks for the singular-sector results (singular_claude).
# Run: python3 -I reversal_check.py
#
# 1. g(u_0#u_1#...#u_k) = sum_i prod_{j<i} |u_j|   over {a,#}:  minimal rep (dim 3), hypotheses of the
#    affine-context theorem (symbolic in l), and a copyless machine for the reversal g^r (Horner).
# 2. MPS Example 52:  f(0^{m1}1^{k1}...0^{mt}1^{kt}) = (...((m1+k1)m2+k2)...)mt+kt :
#    copyless machine for f, minimal rep of f^r, hypotheses of the affine-context theorem for f^r.
# 3. The Zariski closure of the monoid of g: maximal subgroups (symbolic).
import itertools, sys
import sympy as sp

def words(alph, n):
    for L in range(n + 1):
        for t in itertools.product(alph, repeat=L):
            yield ''.join(t)

# ---------------------------------------------------------------- generic minimal representation (Hankel)
def minimal_rep(f, alph, depth):
    P = list(words(alph, depth)); S = list(words(alph, depth))
    H = sp.Matrix([[f(p + s) for s in S] for p in P])
    rows = []; cur = sp.zeros(0, len(S))
    for i in range(len(P)):
        t = cur.col_join(H[i, :])
        if t.rank() > cur.rows:
            cur = t; rows.append(i)
    d = len(rows)
    Hr = H.extract(rows, list(range(len(S))))
    cols = []; cc = sp.zeros(d, 0)
    for j in range(len(S)):
        t = cc.row_join(Hr[:, j])
        if t.rank() > cc.cols:
            cc = t; cols.append(j)
    B = H.extract(rows, cols); Binv = B.inv()
    Pw = [P[i] for i in rows]; Sw = [S[j] for j in cols]
    lam = sp.Matrix([[f(s) for s in Sw]]) * Binv
    M = {a: sp.Matrix([[f(p + a + s) for s in Sw] for p in Pw]) * Binv for a in alph}
    gam = sp.Matrix([f(p) for p in Pw])
    return lam, M, gam, Pw, Sw

def Mw(M, w, d):
    X = sp.eye(d)
    for a in w:
        X = X * M[a]
    return X

def check_rep(lam, M, gam, f, alph, n):
    d = lam.cols
    return all((lam * Mw(M, w, d) * gam)[0, 0] == f(w) for w in words(alph, n))

def is_minimal(lam, M, gam, alph):
    d = lam.cols
    R = sp.Matrix.vstack(*[lam * Mw(M, w, d) for w in words(alph, d)])
    C = sp.Matrix.hstack(*[Mw(M, w, d) * gam for w in words(alph, d)])
    return R.rank() == d and C.rank() == d

# ---------------------------------------------------------------- 1. the function g and its reversal
def g(w):
    blocks = w.split('#')
    tot, prod = 0, 1
    for i, u in enumerate(blocks):
        tot += prod          # term i = prod_{j<i} |u_j|
        prod *= len(u)
    return sp.Integer(tot)

def g_rev(w):
    return g(w[::-1])

def ccra_g_rev(w):
    # registers x (init 0), A (init 0);  a: A:=A+1 ;  #: x:=x*A+1, A:=0 ; output x*A+1.  Copyless.
    x, A = 0, 0
    for c in w:
        if c == 'a':
            A = A + 1
        else:
            x, A = x * A + 1, 0
    return sp.Integer(x * A + 1)

print('=== 1. g(u_0#...#u_k) = sum_i prod_{j<i}|u_j| ===')
ok = all(ccra_g_rev(w) == g_rev(w) for w in words('a#', 12))
print('copyless machine (x:=x*A+1, A:=0 on #) computes g^r on all words of length <= 12:', ok)

# hand-derived representation on row coordinates (S,Q,P)
lamg = sp.Matrix([[1, 0, 1]])
Mg = {'a': sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 1]]),     # (S,Q,P) -> (S, Q+P, P)
      '#': sp.Matrix([[1, 0, 0], [1, 0, 1], [0, 0, 0]])}     # (S,Q,P) -> (S+Q, 0, Q)
gamg = sp.Matrix([1, 0, 0])
print('hand representation computes g (|w|<=11):', check_rep(lamg, Mg, gamg, g, 'a#', 11))
print('hand representation minimal:', is_minimal(lamg, Mg, gamg, 'a#'))
print('ranks: M_a', Mg['a'].rank(), ' M_#', Mg['#'].rank(), ' M_#^2', (Mg['#'] ** 2).rank())
lam2, M2, gam2, _, _ = minimal_rep(g, 'a#', 4)
print('Hankel minimal dimension of g:', lam2.cols, '; of g^r:', minimal_rep(g_rev, 'a#', 4)[0].cols)

l = sp.symbols('l', integer=True, nonnegative=True)
Ma_pow = sp.eye(3) + l * (Mg['a'] - sp.eye(3))          # M_a unipotent, (M_a - I)^2 = 0
assert (Mg['a'] - sp.eye(3)) ** 2 == sp.zeros(3)
b_l = Mg['a'] * Ma_pow * Mg['#']                        # block a^{l+1} #
r1 = sp.Matrix([[1, 0, 0]]); r2 = sp.Matrix([[0, 0, 1]])
print('r1*M_b(l) =', list(r1 * b_l), ' (should be r1)')
print('r2*M_b(l) =', list(r2 * b_l), ' (should be beta*r1 + alpha*r2)')
alpha = (r2 * b_l)[0, 2]; beta = (r2 * b_l)[0, 0]
print('alpha(l) =', alpha, ' beta(l) =', beta, ' beta/(alpha-1) =', sp.simplify(beta / (alpha - 1)))
print('lambda*M_u for u=eps:', list(lamg), ' = r1 + r2, not in Q r1')

# ---------------------------------------------------------------- 2. MPS Example 52
def mps_blocks(w):
    # w = 0^{m1} 1^{k1} ... 0^{mt} 1^{kt}, m1,kt >= 0, others >= 1
    ms, ks = [], []
    i = 0
    while True:
        j = i
        while j < len(w) and w[j] == '0':
            j += 1
        m = j - i
        k0 = j
        while j < len(w) and w[j] == '1':
            j += 1
        k = j - k0
        ms.append(m); ks.append(k)
        i = j
        if i >= len(w):
            break
    return ms, ks

def mps_f(w):
    ms, ks = mps_blocks(w)
    v = 1
    for m, k in zip(ms, ks):
        v = v * m + k
    return sp.Integer(v)

def mps_f_rev(w):
    return mps_f(w[::-1])

def ccra_mps_f(w):
    # control mode in {Z,O} (inside a 0-run / inside a 1-run); registers v (init 1), c (init 0)
    mode, v, c = 'Z', 1, 0
    for ch in w:
        if ch == '0':
            if mode == 'Z':
                c = c + 1
            else:
                mode, c = 'Z', 1
        else:
            if mode == 'Z':
                v, c, mode = v * c + 1, 0, 'O'
            else:
                v = v + 1
    return sp.Integer(v * c if mode == 'Z' else v)

print()
print('=== 2. MPS Example 52 ===')
print('copyless machine for f correct on |w|<=12:', all(ccra_mps_f(w) == mps_f(w) for w in words('01', 12)))
lamr, Mr, gamr, Pw, Sw = minimal_rep(mps_f_rev, '01', 4)
d = lamr.cols
print('minimal dimension of f^r:', d, '; of f:', minimal_rep(mps_f, '01', 4)[0].cols)
print('rep of f^r verified on |w|<=10:', check_rep(lamr, Mr, gamr, mps_f_rev, '01', 10))
print('ranks of minimal letter matrices of f^r: M_0', Mr['0'].rank(), ' M_1', Mr['1'].rank())
# blocks b_l = 0 0^l 1 ; prefix u = '1'
N0 = Mr['0'] - sp.eye(d)
# M_0 is not unipotent in general; compute M_0^l symbolically via Jordan form
P0, J0 = Mr['0'].jordan_form()
M0l = sp.simplify(P0 * J0 ** l * P0.inv())
bl = sp.simplify(Mr['0'] * M0l * Mr['1'])
for test in range(6):
    assert sp.simplify(bl.subs(l, test) - Mw(Mr, '0' * (test + 1) + '1', d)) == sp.zeros(d)
u = '1'
start = lamr * Mw(Mr, u, d)
orbit = [start]
for w in [[0], [1], [2], [0, 1], [3, 0], [1, 1, 2]]:
    v = start
    for t in w:
        v = v * bl.subs(l, t)
    orbit.append(v)
X = sp.Matrix.vstack(*orbit)
print('dim X = span{lambda M_u M_b...} with u="1", b_l = 0^{l+1}1 :', X.rank())
# find r1 fixed by all b_l : solve r*(bl(t)-I) = 0 for t = 0..3 within X
basisX = X.rowspace()
Bx = sp.Matrix.vstack(*basisX)                # 2 x d
cs = sp.symbols('c0:2')
r = sp.Matrix([cs]) * Bx
eqs = []
for t in range(4):
    eqs += list(r * (bl.subs(l, t) - sp.eye(d)))
sol = sp.solve(eqs, cs, dict=True)
print('fixed rows in X:', sol)
c_sol = sol[0]
free = [c for c in cs if c not in c_sol] or [cs[0]]
r1 = sp.simplify(r.subs(c_sol).subs({free[0]: 1}))
# r2 := start (lambda M_u), check it is not proportional to r1
r2 = start
print('r1 =', list(r1))
print('r2 = lambda M_u =', list(r2), '; rank[r1;r2] =', sp.Matrix.vstack(r1, r2).rank())
img = sp.simplify(r2 * bl)
coef = sp.symbols('A B')
sol2 = sp.solve(list(img - coef[0] * r1 - coef[1] * r2), coef, dict=True)
print('r1 * M_b(l) - r1 =', list(sp.simplify(r1 * bl - r1)))
print('r2 * M_b(l) = beta r1 + alpha r2 with', sol2)
al = sp.simplify(sol2[0][coef[1]]); be = sp.simplify(sol2[0][coef[0]])
print('alpha(l) =', al, ' beta(l) =', be, ' beta/(alpha-1) =', sp.simplify(be / (al - 1)))

# ---------------------------------------------------------------- 3. closure of the monoid of g
print()
print('=== 3. Zariski closure of the monoid of g ===')
t0, uu, ss, tt = sp.symbols('t0 u s t')
def phi(t0, u, s, t):
    return sp.Matrix([[1, 0, 0], [u, t * s, s], [u * t0, t * s * t0, s * t0]])
# every word with at least one # has this form; check closure under right multiplication by M_a, M_#
A1 = sp.simplify(phi(t0, uu, ss, tt) * Mg['a'])
A2 = sp.simplify(phi(t0, uu, ss, tt) * Mg['#'])
print('phi*M_a = phi(t0,u,s,t+1):', sp.simplify(A1 - phi(t0, uu, ss, tt + 1)) == sp.zeros(3))
print('phi*M_# = phi(t0,u+t*s,t*s,0):', sp.simplify(A2 - phi(t0, uu + tt * ss, tt * ss, 0)) == sp.zeros(3))
print('M_a^n*phi = phi(t0+n,...):', sp.simplify((sp.eye(3) + l * (Mg['a'] - sp.eye(3))) * phi(t0, uu, ss, tt) - phi(t0 + l, uu, ss, tt)) == sp.zeros(3))
print('M_# itself = phi(0,1,1,0):', phi(0, 1, 1, 0) == Mg['#'])
# rank-2 idempotent e and its maximal subgroup:  e = projection onto span{e_S, (0,vQ,vP)}
vQ, vP, sig, tau = sp.symbols('vQ vP sigma tau')
# general element with first row e1 and rank<=1 block [q;p] = (sigma,tau)^T (vS,vQ,vP)
def elt(sig, tau, vS, vQ, vP):
    return sp.Matrix([[1, 0, 0], [sig * vS, sig * vQ, sig * vP], [tau * vS, tau * vQ, tau * vP]])
e = elt(1, 0, 0, 1, 0)                                # (S,Q,P) -> (S, Q, 0): rank-2 idempotent
print('e idempotent:', e * e == e, ' rank', e.rank(), ' e in closure (block rank<=1, first row e1): yes')
a_, b_ = sp.symbols('a b')
h = elt(1, 0, b_, a_, 0)                               # (S,Q,P) -> (S + bQ, aQ, 0)
print('h = e h e:', sp.simplify(e * h * e - h) == sp.zeros(3))
print('action of h on im(e) = span{e_S, e_Q}: r_S -> r_S, r_Q -> b r_S + a r_Q  (Aff(1))')
print('product of two such:', list(sp.simplify(elt(1, 0, b_, a_, 0) * elt(1, 0, sp.Symbol("b2"), sp.Symbol("a2"), 0))))
# is e in the closure of the actual words?  e = phi(t0=0, u=0, s=1, t=1)
print('e = phi(0,0,1,1):', phi(0, 0, 1, 1) == e)
