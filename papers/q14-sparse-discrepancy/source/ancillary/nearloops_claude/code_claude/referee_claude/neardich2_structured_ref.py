"""Structured instances for the v4 near-dichotomy (dist(P,N) >= 2) on n = 6, 7, 8:
P = union of 1-3 random small clusters (balls of radius 0/1 around random centres, possibly
thinned), W = (closed 1- or 2-neighbourhood of P) minus P, optionally enlarged greedily keeping it
near-loop-free; N = rest.  Keep instances with W near-loop-free and P, N nonempty; test all splits
of the complement's 1-step components (near-dichotomy), and run the v4 proof-step checks on K
(labelling, admissibility, Components claim, Gamma tree, near-pairs hypothesis/conclusion).
Run: python3 -I neardich2_structured_ref.py"""
import sys, os, random, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube
from neardich2_ref import ConedK, check_splits

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_neardich2_structured.txt"), "w")
def log(s):
    print(s, flush=True); out.write(s + "\n"); out.flush()

def gen(c, rng):
    P = 0
    for _ in range(rng.randint(1, 3)):
        z = rng.randrange(c.N)
        ball = c.ball1[z] if rng.random() < 0.5 else (1 << z)
        if rng.random() < 0.4:
            ball &= rng.getrandbits(c.N) | (1 << z)
        P |= ball
    nb = c.ball1 if rng.random() < 0.7 else c.ball2
    W = c.dilate(P, nb) & ~P
    if rng.random() < 0.3:
        order = list(range(c.N)); rng.shuffle(order)
        for v in order:
            if not ((W | P) >> v) & 1 and not c.has_nearloop(W | (1 << v)) and not (c.ball1[v] & P):
                W |= 1 << v
    return P, W

def proof_checks(K, P, W):
    c = K.c; N = c.N; n = c.n
    Nn = c.full ^ P ^ W
    lab = {z: ('P' if P >> z & 1 else ('N' if Nn >> z & 1 else 'M')) for z in range(N)}
    f = dict(welldef=0, admiss=0, comps=0, tree=0, hyp=0, concl=0)
    for idx, q in enumerate(K.squares):
        a, b, b2, a2 = q
        opp = ((W >> a & 1) and (W >> a2 & 1)) or ((W >> b & 1) and (W >> b2 & 1))
        mP = any(P >> z & 1 for z in q); mN = any(Nn >> z & 1 for z in q)
        L = 'M' if opp else ('P' if mP else ('N' if mN else None))
        if L is None or (mP and mN and L != 'M'):
            f['welldef'] += 1
        lab[N + idx] = L
    if any(lab[u] == 'P' and lab[w] == 'N' for u in range(K.V) for w in K.adj[u]):
        f['admiss'] += 1
    for Lset, A in ((('M','N'), W | Nn), (('M','P'), W | P), (('M',), W)):
        kc = K.components([v for v in range(K.V) if lab[v] in Lset])
        kcorners = sorted(sum(1 << v for v in C if v < N) for C in kc)
        if 0 in kcorners or kcorners != sorted(c.components(A, c.ball2)):
            f['comps'] += 1
    nodes = []; nodeof = {}
    for L in ('P','M','N'):
        for C in K.components([v for v in range(K.V) if lab[v] == L]):
            for v in C: nodeof[v] = len(nodes)
            nodes.append((L, C))
    edges = set()
    for u in range(K.V):
        for w in K.adj[u]:
            if nodeof[u] != nodeof[w]:
                edges.add((min(nodeof[u], nodeof[w]), max(nodeof[u], nodeof[w])))
    if len(edges) != len(nodes) - 1:
        f['tree'] += 1
    for L, D in nodes:
        if L != 'M': continue
        Dc = [v for v in D if v < N]
        if any((d ^ (e ^ c.mask)).bit_count() <= 1 for d in Dc for e in Dc) or any(v >= N and K.bar[v] in D for v in D):
            f['hyp'] += 1; continue
        negD = {K.bar[v] for v in D}
        comps = K.components([v for v in range(K.V) if v not in D])
        Zs = [C for C in comps if C & negD]
        if len(Zs) != 1 or not negD <= Zs[0]:
            f['concl'] += 1; continue
        Rset = {v for v in range(N) if v not in Zs[0]}
        if any(((r ^ c.mask) ^ (1 << i)) in Rset for r in Rset for i in range(n)) or any((r ^ c.mask) in Rset for r in Rset):
            f['concl'] += 1
    return f, len(nodes)

rng = random.Random(8)
for n, T, doK in [(6, 4000, True), (7, 1500, True), (8, 400, False)]:
    c = Cube(n)
    K = ConedK(n) if doK else None
    kept = splits = viol = both = 0
    agg = dict(welldef=0, admiss=0, comps=0, tree=0, hyp=0, concl=0)
    maxnodes = 0
    t0 = time.time()
    for _ in range(T):
        P, W = gen(c, rng)
        Nn = c.full ^ P ^ W
        if P == 0 or Nn == 0 or c.has_nearloop(W):
            continue
        kept += 1
        cnt, v, b, k = check_splits(c, W, rng, 1024)
        splits += cnt; viol += v; both += b
        if doK and kept <= (300 if n == 6 else 60):
            fl, nn = proof_checks(K, P, W)
            maxnodes = max(maxnodes, nn)
            for key in agg: agg[key] += fl[key]
    log(f"n={n}: instances with W near-loop-free and P,N nonempty: {kept}; splits {splits}; near-dichotomy "
        f"violations {viol}; both near-thick {both}; proof-step failures on K: {agg if doK else 'n/a'}; "
        f"max #nodes {maxnodes} ({time.time()-t0:.0f}s)")
out.close()
