"""Level-1 (and 1.5) tests of lem:neartransfer / cor:neartransfer (insert v4, l >= 1).
 (a) random odd 2-Lipschitz psi (same generators as transfer_random_ref.py), l in {1, 1.5};
 (b) simulated annealing (anchor parametrisation) searching for psi with an antipodal
     l-path in Q_T avoiding Zn;
 (c) T = empty: {|psi| <= 1} contains a 2-loop (lem:K12lv), random psi on Q_S.
Run: python3 -I transfer_l1_ref.py [random_trials] [anneal_runs] [anneal_steps]
"""
import sys, os, random, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube
from transfer_random_ref import gen, gen_any, analyse, odd_ok, lip_ok, cube

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_transfer_l1.txt"), "w")


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def from_anchors(anchors, n):
    N = 1 << n
    m = N - 1
    f = [min(c + 2 * (z ^ a).bit_count() for a, c in anchors) for z in range(N)]
    return [(f[z] - f[z ^ m]) / 2 for z in range(N)]


def score(vals, s, t, l, ball):
    cs = cube(s)
    ct = cube(t)
    Ns = 1 << s
    Zn = 0
    slicesz = 0
    for rho in range(1 << t):
        W = 0
        for x in range(Ns):
            if abs(vals[x | (rho << s)]) <= l + 1e-9:
                W |= 1 << x
        slicesz += bin(W).count("1")
        if cs.has_nearloop(W):
            Zn |= 1 << rho
    comp = ct.full ^ Zn
    outn = bin(comp).count("1")
    best = t + 1
    viol = False
    if comp:
        for C in ct.components(comp, ball):
            negC = ct.negset(C)
            if negC & C:
                viol = True
                best = 0
            else:
                best = min(best, min((a ^ b).bit_count() for a in ct.bits(C) for b in ct.bits(negC)))
    return 4.0 * outn - 3.0 * best - slicesz / Ns, viol, outn


def main():
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
    runs = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    steps = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    rng = random.Random(101)
    t0 = time.time()
    stats = {}
    for _ in range(R):
        s = rng.choice([1, 2, 3, 3, 4, 4, 5])
        t = rng.choice([1, 2, 2, 3, 3, 4])
        if s + t > 8:
            t = 8 - s
        l = rng.choice([1, 1, 1.5])
        vals = gen(s, t, rng)
        assert odd_ok(vals, s + t) and lip_ok(vals, s + t)
        Zn, cZn, cG1, cZ11, cZ20 = analyse(vals, s, t, l)
        st = stats.setdefault(l, [0, 0, 0, 0, 0])
        st[0] += 1
        if Zn != cube(t).full:
            st[1] += 1
        if not cZn:
            st[2] += 1
            log(f"VIOLATION random s={s} t={t} l={l} vals={vals}")
        if not cG1:
            st[3] += 1
        if not cZ20:
            st[4] += 1
    log(f"(a) random, per l: [trials, Zn nontrivial, Zn NOT l-coarse (must be 0), 1-loop variant not l-coarse, "
        f"2-loop variant not l-coarse] = {stats}  ({time.time()-t0:.0f}s)")
    # (b) annealing
    t0 = time.time()
    found = 0
    maxout = []
    acc = 0
    for run in range(runs):
        s = rng.choice([2, 3, 3, 4, 4, 5])
        t = rng.choice([2, 3, 3, 4, 4])
        if s + t > 9:
            t = 9 - s
        l = rng.choice([1, 1, 1.5])
        n = s + t
        N = 1 << n
        ball = [0] * (1 << t)
        for z in range(1 << t):
            for w in range(1 << t):
                if (z ^ w).bit_count() <= l:
                    ball[z] |= 1 << w
        anchors = [(rng.randrange(N), rng.uniform(-n, n)) for _ in range(rng.randint(2, 8))]
        vals = from_anchors(anchors, n)
        cur, viol, sz = score(vals, s, t, l, ball)
        best = sz
        for it in range(steps):
            na = list(anchors)
            r = rng.random()
            if r < 0.4:
                i = rng.randrange(len(na)); a, c = na[i]; na[i] = (a, c + rng.gauss(0, 1))
            elif r < 0.7:
                i = rng.randrange(len(na)); a, c = na[i]; na[i] = (a ^ (1 << rng.randrange(n)), c)
            elif r < 0.85 and len(na) < 14:
                na.append((rng.randrange(N), rng.uniform(-n, n)))
            elif len(na) > 1:
                na.pop(rng.randrange(len(na)))
            nv = from_anchors(na, n)
            new, viol, sz = score(nv, s, t, l, ball)
            temp = 3.0 * (1 - it / steps) + 0.05
            if new >= cur or rng.random() < math.exp((new - cur) / temp):
                acc += 1
                anchors, vals, cur = na, nv, new
                best = max(best, sz)
                if viol:
                    found += 1
                    log(f"VIOLATION anneal s={s} t={t} l={l} vals={vals}")
                    break
        maxout.append((s, t, l, best))
    log(f"(b) annealing: runs={runs} steps={steps} accepted={acc} violations={found} "
        f"max #rho outside Zn per run (first 40): {maxout[:40]}  ({time.time()-t0:.0f}s)")
    # (c) T empty
    bad = 0
    for _ in range(20000):
        s = rng.randint(1, 7)
        vals = gen_any(s, rng)
        c = cube(s)
        W = sum(1 << z for z in range(1 << s) if abs(vals[z]) <= 1 + 1e-9)
        if not c.has_loop(W, 2):
            bad += 1
    log(f"(c) T empty: 20000 random psi (|S|<=7): {{|psi|<=1}} without a 2-loop: {bad} (must be 0)")


main()
out.close()
