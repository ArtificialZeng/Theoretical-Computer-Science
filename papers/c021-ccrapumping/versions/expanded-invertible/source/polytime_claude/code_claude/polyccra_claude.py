# Polynomial-time decision procedure for condition (3) of the c021 main theorem
# (CCRA-computability of invertible series), as described in section_claude.tex.
#
# Input: invertible rational matrices M_1..M_k (minimal letter matrices).
# Output: verdict of condition (3):  G^o triangularizable over Q  and  R_u(G) abelian,
#         where G is the Zariski closure of Gamma = <M_1..M_k>.
#
# Steps (numbering as in section_claude.tex):
#   1. A = span(Gamma), J = rad(A) (trace form), flag F_k = J^k Q^d, adapted basis
#      -> block upper triangular form; b_P = block-diagonal part (completely reducible).
#   2. (a)-test: H^o split torus, via B = finite-image part of Ad(Gamma-bar) on M_d(Q),
#      C = centraliser of B;  (a) <=> C commutative and split.  Finiteness of a completely
#      reducible group is tested by the self-contained trace-duality test `is_finite_cr`.
#   3. Layered computation of Lie(R_u(G)) in the abelian regime (Proposition "layer").
import itertools, random
import flint
from linalg_claude import (Q, ZERO, ONE, eye, zeros, vec, unvec, is_zero_mat, from_rows,
                           rref_basis, rank, nullspace, solve_particular, Subspace,
                           intersect, mat_bits, vec_bits)


def to_fmpq_mat(A):
    rows = [[Q(int(x.p), int(x.q)) if isinstance(x, flint.fmpq) else
             (Q(int(x.numerator), int(x.denominator)) if hasattr(x, 'numerator') else Q(x))
             for x in row] for row in A]
    return flint.fmpq_mat(len(rows), len(rows[0]), [x for r in rows for x in r])


def trace(X):
    return sum((X[i, i] for i in range(X.nrows())), ZERO)


# ---------------------------------------------------------------- step 1
def span_algebra(gens, d):
    """basis (as matrices) of span of all words; also returns the words' matrices used."""
    S = Subspace([], d * d)
    basis_mats = []
    queue = [eye(d)]
    while queue:
        X = queue.pop(0)
        v = vec(X)
        if not S.contains(v):
            S = S.add([v])
            basis_mats.append(X)
            for g in gens:
                queue.append(X * g)
    return basis_mats, S


def radical(Abasis, d):
    r = len(Abasis)
    T = flint.fmpq_mat(r, r, [trace(Abasis[i] * Abasis[j]) for i in range(r) for j in range(r)])
    ns = nullspace(T)
    J = []
    for c in ns:
        X = zeros(d, d)
        for i in range(r):
            if c[i] != 0:
                X += c[i] * Abasis[i]
        J.append(X)
    return J


def radical_flag(J, d):
    """F_0 = Q^d, F_{k+1} = J F_k; returns list of Subspaces (nonzero ones)."""
    F = [Subspace([[ONE if i == j else ZERO for i in range(d)] for j in range(d)], d)]
    while True:
        cur = F[-1]
        vs = []
        for X in J:
            for b in cur.basis:
                col = flint.fmpq_mat(d, 1, b)
                vs.append(list((X * col).entries()))
        nxt = Subspace(vs, d)
        if nxt.dim == 0:
            break
        assert nxt.dim < cur.dim
        F.append(nxt)
    return F


def adapted_basis(F, d):
    """columns ordered deepest-first so that Gamma is block upper triangular.
    returns P (d x d), blk (block index per coordinate), m (number of blocks)."""
    m = len(F)
    cols = []
    blk = []
    S = Subspace([], d)
    for p in range(m):          # block p spans a complement of F_{m-p} in F_{m-1-p}
        k = m - 1 - p
        for b in F[k].basis:
            if not S.contains(b):
                S = S.add([b])
                cols.append(b)
                blk.append(p)
    assert len(cols) == d
    P = flint.fmpq_mat(d, d, [cols[j][i] for i in range(d) for j in range(d)])
    return P, blk, m


