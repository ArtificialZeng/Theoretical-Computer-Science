"""Exact checks for section_claude.tex (polynomial ambiguity in the invertible sector).

Run:  python3 -I polyamb_check_claude.py SEED COUNT
(the script adds the c021 toolkits and the user site-packages holding python-flint explicitly).

Checks:
 (A) random trim polynomially ambiguous automata (block-triangular, SCCs with weighted permutation
     letters, then forward/backward state splitting so that letter matrices become singular and
     the SCC blocks are not monomial).  For each: verify PA by the EDA criterion, minimize, verify
     invertibility, and run the independent condition-(a) test of the paper's polynomial-time
     procedure (Lemma atest): Theorem thm:polyamb predicts (a) always holds.
     Also report whether R_u is commutative (CCRA) or not (PA but not CCRA).
 (B) the Component lemma on every SCC block: find E in the minimum ideal of the support monoid,
     check that E B E is a group, the fixed-point facts (i), (ii), multiplicativity of chi, and the
     factorization identity (eq:factor) exactly on random elements of L.
 (C) control: random dense invertible automata (generally not PA): count (a)-test failures.
"""
import sys, os, random, itertools
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
C021 = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(C021, 'checks_claude'))
sys.path.insert(0, os.path.join(C021, 'polytime_claude', 'code_claude'))
sys.path.append(os.path.expanduser('~/.local/lib/python3.13/site-packages'))
import wa
import flint
from polyccra_claude import to_fmpq_mat, Setup, a_test, u_layers

WEIGHTS = [Fr(1), Fr(-1), Fr(2), Fr(-2), Fr(1, 2), Fr(-1, 2), Fr(3), Fr(1, 3), Fr(-3, 2), Fr(2, 3)]


# ------------------------------------------------------------------ automata utilities
def support_graph(Ms, n):
    adj = [set() for _ in range(n)]
    for A in Ms.values():
        for p in range(n):
            for q in range(n):
                if A[p][q] != 0:
                    adj[p].add(q)
    return adj


def reach(adj, srcs):
    seen = set(srcs)
    st = list(srcs)
    while st:
        p = st.pop()
        for q in adj[p]:
            if q not in seen:
                seen.add(q)
                st.append(q)
    return seen


def trim(lam, Ms, gam):
    n = len(lam)
    adj = support_graph(Ms, n)
    radj = [set() for _ in range(n)]
    for p in range(n):
        for q in adj[p]:
            radj[q].add(p)
    acc = reach(adj, [p for p in range(n) if lam[p] != 0])
    coacc = reach(radj, [q for q in range(n) if gam[q] != 0])
    keep = sorted(acc & coacc)
    lam2 = [lam[p] for p in keep]
    gam2 = [gam[p] for p in keep]
    Ms2 = {a: [[A[p][q] for q in keep] for p in keep] for a, A in Ms.items()}
    return lam2, Ms2, gam2


def sccs(adj, n):
    """Tarjan; returns list of components (lists of states)."""
    index, low, onst, st, out = {}, {}, set(), [], []
    counter = [0]
    sys.setrecursionlimit(10000)

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        st.append(v)
        onst.add(v)
        for w in adj[v]:
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in onst:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = st.pop()
                onst.discard(w)
                comp.append(w)
                if w == v:
                    break
            out.append(comp)
    for v in range(n):
        if v not in index:
            strong(v)
    return out


def is_pa_trim(Ms, n):
    """EDA criterion on a trim automaton: PA iff no state p and pair (q,r), q != r, with
    (p,p) ->* (q,r) ->* (p,p) in the square automaton."""
    pairs = [(p, q) for p in range(n) for q in range(n)]
    pid = {pr: i for i, pr in enumerate(pairs)}
    adj = [set() for _ in pairs]
    for A in Ms.values():
        succ = [[q for q in range(n) if A[p][q] != 0] for p in range(n)]
        for (p, q) in pairs:
            for p2 in succ[p]:
                for q2 in succ[q]:
                    adj[pid[(p, q)]].add(pid[(p2, q2)])
    comps = sccs(adj, len(pairs))
    for comp in comps:
        prs = [pairs[i] for i in comp]
        if any(p == q for p, q in prs) and any(p != q for p, q in prs):
            return False
    return True


