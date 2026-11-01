"""Fresh referee checks; reads frozen inputs and writes only this audit's output.

Finite computations supplement the reconstructed quantified proofs in math.md.
No proposer checker, search routine, or previous acceptance is used as evidence.
"""
import ast
import bisect
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations
import json
import math
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
JOB = 'robust-stopping-referee-e7c6798337e7'
OUT = ROOT / 'audit/referee-e7c6798337e7-checks.json'
results = {'job_id': JOB, 'status': 'in_progress', 'checks': {}}


def save():
    OUT.write_text(json.dumps(results, indent=2, default=str) + '\n')


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def cost(b, t, x):
    return b + t - 1 if t <= x else x


def forecast_cost(b, p, t):
    return sum(prob * cost(b, t, x) for x, prob in p.items())


def check(b, R, p, f, lam, alpha, y, value=None):
    r = R - 1
    assert sum(f.values()) == 1 and all(t >= 1 and q > 0 for t, q in f.items())
    assert lam >= 0 and all(v >= 0 for v in y.values())
    assert len(f) <= b + 1 and sum(t >= b for t in f) <= 2
    S = set(range(1, b + 1)) | {d + 1 for d, q in p.items() if q and d >= b}
    assert set(f) <= S
    mu = sum((t - 1) * q for t, q in f.items())
    assert mu <= r * b
    for x in range(1, b):
        prefix = sum((b + t - 1 - x) * q for t, q in f.items() if t <= x)
        assert prefix <= r * x
        assert y.get(x, 0) * (r * x - prefix) == 0
    assert lam * (r * b - mu) == 0
    # Check direct original costs for each distinct actual-horizon interval.
    horizons = set(range(1, b + 1)) | set(f) | {t - 1 for t in f if t > 1}
    for x in horizons:
        assert sum(q * cost(b, t, x) for t, q in f.items()) <= R * min(x, b)
    assert b + mu <= R * b  # Constant cost after the final support day.
    # Independently choose additional omitted buy-days around each jump.
    days = S | {max(S) + 1, max(S) + 1000}
    for d in p:
        days.update(t for t in (d - 1, d, d + 1, d + 2) if t >= 1)
    for t in days:
        lhs = forecast_cost(b, p, t) + lam * (t - 1)
        lhs += sum((b + t - 1 - x) * v for x, v in y.items() if x >= t)
        assert lhs >= alpha
        if t in f:
            assert lhs == alpha
    J = sum(q * forecast_cost(b, p, t) for t, q in f.items())
    dual = alpha - r * sum(x * v for x, v in y.items()) - lam * r * b
    assert J == dual
    if value is not None:
        assert J == value
    return J


def rational_map(d):
    return {int(k): F(v) for k, v in d.items()}


def solve_equalities(A, rhs):
    n = len(rhs)
    M = [[F(x) for x in row] + [F(q)] for row, q in zip(A, rhs)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if M[i][col]), None)
        if pivot is None:
            return None
        M[col], M[pivot] = M[pivot], M[col]
        q = M[col][col]
        M[col] = [v / q for v in M[col]]
        for i in range(n):
            if i != col:
                q = M[i][col]
                M[i] = [v - q * w for v, w in zip(M[i], M[col])]
    return tuple(row[-1] for row in M)


def enumerate_vertices(b, R, days, with_moment):
    n = len(days)
    inequalities = []
    for x in range(1, b):
        inequalities.append(([b + t - 1 - x if t <= x else 0 for t in days], (R - 1) * x))
    if with_moment:
        inequalities.append(([t - 1 for t in days], (R - 1) * b))
    for i in range(n):
        inequalities.append(([-int(j == i) for j in range(n)], F(0)))
    vertices = set()
    for chosen in combinations(inequalities, n - 1):
        f = solve_equalities([[1] * n] + [a for a, _ in chosen], [1] + [v for _, v in chosen])
        if f is not None and all(sum(a * q for a, q in zip(row, f)) <= v for row, v in inequalities):
            vertices.add(f)
    assert vertices
    return vertices