class Setup:
    def __init__(self, gens):
        self.d = d = gens[0].nrows()
        self.orig = gens
        Ab, _ = span_algebra(gens, d)
        self.dimA = len(Ab)
        J = radical(Ab, d)
        self.dimJ = len(J)
        F = radical_flag(J, d)
        P, blk, m = adapted_basis(F, d)
        self.P, self.blk, self.m = P, blk, m
        Pi = P.inv()
        self.gens = [Pi * g * P for g in gens]
        for g in self.gens:
            for r in range(d):
                for c in range(d):
                    if blk[c] < blk[r]:
                        assert g[r, c] == 0, "not block upper triangular"
        self.bdiag = [self.diag_part(g) for g in self.gens]
        self.nu = [b.inv() * g for b, g in zip(self.bdiag, self.gens)]

    def dist(self, r, c):
        return self.blk[c] - self.blk[r]

    def diag_part(self, X):
        d = self.d
        return flint.fmpq_mat(d, d, [X[r, c] if self.blk[r] == self.blk[c] else ZERO
                                     for r in range(d) for c in range(d)])

    def trunc(self, X, j):
        d = self.d
        return flint.fmpq_mat(d, d, [X[r, c] if 0 <= self.dist(r, c) <= j else ZERO
                                     for r in range(d) for c in range(d)])

    def comp(self, X, t):
        d = self.d
        return flint.fmpq_mat(d, d, [X[r, c] if self.dist(r, c) == t else ZERO
                                     for r in range(d) for c in range(d)])

    def vbasis(self, t):
        d = self.d
        out = []
        for r in range(d):
            for c in range(d):
                if self.dist(r, c) == t:
                    E = zeros(d, d)
                    E[r, c] = ONE
                    out.append(E)
        return out

    def nexp(self, X, j):
        d = self.d
        R = eye(d)
        T = eye(d)
        for k in range(1, self.m + 1):
            T = self.trunc(T * X, j) * Q(1, k)
            if is_zero_mat(T):
                break
            R += T
        return self.trunc(R, j)

    def nlog(self, U, j):
        d = self.d
        N = self.trunc(U, j) - eye(d)
        R = zeros(d, d)
        T = eye(d)
        for k in range(1, self.m + 1):
            T = self.trunc(T * N, j)
            if is_zero_mat(T):
                break
            R += Q((-1) ** (k + 1), k) * T
        return R


