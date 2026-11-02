"""Random and adversarial tests of lem:neartransfer / cor:neartransfer.

For odd 2-Lipschitz psi on Q_{S cup T} and level l, let
  Zn  = {rho : {s : |psi(s,rho)| <= l} contains a near-loop}          (claimed l-coarse)
  G1  = {rho : slice contains a 1-loop}                                 (only (l-1)-coarse)
  Z11 = {rho : slice contains a 1-path with dist(end,-start) <= 1}      (remark: not l-coarse)
  Z20 = {rho : slice contains a 2-loop}                                 (remark: not l-coarse)
A symmetric set X in Q_T is l-coarse iff Q_T \\ X contains no l-loop (lem:coarse).
We count violations for Zn (must be 0) and, as a harness sanity check, for G1, Z11, Z20.
Run: python3 -I transfer_random_ref.py [trials] [seed]
"""
import sys, os, random, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube

HERE = os.path.dirname(os.path.abspath(__file__))
cubes = {}


def cube(n):
    if n not in cubes:
        cubes[n] = Cube(n)
    return cubes[n]


def lip_ok(vals, n):
    N = 1 << n
    for z in range(N):
        for i in range(n):
            w = z ^ (1 << i)
            if abs(vals[z] - vals[w]) > 2 + 1e-9:
                return False
    return True


def odd_ok(vals, n):
    N = 1 << n
    m = N - 1
    return all(abs(vals[z] + vals[z ^ m]) < 1e-9 for z in range(N))


def gen_mcshane(n, rng):
    N = 1 << n
    k = rng.randint(1, 6)
    anchors = [rng.randrange(N) for _ in range(k)]
    R = n + 1
    cs = [rng.choice([rng.uniform(-R, R), float(rng.randint(-R, R))]) for _ in range(k)]
    f = [min(c + 2 * (z ^ a).bit_count() for a, c in zip(anchors, cs)) for z in range(N)]
    m = N - 1
    return [(f[z] - f[z ^ m]) / 2 for z in range(N)]


def gen_distdiff(n, rng):
    N = 1 << n
    m = N - 1
    Y = [z for z in range(N) if rng.random() < rng.uniform(0.05, 0.5)]
    if not Y:
        Y = [rng.randrange(N)]
    negY = [y ^ m for y in Y]
    out = []
    for z in range(N):
        a = min((z ^ y).bit_count() for y in negY)
        b = min((z ^ y).bit_count() for y in Y)
        out.append(float(a - b))
    return out


def gen_characters(n, rng):
    """random combination of odd-degree characters, scaled to be 2-Lipschitz."""
    N = 1 << n
    terms = []
    for _ in range(rng.randint(1, 4)):
        size = rng.choice([1, 1, 3, 3, 5]) if n >= 5 else rng.choice([1, 3]) if n >= 3 else 1
        size = min(size, n if n % 2 == 1 else n - 1)
        A = rng.sample(range(n), size)
        terms.append((sum(1 << i for i in A), rng.uniform(-1, 1)))
    vals = []
    for z in range(N):
        v = 0.0
        for Am, c in terms:
            v += c * (-1) ** ((z & Am).bit_count())
        vals.append(v)
    L = 0
    for z in range(N):
        for i in range(n):
            L = max(L, abs(vals[z] - vals[z ^ (1 << i)]))
    if L == 0:
        return [0.0] * N
    sc = 2 / L * rng.uniform(0.6, 1.0)
    if rng.random() < 0.5:
        sc = 2 / L
    return [v * sc for v in vals]


def gen_sum(s, t, rng):
    """psi(s,rho) = alpha(s) + beta(rho), alpha,beta odd 2-Lipschitz."""
    a = gen_any(s, rng) if s > 0 else [0.0]
    b = gen_any(t, rng) if t > 0 else [0.0]
    out = []
    for z in range(1 << (s + t)):
        zs = z & ((1 << s) - 1)
        zt = z >> s
        out.append(a[zs] + b[zt])
    return out


def gen_any(n, rng):
    r = rng.random()
    if r < 0.4:
        v = gen_mcshane(n, rng)
    elif r < 0.7:
        v = gen_distdiff(n, rng)
    else:
        v = gen_characters(n, rng)
    if rng.random() < 0.3:
        c = rng.uniform(0.5, n + 1)
        v = [max(-c, min(c, x)) for x in v]
    return v


def gen(s, t, rng):
    r = rng.random()
    if r < 0.25:
        v = gen_sum(s, t, rng)
    elif r < 0.45:
        # mix two
        v1 = gen_any(s + t, rng)
        v2 = gen_any(s + t, rng)
        lam = rng.random()
        v = [lam * x + (1 - lam) * y for x, y in zip(v1, v2)]
    else:
        v = gen_any(s + t, rng)
    # random cube automorphism (coordinate perm + sign flips keep oddness and Lipschitz)
    return v


def analyse(vals, s, t, l):
    cs = cube(s)
    ct = cube(t)
    Ns = 1 << s
    Nt = 1 << t
    Zn = 0
    G1 = 0
    Z11 = 0
    Z20 = 0
    for rho in range(Nt):
        W = 0
        for x in range(Ns):
            if abs(vals[x | (rho << s)]) <= l + 1e-9:
                W |= 1 << x
        if cs.has_nearloop(W):
            Zn |= 1 << rho
        if cs.has_loop(W, 1):
            G1 |= 1 << rho
        if cs.has_generalized_loop(W, 1, 1):
            Z11 |= 1 << rho
        if cs.has_loop(W, 2):
            Z20 |= 1 << rho
    def coarse(X):
        return not ct.has_loop(ct.full ^ X, l)
    return Zn, coarse(Zn), coarse(G1), coarse(Z11), coarse(Z20)


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rng = random.Random(seed)
    stats = {}
    t0 = time.time()
    viol = []
    for it in range(trials):
        s = rng.choice([1, 2, 3, 3, 4, 4, 5])
        t = rng.choice([1, 2, 2, 3, 3, 4])
        if s + t > 8:
            t = 8 - s
        l = rng.choice([2, 2, 3, 2.5, 4])
        vals = gen(s, t, rng)
        assert odd_ok(vals, s + t) and lip_ok(vals, s + t)
        Zn, cZn, cG1, cZ11, cZ20 = analyse(vals, s, t, l)
        key = (s, t)
        st = stats.setdefault(key, [0, 0, 0, 0, 0, 0])
        st[0] += 1
        if Zn != cube(t).full:
            st[1] += 1
        if not cZn:
            st[2] += 1
            viol.append((s, t, l, vals))
        if not cG1:
            st[3] += 1
        if not cZ11:
            st[4] += 1
        if not cZ20:
            st[5] += 1
    lines = [f"trials={trials} seed={seed} time={time.time()-t0:.1f}s",
             "(|S|,|T|): trials, Zn nontrivial (!= whole cube), Zn NOT l-coarse [must be 0], "
             "G1 not l-coarse, Z11 not l-coarse, Z20 not l-coarse"]
    tot = [0] * 6
    for key in sorted(stats):
        lines.append(f"  {key}: {stats[key]}")
        tot = [a + b for a, b in zip(tot, stats[key])]
    lines.append(f"  TOTAL: {tot}")
    for v in viol[:3]:
        lines.append(f"VIOLATION s={v[0]} t={v[1]} l={v[2]} vals={v[3]}")
    msg = "\n".join(lines)
    print(msg)
    with open(os.path.join(HERE, f"log_transfer_random_seed{seed}.txt"), "w") as f:
        f.write(msg + "\n")


if __name__ == "__main__":
    main()
