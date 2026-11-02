import sys
sys.path.insert(0, '.')
from cover_search import *

def cycle_bundles(n, m):
    E = []
    for i in range(n):
        E += [(i, (i+1) % n)] * m
    return Instance(n, E)

def complete(n, mult=1):
    E = []
    for i in range(n):
        for j in range(i+1, n):
            E += [(i, j)] * mult
    return Instance(n, E)

def multigraph(n, edgelist):
    return Instance(n, edgelist)

if __name__ == "__main__":
    D = int(sys.argv[1])
    which = sys.argv[2]
    args = list(map(int, sys.argv[3:]))
    if which == "cycle":
        inst = cycle_bundles(*args)
    elif which == "complete":
        inst = complete(*args)
    print(which, args, "D=", D, "m=", inst.m, "degs", inst.deg, flush=True)
    t = time.time()
    st, P = cegar(inst, D, init=512, verbose=True, timeout=3000)
    print("RESULT", which, args, D, st, f"{time.time()-t:.1f}s", flush=True)
    if st == "COVER":
        print("   verified min-max |g| =", verify_cover(inst, D, P))
        print("   P sizes", [len(p) for p in P])