# ---------------------------------------------------------------- finiteness test
def is_finite_cr(gens, n, want_order_bound=False):
    """Deterministic test whether the completely reducible group generated by `gens`
    (n x n rational, invertible) is finite.  Trace-duality lattice + Reynolds form.
    Returns (finite: bool, reason: str)."""
    words, _ = span_algebra(gens, n)
    r = len(words)
    G = [[trace(words[i] * words[j]) for j in range(r)] for i in range(r)]
    for row in G:
        for x in row:
            if x.q != 1 or abs(int(x.p)) > n:
                return False, "trace not an integer of size <= n"
    Gm = flint.fmpq_mat(r, r, [x for row in G for x in row])
    detG = Gm.det()
    # lattice closure in coordinates x -> (tr(x w_i))_i  (dual-basis coordinates)
    def coords(X):
        return [trace(X * words[i]) for i in range(r)]
    gens_all = list(gens)
    # integer HNF of current lattice
    cur = [coords(w) for w in words]       # = rows of G
    mats = list(words)                      # representatives spanning current lattice over Z
    import math
    steps = 0
    while True:
        steps += 1
        new_rows = []
        new_mats = []
        for X in mats:
            for g in gens_all:
                Y = X * g
                cy = coords(Y)
                if any(c.q != 1 for c in cy):
                    return False, "lattice escapes the trace dual"
                new_rows.append(cy)
                new_mats.append(Y)
        allrows = cur + new_rows
        Z = flint.fmpz_mat(len(allrows), r, [int(c.p) for row in allrows for c in row])
        H = Z.hnf()
        Hrows = [[H[i, j] for j in range(r)] for i in range(H.nrows()) if any(H[i, j] != 0 for j in range(r))]
        Zc = flint.fmpz_mat(len(cur), r, [int(c.p) for row in cur for c in row]).hnf()
        Crows = [[Zc[i, j] for j in range(r)] for i in range(Zc.nrows()) if any(Zc[i, j] != 0 for j in range(r))]
        if Hrows == Crows:
            break
        # keep representatives: we need matrices spanning the new lattice; recover from
        # coordinates via dual basis (coordinates determine the element)
        Ginv = Gm.inv()
        mats = []
        cur = []
        for row in Hrows:
            # element with coordinates row: X = sum_i row_i w_i^#,  w^# = Ginv * w
            X = zeros(n, n)
            for i in range(r):
                if row[i] != 0:
                    wi = zeros(n, n)
                    for jx in range(r):
                        if Ginv[i, jx] != 0:
                            wi += Ginv[i, jx] * words[jx]
                    X += Q(int(row[i])) * wi
            mats.append(X)
            cur.append([Q(int(c)) for c in row])
        if steps > 4 * r * (abs(int(detG.p)).bit_length() + 2):
            raise RuntimeError("lattice closure did not stabilise (should not happen)")
    # Reynolds projection of the identity onto invariant symmetric forms
    symb = []
    for i in range(n):
        for j in range(i, n):
            E = zeros(n, n)
            E[i, j] = ONE
            E[j, i] = ONE
            symb.append(E)
    s = len(symb)
    Ssub = Subspace([vec(E) for E in symb], n * n)
    def rho(g, X):
        return g.transpose() * X * g
    # invariants: (rho(g)-1)X = 0
    rows = []
    for g in gens:
        cols = [vec(rho(g, E) - E) for E in symb]
        for k in range(n * n):
            rows.append([cols[c][k] for c in range(s)])
    A = flint.fmpq_mat(len(rows), s, [x for row in rows for x in row])
    inv = nullspace(A)
    inv_mats = []
    for c in inv:
        X = zeros(n, n)
        for t in range(s):
            if c[t] != 0:
                X += c[t] * symb[t]
        inv_mats.append(X)
    img = []
    for g in gens:
        for E in symb:
            img.append(vec(rho(g, E) - E))
    Img = Subspace(img, n * n)
    if Img.dim + len(inv_mats) != s:
        return False, "Reynolds decomposition not direct (not completely reducible?)"
    # write I = I0 + I1, I0 in span(inv_mats), I1 in Img
    cols = [vec(X) for X in inv_mats] + Img.basis
    Am = flint.fmpq_mat(n * n, len(cols), [cols[c][k] for k in range(n * n) for c in range(len(cols))])
    sol = solve_particular(Am, vec(eye(n)))
    assert sol is not None
    I0 = zeros(n, n)
    for t, X in enumerate(inv_mats):
        if sol[t] != 0:
            I0 += sol[t] * X
    for k in range(1, n + 1):
        sub = flint.fmpq_mat(k, k, [I0[i, j] for i in range(k) for j in range(k)])
        if sub.det() <= 0:
            return False, "Reynolds form not positive definite"
    return True, "finite (invariant lattice and positive definite form)"


def enumerate_group(gens, limit=200000):
    """BFS enumeration of a finite matrix group (generators and inverses)."""
    n = gens[0].nrows()
    allg = list(gens) + [g.inv() for g in gens]
    key = lambda X: tuple(X.entries())
    I = eye(n)
    elems = {key(I): I}
    order = [I]
    i = 0
    while i < len(order):
        X = order[i]
        i += 1
        for g in allg:
            Y = X * g
            k = key(Y)
            if k not in elems:
                elems[k] = Y
                order.append(Y)
                if len(order) > limit:
                    raise RuntimeError("group too large")
    return order


# ---------------------------------------------------------------- step 2: (a)-test
def restrict_action(ops, sub_basis_vecs, N):
    """matrices of operators (on Q^N, given as fmpq_mat N x N) restricted to the invariant
    subspace with basis sub_basis_vecs."""
    S = Subspace(sub_basis_vecs, N)
    out = []
    for T in ops:
        cols = []
        for b in S.basis:
            img = list((T * flint.fmpq_mat(N, 1, b)).entries())
            cols.append(S.coords(img))
        k = len(S.basis)
        out.append(flint.fmpq_mat(k, k, [cols[j][i] for i in range(k) for j in range(k)]))
    return out, S