# ------------------------------------------------------------------ generator
def gen_block_pa(rng, letters, sizes, p_off=0.35):
    n = sum(sizes)
    Ms = {a: wa.zeros(n, n) for a in letters}
    blocks = []
    s0 = 0
    for k in sizes:
        idx = list(range(s0, s0 + k))
        blocks.append(idx)
        s0 += k
        while True:
            perms = {a: rng.sample(range(k), k) for a in letters}
            adj = [set(perms[a][i] for a in letters) for i in range(k)]
            if len(reach(adj, [0])) == k:
                break
        for a in letters:
            for i in range(k):
                Ms[a][idx[i]][idx[perms[a][i]]] = rng.choice(WEIGHTS)
    for bi in range(len(blocks)):
        for bj in range(bi + 1, len(blocks)):
            for p in blocks[bi]:
                for q in blocks[bj]:
                    for a in letters:
                        if rng.random() < p_off:
                            Ms[a][p][q] = rng.choice(WEIGHTS)
    lam = [rng.choice(WEIGHTS) if rng.random() < 0.6 else Fr(0) for _ in range(n)]
    gam = [rng.choice(WEIGHTS) if rng.random() < 0.6 else Fr(0) for _ in range(n)]
    lam[0] = Fr(1)
    gam[n - 1] = Fr(1)
    return lam, Ms, gam


def split_forward(rng, lam, Ms, gam, s):
    """split state s into s and a new copy n with the same future (forward bisimulation)."""
    n = len(lam)
    new = {}
    for a, A in Ms.items():
        B = wa.zeros(n + 1, n + 1)
        for p in range(n):
            for q in range(n):
                if A[p][q] != 0:
                    if q == s and rng.random() < 0.5:
                        B[p][n] = A[p][q]
                    else:
                        B[p][q] = A[p][q]
        B[n] = list(B[s])
        new[a] = B
    lam2 = list(lam) + [Fr(0)]
    gam2 = list(gam) + [gam[s]]
    return lam2, new, gam2


def split_backward(rng, lam, Ms, gam, s):
    T = {a: wa.transpose(A) for a, A in Ms.items()}
    g2, T2, l2 = split_forward(rng, gam, T, lam, s)
    return l2, {a: wa.transpose(A) for a, A in T2.items()}, g2


def gen_pa(rng, letters, nblocks, maxsize, nsplit, maxtotal=6):
    while True:
        sizes = [rng.randint(1, maxsize) for _ in range(nblocks)]
        if sum(sizes) <= maxtotal:      # keeps the minimal dimension <= 6 (a-test cost)
            break
    lam, Ms, gam = gen_block_pa(rng, letters, sizes)
    for _ in range(nsplit):
        s = rng.randrange(len(lam))
        if rng.random() < 0.5:
            lam, Ms, gam = split_forward(rng, lam, Ms, gam, s)
        else:
            lam, Ms, gam = split_backward(rng, lam, Ms, gam, s)
    return lam, Ms, gam


def same_series(A1, A2, letters, maxlen):
    for w in wa.words(letters, maxlen):
        if wa.evalw(*A1, w) != wa.evalw(*A2, w):
            return False
    return True


# ------------------------------------------------------------------ component lemma check
def boolmat(A):
    return tuple(tuple(1 if x != 0 else 0 for x in row) for row in A)


def bmul(X, Y):
    k = len(X)
    return tuple(tuple(1 if any(X[i][r] and Y[r][j] for r in range(k)) else 0 for j in range(k))
                 for i in range(k))


