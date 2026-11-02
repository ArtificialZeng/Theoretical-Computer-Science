"""Enumerate all sparsity patterns: j <= 5 items, each item relevant to a set of 1 or 2 of the
n=5 functions (n<5 = functions with no items), up to relabelling of functions and items."""
import itertools
NF = 5
EDGES = [(a,) for a in range(NF)] + [(a, b) for a in range(NF) for b in range(a+1, NF)]
PERMS = list(itertools.permutations(range(NF)))
def canon(edges):
    best = None
    for pi in PERMS:
        e2 = tuple(sorted(tuple(sorted(pi[v] for v in e)) for e in edges))
        if best is None or e2 < best:
            best = e2
    return best
def all_patterns(maxj=5, pairs_only=False):
    out = {}
    E = [e for e in EDGES if (len(e) == 2 or not pairs_only)]
    for j in range(maxj + 1):
        seen = set()
        for combo in itertools.combinations_with_replacement(E, j):
            cf = canon(combo)
            seen.add(cf)
        out[j] = sorted(seen)
    return out
def to_Js(edges):
    return [tuple(k for k, e in enumerate(edges) if i in e) for i in range(NF)]
if __name__ == '__main__':
    P = all_patterns()
    print({j: len(v) for j, v in P.items()}, 'total', sum(len(v) for v in P.values()))
    Q = all_patterns(pairs_only=True)
    print('pairs only', {j: len(v) for j, v in Q.items()})
    # completeness check: number of labelled multisets equals sum over classes of orbit sizes
    from math import comb
    for j in range(6):
        tot = 0
        for cf in P[j]:
            orbit = {tuple(sorted(tuple(sorted(pi[v] for v in e)) for e in cf)) for pi in PERMS}
            tot += len(orbit)
        print(j, 'orbit sum', tot, 'expected', comb(15 + j - 1, j))