def central_idempotents(ops, N, rng):
    """primitive central idempotents of the semisimple algebra Env(ops) (ops invertible);
    randomized primitive-element method (sufficient for sanity checks)."""
    words, _ = span_algebra(ops, N)
    a = len(words)
    # centre: z = sum c_i w_i commuting with all ops
    rows = []
    for g in ops:
        cols = [vec(w * g - g * w) for w in words]
        for k in range(N * N):
            rows.append([cols[c][k] for c in range(a)])
    A = flint.fmpq_mat(len(rows), a, [x for row in rows for x in row])
    zc = nullspace(A)
    Zb = []
    for c in zc:
        X = zeros(N, N)
        for i in range(a):
            if c[i] != 0:
                X += c[i] * words[i]
        Zb.append(X)
    dimZ = len(Zb)
    for attempt in range(50):
        z = zeros(N, N)
        for X in Zb:
            z += Q(rng.randint(-20, 20)) * X
        mp = z.minpoly()
        if mp.degree() == dimZ:
            break
    else:
        raise RuntimeError("no primitive element found")
    fac = mp.factor()[1]
    idem = []
    for (p, e) in fac:
        assert e == 1
        q = mp // p          # exact division
        # find u with u*q = 1 mod p
        g, s, t = q.xgcd(p)
        assert g.degree() == 0
        u = s * (1 / g.coeffs()[0])
        poly = (u * q) % mp
        E = zeros(N, N)
        P = eye(N)
        coeffs = poly.coeffs()
        for cf in coeffs:
            E += cf * P
            P = P * z
        idem.append(E)
    return idem


