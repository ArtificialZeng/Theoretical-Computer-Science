# Exact linear algebra over Q on top of python-flint (fmpq / fmpq_mat).
# Written for the polytime_claude sanity checks of c021.  Everything is exact.
import flint

Q = flint.fmpq
ZERO = Q(0)
ONE = Q(1)


def M(rows):
    """fmpq_mat from a list of lists (entries int/Fraction/fmpq)."""
    r = len(rows)
    c = len(rows[0]) if r else 0
    return flint.fmpq_mat(r, c, [Q(int(x.numerator), int(x.denominator)) if hasattr(x, 'numerator') and not isinstance(x, flint.fmpq) else Q(x) for row in rows for x in row])


def eye(n):
    return flint.fmpq_mat(n, n, [ONE if i == j else ZERO for i in range(n) for j in range(n)])


def zeros(r, c):
    return flint.fmpq_mat(r, c)


def vec(X):
    """row-major flattening of an fmpq_mat"""
    return list(X.entries())


def unvec(v, r, c):
    return flint.fmpq_mat(r, c, list(v))


def is_zero_mat(X):
    return all(e == 0 for e in X.entries())


def from_rows(vectors, ncols):
    if not vectors:
        return flint.fmpq_mat(0, ncols)
    return flint.fmpq_mat(len(vectors), ncols, [x for v in vectors for x in v])


def rref_basis(vectors, ncols):
    """RREF basis (list of row vectors) of the span of `vectors`, plus pivot columns."""
    if not vectors:
        return [], []
    A = from_rows(vectors, ncols)
    R, rk = A.rref()
    rows = [list(R.entries()[i * ncols:(i + 1) * ncols]) for i in range(rk)]
    piv = []
    for row in rows:
        for j, x in enumerate(row):
            if x != 0:
                piv.append(j)
                break
    return rows, piv


def rank(vectors, ncols):
    if not vectors:
        return 0
    return from_rows(vectors, ncols).rank()


def nullspace(A):
    """basis of {x : A x = 0} for an fmpq_mat A (r x c); returns list of vectors (lists)."""
    r, c = A.nrows(), A.ncols()
    if r == 0:
        return [[ONE if i == j else ZERO for i in range(c)] for j in range(c)]
    R, rk = A.rref()
    E = R.entries()
    piv = []
    for i in range(rk):
        for j in range(c):
            if E[i * c + j] != 0:
                piv.append(j)
                break
    free = [j for j in range(c) if j not in piv]
    basis = []
    for f in free:
        x = [ZERO] * c
        x[f] = ONE
        for i, p in enumerate(piv):
            x[p] = -E[i * c + f]
        basis.append(x)
    return basis


def solve_particular(A, b):
    """one solution x of A x = b (A fmpq_mat r x c, b list) or None.
    Deterministic choice: free variables set to 0 (RREF rule)."""
    r, c = A.nrows(), A.ncols()
    aug = flint.fmpq_mat(r, c + 1, [x for i in range(r) for x in (list(A.entries()[i * c:(i + 1) * c]) + [b[i]])])
    R, rk = aug.rref()
    E = R.entries()
    x = [ZERO] * c
    for i in range(rk):
        row = E[i * (c + 1):(i + 1) * (c + 1)]
        p = next(j for j in range(c + 1) if row[j] != 0)
        if p == c:
            return None
        x[p] = row[c]
    return x


class Subspace:
    """Subspace of Q^n given by an RREF basis."""

    def __init__(self, vectors, n):
        self.n = n
        self.basis, self.piv = rref_basis([list(v) for v in vectors], n)

    @property
    def dim(self):
        return len(self.basis)

    def contains(self, v):
        v = list(v)
        for row, p in zip(self.basis, self.piv):
            if v[p] != 0:
                c = v[p]
                v = [a - c * b for a, b in zip(v, row)]
        return all(x == 0 for x in v)

    def coords(self, v):
        """coordinates of v w.r.t. the RREF basis (assumes v in span)"""
        v = list(v)
        cs = []
        for row, p in zip(self.basis, self.piv):
            c = v[p]
            cs.append(c)
            if c != 0:
                v = [a - c * b for a, b in zip(v, row)]
        assert all(x == 0 for x in v), "vector not in subspace"
        return cs

    def reduce(self, v):
        v = list(v)
        for row, p in zip(self.basis, self.piv):
            if v[p] != 0:
                c = v[p]
                v = [a - c * b for a, b in zip(v, row)]
        return v

    def add(self, vectors):
        # incremental RREF insertion (returns a new Subspace)
        S = Subspace.__new__(Subspace)
        S.n = self.n
        S.basis = [list(r) for r in self.basis]
        S.piv = list(self.piv)
        for v in vectors:
            v = S.reduce(v)
            p = next((j for j, x in enumerate(v) if x != 0), None)
            if p is None:
                continue
            c = v[p]
            v = [x / c for x in v]
            for i, row in enumerate(S.basis):
                if row[p] != 0:
                    f = row[p]
                    S.basis[i] = [a - f * b for a, b in zip(row, v)]
            # insert keeping pivots sorted
            k = 0
            while k < len(S.piv) and S.piv[k] < p:
                k += 1
            S.basis.insert(k, v)
            S.piv.insert(k, p)
        return S

    def __eq__(self, other):
        return self.n == other.n and self.basis == other.basis


def intersect(S, T):
    """intersection of two subspaces of Q^n"""
    n = S.n
    if S.dim == 0 or T.dim == 0:
        return Subspace([], n)
    # solve sum a_i s_i - sum b_j t_j = 0
    cols = S.basis + [[-x for x in t] for t in T.basis]
    A = flint.fmpq_mat(n, len(cols), [cols[j][i] for i in range(n) for j in range(len(cols))])
    ns = nullspace(A)
    vs = []
    for x in ns:
        v = [ZERO] * n
        for i, s in enumerate(S.basis):
            if x[i] != 0:
                v = [a + x[i] * b for a, b in zip(v, s)]
        vs.append(v)
    return Subspace(vs, n)


def mat_bits(X):
    """max bit size of numerator/denominator over entries"""
    b = 0
    for e in X.entries():
        b = max(b, int(e.p).bit_length(), int(e.q).bit_length())
    return b


def vec_bits(v):
    b = 0
    for e in v:
        e = Q(e)
        b = max(b, int(e.p).bit_length(), int(e.q).bit_length())
    return b
