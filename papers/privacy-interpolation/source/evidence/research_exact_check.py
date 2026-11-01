"""Exact finite research checks and greedy-path certificates; standard library.

This is a finite test, not proof or an independent mathematical referee.
Run from any directory. Outputs only beside this script inside the project.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


def compositions(total, n, prefix=()):
    if n == 1:
        yield prefix + (total,)
    else:
        for a in range(1, total - n + 2):
            yield from compositions(total - a, n - 1, prefix + (a,))


def vectors(total, n):
    return [tuple(F(a, total) for a in c) for c in compositions(total, n)]


def cuts(n):
    return [tuple(i for i in range(n) if mask & (1 << i))
            for mask in range(1, (1 << n) - 1)]


def mass(x, subset):
    return sum((x[i] for i in subset), F(0))


def h(e, a):
    if a <= F(1, 2) / e:
        return e * a
    if a <= F(1, 2):
        return 1 - 1 / (4 * e * a)
    return 1 - (1 - a) / e


def binary_exp(a, b):
    a, b = min(a, b), max(a, b)
    if b <= F(1, 2):
        return b / a
    if a >= F(1, 2):
        return (1 - a) / (1 - b)
    return 1 / (4 * a * (1 - b))


def endpoint_exp(p, q):
    return max(max(a / b, b / a) for a, b in zip(p, q))


def value_exp(p, q):
    order = sorted(range(len(p)), key=lambda i: q[i] / p[i], reverse=True)
    a = b = F(0)
    answer = F(1)
    for i in order[:-1]:
        a += p[i]
        b += q[i]
        assert b >= a
        answer = max(answer, binary_exp(a, b))
    return answer


def greedy(p, order, e):
    answer = [F(0)] * len(p)
    a = F(0)
    previous = F(0)
    for i in order:
        a += p[i]
        current = h(e, a)
        answer[i] = current - previous
        previous = current
    return tuple(answer)


def decompose(p, q, e):
    """Enumerative ray-to-face algorithm; <=n vertices, exact fractions."""
    n = len(p)
    subsets = cuts(n)
    ranks = [h(e, mass(p, subset)) for subset in subsets]
    vertex_data = []
    seen = set()
    for order in permutations(range(n)):
        z = greedy(p, order, e)
        if z not in seen:
            seen.add(z)
            vertex_data.append((order, z, [mass(z, a) for a in subsets]))
    x = tuple(q)
    weight = F(1)
    result = []
    trace = []
    for stage in range(n):
        xm = [mass(x, subset) for subset in subsets]
        assert all(a <= b for a, b in zip(xm, ranks))
        tight = [j for j, (a, b) in enumerate(zip(xm, ranks)) if a == b]
        order, z, zm = next(data for data in vertex_data
                            if all(data[2][j] == ranks[j] for j in tight))
        if x == z:
            result.append((weight, order, z))
            trace.append({'stage': stage, 'terminal': True,
                          'tight_masks': [sum(1 << i for i in subsets[j])
                                          for j in tight]})
            break
        alpha = min((ranks[j] - zm[j]) / (xm[j] - zm[j])
                    for j in range(len(subsets)) if xm[j] > zm[j])
        assert alpha > 1
        result.append((weight * (1 - 1 / alpha), order, z))
        weight /= alpha
        xp = tuple(z[i] + alpha * (x[i] - z[i]) for i in range(n))
        new_tight = [j for j, subset in enumerate(subsets)
                     if mass(xp, subset) == ranks[j]]
        assert set(tight) < set(new_tight)
        trace.append({'stage': stage, 'terminal': False, 'alpha': str(alpha),
                      'tight_count_before': len(tight),
                      'tight_count_after': len(new_tight)})
        x = xp
    else:
        raise AssertionError('face dimension did not decrease as proved')
    assert len(result) <= n
    assert all(w > 0 for w, _, _ in result)
    assert sum((w for w, _, _ in result), F(0)) == 1
    assert tuple(sum((w * z[i] for w, _, z in result), F(0))
                 for i in range(n)) == tuple(q)
    return result, trace


def verify_path(p, q, e, decomposition):
    # Test all branch switches and exact rational midpoints between them.
    # These samples supplement the analytic v-Lipschitz argument, not replace it.
    switches = {F(1), e}
    for _, order, _ in decomposition:
        a = F(0)
        for i in order[:-1]:
            a += p[i]
            if a < F(1, 2):
                switch = 1 / (2 * a)
                if 1 < switch < e:
                    switches.add(switch)
    ordered = sorted(switches)
    samples = ordered + [(a + b) / 2 for a, b in zip(ordered, ordered[1:])]
    checks = 0
    for u in samples:
        r = [F(0)] * len(p)
        d = [F(0)] * len(p)
        for w, order, _ in decomposition:
            a = F(0)
            prev = F(0)
            for i in order:
                a += p[i]
                level = h(u, a)
                derivative = min(level, 1 - level) - min(prev, 1 - prev)
                coordinate = level - prev
                assert coordinate > 0 and abs(derivative) <= coordinate
                r[i] += w * coordinate
                d[i] += w * derivative
                prev = level
        assert sum(r) == 1 and sum(d) == 0
        assert all(a > 0 and abs(b) <= a for a, b in zip(r, d))
        if u == 1:
            assert tuple(r) == tuple(p)
        if u == e:
            assert tuple(r) == tuple(q)
        checks += len(p)
    return checks, len(ordered) - 2


def serialize(p, q, e, result, trace):
    return {'p': list(map(str, p)), 'q': list(map(str, q)),
            'exp_optimal_cost': str(e),
            'paths': [{'weight': str(w), 'order_zero_based': list(order),
                       'terminal_vertex': list(map(str, z))}
                      for w, order, z in result],
            'decomposition_trace': trace}


def main():
    root = Path(__file__).resolve().parents[1]
    original = hashlib.sha256((root / 'source.md').read_bytes()).hexdigest()
    assert original == '9488f12633da72d763b0ad127ff791f002ff7451ea26826a68d35a832f0bad15'
    counts = {'held_out_pairs': 0, 'all_subset_checks': 0,
              'decomposed_pairs': 0, 'path_coordinate_samples': 0,
              'max_paths': 0, 'worst_bound_equality_pairs': 0}
    # Denominator 9 was not used by the triage's denominator-8 prefix checks.
    for n in range(2, 5):
        subsets = cuts(n)
        for p, q in product(vectors(9, n), repeat=2):
            e = value_exp(p, q)
            all_e = max(binary_exp(mass(p, a), mass(q, a)) for a in subsets)
            assert e == all_e
            eta_e = endpoint_exp(p, q)
            assert eta_e <= e <= ((eta_e + 1) / 2) ** 2
            if eta_e > 1:
                equality = e == ((eta_e + 1) / 2) ** 2
                binary_ratios = all(q[i] / p[i] in (eta_e, 1 / eta_e)
                                    for i in range(n))
                assert equality == binary_ratios
                counts['worst_bound_equality_pairs'] += equality
            for u in {F(1), e, (1 + e) / 2, 2 * e}:
                membership = all(mass(q, a) <= h(u, mass(p, a)) for a in subsets)
                assert membership == (e <= u)
            counts['held_out_pairs'] += 1
            counts['all_subset_checks'] += len(subsets)
    certificates = []
    for n in range(2, 5):
        for p, q in product(vectors(6, n), repeat=2):
            e = value_exp(p, q)
            result, trace = decompose(p, q, e)
            checks, _ = verify_path(p, q, e, result)
            counts['decomposed_pairs'] += 1
            counts['path_coordinate_samples'] += checks
            counts['max_paths'] = max(counts['max_paths'], len(result))
    # Structured five-output cases, including ties and a highly imbalanced pair.
    cases = [
        ([1, 1, 2, 3, 5], [2, 5, 1, 3, 1]),
        ([1, 1, 1, 1, 20], [20, 1, 1, 1, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([2, 2, 2, 3, 3], [1, 1, 1, 4, 5]),
        ([1, 3, 3, 9, 12], [9, 1, 9, 3, 6]),
        ([2, 2, 2, 2, 2], [1, 1, 2, 3, 3]),
    ]
    for a, b in cases:
        assert sum(a) == sum(b)
        p, q = tuple(F(x, sum(a)) for x in a), tuple(F(x, sum(b)) for x in b)
        e = value_exp(p, q)
        result, trace = decompose(p, q, e)
        checks, _ = verify_path(p, q, e, result)
        counts['decomposed_pairs'] += 1
        counts['path_coordinate_samples'] += checks
        counts['max_paths'] = max(counts['max_paths'], len(result))
        certificates.append(serialize(p, q, e, result, trace))
    # Exact auxiliary obstruction: even the best reparameterized affine path fails.
    p = (F(1, 12), F(1, 12), F(5, 6))
    q = (F(1, 12), F(1, 2), F(5, 12))
    a = max(qi / pi - 1 for pi, qi in zip(p, q))
    d = max(1 - qi / pi for pi, qi in zip(p, q))
    crossing = (a - d) / (2 * a * d)
    assert crossing == F(9, 10)
    affine_length_e = (1 + a * crossing) * (1 - d * crossing) / (1 - d)
    assert affine_length_e == F(121, 20) > value_exp(p, q) == 6
    result = {'job_id': 'privacy-interpolation-research-1e71d7ce81cd',
              'status': 'passed: exact finite evidence; no referee certification',
              'arithmetic': 'fractions.Fraction; no numerical tolerance',
              'coverage': {'prefix_value_and_envelope':
                           'all ordered positive denominator-9 pairs, n=2..4',
                           'finite_path_decomposition':
                           'all ordered positive denominator-6 pairs, n=2..4, plus six listed n=5 cases',
                           'path_speed':
                           'all exact branch switches and rational midpoints for these decompositions; analytic proof separate'},
              'counts': counts,
              'reparameterized_affine_counterexample': {
                  'p': list(map(str, p)), 'q': list(map(str, q)),
                  'exp_affine_length': str(affine_length_e),
                  'exp_optimal_cost': '6',
                  'note': 'named subsidiary claim only; does not disprove original source'},
              'source_sha256': original}
    output = Path(__file__).with_name('research-exact-results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    Path(__file__).with_name('research-path-certificates.json').write_text(
        json.dumps({'certificates': certificates}, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
