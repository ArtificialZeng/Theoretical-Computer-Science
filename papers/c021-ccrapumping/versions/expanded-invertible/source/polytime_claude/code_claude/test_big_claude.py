# Larger quasi-unipotent instances with big finite part (random signed permutation blocks of size s,
# typically generating a large subgroup of the hyperoctahedral group of order 2^s s!) and m layers.
# YES family: Gamma inside a conjugate of L x| N with N abelian (must answer YES).
# NO  family: generic block-unipotent perturbations (no ground truth; internal assertions only).
# The finite quotient is never enumerated.  usage: python3 test_big_claude.py SEED N s m
import sys, random, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import flint
from linalg_claude import Q, ZERO, ONE, eye, zeros, is_zero_mat
from polyccra_claude import decide_qu
seed, N, s, m = (int(x) for x in sys.argv[1:5])
R = random.Random(seed)
def signed_perm(s):
    p = list(range(s)); R.shuffle(p); M = zeros(s, s)
    for i in range(s): M[p[i], i] = Q(R.choice([1, -1]))
    return M
def mexp(X):
    n = X.nrows(); Rm, T = eye(n), eye(n)
    for k in range(1, n + 1):
        T = T * X * Q(1, k)
        if is_zero_mat(T): break
        Rm += T
    return Rm
for fam in ['yes', 'no']:
    for t in range(N):
        n = s * m; k = 3
        ells = []
        for _ in range(k):
            P = signed_perm(s); mu = Q(R.choice([1, -1])); L = zeros(n, n)
            for q in range(m):
                for i in range(s):
                    for j in range(s):
                        L[q*s+i, q*s+j] = (mu**q) * P[i, j]
            ells.append(L)
        Xs = []
        for _ in range(k):
            X = zeros(n, n)
            if fam == 'yes':
                for i in range(1, m):
                    D = [Q(R.randint(-2, 2)) for _ in range(s)]
                    for q in range(m - i):
                        for u in range(s): X[q*s+u, (q+i)*s+u] = D[u]
            else:
                for r in range(n):
                    for c in range(n):
                        if c // s > r // s and R.random() < 0.3: X[r, c] = Q(R.randint(-1, 1))
            Xs.append(X)
        vX = zeros(n, n)
        for r in range(n):
            for c in range(n):
                if c // s > r // s and R.random() < 0.5: vX[r, c] = Q(R.randint(-2, 2), R.choice([1, 2]))
        v = mexp(vX); vi = v.inv()
        gens = [v * l * mexp(X) * vi for l, X in zip(ells, Xs)]
        t0 = time.time()
        verdict, det = decide_qu(gens)
        bits = [(h['bits_u'], h['bits_v']) for h in (det.get('hist') or [])]
        print(f'{fam}[{t}] d={n} m={det["m"]} finite={det["finite_semisimple_part"]} verdict={verdict} '
              f'time={time.time()-t0:.1f}s bits(u,v)={bits}', flush=True)
        if fam == 'yes': assert verdict is True
