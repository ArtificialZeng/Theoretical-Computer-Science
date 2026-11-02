# Exact checks of the concrete claims made in section_claude.tex.  Run: python3 -I section_checks.py
import itertools
import sympy as sp

def words(alph, n):
    for L in range(n + 1):
        for t in itertools.product(alph, repeat=L):
            yield ''.join(t)

def Mw(M, w, d):
    X = sp.eye(d)
    for a in w:
        X = X * M[a]
    return X

def represents(lam, M, gam, f, alph, n):
    d = lam.cols
    return all((lam * Mw(M, w, d) * gam)[0, 0] == f(w) for w in words(alph, n))

def minimal(lam, M, gam, alph):
    d = lam.cols
    R = sp.Matrix.vstack(*[lam * Mw(M, w, d) for w in words(alph, d)])
    C = sp.Matrix.hstack(*[Mw(M, w, d) * gam for w in words(alph, d)])
    return R.rank() == d and C.rank() == d

def blocks_value(w, factor):
    tot, prod = 0, 1
    for u in w.split('#'):
        tot += prod
        prod *= factor(len(u))
    return sp.Integer(tot) if isinstance(tot, int) else tot

g = lambda w: blocks_value(w, lambda n: n)
h = lambda w: blocks_value(w, lambda n: n + 1)
g2 = lambda w: blocks_value(w, lambda n: sp.Integer(2) ** n)

Ma = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 1]])
Mh = sp.Matrix([[1, 0, 0], [1, 0, 1], [0, 0, 0]])      # g
Mhp = sp.Matrix([[1, 0, 0], [1, 0, 1], [1, 0, 1]])     # h
lam = sp.Matrix([[1, 0, 1]]); gam = sp.Matrix([1, 0, 0])
Mg = {'a': Ma, '#': Mh}; MH = {'a': Ma, '#': Mhp}
print('g: representation correct (|w|<=11):', represents(lam, Mg, gam, g, 'a#', 11), ' minimal:', minimal(lam, Mg, gam, 'a#'))
print('h: representation correct (|w|<=11):', represents(lam, MH, gam, h, 'a#', 11), ' minimal:', minimal(lam, MH, gam, 'a#'))
print('bases in the minimality claim (g): det rows', sp.Matrix.vstack(lam, lam * Ma, lam * Mh).det(),
      ' det cols', sp.Matrix.hstack(gam, Mh * gam, Ma * Mh * gam).det())
print('bases in the minimality claim (h): det rows', sp.Matrix.vstack(lam, lam * Ma, lam * Mhp).det(),
      ' det cols', sp.Matrix.hstack(gam, Mhp * gam, Ma * Mhp * gam).det())
l = sp.symbols('l', integer=True, nonnegative=True)
Mal = sp.eye(3) + l * (Ma - sp.eye(3))
r1 = sp.Matrix([[1, 0, 0]]); r2 = sp.Matrix([[0, 0, 1]])
print('g: r1 M_{a^l#} =', list(r1 * Mal * Mh), ' r2 M_{a^l#} =', list(r2 * Mal * Mh))
print('h: r1 M_{a^l#} =', list(r1 * Mal * Mhp), ' r2 M_{a^l#} =', list(r2 * Mal * Mhp))
# h: every word containing # has rank exactly 2; M'_# in a group
ranks = set(Mw(MH, w, 3).rank() for w in words('a#', 9) if '#' in w)
print('h: ranks of word matrices containing #, |w|<=9:', ranks, ' rank M_#^2 =', (Mhp ** 2).rank())
ranks_g = set(Mw(Mg, w, 3).rank() for w in words('a#', 9) if '#' in w)
print('g: ranks of word matrices containing #, |w|<=9:', ranks_g)
print('r1 fixed by all letters (g,h):', r1 * Ma == r1 and r1 * Mh == r1 and r1 * Mhp == r1)
# g, h machines for reversals
def mach_rev(w, A0):
    x, A = 0, A0
    for ch in w:
        if ch == 'a': A += 1
        else: x, A = x * A + 1, A0
    return x * A + 1
print('g^r machine (|w|<=12):', all(mach_rev(w, 0) == g(w[::-1]) for w in words('a#', 12)))
print('h^r machine (|w|<=12):', all(mach_rev(w, 1) == h(w[::-1]) for w in words('a#', 12)))
# the 2^{|u_j|} series: registers T, D (init 1): a: T:=T/2, D:=2D ; #: T:=T+1 ; output T*D
def mach_g2(w):
    T, D = sp.Integer(1), sp.Integer(1)
    for ch in w:
        if ch == 'a': T, D = T / 2, 2 * D
        else: T = T + 1
    return T * D
print('sum_i prod_{j<i} 2^|u_j| machine (|w|<=12):', all(mach_g2(w) == g2(w) for w in words('a#', 12)))

