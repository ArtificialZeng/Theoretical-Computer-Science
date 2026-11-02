# Driver: python3 -I test_detpoly_claude.py FAMILY SEED NTESTS [L]
# families: deep_yes, deep_no (torus + monomial finite part, as in polytime_claude/test_deep),
#           weyl2, weyl3 (multiplicative affine Weyl group A~_n with a unipotent extension)
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from detpoly_check_claude import *

family = sys.argv[1] if len(sys.argv) > 1 else 'deep_yes'
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
ntests = int(sys.argv[3]) if len(sys.argv) > 3 else 5
Lw = int(sys.argv[4]) if len(sys.argv) > 4 else 3
R = random.Random(seed)


def monomial(s, torus):
    p = list(range(s)); R.shuffle(p)
    M = zeros(s, s)
    for i in range(s):
        val = Q(R.choice([1, -1]))
        if torus and R.random() < 0.5:
            val *= Q(R.choice([2, 3, 1]), R.choice([1, 2]))
        M[p[i], i] = val
    return M


def rand_GL(n):
    while True:
        P = flint.fmpq_mat(n, n, [Q(R.randint(-1, 1)) for _ in range(n * n)])
        if P.det() != 0:
            return P


def deep_instance(yes):
    while True:
        m = R.choice([3, 4, 4, 5]); s = R.choice([1, 1, 2])
        if m * s <= 6:
            break
    n = m * s; k = R.choice([2, 3])
    ells = []
    for _ in range(k):
        mu = Q(R.choice([1, -1, 2, 3, -2]), R.choice([1, 1, 2]))
        P = monomial(s, True)
        L = zeros(n, n)
        for q in range(m):
            for i in range(s):
                for j in range(s):
                    L[q * s + i, q * s + j] = (mu ** q) * P[i, j]
        ells.append(L)
    Xs = []
    for _ in range(k):
        X = zeros(n, n)
        if yes:
            for i in range(1, m):
                D = [Q(R.randint(-2, 2)) for _ in range(s)]
                for q in range(m - i):
                    for t in range(s):
                        X[q * s + t, (q + i) * s + t] = D[t]
        else:
            for r in range(n):
                for c in range(n):
                    if c // s > r // s and R.random() < 0.5:
                        X[r, c] = Q(R.randint(-2, 2))
        Xs.append(X)
    vX = zeros(n, n)
    for r in range(n):
        for c in range(n):
            if c // s > r // s and R.random() < 0.6:
                vX[r, c] = Q(R.randint(-2, 2), R.choice([1, 2]))
    v = mexp(vX)
    P = rand_GL(n) if R.random() < 0.7 else eye(n)
    vi, Pi = v.inv(), P.inv()
    return [P * v * l * mexp(X) * vi * Pi for l, X in zip(ells, Xs)]


def perm_matrix(n1, i, j):
    P = eye(n1)
    P[i, i] = ZERO; P[j, j] = ZERO; P[i, j] = ONE; P[j, i] = ONE
    return P


def weyl_instance(nb):
    n = R.choice([2, 3]); n1 = n + 1
    base = [perm_matrix(n1, i, i + 1) for i in range(n)]
    D = eye(n1); D[0, 0] = Q(2); D[n, n] = Q(1, 2)
    base.append(D * perm_matrix(n1, 0, n))
    # nb blocks: V, V, ..., trivial line; generator = block upper triangular with random corners
    dims = [n1] * (nb - 1) + [1]
    off = [sum(dims[:i]) for i in range(nb)]
    d = sum(dims)
    gens = []
    for g in base:
        M = zeros(d, d)
        for b in range(nb):
            blkm = g if dims[b] == n1 else eye(1)
            for r in range(dims[b]):
                for c in range(dims[b]):
                    M[off[b] + r, off[b] + c] = blkm[r, c]
        for b1 in range(nb):
            for b2 in range(b1 + 1, nb):
                for r in range(dims[b1]):
                    for c in range(dims[b2]):
                        if R.random() < 0.5:
                            M[off[b1] + r, off[b2] + c] = Q(R.randint(-1, 1))
        gens.append(M)
    P = rand_GL(d) if R.random() < 0.5 else eye(d)
    Pi = P.inv()
    return [P * g * Pi for g in gens]


stats = dict(tests=0, T1=0, Z3=0, xhat=0, skipped=0)
t0 = time.time()
for t in range(ntests):
    if family.startswith('deep'):
        gens = deep_instance(family == 'deep_yes')
    else:
        gens = weyl_instance(int(family[-1]))
    try:
        D = Detpoly(gens)
        D.iterative = (os.environ.get('ITER') == '1')
        res = D.run(Lw)
    except (RuntimeError, AssertionError) as e:
        stats['skipped'] += 1
        print(f"[{t}] skipped: {e}", flush=True)
        continue
    stats['tests'] += 1
    stats['T1'] += bool(res.get('T1_ok'))
    stats['Z3'] += bool(res.get('Z3_ok'))
    stats['xhat'] += bool(res.get('xhat_in_U'))
    print(f"[{t}] {res}", flush=True)
print(family, stats, f"{time.time() - t0:.1f}s")
