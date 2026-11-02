import sys, random, time
sys.path.insert(0, '.')
from cover_search import *
D = int(sys.argv[1]); seed0 = int(sys.argv[2]); cnt = int(sys.argv[3])
for s in range(seed0, seed0 + cnt):
    rnd = random.Random(s)
    n = rnd.choice([3, 4, 5, 6])
    m = rnd.randint(12, 18)
    # random multigraph, avoid isolated, allow private edges rarely
    E = []
    for _ in range(m):
        if rnd.random() < 0.08:
            E.append((rnd.randrange(n),))
        else:
            u, v = rnd.sample(range(n), 2)
            E.append((u, v))
    inst = Instance(n, E)
    t = time.time()
    st, P = cegar(inst, D, verbose=False, timeout=1200)
    print(f"seed={s} n={n} m={m} degs={inst.deg} edges={sorted(E)} -> {st} ({time.time()-t:.1f}s)", flush=True)
    if st == "COVER":
        print("   verified", verify_cover(inst, D, P), flush=True)