def check_component(rng, rho, letters, ntests=30):
    """rho: dict letter -> kxk Fraction matrix satisfying (U). Returns dict of results."""
    k = len(next(iter(rho.values())))
    # support monoid with witness words
    I = tuple(tuple(1 if i == j else 0 for j in range(k)) for i in range(k))
    word_of = {I: ''}
    queue = [I]
    while queue:
        X = queue.pop(0)
        for a in letters:
            Y = bmul(X, boolmat(rho[a]))
            if Y not in word_of:
                word_of[Y] = word_of[X] + a
                queue.append(Y)
    Bset = list(word_of)
    # check support morphism on random words (no cancellation)
    def rw(w):
        R = wa.eye(k)
        for a in w:
            R = wa.mm(R, rho[a])
        return R
    for _ in range(20):
        u = ''.join(rng.choice(letters) for _ in range(rng.randint(0, 6)))
        v = ''.join(rng.choice(letters) for _ in range(rng.randint(0, 6)))
        assert boolmat(rw(u + v)) == bmul(boolmat(rw(u)), boolmat(rw(v)))
    # an element of the minimum ideal: the product of all elements of the monoid lies in every
    # ideal.  Its word is the concatenation of witness words; matrices are multiplied from a cache.
    cache = {}
    def rwc(wd):
        if wd not in cache:
            cache[wd] = rw(wd)
        return cache[wd]
    x = I
    Rx = wa.eye(k)
    for b in Bset:
        x = bmul(x, b)
        Rx = wa.mm(Rx, rwc(word_of[b]))
    best, Rbest = x, Rx
    Re = Rbest
    while bmul(x, x) != x:
        x = bmul(x, best)
        Re = wa.mm(Re, Rbest)
    E = x
    J = None
    assert boolmat(Re) == E
    Mgrp = {bmul(bmul(E, b), E) for b in Bset}
    nM = len(Mgrp)
    # group check: every element has a power equal to E, and E is identity
    for g in Mgrp:
        assert bmul(E, g) == g == bmul(g, E)
        y, ok = g, False
        for _ in range(nM + 1):
            if y == E:
                ok = True
                break
            y = bmul(y, g)
        assert ok, "EBE not a group"
    Theta = [i for i in range(k) if E[i][i]]
    # (i)
    for t in Theta:
        for t2 in Theta:
            if t != t2:
                assert not E[t][t2]
    # (ii)
    for pp in range(k):
        for q in range(k):
            if E[pp][q]:
                mids = [t for t in Theta if E[pp][t] and E[t][q]]
                assert len(mids) == 1, (pp, q, mids)
    # random elements of L: (e x e)^n and products
    def rand_L():
        R = None
        for _ in range(rng.randint(1, 2)):
            xw = ''.join(rng.choice(letters) for _ in range(rng.randint(0, 4)))
            B = wa.mpow(wa.mm(wa.mm(Re, rw(xw)), Re), nM)
            R = B if R is None else wa.mm(R, B)
        return R
    def chi(Z):
        return [[Z[t][t2] for t2 in Theta] for t in Theta]
    nfac = 0
    for _ in range(ntests):
        Rz, Ry, Rz2 = rand_L(), rand_L(), rand_L()
        for R in (Rz, Ry, Rz2):
            assert boolmat(R) == E
            cz = chi(R)
            assert all(cz[i][j] == 0 for i in range(len(Theta)) for j in range(len(Theta)) if i != j)
            assert all(cz[i][i] != 0 for i in range(len(Theta)))
        assert chi(wa.mm(Rz, Ry)) == wa.mm(chi(Rz), chi(Ry))
        lhs = wa.mm(wa.mm(Rz, Ry), Rz2)   # rho is multiplicative, so this is rho(z y z')
        iota = [[Fr(1) if i == Theta[j] else Fr(0) for j in range(len(Theta))] for i in range(k)]
        rhs = wa.mm(wa.mm(wa.mm(wa.mm(Rz, iota), chi(Ry)), wa.transpose(iota)), Rz2)
        assert lhs == rhs, "factorization identity fails"
        nfac += 1
    return dict(k=k, monoid=len(Bset), group=nM, theta=len(Theta), factor_checks=nfac)


