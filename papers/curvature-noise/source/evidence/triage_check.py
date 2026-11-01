#!/usr/bin/env python3
"""Independent symmetry-compressed exact falsification test; not a proof."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def choose(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def ceil(q):
    return -((-q.numerator) // q.denominator)


def main():
    source = ROOT / 'source.md'
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    assert source_hash == '55e12bf5b8e7b5489014d1286ec0463b9bec718f4d5369b338c8e1403a6259cd'
    families = points = tails = marginal_tests = 0
    for n in range(5, 12):
        for k in range(2, n-1):
            for r in range(1, min(k-1, n-k-1)+1):
                for eps in (F(1, 10), F(1, 3), F(3, 4)):
                    for kap in (F(0), F(1, 2), F(9, 10)):
                        rho = (1-eps)/(1+eps)
                        a, b = rho*(1-kap), rho*kap
                        c = (1-rho)*(1-kap)/(1-a)
                        assert 0 < c <= 1 and c >= (1-kap)*eps
                        def value(h, t):
                            return h+a*t+b*min(t, r)
                        assert value(k, 0) == k
                        assert value(1, 0) == 1 and value(0, 1) == rho
                        full = value(k, n-k)
                        exact_curvature = 1-min(full-value(k-1, n-k),
                                                (full-value(k, n-k-1))/rho)
                        assert exact_curvature == kap
                        # The baseline transcript itself is a valid promised input:
                        # F0(s)=a*s+b*min(s,r), singleton rho, full marginal a.
                        assert 1-a/rho == kap
                        for h in range(k+1):
                            for t in range(n-k+1):
                                s, f = h+t, value(h, t)
                                f0 = a*s+b*min(s, r)
                                g0 = (1+eps)*f0
                                g = max(g0, (1-eps)*f)
                                assert 0 <= f <= s
                                assert f0 <= f <= f0+(1-a)*h
                                assert (1-eps)*f <= g <= (1+eps)*f
                                theta = (1-rho)*((1-kap)*s+kap*r)/(1-a)
                                if s <= r or h <= theta:
                                    assert g == g0
                                if s > r:
                                    assert theta >= c*s
                                # Good marginal is constant; bad marginal decreases.
                                if h < k:
                                    assert value(h+1, t)-f == 1
                                    marginal_tests += 1
                                if t < n-k:
                                    d = value(h, t+1)-f
                                    assert d >= 0
                                    if t+1 < n-k:
                                        assert d >= value(h, t+2)-value(h, t+1)
                                    marginal_tests += 1
                                points += 1
                        # Exact probability over all hidden k-sets, for each query size.
                        for s in range(r+1, n+1):
                            threshold = (1-rho)*((1-kap)*s+kap*r)/(1-a)
                            t0 = ceil(c*s)
                            def mass(h):
                                return F(choose(s, h)*choose(n-s, k-h), comb(n, k))
                            leak = sum((mass(h) for h in range(k+1)
                                        if h > threshold), F(0))
                            enlarged = sum((mass(h) for h in range(k+1)
                                            if h >= t0), F(0))
                            union = choose(s, t0)*F(k, n)**t0
                            assert leak <= enlarged <= union
                            tails += 1
                        families += 1
    result = {
        'job_id': 'curvature-noise-triage-903fc47916c5',
        'status': 'finite exact observations; unaccepted; no novelty certification',
        'source_sha256_before_and_after': source_hash,
        'n_range_inclusive': [5, 11],
        'k_range': '2 <= k <= n-2',
        'r_range': '1 <= r <= min(k-1,n-k-1)',
        'epsilon_grid': ['1/10', '1/3', '3/4'],
        'curvature_grid': ['0', '1/2', '9/10'],
        'hard_family_parameter_tuples': families,
        'feasible_hidden_outside_count_pairs': points,
        'marginal_checks': marginal_tests,
        'exact_hypergeometric_tail_checks': tails,
        'coverage': 'All feasible (h,t) count pairs and query cardinalities for the stated grids; symmetry compresses subsets.',
        'not_checked': 'General analytic quantifiers, adaptive algorithm theorem, asymptotics, novelty, curvature=1.'
    }
    assert hashlib.sha256(source.read_bytes()).hexdigest() == source_hash
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
