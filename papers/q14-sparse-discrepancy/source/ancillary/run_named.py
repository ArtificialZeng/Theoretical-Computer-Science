import sys, time
sys.path.insert(0, '.')
from cover_search import *
def wheel(n, mr=1, ms=1):
    E = []
    for i in range(n):
        E += [(i, (i+1) % n)] * mr
        E += [(i, n)] * ms
    return Instance(n+1, E)
def complete(n, mult=1):
    E = []
    for i in range(n):
        for j in range(i+1, n):
            E += [(i, j)] * mult
    return Instance(n, E)
def k2n(n, mult=1):
    # hubs 0,1 ; middles 2..n+1, each middle joined to both hubs by `mult` items
    E = []
    for i in range(2, n + 2):
        E += [(0, i)] * mult + [(1, i)] * mult
    return Instance(n + 2, E)
D = int(sys.argv[1]); which = sys.argv[2]; args = list(map(int, sys.argv[3:]))
inst = {"wheel": wheel, "complete": complete, "k2n": k2n}[which](*args)
print(which, args, "m=", inst.m, "degs", inst.deg, flush=True)
t = time.time()
st, P = cegar(inst, D, verbose=False, timeout=5000)
print("RESULT", which, args, D, st, f"{time.time()-t:.1f}s", flush=True)
if st == "COVER":
    print("   verified", verify_cover(inst, D, P))
