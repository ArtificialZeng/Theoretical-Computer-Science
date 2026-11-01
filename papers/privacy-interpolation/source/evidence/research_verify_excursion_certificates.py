#!/usr/bin/env python3
"""Exact consumer of saved path certificates; no generator imports.

Every continuous cell is verified by quadratic polynomial minimization,
not by sampling times. Standard library only. This is independent code,
not independent-context mathematical review.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import argparse

ROOT = Path(__file__).resolve().parent


def minimum(poly, left, right):
    a, b, c = poly
    points = [left, right]
    if a > 0 and left <= -b/(2*a) <= right:
        points.append(-b/(2*a))
    return min(a*u*u+b*u+c for u in points)


def at(coeff, u):
    a, b, c = coeff
    return a*u+b/u+c


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='research-excursion-path-certificates.json')
    parser.add_argument('--output', default='research-excursion-independent-verification.json')
    args = parser.parse_args()
    path = ROOT/args.input
    records = json.loads(path.read_text())['certificates']
    cells = coords = degenerate = 0
    for record in records:
        e, a, x, b, z, h = [Q(record[k]) for k in ['E', 'a', 'x', 'B', 'Z', 'peak']]
        p, q = [list(map(Q, record[k])) for k in ['p', 'q']]
        assert e > 1 and a > 0 and a*(1+e) < 1
        high = a*e
        minimum_exp = e if high <= Q(1, 2) else 1/(4*a*(1-high))
        assert 1 <= x <= b and z == b*b and z >= minimum_exp
        assert b <= (1+e)/2
        if record.get('family', 'small-swapped') == 'small-swapped':
            assert high <= Q(1, 2) and x*x <= e
            assert x+e/x == 2*b
        assert h == 1-2*a*b and h >= p[0] and h > 0
        assert p == [1-a*(1+e), a, a*e]
        assert q == [p[0], p[2], p[1]]
        previous = p
        previous_u = Q(1)
        for cell in record['half_cells']:
            left, right = map(Q, cell['interval'])
            assert 1 <= left <= right <= b
            assert left == previous_u
            coeffs = [list(map(Q, c)) for c in cell['coefficients']]
            assert [sum(c[k] for c in coeffs) for k in range(3)] == [0, 0, 1]
            assert [at(c, left) for c in coeffs] == previous
            for aa, bb, cc in coeffs:
                # u*r > 0 and u*(r +/- dr/ds) >= 0, where s=log u.
                assert minimum((aa, cc, bb), left, right) > 0
                assert minimum((2*aa, cc, Q(0)), left, right) >= 0
                assert minimum((Q(0), cc, 2*bb), left, right) >= 0
                coords += 1
            aa, bb, cc = coeffs[0]
            assert minimum((-aa, h-cc, -bb), left, right) >= 0
            previous = [at(c, right) for c in coeffs]
            previous_u = right
            cells += 1
            degenerate += left == right
        assert previous == [h, a*b, a*b]
        assert previous_u == b
        # Symmetry gives continuity at the midpoint and the second endpoint q;
        # time reversal only changes derivative signs, so speed inequalities persist.
        assert [p[0], p[2], p[1]] == q
        # At the midpoint the two changing coordinates saturate the endpoint
        # upper bounds, certifying the global peak lower bound h exactly.
        assert previous[0] == 1-previous[1]-previous[2] == h
    result = {'status': 'all serialized continuous cells verified exactly',
              'job_id': 'privacy-interpolation-research-294f008bff48',
              'certificates': len(records), 'half_cells': cells,
              'coordinate_cells': coords, 'degenerate_half_cells': degenerate,
              'full_path_rule': 'reflect time and swap the two changing coordinates',
              'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'limits': 'Independent implementation in this research context; no fresh referee or novelty acceptance.'}
    (ROOT/args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
