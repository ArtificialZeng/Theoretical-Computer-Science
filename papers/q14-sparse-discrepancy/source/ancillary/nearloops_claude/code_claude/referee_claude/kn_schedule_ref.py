"""Deletion schedules on complete graphs (independent re-implementation).
State: multiset of levels of the remaining K_m.  Rules (as in the paper + insert):
  * m <= 1: good.  m == 2: good iff max level >= 2 (leaf rule (a); (1,1) is not good).
  * base: m <= 5 and all levels >= 2 (Theorem thm:H(b)).
  * deletion/cheap deletion: pick h; all other vertices must have level >= 2; pick J among
    the others with |J| <= l_h, and J empty if l_h = 1; the others drop by one.
  (1-sums / leaves do not occur for m >= 3 in complete graphs.)
Computes the least uniform level L such that (K_n, L) is reducible, and also with
cheap deletions disabled (only rule (b)), for comparison with Cor. cor:examples(vii) (n-3).
Also verifies the explicit K_{2L+1} schedule of Cor. cor:maxtwod(iv).
Run: python3 -I kn_schedule_ref.py [nmax]
"""
import sys, os, time
from functools import lru_cache
from itertools import product

sys.setrecursionlimit(100000)
HERE = os.path.dirname(os.path.abspath(__file__))


def make_good(cheap=True):
    @lru_cache(maxsize=None)
    def good(state):
        # state: tuple of levels sorted descending, capped at m+1
        m = len(state)
        if m <= 1:
            return True
        if m == 2:
            return max(state) >= 2
        if m <= 5 and min(state) >= 2:
            return True
        # group by level
        levels = sorted(set(state), reverse=True)
        counts = {v: state.count(v) for v in levels}
        for lh in levels:
            others = dict(counts)
            others[lh] -= 1
            if others[lh] == 0:
                del others[lh]
            if min(others) < 2:
                continue
            vals = sorted(others)
            maxJ = lh if (cheap and lh >= 2) else 0
            # choose how many of each level go to J
            ranges = [range(0, min(others[v], maxJ) + 1) for v in vals]
            for js in product(*ranges):
                if sum(js) > maxJ:
                    continue
                new = []
                for v, j in zip(vals, js):
                    new += [v] * j + [v - 1] * (others[v] - j)
                m2 = m - 1
                new = tuple(sorted((min(x, m2 + 1) for x in new), reverse=True))
                if good(new):
                    return True
        return False
    return good


def least_uniform(n, good):
    L = 1
    while True:
        st = tuple([min(L, n + 1)] * n)
        if good(st):
            return L
        L += 1


def verify_schedule(L):
    """explicit schedule of Cor (iv): K_{2L+1} at level L -> K_{2L-1} at level L-1."""
    levels = [L] * (2 * L + 1)
    log = []
    while len(levels) > 5:
        Lc = levels[0]
        assert all(x == Lc for x in levels) and len(levels) == 2 * Lc + 1 and Lc >= 3
        # step 1: delete vertex 0 with J = next Lc vertices
        h = levels.pop(0)
        assert all(x >= 2 for x in levels) and h >= 2
        J = list(range(Lc))
        assert len(J) <= h
        levels = [x if i in J else x - 1 for i, x in enumerate(levels)]
        # now Lc at level Lc (indices 0..Lc-1), Lc at level Lc-1
        assert sorted(levels) == sorted([Lc] * Lc + [Lc - 1] * Lc)
        # step 2: delete one vertex of level Lc-1, J = the other Lc-1 vertices of level Lc-1
        idx = [i for i, x in enumerate(levels) if x == Lc - 1]
        hi = idx[0]
        h = levels[hi]
        rest = [x for i, x in enumerate(levels) if i != hi]
        assert all(x >= 2 for x in rest) and h >= 2
        Jset = [i for i, x in enumerate(rest) if x == Lc - 1]
        assert len(Jset) == Lc - 1 <= h
        levels = [x if i in Jset else x - 1 for i, x in enumerate(rest)]
        log.append(len(levels))
    assert len(levels) == 5 and all(x == 2 for x in levels)
    return True


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    out = open(os.path.join(HERE, "log_kn_schedule.txt"), "w")

    def log(s):
        print(s, flush=True)
        out.write(s + "\n")
        out.flush()
    for L in range(3, 30):
        verify_schedule(L)
    log("explicit K_{2L+1} schedule of Cor (iv) verified step by step for L = 3..29")
    goodC = make_good(True)
    goodB = make_good(False)
    for n in range(3, nmax + 1):
        t0 = time.time()
        Lc = least_uniform(n, goodC)
        Lb = least_uniform(n, goodB)
        log(f"K_{n}: least uniform level with cheap deletions = {Lc} (floor(n/2) = {n//2}); "
            f"with rule (b) only = {Lb} (n-3 = {n-3}); cache={goodC.cache_info().currsize} time={time.time()-t0:.1f}s")
    out.close()