snapshot = json.loads((ROOT / 'audit/snapshot.json').read_text())
assert all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in snapshot['files'].items())
assert hashlib.sha256(json.dumps(snapshot['files'], sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest() == snapshot['digest']
results['snapshot_digest'] = snapshot['digest']
results['checks']['frozen_files'] = len(snapshot['files'])
save()

count = 0
for name in ('evidence/oracle-test-cases.json', 'evidence/bisection-test-cases.json'):
    for rec in json.loads((ROOT / name).read_text()):
        out = rec['result']
        check(rec['b'], F(rec['R']), rational_map(rec['p']), rational_map(out['policy']),
              F(out['lam']), F(out['alpha']), rational_map(out['y']), F(rec['value']))
        count += 1
results['checks']['saved_full_model_certificates'] = count
save()

linear_count = 0
for rec in json.loads((ROOT / 'evidence/linear-oracle-test-cases.json').read_text()):
    b, r = rec['b'], F(rec['R']) - 1
    c, f, y = (rational_map(rec[k]) for k in ('costs', 'policy', 'y'))
    alpha = F(rec['alpha'])
    assert sum(f.values()) == 1 and min(f.values()) > 0
    for x in range(1, b):
        assert sum((b + t - 1 - x) * q for t, q in f.items() if t <= x) <= r * x
    assert all(v >= 0 for v in y.values())
    assert all(c[t] + sum((b + t - 1 - x) * v for x, v in y.items() if x >= t) >= alpha for t in c)
    assert sum(c[t] * q for t, q in f.items()) == alpha - r * sum(x * q for x, q in y.items()) == F(rec['value'])
    linear_count += 1
results['checks']['saved_arbitrary_cost_certificates'] = linear_count
save()

oracle = module('referee_prefix', 'evidence/prefix_oracle.py')
uniform = module('referee_uniform', 'revision/uniform_frontier.py')
rng = random.Random(77183143)
new_calls, vertex_comparisons, normalized_checks = [], 0, 0
for b in range(2, 6):
    rho = F(b ** b, b ** b - (b - 1) ** b)
    for R in (rho, rho + F(1, 113), F(2), F(13, 2)):
        horizon_sets = ([1], [1, b - 1, b, b + 2])
        for horizons in horizon_sets:
            weights = {x: rng.randrange(1, 12) for x in set(horizons)}
            p = {x: F(w, sum(weights.values())) for x, w in weights.items()}
            p[10 ** 18] = F(0)  # Zero atoms must not enlarge the support.
            out = oracle.optimize(b, R, p, max_chord_probes=0)
            assert out.get('chord_probes', 0) == 0
            J = check(b, R, p, out['policy'], out['lam'], out['alpha'], out['y'])
            new_calls.append({'b': b, 'R': str(R), 'p': {str(k): str(v) for k, v in p.items()},
                              'value': str(J), 'calls': out['calls'], 'bisections': out['isolation_steps']})
            if b <= 4:
                days = sorted(set(range(1, b + 1)) | {d + 1 for d, q in p.items() if q and d >= b})
                vertices = enumerate_vertices(b, R, days, True)
                assert min(sum(q * forecast_cost(b, p, t) for t, q in zip(days, f)) for f in vertices) == J
                vertex_comparisons += 1
    days = list(range(1, b + 2))
    for R in (rho, F(2), F(9, 2)):
        vertices = enumerate_vertices(b, R, days, False)
        for _ in range(8):
            c = {t: F(rng.randrange(-18, 19), rng.randrange(1, 12)) for t in days}
            f, alpha, y, events = oracle.linear_oracle(b, R, c)
            J = sum(c[t] * q for t, q in f.items())
            assert J == min(sum(c[t] * q for t, q in zip(days, v)) for v in vertices)
            assert events <= b - 1
            normalized_checks += 1
results['checks']['new_pure_bisection_cases'] = new_calls
results['checks']['independent_vertex_optimum_comparisons'] = vertex_comparisons
results['checks']['new_signed_cost_vertex_comparisons'] = normalized_checks
save()

# Huge encoded positive horizons and huge R numerator attack distinct bit issues.
big_cases = [(2, F(7, 5), {1: F(9, 10), 10 ** 60: F(1, 10)}),
             (3, F(3, 2), {1: F(2, 5), 2: F(3, 5)}),
             (2, F(10 ** 60, 3), {1: F(1, 7), 5: F(6, 7)})]
for b, R, p in big_cases:
    out = oracle.optimize(b, R, p, max_chord_probes=0)
    check(b, R, p, out['policy'], out['lam'], out['alpha'], out['y'])
results['checks']['large_encoded_input_cases'] = len(big_cases)
save()

uniform_checks, endpoint_checks, unique_vertex_cases, sharp_families = 0, 0, 0, []
for b in list(range(2, 21)) + [37, 64]:
    p = {x: F(1, b) for x in range(1, b + 1)}
    data = uniform.frontier(b)
    a = b - 1
    assert data['segments'][-1]['lower'] == F(a ** b, b ** b - a ** b)
    for row in data['segments']:
        j = row['j']
        q = F(b, a) ** j
        assert row['A'] == q - 1 and row['C'] == (2 * b - j) * q - 2 * b
        for r in (row['lower'], row['upper'], (2 * row['lower'] + 5 * row['upper']) / 7):
            out = uniform.policy(b, r, segment=j)
            J = check(b, 1 + r, p, out['policy'], out['lambda'], out['alpha'], out['y'], out['value'])
            assert sum((t - 1) * q for t, q in out['policy'].items()) == r * b
            for t in range(1, b + 4):
                slack = forecast_cost(b, p, t) + out['lambda'] * (t - 1) - out['alpha']
                slack += sum((b + t - 1 - x) * v for x, v in out['y'].items() if x >= t)
                assert (slack == 0) == (t <= j or t == b + 1)
            assert all(v > 0 for v in out['y'].values())
            if r in (row['lower'], row['upper']):
                assert out['policy'] == uniform.policy(b, r)['policy']
                endpoint_checks += 1
            elif b <= 4:
                days = list(range(1, b + 2))
                vertices = enumerate_vertices(b, 1 + r, days, True)
                values = [(sum(q * forecast_cost(b, p, t) for t, q in zip(days, f)), f) for f in vertices]
                best = min(v for v, f in values)
                opts = [f for v, f in values if v == best]
                assert best == J and len(opts) == 1
                assert opts[0] == tuple(out['policy'].get(t, F(0)) for t in days)
                unique_vertex_cases += 1
            uniform_checks += 1
        if j < b:
            assert data['segments'][j]['slope'] - row['slope'] == -F(b + row['C'], 2 * b)
    low = data['segments'][-1]
    r = (low['lower'] + low['upper']) / 2
    assert len(uniform.policy(b, r)['policy']) == b + 1
    sharp_families.append(b)
    for r in (F(1), F(101, 97), F(17)):
        out = uniform.policy(b, r)
        check(b, 1 + r, p, out['policy'], out['lambda'], out['alpha'], out['y'], data['m'])
results['checks']['uniform_certificate_queries'] = uniform_checks
results['checks']['uniform_endpoint_formula_checks'] = endpoint_checks
results['checks']['uniform_independent_unique_vertex_cases'] = unique_vertex_cases
results['checks']['uniform_sharp_support_b'] = sharp_families
save()

# Separate loader, direct Fraction(float), and line tracer for both unchanged classes.
software = []
expected_levels = [3.000001907348633, 3.0000000004656613, 2.9999999999995453]
for filename in ('Figure1_Performance_Comparison_Under_Prediction_Error.py',
                 'Table2_Consistency_Comparison_under_Fixed_Robustness.py'):
    path = ROOT / 'literature/kf26-official-code' / filename
    raw = path.read_bytes()
    node = next(n for n in ast.parse(raw).body if isinstance(n, ast.ClassDef) and n.name == 'SkiRentalOptimizer')
    ns = {'math': math, 'bisect': bisect}
    exec(compile(ast.Module(body=[node], type_ignores=[]), filename, 'exec'), ns)
    cls = ns['SkiRentalOptimizer']
    for tolerance, expected in zip((1e-5, 1e-9, 1e-12), expected_levels):
        obj = cls(3, 1.5, [1, 2], [.4, .6])
        h = obj.solve(tolerance=tolerance)
        law = {t: F(v) for t, v in obj.construct_policy_pmf(h).items()}
        assert h == expected
        assert law == {1: F(1, 4), 2: F(3, 8), 3: F(3, 8)}
        assert obj.is_feasible(14 / 5) is False and obj.is_feasible(3) is True
        p = {1: F(2, 5), 2: F(3, 5)}
        J = sum(q * forecast_cost(3, p, t) for t, q in law.items())
        mu = sum((t - 1) * q for t, q in law.items())
        assert (J, mu) == (F(12, 5), F(9, 8))
        actual = {x: sum(q * cost(3, t, x) for t, q in law.items()) for x in (1, 2, 3)}
        assert actual == {1: F(3, 2), 2: F(3), 3: F(33, 8)}
        assert all(v <= F(3, 2) * min(x, 3) for x, v in actual.items())
        software.append({'filename': filename, 'sha256': hashlib.sha256(raw).hexdigest(),
                         'tolerance': tolerance, 'level': h, 'law': law, 'J': J, 'moment': mu,
                         'direct_horizon_costs': actual, 'all_x_ge_3': '33/8 <= 9/2'})
    states = []
    def tracer(frame, event, arg):
        if frame.f_code.co_name == 'construct_policy_pmf' and event in ('line', 'return'):
            states.append({k: ({t: F(v) for t, v in q.items()} if isinstance(q, dict) else F(q))
                           for k, q in frame.f_locals.items() if k in ('F', 'mu', 'pmf')})
        return tracer
    assert sys.gettrace() is None
    sys.settrace(tracer)
    try:
        obj.construct_policy_pmf(3)
    finally:
        sys.settrace(None)
    assert any(s.get('F') == F(19, 16) and s.get('pmf', {}).get(3) == F(9, 16) for s in states)
    assert states[-1]['pmf'][3] == F(3, 8)
    software.append({'filename': filename, 'construction_at_3_final_locals': states[-1],
                     'overshoot_F_19_over_16_and_day3_9_over_16_seen': True})
results['checks']['software'] = software
save()

# Objective separation verified against the original definitions.
for p, lam, alpha, f, expected in [
    ({1: F(2, 5), 2: F(3, 5)}, F(7, 10), F(3), {1: F(1, 4), 3: F(3, 4)}, F(39, 20)),
    ({1: F(1, 2), 2: F(1, 2)}, F(3, 4), F(3), {1: F(1, 4), 3: F(3, 4)}, F(15, 8)),
    ({1: F(1, 2), 2: F(1, 4)}, F(1, 2), F(2), {2: F(1, 2), 3: F(1, 2)}, F(5, 4)),
]:
    check(3, F(3, 2), p, f, lam, alpha, {}, expected)
    assert all(forecast_cost(3, p, t) + lam * (t - 1) > alpha for t in (2 if 1 in f else 1, 4, 1000))
results['checks']['objective_separation_global_certificates'] = 3
assert all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in snapshot['files'].items())
results['status'] = 'passed'
results['limits'] = 'Finite tests supplement analytic all-input and infinite-tail proofs. Software observations cover only the six specified calls; no universal implementation assertion.'
save()
print(json.dumps({'status': results['status'], 'audit': str(OUT.relative_to(ROOT)),
                  'checks': {k: (len(v) if isinstance(v, list) else v) for k, v in results['checks'].items()}}, default=str))
