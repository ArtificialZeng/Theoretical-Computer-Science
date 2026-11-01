#!/usr/bin/env python3
"""Exact, finite falsification checks; standard library; no analytic certification.

The Bellman check enumerates ALL hidden sets, ALL query sets of every size,
ALL feasible k-set outputs and ALL adaptive policies up to the stated depth.
Randomization cannot improve this finite uniform-prior expected objective,
since a randomized policy is a distribution over deterministic policies.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb, lcm
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE = '55e12bf5b8e7b5489014d1286ec0463b9bec718f4d5369b338c8e1403a6259cd'


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def masks(n, k):
    return [sum(1 << i for i in cc) for cc in combinations(range(n), k)]


def finite_policy_check(n, k, r, eps, kap, depth):
    rho = (1-eps)/(1+eps)
    a, b = rho*(1-kap), rho*kap
    den = lcm(a.denominator, b.denominator)
    ai, bi = int(a*den), int(b*den)
    ep, ed = eps.numerator, eps.denominator
    hidden = masks(n, k)
    outputs = hidden  # All feasible outputs may be extended to size k.
    all_queries = range(1 << n)
    values = []
    oracle_columns = [[] for _ in all_queries]
    promises = 0
    for hh in hidden:
        def value(ss):
            h = (ss & hh).bit_count()
            t = ss.bit_count()-h
            return den*h+ai*t+bi*min(t, r)
        values.append(tuple(value(ss) for ss in outputs))
        assert value(hh) == k*den
        for ss in all_queries:
            s = ss.bit_count()
            f0 = ai*s+bi*min(s, r)
            ff = value(ss)
            gg = max((ed+ep)*f0, (ed-ep)*ff)
            assert (ed-ep)*ff <= gg <= (ed+ep)*ff
            assert 0 <= ff <= den*s
            if s <= r:
                assert gg == (ed+ep)*f0
            oracle_columns[ss].append(gg)
            promises += 1
    partitions = []
    max_leak = 0
    for ss, column in enumerate(oracle_columns):
        s = ss.bit_count()
        base = (ed+ep)*(ai*s+bi*min(s, r))
        max_leak = max(max_leak, sum(v != base for v in column))
        groups = {}
        for i, v in enumerate(column):
            groups[v] = groups.get(v, 0) | (1 << i)
        partitions.append(tuple(sorted(groups.values())))
    partitions = tuple(set(partitions))
    prior = (1 << len(hidden))-1

    @lru_cache(None)
    def terminal(belief):
        ids = [i for i in range(len(hidden)) if (belief >> i) & 1]
        return max(sum(values[i][j] for i in ids)
                   for j in range(len(outputs)))

    @lru_cache(None)
    def optimum(belief, qleft):
        result = terminal(belief)
        if qleft == 0:
            return result
        seen = set()
        for pp in partitions:
            branches = tuple(sorted(bb for bb in (belief & x for x in pp) if bb))
            if len(branches) < 2 or branches in seen:
                continue
            seen.add(branches)
            result = max(result, sum(optimum(bb, qleft-1) for bb in branches))
        return result

    pop = len(hidden)
    p = F(max_leak, pop)
    beta_hypergeo = a+(1-a)*F(k, n)+(b/k)*sum(
        F(choose(k, h)*choose(n-k, k-h), choose(n, k))*min(k-h, r)
        for h in range(k+1))
    beta_exhaustive = F(terminal(prior), pop*k*den)
    assert beta_hypergeo == beta_exhaustive
    coarse_beta = a+b*F(r, k)+(1-a)*F(k, n)
    assert beta_exhaustive <= coarse_beta
    results = []
    for qq in range(depth+1):
        ratio = F(optimum(prior, qq), pop*k*den)
        bound = beta_exhaustive+min(F(1), qq*p)
        assert ratio <= bound
        results.append({'Q': qq, 'exact_optimal_prior_expected_ratio': str(ratio),
                        'bound_8': str(bound), 'bound_holds': True})
    return {'n': n, 'k': k, 'r': r, 'epsilon': str(eps), 'curvature': str(kap),
            'hidden_instances': pop, 'query_sets_all_sizes': 1 << n,
            'outputs_all_k_sets': len(outputs), 'max_leak_probability': str(p),
            'beta': str(beta_exhaustive), 'coarse_beta': str(coarse_beta),
            'promise_checks': promises, 'adaptive_policy_depth': depth,
            'bellman_cached_states': optimum.cache_info().currsize, 'results': results}


def heldout_count_checks():
    """New, disjoint n range and epsilon/curvature grids from triage."""
    tuples = points = tails = 0
    for n in range(12, 19):
        for k in range(2, min(6, n-2)+1):
            for r in sorted({1, k-1}):
                if n <= k+r:
                    continue
                for eps in (F(1, 101), F(2, 5), F(99, 100)):
                    for kap in (F(1, 101), F(2, 3), F(99, 100)):
                        rho = (1-eps)/(1+eps)
                        a, b = rho*(1-kap), rho*kap
                        c = (1-rho)*(1-kap)/(1-a)
                        assert 0 < c <= 1 and c >= (1-kap)*eps
                        for s in range(n+1):
                            leakage = F(0)
                            for h in range(max(0, k+s-n), min(k, s)+1):
                                t = s-h
                                ff = h+a*t+b*min(t, r)
                                f0 = a*s+b*min(s, r)
                                gg = max((1+eps)*f0, (1-eps)*ff)
                                assert f0 <= ff <= f0+(1-a)*h
                                assert (1-eps)*ff <= gg <= (1+eps)*ff
                                theta = (1-rho)*((1-kap)*s+kap*r)/(1-a)
                                if s <= r or h <= theta:
                                    assert gg == (1+eps)*f0
                                if gg != (1+eps)*f0:
                                    assert s > r and h > theta >= c*s
                                    leakage += F(choose(s, h)*choose(n-s, k-h), choose(n, k))
                                points += 1
                            if s > r:
                                jj = -((-c*s).numerator // (-c*s).denominator)
                                enlarged = sum((F(choose(s, h)*choose(n-s, k-h), choose(n, k))
                                                for h in range(jj, min(k, s)+1)), F(0))
                                union = choose(s, jj)*F(k, n)**jj
                                assert leakage <= enlarged <= union
                                tails += 1
                        tuples += 1
    return {'n_range_inclusive': [12, 18], 'k_range': '2..min(6,n-2)',
            'r_values': '1 and k-1 when n>k+r',
            'epsilon_grid': ['1/101', '2/5', '99/100'],
            'curvature_grid': ['1/101', '2/3', '99/100'],
            'parameter_tuples': tuples, 'feasible_count_points': points,
            'exact_hypergeometric_tail_checks': tails}


def main():
    before = hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
    assert before == EXPECTED_SOURCE
    cases = []
    for eps, kap in [(F(3, 4), F(1, 2)), (F(1, 3), F(9, 10)),
                     (F(2, 5), F(0)), (F(99, 100), F(2, 3))]:
        cases.append(finite_policy_check(6, 2, 1, eps, kap, 2))
    cases.append(finite_policy_check(8, 3, 2, F(3, 4), F(1, 2), 1))
    heldout = heldout_count_checks()
    after = hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
    assert after == before
    print(json.dumps({'job_id': 'curvature-noise-research-5a09759394ef',
        'status': 'exact finite falsification checks only; no fresh review or novelty certification',
        'source_sha256_before_and_after': after,
        'adaptive_policy_checks': cases, 'heldout_count_checks': heldout,
        'limits': 'Finite policy horizons and finite grids. No computer proof of asymptotics or arbitrary Q. Exponential relaxation with Euler e is proved analytically, not numerically certified here.'}, indent=2))


if __name__ == '__main__':
    main()
