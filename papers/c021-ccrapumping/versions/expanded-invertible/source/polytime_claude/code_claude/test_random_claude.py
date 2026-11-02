# Random cross-checks of the polynomial-time procedure against the exponential ground truth.
# usage: python3 test_random_claude.py SEED NTESTS FAMILY
#   FAMILY in {qu_yes, qu_rand, tor_yes, tor_rand}
import sys, random, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import flint
from linalg_claude import Q, ZERO, ONE, eye, zeros, vec, unvec, is_zero_mat, Subspace
from polyccra_claude import Setup, a_test, u_layers, decide, is_finite_cr
from groundtruth_claude import gt_qu, gt_general, lie_closure

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
ntests = int(sys.argv[2]) if len(sys.argv) > 2 else 20
family = sys.argv[3] if len(sys.argv) > 3 else 'qu_rand'
R = random.Random(seed)


def rand_signed_perm(n):
    p = list(range(n))
    R.shuffle(p)
    M = zeros(n, n)
    for i in range(n):
        M[p[i], i] = Q(R.choice([1, -1]))
    return M


def rand_monomial(n, torus):
    P = rand_signed_perm(n)
    if torus:
        D = zeros(n, n)
        for i in range(n):
            D[i, i] = Q(R.choice([1, 1, 2, 3])) if R.random() < 0.6 else Q(1, R.choice([1, 2, 3]))
        P = P * D
    return P


def blockdiag(blocks):
    n = sum(b.nrows() for b in blocks)
    M = zeros(n, n)
    o = 0
    for b in blocks:
        k = b.nrows()
        for i in range(k):
            for j in range(k):
                M[o + i, o + j] = b[i, j]
        o += k
    return M


def block_index(sizes):
    blk = []
    for p, s in enumerate(sizes):
        blk += [p] * s
    return blk


def rand_strict_upper(blk, density=0.6, rng_vals=(-2, 2)):
    n = len(blk)
    X = zeros(n, n)
    for r in range(n):
        for c in range(n):
            if blk[c] > blk[r] and R.random() < density:
                X[r, c] = Q(R.randint(*rng_vals), R.choice([1, 1, 2]))
    return X


def mexp(X):
    n = X.nrows()
    Rm = eye(n)
    T = eye(n)
    for k in range(1, n + 1):
        T = T * X * Q(1, k)
        if is_zero_mat(T):
            break
        Rm += T
    return Rm


def rand_GL(n):
    while True:
        P = flint.fmpq_mat(n, n, [Q(R.randint(-2, 2)) for _ in range(n * n)])
        if P.det() != 0:
            return P


def make_instance(fam):
    torus = fam.startswith('tor')
    m = R.choice([2, 3, 3, 4])
    sizes = [R.choice([1, 1, 2]) for _ in range(m)]
    blk = block_index(sizes)
    n = len(blk)
    k = R.choice([2, 2, 3])
    ells = [blockdiag([rand_monomial(s, torus) for s in sizes]) for _ in range(k)]
    if fam.endswith('yes'):
        # abelian L-stable N: supported on the first block row (or last block column)
        if R.random() < 0.5:
            supp = [(r, c) for r in range(n) for c in range(n) if blk[r] == 0 and blk[c] > 0]
        else:
            supp = [(r, c) for r in range(n) for c in range(n) if blk[c] == m - 1 and blk[r] < m - 1]
        seeds = []
        for _ in range(R.choice([1, 2])):
            X = zeros(n, n)
            for (r, c) in supp:
                if R.random() < 0.5:
                    X[r, c] = Q(R.randint(-2, 2))
            seeds.append(X)
        # Ad(<ells>)-stable span (no brackets needed: abelian)
        S = Subspace([], n * n)
        queue = list(seeds)
        while queue:
            X = queue.pop()
            if S.contains(vec(X)):
                continue
            S = S.add([vec(X)])
            for l in ells:
                li = l.inv()
                queue.append(l * X * li)
                queue.append(li * X * l)
        Nb = [unvec(b, n, n) for b in S.basis]
        Xs = []
        for _ in range(k):
            X = zeros(n, n)
            for B in Nb:
                X += Q(R.randint(-2, 2)) * B
            Xs.append(X)
    else:
        Xs = [rand_strict_upper(blk) for _ in range(k)]
    v = mexp(rand_strict_upper(blk, 0.5))
    P = rand_GL(n) if R.random() < 0.7 else eye(n)
    vi, Pi = v.inv(), P.inv()
    gens = [P * v * l * mexp(X) * vi * Pi for l, X in zip(ells, Xs)]
    return gens, dict(sizes=sizes, k=k)


stats = dict(tests=0, agree=0, mismatch=0, skipped=0)
t0 = time.time()
for t in range(ntests):
    gens, meta = make_instance(family)
    S = Setup(gens)
    try:
        if family.startswith('qu'):
            fin, why = is_finite_cr(S.bdiag, S.d)
            assert fin, "qu family must have finite semisimple part"
            Sgt, order = gt_qu(S)
            ok_a = True
        else:
            ok_a, info = a_test(S, random.Random(seed * 1000 + t))
            assert ok_a, "monomial families satisfy (a)"
            Sgt, order = gt_general(S, info['_B'])
    except RuntimeError as e:
        stats['skipped'] += 1
        print(f"[{t}] skipped ({e})")
        continue
    rec = {}
    res = u_layers(S, record=rec)
    gt_mats = [unvec(b, S.d, S.d) for b in Sgt.basis]
    gt_abelian = all(is_zero_mat(X * Y - Y * X) for X in gt_mats for Y in gt_mats)
    # compare level-wise projections up to the level reached
    agree = True
    last = (S.m - 1) if res[0] == 'abelian' else res[1] - 1
    for j in range(1, last + 1):
        proj = Subspace([vec(S.trunc(X, j)) for X in gt_mats], S.d * S.d)
        ours = Subspace([vec(X) for X in rec['ub'][j]], S.d * S.d)
        if not (proj == ours):
            agree = False
            print(f"   level {j}: GT dim {proj.dim} vs ours {ours.dim}")
    if (res[0] == 'abelian') != gt_abelian:
        agree = False
    stats['tests'] += 1
    stats['agree' if agree else 'mismatch'] += 1
    bits = [h['bits_u'] for h in rec.get('hist', [])]
    print(f"[{t}] d={S.d} m={S.m} sizes={meta['sizes']} |quot|={order} verdict={res[0]} "
          f"GT_abelian={gt_abelian} dimU_GT={Sgt.dim} agree={agree} bits_u={bits}")
print(family, stats, f"time {time.time() - t0:.1f}s")
