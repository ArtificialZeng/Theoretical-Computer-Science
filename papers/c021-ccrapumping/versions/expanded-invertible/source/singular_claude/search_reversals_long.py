# Longer-word affine-context search in the CCRA series g^r, h^r, F (theorem predicts: none) and controls g, h, F^r.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import affine_context_search as acs
def g(w):
    tot, prod = 0, 1
    for u in w.split('1'):
        tot += prod; prod *= len(u)
    return tot
def h(w):
    tot, prod = 0, 1
    for u in w.split('1'):
        tot += prod; prod *= len(u) + 1
    return tot
for name, fn in {'g^r': lambda w: g(w[::-1]), 'h^r': lambda w: h(w[::-1]), 'g': g}.items():
    rep = acs.rep_from_function(fn, '01', 4)
    lam, M, gam, d = rep
    res = acs.search(acs.tofr(lam)[0], {a: acs.tofr(M[a]) for a in '01'}, '01', maxu=3, maxx=2, maxy=3, maxz=3)
    print(name, 'words up to length 3: affine context:', res[0][:4] if res else None, flush=True)
