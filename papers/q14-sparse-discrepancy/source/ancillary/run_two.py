import sys
sys.path.insert(0, '.')
from cover_search import *
D = int(sys.argv[1]); nfun = int(sys.argv[2])
for m in range(int(sys.argv[3]), int(sys.argv[4])+1):
    inst = Instance(nfun, [tuple(range(nfun))]*m)
    t=time.time()
    st, P = cegar(inst, D, init=256, verbose=False, timeout=600)
    print(f"n={nfun} m={m} D={D}: {st} ({time.time()-t:.1f}s)", flush=True)
    if st == "COVER":
        print("   verified min-max |g| =", verify_cover(inst, D, P))
        break
