#!/usr/bin/env python3
"""Portable finite checks for the curvature/noise note.

Standard library only; no source fulltexts, frozen dossier or network required.
Derived from the separate mathematical review's exact verifier.
These finite checks do not prove the arbitrary-parameter theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, lcm
import json

def popcount(s):
    # Works on Python 3.9 as well as versions providing int.bit_count.
    return bin(s).count('1')


def masksets(n, k):
    return [sum(1 << i for i in t) for t in combinations(range(n), k)]


def finite_case(n, k, r, eps, kap, two_queries=False):
    rho = (1-eps)/(1+eps)
    a, b = rho*(1-kap), rho*kap
    c = (1-rho)*(1-kap)/(1-a)
    den = lcm(a.denominator, b.denominator)
    av, bv = int(a*den), int(b*den)
    subsets = list(range(1 << n))
    sizes = [popcount(s) for s in subsets]
    hs = masksets(n, k)
    baseline = [av*s+bv*min(s, r) for s in sizes]

    def vals(h):
        # All values scaled by den; oracle values by den*eps.denominator.
        result = []
        for s in subsets:
            good = popcount(s & h)
            bad = sizes[s]-good
            result.append(den*good+av*bad+bv*min(bad, r))
        return result

    v = vals(hs[0])
    pair_checks = 0
    for x in subsets:
        assert v[x] >= 0
        for y in subsets:
            assert v[x]+v[y] >= v[x | y]+v[x & y]
            if (x & y) == x:
                assert v[x] <= v[y]
            pair_checks += 1
    allset = (1 << n)-1
    curvature = 1-min(F(v[allset]-v[allset ^ (1 << i)], v[1 << i])
                      for i in range(n))
    assert curvature == kap
    assert max(v[s] for s in subsets if sizes[s] <= k) == k*den
    assert v[0] == 0 and all(v[1 << i] > 0 for i in range(n))
    # Check the baseline is itself inside the promised exact-curvature class.
    base_curvature = 1-F(baseline[allset]-baseline[allset ^ 1], baseline[1])
    assert base_curvature == kap

    en, ed = eps.numerator, eps.denominator
    answers = []
    payoffs = []
    leakcounts = [0]*len(subsets)
    global_checks = threshold_checks = 0
    for h in hs:
        vv = vals(h)
        gg = []
        payoffs.append([vv[o] for o in hs])
        for s in subsets:
            lo, hi = (ed-en)*vv[s], (ed+en)*vv[s]
            g0 = (ed+en)*baseline[s]
            g = max(g0, lo)
            assert lo <= g <= hi
            if sizes[s] <= r:
                assert g == g0
            if g != g0:
                leakcounts[s] += 1
                good = popcount(s & h)
                assert sizes[s] > r
                assert F(good) > c*sizes[s]
                threshold_checks += 1
            gg.append(g)
            global_checks += 1
        answers.append(gg)
    for s in subsets:
        if sizes[s] <= r:
            continue
        z = c*sizes[s]
        j = (z.numerator+z.denominator-1)//z.denominator
        union = comb(sizes[s], j)*F(k, n)**j
        assert F(leakcounts[s], len(hs)) <= union

    p = F(max(leakcounts), len(hs))
    beta = F(max(sum(row[o] for row in payoffs) for o in range(len(hs))),
             len(hs)*k*den)
    result = {'n': n, 'k': k, 'r': r, 'epsilon': str(eps),
              'curvature': str(kap), 'submodular_set_pairs': pair_checks,
              'hidden_set_oracle_entries': global_checks,
              'revealing_entries_checked': threshold_checks,
              'p_exact': str(p), 'beta_exact': str(beta)}
    if two_queries:
        # Explicit depth-two enumeration, with no general Bellman recursion.
        def terminal(ids):
            return max(sum(payoffs[i][o] for i in ids) for o in range(len(hs)))

        def branches(ids, query):
            d = {}
            for i in ids:
                d.setdefault(answers[i][query], []).append(i)
            return list(d.values())

        ids = list(range(len(hs)))
        zero = terminal(ids)
        one = max(sum(terminal(group) for group in branches(ids, q))
                  for q in subsets)
        # Each first-query response may choose its own second query and output.
        two = max(sum(max(sum(terminal(child) for child in branches(group, q2))
                          for q2 in subsets)
                      for group in branches(ids, q1)) for q1 in subsets)
        ratios = [F(vv, len(hs)*k*den) for vv in [zero, one, two]]
        assert all(vv <= beta+min(F(1), qq*p) for qq, vv in enumerate(ratios))
        result['exact_best_uniform_prior_ratios_Q_0_1_2'] = list(map(str, ratios))
        result['checked_bound_for_all_depth_two_policies'] = True
    return result


def count_case(n, k, r, eps, kap):
    """Exact leakage masses in regimes satisfying the finite theorem's condition.

    Since 8/3 < exp(1) < 3, cn > 3k certifies the hypothesis. Proving
    p <= [(8/3)k/(cn)]^(cr) by integer powers is stronger than needed.
    """
    rho = (1-eps)/(1+eps)
    a, b = rho*(1-kap), rho*kap
    c = (1-rho)*(1-kap)/(1-a)
    assert n > k+r and 1 <= r < k and c*n > 3*k
    population = comb(n, k)
    maximum = F(0)
    witness_size = 0
    for s in range(n+1):
        mass = 0
        f0 = a*s+b*min(s, r)
        for h in range(max(0, k+s-n), min(k, s)+1):
            f = h+a*(s-h)+b*min(s-h, r)
            if (1-eps)*f > (1+eps)*f0:
                mass += comb(s, h)*comb(n-s, k-h)
        p = F(mass, population)
        if p > maximum:
            maximum, witness_size = p, s
    z = c*r
    lower_e_base = F(8, 3)*k/(c*n)
    assert maximum**z.denominator <= lower_e_base**z.numerator
    return {'n': n, 'k': k, 'r': r, 'epsilon': str(eps),
            'curvature': str(kap), 'c': str(c), 'max_leak_probability': str(maximum),
            'maximizing_query_size': witness_size,
            'cn_greater_than_3k': True,
            'stronger_rational_exponential_bound_verified': True}


def main():
    cases = [finite_case(6, 3, 2, F(1, 2), F(1, 3), True),
             finite_case(7, 3, 1, F(1, 7), F(0)),
             finite_case(8, 3, 2, F(7, 8), F(6, 7)),
             finite_case(8, 4, 1, F(1, 17), F(16, 17))]
    counts = [count_case(128, 5, 2, F(1, 2), F(1, 3)),
              count_case(257, 7, 3, F(3, 5), F(2, 5)),
              count_case(89, 4, 1, F(1, 7), F(0)),
              count_case(512, 5, 4, F(1, 19), F(1, 2))]
    assert cases[0]['p_exact'] == '1/20'
    assert cases[0]['beta_exact'] == '359/540'
    assert cases[0]['exact_best_uniform_prior_ratios_Q_0_1_2'] == [
        '359/540', '7/10', '13/18']
    print(json.dumps({'all_checks_passed': True,
                      'independent_cases': cases,
                      'finite_theorem_regime_exact_count_checks': counts,
                      'limits': 'Finite exact checks; not a proof or novelty certificate.'},
                     indent=2))


if __name__ == '__main__':
    main()