# MPS Example 52 and the hand representation of F^r on (S,R,Q,P)
def mps_F(w):
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
    return sp.Integer(v)
Fr = lambda w: mps_F(w[::-1])
# row action: 1:(S,R,Q,P)->(S+R+Q, R+Q, 0, R+Q) ; 0:(S,R,Q,P)->(S,0,Q+P,P)
M1 = sp.Matrix([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 0, 0]])
M0 = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1]])
lamF = sp.Matrix([[0, 1, 0, 1]]); gamF = sp.Matrix([1, 0, 1, 0])
MF = {'0': M0, '1': M1}
print('F^r: hand representation correct (|w|<=11):', represents(lamF, MF, gamF, Fr, '01', 11), ' minimal:', minimal(lamF, MF, gamF, '01'))
P0, J0 = M0.jordan_form()
M0l = sp.simplify(P0 * J0 ** l * P0.inv())
for t in range(6): assert M0l.subs(l, t) == M0 ** t
r1F = sp.Matrix([[1, 0, 0, 0]]); r2F = sp.Matrix([[0, 1, 0, 1]])
print('F^r: r1 M_{0^l 1} =', list(sp.simplify(r1F * M0l * M1)), ' r2 M_{0^l 1} =', list(sp.simplify(r2F * M0l * M1)))
print('F^r: context blocks 0^{l+1}1:  r1 M =', list(sp.simplify(r1F * M0 * M0l * M1)), ' r2 M =', list(sp.simplify(r2F * M0 * M0l * M1)))
print('F^r: ranks M_0, M_1:', M0.rank(), M1.rank())
# machine for F
def mach_F(w):
    last0, v, c = True, 1, 0
    for ch in w:
        if ch == '0':
            c = c + 1 if last0 else 1; last0 = True
        else:
            if last0: v, c = v * c + 1, 0
            else: v = v + 1
            last0 = False
    return v * c if last0 else v
print('F machine (|w|<=12):', all(mach_F(w) == mps_F(w) for w in words('01', 12)))

# ---------------------------------------------------------------- the block-symmetric function E
# E(u_0#...#u_k) = sum_i prod_{j != i} (|u_j|+1)   (elementary symmetric e_k of the m_j=|u_j|+1)
def E(w):
    ms = [len(u) + 1 for u in w.split('#')]
    tot = 0
    for i in range(len(ms)):
        p = 1
        for j, m in enumerate(ms):
            if j != i: p *= m
        tot += p
    return sp.Integer(tot)
# row coordinates (S,P,Q_S,Q_P): a: Q_S+=S, Q_P+=P ;  #: (S,P,Q_S,Q_P) -> (Q_S+S+P, Q_P+P, 0, 0) ; output Q_S+S+P
MEa = sp.Matrix([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]])
MEh = sp.Matrix([[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]])
lamE = sp.Matrix([[0, 1, 0, 0]]); gamE = sp.Matrix([1, 1, 1, 0])
ME = {'a': MEa, '#': MEh}
print()
print('E: representation correct (|w|<=10):', represents(lamE, ME, gamE, E, 'a#', 10), ' minimal:', minimal(lamE, ME, gamE, 'a#'))
print('E: E(w) == E(reverse w) on |w|<=10:', all(E(w) == E(w[::-1]) for w in words('a#', 10)))
print('E: ranks of word matrices containing #, |w|<=8:', set(Mw(ME, w, 4).rank() for w in words('a#', 8) if '#' in w))
MEal = sp.eye(4) + l * (MEa - sp.eye(4))
assert (MEa - sp.eye(4)) ** 2 == sp.zeros(4)
r1E = sp.Matrix([[1, 0, 0, 0]]); r2E = sp.Matrix([[0, 1, 0, 0]])
print('E: r1 M_{a^l#} =', list(r1E * MEal * MEh), '  r2 M_{a^l#} =', list(r2E * MEal * MEh), '  lambda = r2')

# ---------------------------------------------------------------- Theorem onereset: block matrices T(n) for h, h^r, E
def blockT(lam, M, gam, d):
    # factor M_# = C R (rank 2) and return T(n) = R M_a^n C symbolically
    Mh = M['#']
    cols = Mh.columnspace()
    C = sp.Matrix.hstack(*cols[:2])
    R = (C.T * C).inv() * C.T * Mh
    assert C * R == Mh
    Mal = sp.eye(d) + l * (M['a'] - sp.eye(d))
    assert (M['a'] - sp.eye(d)) ** 2 == sp.zeros(d)
    return sp.simplify(R * Mal * C), C, R
for name, (lm, MM, gm) in {'h': (lam, MH, gam), 'E': (lamE, ME, gamE),
                           'h^r': (gam.T, {a: MH[a].T for a in MH}, lam.T)}.items():
    d_ = lm.cols
    T, C, R = blockT(lm, MM, gm, d_)
    print(name, ': T(n) =', T.tolist(), ' det =', sp.factor(T.det()))
