"""(A) Exact checks of the examples in rem:nearlimits.
 (A1) |S|=3, T={t1,t2}, psi = t1+t2+s1 s2 s3, l=2: slices of {|psi|<=2}; the 1-step/defect-1
      variant of Z^natural misses the antipodal 2-path ((1,1),(-1,-1)); Z^natural = Q_T.
 (A2) rem:hublimits(1) example S={s0}, |T|=l, psi = s0 + sum rho: the 2-loop variant
      misses the antipodal l-path (1,-1); Z^natural = Q_T.  l = 2..5.
 (A3) product example of (2): psi_i = sum_{S_i} s + sum_{T_i} rho, |S_i| odd, |T_i| = l:
      slice at rho_i = 1 contains a near-loop, phi_h = sum_i sum_{S_i} s <= -q on the
      product of the slices; also for |S_i| <= 2l (the hypothesis |S_i| > 2l is not needed).
(B) Random test of the extension step of lem:cheap: for q <= l_h sets F_i (each containing a
    near-loop) in Q_{S_i}, every l_h-coarse set {|phi|<=l_h} on Q_{S_1+..+S_q+Q} meets
    F_1 x ... x F_q x Q_Q.  Also q = l_h + 1 (must fail sometimes, e.g. A3).
Run: python3 -I remark_and_extension_ref.py
"""
import sys, os, random, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube
from transfer_random_ref import gen_any

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_remark_extension.txt"), "w")


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def sgn(z, i):
    return -1 if (z >> i) & 1 else 1


# (A1)
cs = Cube(3)
ct = Cube(2)
def psiA1(s, r):
    return sgn(r, 0) + sgn(r, 1) + sgn(s, 0) * sgn(s, 1) * sgn(s, 2)
Zn = Z11 = 0
for r in range(4):
    W = sum(1 << s for s in range(8) if abs(psiA1(s, r)) <= 2)
    desc = sorted(tuple(sgn(s, i) for i in range(3)) for s in cs.bits(W))
    nl = cs.has_nearloop(W)
    g11 = cs.has_generalized_loop(W, 1, 1)
    if nl:
        Zn |= 1 << r
    if g11:
        Z11 |= 1 << r
    log(f"(A1) rho=({sgn(r,0)},{sgn(r,1)}): |slice|={len(desc)} slice={desc if len(desc) < 8 else 'all'} near-loop={nl} 1-step-defect1={g11}")
log(f"(A1) Z^natural == Q_T: {Zn == ct.full};  1-step variant l-coarse (no 2-loop in complement): {not ct.has_loop(ct.full ^ Z11, 2)}")
# check Lipschitz and oddness
okL = all(abs(psiA1(s, r) - psiA1(s ^ (1 << i), r)) <= 2 for s in range(8) for r in range(4) for i in range(3)) and \
      all(abs(psiA1(s, r) - psiA1(s, r ^ (1 << i))) <= 2 for s in range(8) for r in range(4) for i in range(2))
okO = all(psiA1(s ^ 7, r ^ 3) == -psiA1(s, r) for s in range(8) for r in range(4))
log(f"(A1) psi odd: {okO}, 2-Lipschitz: {okL}")

# (A2)
for l in range(2, 6):
    c1 = Cube(1)
    cT = Cube(l)
    Zn = Z20 = 0
    for r in range(1 << l):
        W = sum(1 << s for s in range(2) if abs(sgn(s, 0) + sum(sgn(r, i) for i in range(l))) <= l)
        if c1.has_nearloop(W):
            Zn |= 1 << r
        if c1.has_loop(W, 2):
            Z20 |= 1 << r
    log(f"(A2) l={l}: Z^natural == Q_T: {Zn == cT.full}; 2-loop variant l-coarse: {not cT.has_loop(cT.full ^ Z20, l)}; "
        f"rho=1 in 2-loop variant: {bool(Z20 & 1)}")

# (A3)
for l in [2, 3]:
    for sz in [1, 3, 5, 7]:
        c = Cube(sz)
        W = sum(1 << s for s in range(c.N) if abs(sum(sgn(s, i) for i in range(sz)) + l) <= l)
        nl = c.has_nearloop(W)
        mx = max(sum(sgn(s, i) for i in range(sz)) for s in c.bits(W))
        log(f"(A3) l={l} |S_i|={sz} (|S_i|>2l: {sz > 2*l}): slice at rho_i=1 contains near-loop: {nl}; "
            f"max of sum_{{S_i}} s on slice = {mx}  (so phi_h <= -q on the product)")


# (B) extension step
def random_nearloop_set(c, rng):
    """a random set containing a near-loop: a random 2-path from z to w with dist(w,-z)<=1, plus noise"""
    N = c.N
    z = rng.randrange(N)
    nz = c.neg(z)
    target = rng.choice([nz] + c.nb1[nz])
    A = 1 << z
    cur = z
    steps = 0
    while cur != target and steps < 50:
        # move toward target with a step of length 1 or 2
        diff = cur ^ target
        bits = [i for i in range(c.n) if diff >> i & 1]
        k = min(len(bits), rng.choice([1, 2]))
        flip = rng.sample(bits, k)
        if rng.random() < 0.2 and c.n >= 2:
            flip = rng.sample(range(c.n), min(2, c.n))
        for i in flip:
            cur ^= 1 << i
        A |= 1 << cur
        steps += 1
    A |= 1 << target
    for _ in range(rng.randint(0, 3)):
        A |= 1 << rng.randrange(N)
    if not c.has_nearloop(A):
        return None
    return A


rng = random.Random(9)
t0 = time.time()
res = {}
for trial in range(6000):
    lh = rng.choice([2, 3])
    q = rng.choice([lh, lh, lh + 1]) if lh == 2 else rng.choice([lh, lh + 1])
    sizes = [rng.choice([1, 2, 3]) for _ in range(q)]
    qpriv = rng.choice([0, 0, 1])
    if sum(sizes) + qpriv > 10:
        continue
    Fs = []
    for sz in sizes:
        c = Cube(sz)
        A = None
        while A is None:
            A = random_nearloop_set(c, rng)
        Fs.append(A)
    n = sum(sizes) + qpriv
    phi = gen_any(n, rng)
    # also adversarial phi: phi = sum over blocks of block sums with sign making product region bad
    if rng.random() < 0.3:
        phi = []
        for z in range(1 << n):
            v = 0
            off = 0
            for sz in sizes:
                v += sum(sgn(z, off + i) for i in range(sz))
                off += sz
            v += sum(sgn(z, off + i) for i in range(qpriv))
            phi.append(float(v))
    # does {|phi|<=lh} meet F_1 x ... x F_q x Q?
    hit = False
    for z in range(1 << n):
        if abs(phi[z]) > lh + 1e-9:
            continue
        off = 0
        ok = True
        for sz, A in zip(sizes, Fs):
            part = (z >> off) & ((1 << sz) - 1)
            if not (A >> part) & 1:
                ok = False
                break
            off += sz
        if ok:
            hit = True
            break
    key = "q<=l_h" if q <= lh else "q=l_h+1"
    st = res.setdefault(key, [0, 0])
    st[0] += 1
    if not hit:
        st[1] += 1
log(f"(B) extension step: trials and failures: {res}  (failures must be 0 for q<=l_h) time {time.time()-t0:.1f}s")
out.close()
