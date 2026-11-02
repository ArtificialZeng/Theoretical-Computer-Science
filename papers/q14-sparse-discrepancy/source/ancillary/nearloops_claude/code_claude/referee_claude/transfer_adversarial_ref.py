"""Adversarial (simulated annealing) search for a counterexample to cor:neartransfer:
an odd 2-Lipschitz psi on Q_{S cup T} (values in (1/2)Z) and level l such that
Q_T \\ Zn contains an antipodal l-path (Zn as in transfer_random_ref.py).
Score rewards many rho outside Zn and small Hamming distance between a component of
Q_T \\ Zn (l-step graph) and its negative.  A violation = component equal to its negative.
Run: python3 -I transfer_adversarial_ref.py [runs] [steps] [seed]
"""
import sys, os, random, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube
from transfer_random_ref import gen, odd_ok, lip_ok

HERE = os.path.dirname(os.path.abspath(__file__))
cubes = {}


def cube(n):
    if n not in cubes:
        cubes[n] = Cube(n)
    return cubes[n]


def zn_set(vals, s, t, l):
    cs = cube(s)
    Ns = 1 << s
    Zn = 0
    for rho in range(1 << t):
        W = 0
        base = rho << s
        for x in range(Ns):
            if abs(vals[x | base]) <= l + 1e-9:
                W |= 1 << x
        if cs.has_nearloop(W):
            Zn |= 1 << rho
    return Zn


def score(vals, s, t, l, ballcache):
    ct = cube(t)
    cs = cube(s)
    Ns = 1 << s
    Zn = 0
    slicesz = 0
    for rho in range(1 << t):
        W = 0
        base = rho << s
        for x in range(Ns):
            if abs(vals[x | base]) <= l + 1e-9:
                W |= 1 << x
        slicesz += bin(W).count("1")
        if cs.has_nearloop(W):
            Zn |= 1 << rho
    comp = ct.full ^ Zn
    out = bin(comp).count("1")
    best = t + 1
    viol = False
    if comp:
        for C in ct.components(comp, ballcache):
            negC = ct.negset(C)
            if negC & C:
                viol = True
                best = 0
            else:
                d = min((a ^ b).bit_count() for a in ct.bits(C) for b in ct.bits(negC))
                best = min(best, d)
    sc = 4.0 * out - 3.0 * best - 1.0 * slicesz / Ns
    return sc, viol, out


def from_anchors(anchors, n):
    N = 1 << n
    m = N - 1
    f = [min(c + 2 * (z ^ a).bit_count() for a, c in anchors) for z in range(N)]
    return [(f[z] - f[z ^ m]) / 2 for z in range(N)]


def main():
    runs = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    steps = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    rng = random.Random(seed)
    t0 = time.time()
    found = []
    summary = []
    accepted_total = 0
    for run in range(runs):
        s = rng.choice([2, 3, 3, 4, 4, 5])
        t = rng.choice([3, 4, 4, 5]) if s <= 4 else rng.choice([3, 4])
        if s + t > 9:
            t = 9 - s
        l = rng.choice([2, 2, 3])
        if t <= l:
            t = l + 1
        n = s + t
        N = 1 << n
        ball = [0] * (1 << t)
        for z in range(1 << t):
            for w in range(1 << t):
                if (z ^ w).bit_count() <= l:
                    ball[z] |= 1 << w
        R = n + 2
        anchors = [(rng.randrange(N), rng.uniform(-R, R)) for _ in range(rng.randint(2, 8))]
        vals = from_anchors(anchors, n)
        cur, viol, sz = score(vals, s, t, l, ball)
        bestsz = sz
        T0 = 3.0
        for it in range(steps):
            new_anchors = list(anchors)
            r = rng.random()
            if r < 0.4:
                i = rng.randrange(len(new_anchors))
                a, c = new_anchors[i]
                new_anchors[i] = (a, c + rng.gauss(0, 1.0))
            elif r < 0.7:
                i = rng.randrange(len(new_anchors))
                a, c = new_anchors[i]
                new_anchors[i] = (a ^ (1 << rng.randrange(n)), c)
            elif r < 0.85 and len(new_anchors) < 14:
                new_anchors.append((rng.randrange(N), rng.uniform(-R, R)))
            elif len(new_anchors) > 1:
                new_anchors.pop(rng.randrange(len(new_anchors)))
            nvals = from_anchors(new_anchors, n)
            new, viol, sz = score(nvals, s, t, l, ball)
            temp = T0 * (1 - it / steps) + 0.05
            if new >= cur or rng.random() < math.exp((new - cur) / temp):
                accepted_total += 1
                anchors, vals, cur = new_anchors, nvals, new
                bestsz = max(bestsz, sz)
                if viol:
                    assert odd_ok(vals, n) and lip_ok(vals, n)
                    found.append((s, t, l, list(vals)))
                    break
        summary.append((s, t, l, bestsz))
    lines = [f"runs={runs} steps={steps} seed={seed} time={time.time()-t0:.1f}s accepted moves={accepted_total} violations={len(found)}"]
    lines.append("per run (|S|,|T|,l, max #rho outside Zn reached): " + str(summary))
    for f in found[:3]:
        lines.append(f"VIOLATION {f}")
    msg = "\n".join(lines)
    print(msg)
    with open(os.path.join(HERE, f"log_transfer_adversarial_seed{seed}.txt"), "w") as fh:
        fh.write(msg + "\n")


if __name__ == "__main__":
    main()
