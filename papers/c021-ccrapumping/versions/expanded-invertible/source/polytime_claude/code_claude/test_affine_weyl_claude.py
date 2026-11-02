# Affine Weyl group of type A~_n, realised (i) by affine maps of Q^{n+1} (quasi-unipotent
# sector, R_u(G) = translations, |G/G^o| = (n+1)!), and (ii) multiplicatively inside GL_{n+1}(Q)
# (torus sector, H^o = det-1 diagonal torus, finite part S_{n+1}).  Every word of length <= n in
# the n+1 Coxeter generators lies in a proper (finite) parabolic subgroup, so it has finite order;
# yet the algorithm must find the n-dimensional unipotent radical (case (i)).  The finite
# quotient is never enumerated by the algorithm; the exponential ground truth is run only for small n.
import sys, time, itertools, random
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import flint
from linalg_claude import Q, ZERO, ONE, eye, zeros, vec, unvec, is_zero_mat, Subspace
from polyccra_claude import Setup, u_layers, is_finite_cr, decide, decide_qu
from groundtruth_claude import gt_qu


def perm_matrix(n1, i, j):
    P = eye(n1)
    P[i, i] = ZERO; P[j, j] = ZERO; P[i, j] = ONE; P[j, i] = ONE
    return P


def affine_gens(n):
    n1 = n + 1
    gens = []
    for i in range(n):                      # s_1..s_n
        g = eye(n1 + 1)
        P = perm_matrix(n1, i, i + 1)
        for r in range(n1):
            for c in range(n1):
                g[r, c] = P[r, c]
        gens.append(g)
    g = eye(n1 + 1)                         # s_0 = t_{e1 - e_{n+1}} s_theta
    P = perm_matrix(n1, 0, n)
    for r in range(n1):
        for c in range(n1):
            g[r, c] = P[r, c]
    g[0, n1] = ONE
    g[n, n1] = -ONE
    gens.append(g)
    return gens


def torus_gens(n):
    n1 = n + 1
    gens = [perm_matrix(n1, i, i + 1) for i in range(n)]
    D = eye(n1); D[0, 0] = Q(2); D[n, n] = Q(1, 2)
    gens.append(D * perm_matrix(n1, 0, n))
    return gens


def short_words_finite(gens, maxlen):
    """check: every word of length <= maxlen has a power with all eigenvalues roots of unity...
    here simply: has finite order (power equal to identity within a bound)."""
    d = gens[0].nrows()
    for L in range(1, maxlen + 1):
        for w in itertools.product(range(len(gens)), repeat=L):
            g = eye(d)
            for a in w:
                g = g * gens[a]
            h = g
            for e in range(1, 400):
                if h == eye(d):
                    break
                h = h * g
            else:
                return False, w
    return True, None


for n in range(2, 9):
    gens = affine_gens(n)
    t0 = time.time()
    v, det = decide_qu(gens)
    t1 = time.time()
    msg = ''
    if n <= 4:
        ok, w = short_words_finite(gens, n)
        msg += f' words<=n finite order: {ok}'
    if n <= 5:
        S = Setup(gens)
        Sgt, order = gt_qu(S)
        rec = {}
        res = u_layers(S, record=rec)
        same = Subspace([vec(X) for X in res[1]], S.d * S.d) == Sgt
        msg += f' GT |finite quotient|={order} dimU_GT={Sgt.dim} same={same}'
    print(f'affine A~_{n}: d={det["d"]} m={det["m"]} quasi-unipotent={det["finite_semisimple_part"]} '
          f'verdict(CCRA)={v} time={t1 - t0:.2f}s{msg}', flush=True)

for n in range(2, 6):
    gens = torus_gens(n)
    t0 = time.time()
    v, det = decide(gens, random.Random(n))
    t1 = time.time()
    a = det['a']
    print(f'multiplicative A~_{n}: d={det["d"]} (a)={a["commutative"] and a["split"]} dimB={a["dimB"]} '
          f'dimC={a["dimC"]} verdict(CCRA)={v} time={t1 - t0:.2f}s', flush=True)
