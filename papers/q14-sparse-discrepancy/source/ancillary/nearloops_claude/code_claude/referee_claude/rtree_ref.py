"""Checks for lem:Rtree.
 (1) pi_1(|R_S|) = 1 for n = 1..6 by a sufficient test: take a BFS spanning tree of G_S,
     declare its edges trivial, and repeatedly declare an edge trivial if it is the third side
     of a triangle (3 corners pairwise at distance <= 2) whose two other sides are trivial.
     If all edges become trivial, the edge-path group is trivial.
 (2) For admissible labellings Lambda: Q_n -> {P,M,N} (no P-N pair at distance <= 2) the
     component graph Gamma (components of label classes in G_S, adjacency = some G_S edge)
     is a tree: exhaustive for n = 3, random (with structured generators) for n = 4,5,6.
 (3) lem:nearpairs on G_S with u~v iff dist <= 1: exhaustive over all D for n <= 4
     (connected in G_S, no d,d' in D with dist(d,-d') <= 1), random for n = 5.
Run: python3 -I rtree_ref.py
"""
import sys, os, random, time
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_rtree.txt"), "w")


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def pi1_trivial(n):
    c = Cube(n)
    N = c.N
    edges = set()
    for z in range(N):
        for w in c.nb2[z]:
            if z < w:
                edges.add((z, w))
    triv = set()
    seen = {0}
    dq = deque([0])
    while dq:
        z = dq.popleft()
        for w in c.nb2[z]:
            if w not in seen:
                seen.add(w)
                triv.add((min(z, w), max(z, w)))
                dq.append(w)
    tris = []
    for (a, b) in edges:
        for x in c.nb2[a]:
            if x > b and (b ^ x).bit_count() <= 2:
                tris.append((a, b, x))
    changed = True
    while changed:
        changed = False
        for a, b, x in tris:
            es = [(a, b), (min(a, x), max(a, x)), (min(b, x), max(b, x))]
            k = sum(e in triv for e in es)
            if k == 2:
                for e in es:
                    if e not in triv:
                        triv.add(e)
                        changed = True
    return len(triv) == len(edges), len(edges), len(tris)


def gamma_is_tree(c, lab):
    N = c.N
    comp_id = [-1] * N
    comps = []
    for z in range(N):
        if comp_id[z] >= 0:
            continue
        cid = len(comps)
        comp_id[z] = cid
        stack = [z]
        members = [z]
        while stack:
            u = stack.pop()
            for w in c.nb2[u]:
                if comp_id[w] < 0 and lab[w] == lab[z]:
                    comp_id[w] = cid
                    stack.append(w)
                    members.append(w)
        comps.append(members)
    k = len(comps)
    adj = set()
    for z in range(N):
        for w in c.nb2[z]:
            a, b = comp_id[z], comp_id[w]
            if a != b:
                adj.add((min(a, b), max(a, b)))
    # connected (G_S connected) and acyclic iff #edges = #nodes - 1
    return len(adj) == k - 1, k


def admissible(c, lab):
    for z in range(c.N):
        if lab[z] == 0:
            for w in c.nb2[z]:
                if lab[w] == 2:
                    return False
    return True


def random_admissible(c, rng):
    """labels 0=P,1=M,2=N; structured: grow random P and N seeds, buffer M."""
    N = c.N
    mode = rng.random()
    lab = [1] * N
    if mode < 0.5:
        # random seeds, then M-buffer
        k = rng.randint(1, 6)
        for _ in range(k):
            z = rng.randrange(N)
            want = rng.choice([0, 2])
            ok = all(lab[w] != 2 - want for w in [z] + c.nb2[z])
            if ok:
                lab[z] = want
        # random growth
        for _ in range(rng.randint(0, 4 * N)):
            z = rng.randrange(N)
            if lab[z] != 1:
                continue
            want = rng.choice([0, 2])
            if all(lab[w] != 2 - want for w in c.nb2[z]):
                lab[z] = want
    else:
        # threshold of a random odd 2-Lipschitz-like function
        f = [rng.uniform(-1, 1) for _ in range(N)]
        anchors = [(rng.randrange(N), rng.uniform(-c.n, c.n)) for _ in range(rng.randint(1, 5))]
        g = [min(a + 2 * (z ^ b).bit_count() for b, a in anchors) for z in range(N)]
        thr = rng.uniform(2.0, 2.0 + c.n / 2)
        for z in range(N):
            if g[z] > thr:
                lab[z] = 0
            elif g[z] < -thr:
                lab[z] = 2
        # clean violations
        for z in range(N):
            if lab[z] == 0 and any(lab[w] == 2 for w in c.nb2[z]):
                lab[z] = 1
    return lab


def nearpairs_check(c, D):
    """returns True if lem:nearpairs conclusion holds for D (hypotheses assumed)."""
    N = c.N
    full = c.full
    negD = c.negset(D)
    if negD & D:
        return False
    comps = c.components(full ^ D, c.ball2)
    Zs = [C for C in comps if C & negD]
    if len(Zs) != 1 or (negD & ~Zs[0]):
        return False
    R = full ^ Zs[0]
    # no r, r' in R with dist(r, -r') <= 1
    return (c.dilate(c.negset(R), c.ball1) & R) == 0


def main():
    for n in range(1, 7):
        t0 = time.time()
        ok, ne, nt = pi1_trivial(n)
        log(f"(1) n={n}: R_S has {ne} edges, {nt} triangles; triangle-collapse makes all edges trivial: {ok} ({time.time()-t0:.1f}s)")
    # (2)
    c = Cube(3)
    cnt = 0
    bad = 0
    for code in range(3 ** 8):
        lab = []
        x = code
        for _ in range(8):
            lab.append(x % 3)
            x //= 3
        if not admissible(c, lab):
            continue
        cnt += 1
        ok, k = gamma_is_tree(c, lab)
        if not ok:
            bad += 1
    log(f"(2) n=3: admissible labellings {cnt} (exhaustive), Gamma not a tree: {bad}")
    rng = random.Random(4)
    for n, trials in [(4, 40000), (5, 10000), (6, 2000)]:
        c = Cube(n)
        bad = 0
        maxk = 0
        for _ in range(trials):
            lab = random_admissible(c, rng)
            assert admissible(c, lab)
            ok, k = gamma_is_tree(c, lab)
            maxk = max(maxk, k)
            if not ok:
                bad += 1
        log(f"(2) n={n}: random admissible labellings {trials}, max #nodes {maxk}, Gamma not a tree: {bad}")
    # (3)
    for n in range(1, 5):
        c = Cube(n)
        cnt = bad = 0
        for D in range(1, 1 << c.N):
            if len(c.components(D, c.ball2)) != 1:
                continue
            if c.dilate(c.negset(D), c.ball1) & D:
                continue
            cnt += 1
            if not nearpairs_check(c, D):
                bad += 1
        log(f"(3) n={n}: admissible D (connected, no near pair) {cnt} (exhaustive), violations {bad}")
    c = Cube(5)
    cnt = bad = 0
    for _ in range(200000):
        # random connected D by random growth
        z = rng.randrange(c.N)
        D = 1 << z
        for _ in range(rng.randint(0, 12)):
            cand = c.bits(c.dilate(D, c.ball2) & ~D)
            if not cand:
                break
            D |= 1 << rng.choice(cand)
        if c.dilate(c.negset(D), c.ball1) & D:
            continue
        cnt += 1
        if not nearpairs_check(c, D):
            bad += 1
    log(f"(3) n=5: random admissible D {cnt}, violations {bad}")


main()
out.close()
