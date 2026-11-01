"""Finite triage checks. Standard library only; does not certify a theorem."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json


def compositions(total, n, prefix=()):
    if n == 1:
        yield prefix + (total,)
    else:
        for a in range(1, total - n + 2):
            yield from compositions(total-a, n-1, prefix+(a,))


def flow(e, a):
    if a <= F(1, 2)/e:
        return e*a
    if a <= F(1, 2):
        return 1-1/(4*e*a)
    return 1-(1-a)/e


def travel_exp(a, b):
    lo, hi = sorted((a, b))
    if hi <= F(1, 2):
        return hi/lo
    if lo >= F(1, 2):
        return (1-lo)/(1-hi)
    return 1/(4*lo*(1-hi))


def v(a):
    return min(a, 1-a)


def main():
    counts = dict(pairs=0, proper_subsets=0, membership_tests=0,
                  greedy_coordinate_tests=0)
    scales = tuple(map(F, (1, 2, 3, 4))) + (F(3, 2),)
    for n in range(2, 5):
        vectors = [tuple(F(x, 8) for x in c) for c in compositions(8, n)]
        masks = [tuple(i for i in range(n) if m & (1 << i))
                 for m in range(1, (1 << n)-1)]
        for p, q in product(vectors, repeat=2):
            cuts = [(sum(p[i] for i in a), sum(q[i] for i in a)) for a in masks]
            all_distance = max(travel_exp(a,b) for a,b in cuts)
            order = sorted(range(n), key=lambda i: q[i]/p[i], reverse=True)
            prefixes = [(sum(p[i] for i in order[:j]),
                         sum(q[i] for i in order[:j])) for j in range(1,n)]
            assert all(b >= a for a,b in prefixes)
            assert all_distance == max(travel_exp(a,b) for a,b in prefixes)
            endpoint = max(max(p[i]/q[i], q[i]/p[i]) for i in range(n))
            assert endpoint <= all_distance <= ((endpoint+1)/2)**2
            for e in scales + (all_distance,):
                feasible = all(b <= flow(e,a) for a,b in cuts)
                assert feasible == all(b <= flow(e,a) for a,b in prefixes)
                assert feasible == (all_distance <= e)
                counts['membership_tests'] += 1
            counts['pairs'] += 1
            counts['proper_subsets'] += len(cuts)
        for p in vectors:
            for order in permutations(range(n)):
                for e in scales:
                    cumulative = [F(0)] + [sum(p[i] for i in order[:j])
                                           for j in range(1,n+1)]
                    levels = [flow(e,a) for a in cumulative]
                    for j in range(1,n+1):
                        r = levels[j]-levels[j-1]
                        deriv = v(levels[j])-v(levels[j-1])
                        assert r > 0 and abs(deriv) <= r
                        counts['greedy_coordinate_tests'] += 1
                    assert levels[0] == 0 and levels[-1] == 1
    assert travel_exp(F(1,4), F(3,4)) == 4
    result = {'status':'passed; finite observations only',
              'coverage':'all ordered pairs of positive denominator-8 vectors, n=2..4',
              'arithmetic':'fractions.Fraction', 'counts':counts,
              'binary_obstruction':{'p':['1/4','3/4'],'q':['3/4','1/4'],
                                    'exp_endpoint_distance':3,
                                    'exp_optimal_binary_cost':4}}
    target = Path(__file__).with_name('triage-exact-results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