# ------------------------------------------------------------------ main
def run(seed, count):
    rng = random.Random(seed)
    letters = 'ab' if seed % 2 else 'abc'
    stats = dict(gen=0, pa=0, inv=0, a_true=0, a_false=0, abelian=0, nonabelian=0, comp=0,
                 dims=[], singular_letters=0, nonmonomial_blocks=0)
    for it in range(count):
        lam, Ms, gam = gen_pa(rng, letters, rng.randint(1, 3), 3, rng.randint(0, 3))
        orig = (lam, Ms, gam)
        lam, Ms, gam = trim(lam, Ms, gam)
        n = len(lam)
        if n == 0:
            continue
        stats['gen'] += 1
        assert same_series(orig, (lam, Ms, gam), letters, 4)
        pa = is_pa_trim(Ms, n)
        assert pa, "generator produced a non-PA automaton"
        stats['pa'] += 1
        if any(wa.rank(A) < n for A in Ms.values()):
            stats['singular_letters'] += 1
        # component lemma on every SCC block
        adj = support_graph(Ms, n)
        for comp in sccs(adj, n):
            comp = sorted(comp)
            rho = {a: [[Ms[a][p][q] for q in comp] for p in comp] for a in letters}
            if all(all(x == 0 for row in rho[a] for x in row) for a in letters):
                continue
            if any(sum(1 for x in row if x != 0) > 1 for a in letters for row in rho[a]) or \
               any(sum(1 for i in range(len(comp)) if rho[a][i][j] != 0) > 1
                   for a in letters for j in range(len(comp))):
                stats['nonmonomial_blocks'] += 1
            info = check_component(rng, rho, letters, ntests=8)
            stats['comp'] += 1
        lm, Mm, gm = wa.minimize(lam, Ms, gam)
        d = len(lm)
        if d == 0:
            continue
        assert same_series((lam, Ms, gam), (lm, Mm, gm), letters, 5)
        if any(wa.rank(Mm[a]) < d for a in letters):
            print("  non-invertible minimal rep (unexpected for this generator)", it)
            continue
        stats['inv'] += 1
        stats['dims'].append(d)
        gens = [to_fmpq_mat(Mm[a]) for a in letters]
        S = Setup(gens)
        ok, info = a_test(S, random.Random(seed * 1000 + it))
        if ok:
            stats['a_true'] += 1
            res = u_layers(S)
            if res[0] == 'abelian':
                stats['abelian'] += 1
            else:
                stats['nonabelian'] += 1
        else:
            stats['a_false'] += 1
            print("  COUNTEREXAMPLE CANDIDATE: PA automaton with (a) failing", it, Mm)
    return stats


def control(seed, count, d=3):
    rng = random.Random(seed)
    fails = 0
    tot = 0
    for it in range(count):
        gens = []
        for _ in range(2):
            while True:
                A = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(d)]
                if wa.rank(A) == d:
                    break
            gens.append(A)
        tot += 1
        S = Setup([to_fmpq_mat(A) for A in gens])
        ok, _ = a_test(S, random.Random(it))
        if not ok:
            fails += 1
    return tot, fails


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    st = run(seed, count)
    dims = st.pop('dims')
    print("seed", seed, "stats", st)
    if dims:
        print("minimal dimensions: min", min(dims), "max", max(dims),
              "hist", {k: dims.count(k) for k in sorted(set(dims))})
    tot, fails = control(seed, 20)
    print("control (random invertible 3x3 integer pairs): (a) fails in", fails, "of", tot)
    print("DONE: all assertions passed; (a) held for every invertible PA example"
          if st['a_false'] == 0 else "DONE: (a) FAILED on some PA example")
