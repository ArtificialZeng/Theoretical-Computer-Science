"""Independent consumer of saved rational certificates; no generator imports.

For each exponential cell r_i(u)=A*u+B+C/u, u=exp(s), the speed
conditions are B+2*C/u>=0 and 2*A*u+B>=0. Each is monotone on the
positive cell, so exact endpoint tests cover its ENTIRE closed interval.
Together with positive left endpoint and |r_i'|<=r_i they prove strict
positivity throughout the cell by Gronwall. This mathematical reduction
is the domain-completeness argument; this script is not a formal prover.
"""
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import json


def scalar_coeff(a, middle):
    if not a:
        return (R(0), R(0), R(0))
    if a >= R(1, 2):
        return (R(0), R(1), a - 1)
    if 2 * middle * a <= 1:
        return (a, R(0), R(0))
    return (R(0), R(1), -1 / (4 * a))


def evaluate(c, u):
    a, b, d = c
    return a * u + b + d / u


def verify_cell(coeff, left, right):
    assert left > 0 and right >= left
    assert sum(a for a, _, _ in coeff) == 0
    assert sum(b for _, b, _ in coeff) == 1
    assert sum(c for _, _, c in coeff) == 0
    for c in coeff:
        a, b, d = c
        assert evaluate(c, left) > 0
        for u in (left, right):
            assert b + 2 * d / u >= 0  # r-r'
            assert 2 * a * u + b >= 0  # r+r'
    return len(coeff)


def binary_time_exp(a, b):
    if a > b:
        a, b = b, a
    if b <= R(1, 2):
        return b / a
    if a >= R(1, 2):
        return (1 - a) / (1 - b)
    return 1 / (4 * a * (1 - b))


def verify_record(record):
    p, q = [tuple(map(R, record[key])) for key in ('p', 'q')]
    e = R(record['exp_optimal_cost'])
    n = len(p)
    assert len(q) == n and sum(p) == sum(q) == 1
    assert all(x > 0 for x in p + q)
    paths = [(R(row['weight']), tuple(row['order_zero_based']))
             for row in record['paths']]
    assert 1 <= len(paths) <= n
    assert sum(w for w, _ in paths) == 1 and all(w > 0 for w, _ in paths)
    thresholds = {R(1), e}
    for _, order in paths:
        assert sorted(order) == list(range(n))
        partial = R(0)
        for i in order[:-1]:
            partial += p[i]
            if 0 < partial < R(1, 2):
                threshold = 1 / (2 * partial)
                if 1 < threshold < e:
                    thresholds.add(threshold)
    thresholds = sorted(thresholds)
    if e == 1:
        assert p == q
        return {'cells': 0, 'coordinate_cells': 0, 'lower_witness': []}
    assert len(thresholds) - 1 <= n * (n - 1) + 1
    previous = p
    total = 0
    for left, right in zip(thresholds, thresholds[1:]):
        middle = (left + right) / 2
        coeff = [[R(0), R(0), R(0)] for _ in p]
        for weight, order in paths:
            partial = R(0)
            old = (R(0), R(0), R(0))
            for i in order:
                partial += p[i]
                new = scalar_coeff(partial, middle)
                for k in range(3):
                    coeff[i][k] += weight * (new[k] - old[k])
                old = new
        assert tuple(evaluate(c, left) for c in coeff) == previous
        total += verify_cell(coeff, left, right)
        previous = tuple(evaluate(c, right) for c in coeff)
    assert previous == q
    witness = None
    for size in range(1, n):
        for subset in combinations(range(n), size):
            a, b = sum(p[i] for i in subset), sum(q[i] for i in subset)
            binary = binary_time_exp(a, b)
            assert binary <= e
            if binary == e:
                witness = list(subset)
    assert witness is not None
    return {'cells': len(thresholds) - 1, 'coordinate_cells': total,
            'lower_witness_zero_based': witness}


def main():
    here = Path(__file__).resolve().parent
    records = json.loads((here / 'research-path-certificates.json').read_text())['certificates']
    checks = [verify_record(row) for row in records]
    # Independently check the explicit three-output path on two WHOLE cells.
    first = [(R(0), R(1, 12), R(0)),
             (R(1, 12), R(0), R(0)),
             (-R(1, 12), R(11, 12), R(0))]
    second = [(-R(1, 12), R(1), -R(5, 2)),
              (R(1, 12), R(0), R(0)),
              (R(0), R(0), R(5, 2))]
    verify_cell(first, R(1), R(5))
    verify_cell(second, R(5), R(6))
    assert [evaluate(c, R(5)) for c in first] == [evaluate(c, R(5)) for c in second]
    assert [evaluate(c, R(1)) for c in first] == [R(1, 12), R(1, 12), R(5, 6)]
    assert [evaluate(c, R(6)) for c in second] == [R(1, 12), R(1, 2), R(5, 12)]
    assert R(121, 20) > 6
    assert 5 < 6 and 25 < 30 < 36 and R(5, 6) < R(11, 12) ** 2
    output = {
        'job_id': 'privacy-interpolation-research-1e71d7ce81cd',
        'status': 'passed independent certificate consumer; not a fresh model referee',
        'arithmetic': 'exact Fraction, no generator import',
        'coverage': 'all six saved n=5 certificates; full exponential cells via monotonicity, not time samples',
        'certificates': checks,
        'affine_obstruction': 'two full exponential cells verified, endpoints normalized, coordinate-2 lower bound log 6',
        'limits': 'only serialized certificates and displayed auxiliary path are checked; analytic lemmas remain mathematical arguments'}
    (here / 'research-independent-verification.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
