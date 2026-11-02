"""Exhaustive near-dichotomy check on Q_5 (|S|=5): enumerate all W with no near-loop
(downward-closed family; DFS adding corners in increasing order), and for every split of
the complement into P,N with dist(P,N)>=3 check that exactly one of P,N is near-thick.
Also counts W up to nothing (raw count).  Run: python3 -I neardich_q5_ref.py [n]
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube

n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
c = Cube(n)
N = c.N
full = c.full
cache = {}


def nl(A):
    r = cache.get(A)
    if r is None:
        r = c.has_nearloop(A)
        if len(cache) < 4_000_000:
            cache[A] = r
    return r


stats = dict(W=0, splits=0, viol=0, both=0, maxcomp=0, nontriv=0)
t0 = time.time()
viol_examples = []


def check(W):
    stats['W'] += 1
    comp = c.components(full ^ W, c.ball2)
    k = len(comp)
    stats['maxcomp'] = max(stats['maxcomp'], k)
    if k >= 2:
        stats['nontriv'] += 1
    for bits in range(1 << k):
        P = 0
        for i in range(k):
            if bits >> i & 1:
                P |= comp[i]
        Nn = (full ^ W) ^ P
        stats['splits'] += 1
        pt = not c.has_nearloop(full ^ P)
        nt = not c.has_nearloop(full ^ Nn)
        if not (pt or nt):
            stats['viol'] += 1
            if len(viol_examples) < 5:
                viol_examples.append((W, P, Nn))
        if pt and nt:
            stats['both'] += 1


def dfs(W, start):
    check(W)
    for v in range(start, N):
        W2 = W | (1 << v)
        if not c.has_nearloop(W2):
            dfs(W2, v + 1)


dfs(0, 0)
msg = (f"n={n}: near-loop-free W: {stats['W']}, W whose complement has >=2 G_S-components: "
       f"{stats['nontriv']}, max #components of complement: {stats['maxcomp']}, splits: {stats['splits']}, "
       f"near-dichotomy violations: {stats['viol']}, both near-thick: {stats['both']}, "
       f"time {time.time()-t0:.1f}s")
print(msg)
for W, P, Nn in viol_examples:
    print("VIOLATION", c.bits(W), c.bits(P), c.bits(Nn))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"log_neardich_q{n}.txt"), "w") as f:
    f.write(msg + "\n")
    for W, P, Nn in viol_examples:
        f.write(f"VIOLATION {c.bits(W)} {c.bits(P)} {c.bits(Nn)}\n")
