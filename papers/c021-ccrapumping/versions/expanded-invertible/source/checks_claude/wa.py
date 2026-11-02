"""Exact rational toolkit for weighted automata and copyless CRA (CCRA).

Conventions: f(w) = lam * M_{a1} * ... * M_{an} * gam  (row vector, matrices, column).
All arithmetic is exact (fractions.Fraction); sympy is used only for
characteristic polynomials / factorisation of small matrices.
"""
from fractions import Fraction as Fr
import itertools, random
import sympy

# ---------------------------------------------------------------- matrices
def zeros(n, m):
    return [[Fr(0)] * m for _ in range(n)]

def eye(n):
    A = zeros(n, n)
    for i in range(n):
        A[i][i] = Fr(1)
    return A

def mm(A, B):
    n, k, m = len(A), len(B), len(B[0]) if B else 0
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        Ci[j] += a * Bt[j]
    return C

def vm(v, A):
    m = len(A[0]) if A else 0
    out = [Fr(0)] * m
    for t, a in enumerate(v):
        if a:
            for j in range(m):
                if A[t][j]:
                    out[j] += a * A[t][j]
    return out

def mv(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v)) if A[i][j] and v[j]), Fr(0)) for i in range(len(A))]

def dot(u, v):
    return sum((a * b for a, b in zip(u, v) if a and b), Fr(0))

def madd(A, B, c=Fr(1)):
    return [[A[i][j] + c * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def msc(A, c):
    return [[c * x for x in row] for row in A]

def is_zero(A):
    return all(x == 0 for row in A for x in row)

def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

def transpose(A):
    return [list(r) for r in zip(*A)]

def inv(A):
    n = len(A)
    M = [list(map(Fr, A[i])) + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            raise ZeroDivisionError("singular")
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]

def rank(A):
    M = [list(r) for r in A]
    if not M:
        return 0
    n, m = len(M), len(M[0])
    rk = 0
    for c in range(m):
        p = next((r for r in range(rk, n) if M[r][c] != 0), None)
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        for r in range(n):
            if r != rk and M[r][c] != 0:
                f = M[r][c] / M[rk][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[rk])]
        rk += 1
    return rk

def mpow(A, k):
    R = eye(len(A))
    B = A
    while k:
        if k & 1:
            R = mm(R, B)
        B = mm(B, B)
        k >>= 1
    return R

def comm(A, B):
    return madd(mm(A, B), mm(B, A), Fr(-1))

# ------------------------------------------------------- span / coordinates
class Span:
    """Incremental span of row vectors with coordinate solving."""
    def __init__(self, n):
        self.n = n
        self.vecs = []      # original vectors (basis)
        self.ech = []       # echelon rows: (pivot, row, combo) combo expresses row in terms of basis
    def reduce(self, v):
        v = list(v)
        combo = [Fr(0)] * len(self.vecs)
        for piv, row, cmb in self.ech:
            if v[piv] != 0:
                f = v[piv] / row[piv]
                v = [x - f * y for x, y in zip(v, row)]
                for i, c in enumerate(cmb):
                    if c:
                        combo[i] += f * c
        return v, combo
    def add(self, v):
        r, combo = self.reduce(v)
        piv = next((i for i, x in enumerate(r) if x != 0), None)
        if piv is None:
            return False
        k = len(self.vecs)
        self.vecs.append(list(v))
        cmb = [-c for c in combo] + [Fr(1)]
        for e in self.ech:
            e[2].append(Fr(0))
        self.ech.append((piv, r, cmb))
        return True
    def coords(self, v):
        r, combo = self.reduce(v)
        if any(x != 0 for x in r):
            raise ValueError("not in span")
        return combo + [Fr(0)] * (len(self.vecs) - len(combo))

def minimize(lam, Ms, gam):
    """Return a minimal representation (lam', {a: M'_a}, gam')."""
    letters = list(Ms)
    n = len(lam)
    # forward (reachable rows)
    S = Span(n)
    queue = []
    if S.add(lam):
        queue.append(list(lam))
    while queue:
        r = queue.pop()
        for a in letters:
            r2 = vm(r, Ms[a])
            if S.add(r2):
                queue.append(r2)
    R = S.vecs
    k = len(R)
    if k == 0:
        return [], {a: [] for a in letters}, []
    A = {a: [S.coords(vm(R[i], Ms[a])) for i in range(k)] for a in letters}
    lam1 = S.coords(lam)
    gam1 = [dot(R[i], gam) for i in range(k)]
    # backward (observable columns) in k-dim space; columns as vectors
    T = Span(k)
    queue = []
    if T.add(gam1):
        queue.append(list(gam1))
    while queue:
        c = queue.pop()
        for a in letters:
            c2 = mv(A[a], c)
            if T.add(c2):
                queue.append(c2)
    C = T.vecs  # list of column vectors
    d = len(C)
    if d == 0:
        return [], {a: [] for a in letters}, []
    # A_a C = C B_a : column j of B_a = coords of A_a C_j
    B = {}
    for a in letters:
        cols = [T.coords(mv(A[a], C[j])) for j in range(d)]
        B[a] = transpose(cols)
    lam2 = [dot(lam1, C[j]) for j in range(d)]
    gam2 = T.coords(gam1)
    return lam2, B, gam2

def evalw(lam, Ms, gam, w):
    v = list(lam)
    for a in w:
        v = vm(v, Ms[a])
    return dot(v, gam)

def words(alph, maxlen):
    for L in range(maxlen + 1):
        for t in itertools.product(alph, repeat=L):
            yield t

def hankel_rank(f, alph, L):
    W = list(words(alph, L))
    H = [[f(u + v) for v in W] for u in W]
    return rank(H)

# ------------------------------------------------------- spectral tools
def to_sym(A):
    return sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in row] for row in A])

