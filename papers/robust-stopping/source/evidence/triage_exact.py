"""Small exact vertex test; standard library only, no floating-point solver.

Enumerates all basic feasible solutions of the finite robust-policy polytope.
Finite horizon compression to M=max(b,N+1) is justified in triage-findings.md.
This is a finite observation, not a general optimizer or complexity result.
"""
from fractions import Fraction as Q
from itertools import combinations
import json


def solve(a, y):
    n = len(y)
    z = [[Q(x) for x in row] + [Q(v)] for row, v in zip(a, y)]
    for c in range(n):
        p = next((r for r in range(c, n) if z[r][c]), None)
        if p is None:
            return None
        z[c], z[p] = z[p], z[c]
        d = z[c][c]
        z[c] = [v / d for v in z[c]]
        for r in range(n):
            if r != c:
                d = z[r][c]
                z[r] = [v - d * w for v, w in zip(z[r], z[c])]
    return [z[r][-1] for r in range(n)]


def vertices(b, R, M):
    A = [[Q(b+t-1-x) if t <= x else Q(0) for t in range(1, M+1)]
         for x in range(1, b)]
    A.append([Q(t-1) for t in range(1, M+1)])
    rhs = [(R-1)*x for x in range(1, b)] + [(R-1)*b]
    out = set()
    for k in range(1, min(b+1, M)+1):
        for s in combinations(range(M), k):
            for active in combinations(range(b), k-1):
                mat = [[Q(1)]*k] + [[A[j][t] for t in s] for j in active]
                v = solve(mat, [Q(1)] + [rhs[j] for j in active])
                if v is None or min(v) < 0:
                    continue
                f = tuple(v[s.index(t)] if t in s else Q(0) for t in range(M))
                if all(sum(a*t for a, t in zip(row, f)) <= r
                       for row, r in zip(A, rhs)):
                    out.add(f)
    return sorted(out)


def costs(b, p, M):
    return [sum(prob*(b+t-1 if t <= x else x) for x, prob in p.items())
            for t in range(1, M+1)]


def assess(b, R, p, vv):
    M = len(vv[0])
    g = costs(b, p, M)
    obj = lambda f: sum(x*y for x, y in zip(g, f))
    cap = lambda f: max(x for x, y in zip(g, f) if y)
    best = min(vv, key=obj)
    h = min(map(cap, vv))
    capped = min((f for f in vv if cap(f) <= h), key=obj)
    return dict(b=b, R=str(R), p={str(x):str(v) for x,v in p.items()},
                M=M, vertices=len(vv), costs=list(map(str,g)),
                optimum=str(obj(best)), optimizer=list(map(str,best)),
                threshold=str(h), restricted_optimum=str(obj(capped)),
                restricted_optimizer=list(map(str,capped)),
                strict_policy_separation=obj(capped)>obj(best))


def main():
    records = []
    tested = 0
    for b, R in [(2,Q(7,5)), (3,Q(3,2)), (3,Q(8,5)), (4,Q(3,2))]:
        N = 6
        vv = vertices(b, R, max(b,N+1))
        for x, y in combinations(range(1,N+1), 2):
            for a in [Q(1,5),Q(2,5),Q(3,5),Q(4,5)]:
                p = {x:a,y:1-a}
                rec = assess(b,R,p,vv)
                tested += 1
                if rec['strict_policy_separation']:
                    records.append(rec)
                    print(json.dumps({'tested':tested,'first_separation':rec},indent=2))
                    return
    print(json.dumps({'tested':tested,'separations':records},indent=2))


if __name__ == '__main__':
    main()