def a_test(setup, rng=None):
    """(a): H^o is a Q-split torus.  Returns (bool, info dict)."""
    rng = rng or random.Random(1)
    d = setup.d
    gb = setup.bdiag
    N = d * d
    # conjugation action on M_d(Q) (row-major vec):  X -> g X g^{-1}
    ops = []
    for g in gb:
        gi = g.inv()
        cols = []
        for k in range(N):
            E = zeros(d, d)
            E[k // d, k % d] = ONE
            cols.append(vec(g * E * gi))
        ops.append(flint.fmpq_mat(N, N, [cols[j][i] for i in range(N) for j in range(N)]))
    # semisimplicity of A_theta (Lemma "atest"): radical by the trace criterion
    Aw, _ = span_algebra(ops, N)
    if radical(Aw, N):
        return False, dict(components=[], dimB=0, dimC=0, commutative=False, split=False,
                           reason='A_theta not semisimple')
    idem = central_idempotents(ops, N, rng)
    Bvecs = []
    comps = []
    for E in idem:
        # W = image of E
        imgs = [list(E.transpose().entries()[k * N:(k + 1) * N]) for k in range(N)]  # columns of E
        W = Subspace(imgs, N)
        res, _ = restrict_action(ops, W.basis, N)
        fin, why = is_finite_cr(res, W.dim)
        comps.append((W.dim, fin, why))
        if fin:
            Bvecs += W.basis
    B = Subspace(Bvecs, N)
    # centraliser of B in M_d(Q)
    rows = []
    Bm = [unvec(b, d, d) for b in B.basis]
    for X in Bm:
        cols = []
        for k in range(N):
            E = zeros(d, d)
            E[k // d, k % d] = ONE
            cols.append(vec(E * X - X * E))
        for k in range(N):
            rows.append([cols[c][k] for c in range(N)])
    if rows:
        A = flint.fmpq_mat(len(rows), N, [x for row in rows for x in row])
        Cv = nullspace(A)
    else:
        Cv = [vec(E) for E in [unvec([ONE if t == k else ZERO for t in range(N)], d, d) for k in range(N)]]
    Cm = [unvec(c, d, d) for c in Cv]
    commutative = all(is_zero_mat(X * Y - Y * X) for X in Cm for Y in Cm)
    split = True
    if commutative:
        for X in Cm:
            mp = X.minpoly()
            for (p, e) in mp.factor()[1]:
                if p.degree() != 1 or e != 1:
                    split = False
    info = dict(components=comps, dimB=B.dim, dimC=len(Cm), commutative=commutative, split=split)
    info['_B'] = [unvec(b, d, d) for b in B.basis]
    info['_C'] = Cm
    return commutative and split, info


# ---------------------------------------------------------------- step 3: layered U
def u_layers(setup, check=True, record=None):
    """Layered computation of Lie(R_u(G)) in the abelian regime.
    Returns ('abelian', ubasis) if R_u(G) is abelian, else ('nonabelian', level, ubasis_prev)."""
    S = setup
    d, m = S.d, S.m
    gens, bd = S.gens, S.bdiag
    ubasis = []                 # canonical u_j (truncated matrices)
    v = eye(d)                  # Levi conjugator for G_j
    hist = []
    for j in range(0, m - 1):
        # abelian test for U_{j+1}
        for X in ubasis:
            for Y in ubasis:
                if not is_zero_mat(S.comp(X * Y - Y * X, j + 1)):
                    if record is not None:
                        record['hist'] = hist
                    return ('nonabelian', j + 1, ubasis)
        Mb = [S.trunc(X, j) for X in ubasis] + S.vbasis(j + 1)
        Msub = Subspace([vec(X) for X in Mb], d * d)
        mu = Msub.dim
        Mmats = [unvec(b, d, d) for b in Msub.basis]
        vi = v.inv()
        ell = [S.trunc(v * b * vi, j + 1) for b in bd]
        ells_inv = [l.inv() for l in ell]
        cs = []
        for l, li, g in zip(ell, ells_inv, gens):
            c = S.nlog(S.trunc(li * g, j + 1), j + 1)
            assert Msub.contains(vec(c)), "cocycle value not in M"
            cs.append(Msub.coords(vec(c)))
        Aa = []
        for l, li in zip(ell, ells_inv):
            cols = []
            for X in Mmats:
                Y = S.trunc(l * X * li, j + 1)
                cols.append(Msub.coords(vec(Y)))
            Aa.append(flint.fmpq_mat(mu, mu, [cols[c][r] for r in range(mu) for c in range(mu)]))
        # commutant E of {A_a}: phi A - A phi = 0, phi as mu x mu (row-major unknowns)
        rows = []
        for A in Aa:
            for r in range(mu):
                for c in range(mu):
                    row = [ZERO] * (mu * mu)
                    # (phi A)_{rc} = sum_k phi_{rk} A_{kc};  (A phi)_{rc} = sum_k A_{rk} phi_{kc}
                    for k in range(mu):
                        row[r * mu + k] += A[k, c]
                        row[k * mu + c] -= A[r, k]
                    rows.append(row)
        Ecom = nullspace(flint.fmpq_mat(len(rows), mu * mu, [x for row in rows for x in row])) if rows else \
            [[ONE if t == s else ZERO for t in range(mu * mu)] for s in range(mu * mu)]
        Emats = [unvec(e, mu, mu) for e in Ecom]
        ne = len(Emats)
        # Phi-system: unknowns (x_1..x_ne, y_1..y_mu):  sum_i x_i E_i c_a - (I - A_a^{-1}) y = 0
        rows = []
        Imu = eye(mu)
        for A, c in zip(Aa, cs):
            cm = flint.fmpq_mat(mu, 1, c)
            Ecols = [list((Ei * cm).entries()) for Ei in Emats]
            Bm = Imu - A.inv()
            for r in range(mu):
                rows.append([Ecols[i][r] for i in range(ne)] + [-Bm[r, s] for s in range(mu)])
        ns = nullspace(flint.fmpq_mat(len(rows), ne + mu, [x for row in rows for x in row]))
        Phi = Subspace([x[:ne] for x in ns], ne)
        phis = []
        for x in Phi.basis:
            P = zeros(mu, mu)
            for i in range(ne):
                if x[i] != 0:
                    P += x[i] * Emats[i]
            phis.append(P)
        if phis:
            stack = flint.fmpq_mat(mu * len(phis), mu, [x for P in phis for x in P.entries()])
            Wc = nullspace(stack)
        else:
            Wc = [[ONE if t == s else ZERO for t in range(mu)] for s in range(mu)]
        Wsub = Subspace(Wc, mu)
        # back to matrices
        new_u = []
        for w in Wsub.basis:
            X = zeros(d, d)
            for i in range(mu):
                if w[i] != 0:
                    X += w[i] * Mmats[i]
            new_u.append(X)
        Usub = Subspace([vec(X) for X in new_u], d * d)
        new_u = [unvec(b, d, d) for b in Usub.basis]
        # new Levi conjugator (as in Lemma "sizes" of section_claude.tex):
        # RREF basis of u_{j+1} in coordinates ordered by increasing distance; u_a = lift of
        # c_a mod v_{j+1} read off at pivots of distance <= j; r_a = (c_a - u_a)_{j+1};
        # solve (1 - Ad(b_a)^{-1}) y + w_a = r_a, y in v_{j+1}, w_a in u_{j+1} cap v_{j+1}.
        pos = sorted([(S.dist(r, c), r, c) for r in range(d) for c in range(d) if S.dist(r, c) >= 1])
        def dvec(X):
            return [X[r, c] for (_, r, c) in pos]
        Ud = Subspace([dvec(X) for X in new_u], len(pos))
        low = [(row, p) for row, p in zip(Ud.basis, Ud.piv) if pos[p][0] <= j]
        top = [row for row, p in zip(Ud.basis, Ud.piv) if pos[p][0] == j + 1]
        topidx = [i for i, (t, _, _) in enumerate(pos) if t == j + 1]
        for row in top:
            assert all(row[i] == 0 for i in range(len(pos)) if pos[i][0] != j + 1)
        nv = len(topidx)
        nw = len(top)
        k = len(gens)
        rows = []
        rhs = []
        V1 = S.vbasis(j + 1)          # same order as topidx (row-major within distance j+1)
        assert len(V1) == nv
        for ia, (b, g) in enumerate(zip(bd, gens)):
            cm = S.nlog(S.trunc(ell[ia].inv() * g, j + 1), j + 1)
            cv = dvec(cm)
            ua = [ZERO] * len(pos)
            for row, p in low:
                if cv[p] != 0:
                    ua = [x + cv[p] * y for x, y in zip(ua, row)]
            ra = [cv[i] - ua[i] for i in range(len(pos))]
            assert all(ra[i] == 0 for i in range(len(pos)) if pos[i][0] <= j), "lift failed"
            bi = b.inv()
            cols = []
            for E in V1:
                Z = E - bi * E * b
                cols.append([Z[pos[i][1], pos[i][2]] for i in topidx])
            for e in range(nv):
                row = [cols[s][e] for s in range(nv)]
                for ib in range(k):
                    row += [top[t][topidx[e]] if ib == ia else ZERO for t in range(nw)]
                rows.append(row)
                rhs.append(ra[topidx[e]])
        Am = flint.fmpq_mat(len(rows), nv + k * nw, [x for row in rows for x in row])
        sol = solve_particular(Am, rhs)
        assert sol is not None, "no Levi correction found (theory violated)"
        Y = zeros(d, d)
        for s in range(nv):
            if sol[s] != 0:
                Y += sol[s] * V1[s]
        v = S.trunc(S.nexp(-Y, j + 1) * v, j + 1)
        if check:
            vi = v.inv()
            for b, g in zip(bd, gens):
                l = S.trunc(v * b * vi, j + 1)
                c = S.nlog(S.trunc(l.inv() * g, j + 1), j + 1)
                assert Usub.contains(vec(c)), "Levi conjugator invariant fails"
            # Ad(Gamma)-stability of u_{j+1}
            for g in gens:
                gi = g.inv()
                for X in new_u:
                    assert Usub.contains(vec(S.trunc(g * X * gi, j + 1))), "u not Ad-stable"
        if record is not None:
            record.setdefault('ub', {})[j + 1] = new_u
        hist.append(dict(level=j + 1, dimM=mu, dimE=ne, dimPhi=len(phis), dimU=len(new_u),
                         bits_u=max([mat_bits(X) for X in new_u] + [0]), bits_v=mat_bits(v)))
        ubasis = new_u
    if record is not None:
        record['hist'] = hist
    # final abelian check (level m-1 is the whole group)
    for X in ubasis:
        for Y in ubasis:
            assert is_zero_mat(X * Y - Y * X)
    return ('abelian', ubasis)


def decide(gens, rng=None, record=None):
    """decide condition (3) for Gamma = <gens>.  Returns (verdict, details)."""
    S = Setup(gens)
    det = dict(d=S.d, dimA=S.dimA, dimJ=S.dimJ, m=S.m)
    ok, info = a_test(S, rng)
    det['a'] = info
    if not ok:
        return False, det
    rec = {}
    res = u_layers(S, record=rec)
    det['u'] = res[0]
    det['hist'] = rec.get('hist')
    if res[0] == 'nonabelian':
        det['nonabelian_level'] = res[1]
        return False, det
    det['dimU'] = len(res[1])
    return True, det


def decide_qu(gens, record=None):
    """quasi-unipotent sector: test finiteness of b_P(Gamma), then layered U."""
    S = Setup(gens)
    fin, why = is_finite_cr(S.bdiag, S.d)
    det = dict(d=S.d, dimA=S.dimA, dimJ=S.dimJ, m=S.m, finite_semisimple_part=fin, why=why)
    if not fin:
        return None, det   # not quasi-unipotent
    rec = {}
    res = u_layers(S, record=rec)
    det['u'] = res[0]
    det['hist'] = rec.get('hist')
    return res[0] == 'abelian', det