def charpoly(A):
    x = sympy.Symbol('x')
    return sympy.Poly(to_sym(A).charpoly(x).as_expr(), x)

def poly_at(coeffs, A):
    """coeffs: list highest-first of Fractions; Horner."""
    n = len(A)
    R = zeros(n, n)
    for c in coeffs:
        R = mm(R, A)
        for i in range(n):
            R[i][i] += c
    return R

def jordan_parts(A):
    """Multiplicative Jordan-Chevalley decomposition over Q: A = S U, S semisimple, U unipotent,
    S, U polynomials in A.  Newton iteration on the squarefree part of the char. polynomial."""
    x = sympy.Symbol('x')
    p = charpoly(A)
    P = sympy.Poly(sympy.sqf_part(p.as_expr()), x)
    dP = P.diff(x)
    cP = [Fr(int(sympy.fraction(c)[0]), int(sympy.fraction(c)[1])) for c in P.all_coeffs()]
    cdP = [Fr(int(sympy.fraction(c)[0]), int(sympy.fraction(c)[1])) for c in dP.all_coeffs()]
    S = [list(r) for r in A]
    for _ in range(64):
        PS = poly_at(cP, S)
        if is_zero(PS):
            break
        S = madd(S, mm(PS, inv(poly_at(cdP, S))), Fr(-1))
    else:
        raise RuntimeError("Newton did not converge")
    U = mm(inv(S), A)
    return S, U

def is_unipotent(A):
    n = len(A)
    N = madd(A, eye(n), Fr(-1))
    return is_zero(mpow(N, n)) if n else True

def splits_over_Q(A):
    x = sympy.Symbol('x')
    p = charpoly(A)
    _, facs = sympy.factor_list(p.as_expr(), x)
    return all(sympy.degree(f, x) == 1 for f, _ in facs)

def power_splits(A, kmax=24):
    """Is there k<=kmax with charpoly(A^k) split over Q?"""
    B = eye(len(A))
    for k in range(1, kmax + 1):
        B = mm(B, A)
        if splits_over_Q(B):
            return k
    return None

# ------------------------------------------------------- multiaffine polynomials
# polynomial: dict frozenset(var indices) -> Fraction
def padd(p, q, c=Fr(1)):
    r = dict(p)
    for m, v in q.items():
        r[m] = r.get(m, Fr(0)) + c * v
        if r[m] == 0:
            del r[m]
    return r

def pmul(p, q):
    r = {}
    for m1, v1 in p.items():
        for m2, v2 in q.items():
            if m1 & m2:
                raise ValueError("not multiaffine (copyless violated)")
            m = m1 | m2
            r[m] = r.get(m, Fr(0)) + v1 * v2
            if r[m] == 0:
                del r[m]
    return r

def pconst(c):
    return {frozenset(): Fr(c)} if c != 0 else {}

def pvar(i):
    return {frozenset([i]): Fr(1)}

def peval(p, x):
    tot = Fr(0)
    for m, v in p.items():
        t = v
        for i in m:
            t *= x[i]
        tot += t
    return tot

def pcompose(p, P):
    """p o P where P is a tuple of polynomials (one per register)."""
    r = {}
    for m, v in p.items():
        t = pconst(v)
        for i in m:
            t = pmul(t, P[i])
        r = padd(r, t)
    return r

def pvars(p):
    s = set()
    for m in p:
        s |= m
    return s

class CCRA:
    """Deterministic CRA with polynomial updates. delta[(q,a)] = (q2, P) with P tuple of polys."""
    def __init__(self, states, q0, nreg, alph, delta, x0, out):
        self.states, self.q0, self.r, self.alph = list(states), q0, nreg, list(alph)
        self.delta, self.x0, self.out = delta, [Fr(v) for v in x0], out
    def is_copyless(self):
        for (q, a), (q2, P) in self.delta.items():
            seen = set()
            for p in P:
                vs = pvars(p)
                if vs & seen:
                    return False
                seen |= vs
        return True
    def run(self, w):
        q, x = self.q0, list(self.x0)
        for a in w:
            q2, P = self.delta[(q, a)]
            x = [peval(p, x) for p in P]
            q = q2
        return peval(self.out[q], x)
    def representation(self):
        """Pullback representation on (state, multiaffine monomial)."""
        mons = [frozenset(s) for k in range(self.r + 1) for s in itertools.combinations(range(self.r), k)]
        idx = {}
        for q in self.states:
            for m in mons:
                idx[(q, m)] = len(idx)
        n = len(idx)
        Ms = {}
        for a in self.alph:
            B = zeros(n, n)
            for q in self.states:
                q2, P = self.delta[(q, a)]
                for m2 in mons:
                    pb = pcompose({m2: Fr(1)}, P)
                    for m, v in pb.items():
                        B[idx[(q, m)]][idx[(q2, m2)]] += v
            Ms[a] = B
        lam = [Fr(0)] * n
        for m in mons:
            t = Fr(1)
            for i in m:
                t *= self.x0[i]
            lam[idx[(self.q0, m)]] = t
        gam = [Fr(0)] * n
        for q in self.states:
            for m, v in self.out[q].items():
                gam[idx[(q, m)]] = v
        return lam, Ms, gam
