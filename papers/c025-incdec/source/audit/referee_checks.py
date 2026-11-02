#!/usr/bin/env python3
"""Fresh exact finite checks; independent of every proposer implementation.

The written proof, rather than this bounded test, establishes the theorem.
Run from the project root. Writes only this referee's audit output.
"""
import hashlib
import itertools
import json
import random
from fractions import Fraction
from pathlib import Path

JOB = 'c025-incdec-referee-2ab23be91f58'
rng = random.Random(250211)
stats = dict(instances=0, greedy_orders=0, comparator_checks=0,
             branch_nonnegative=0, branch_negative=0, branch_zero=0,
             reversed_instances=0, zero_endpoint_instances=0,
             all_ties_instances=0, minimum_slack=None, maximum_ratio=Fraction(1))


def hypotheses(q, n):
    assert len(q) == 1 << n and q[0] == 0 and min(q) >= 0
    # Edge monotonicity and every elementary submodular square are sufficient.
    for s in range(1 << n):
        missing = [i for i in range(n) if not (s >> i) & 1]
        for i in missing:
            assert q[s | (1 << i)] >= q[s]
        for i, j in itertools.combinations(missing, 2):
            assert q[s | (1 << i)] + q[s | (1 << j)] >= q[s] + q[s | (1 << i) | (1 << j)]


def verify(h, g, all_ties=False):
    n = (len(h) - 1).bit_length()
    hypotheses(h, n)
    hypotheses(g, n)
    full = (1 << n) - 1
    original = [h[s] + g[full ^ s] for s in range(full + 1)]
    reverse = h[full] < g[full]
    stats['reversed_instances'] += reverse
    stats['zero_endpoint_instances'] += not h[full] or not g[full]
    if reverse:
        h, g = g, h
    H, G = h[full], g[full]
    assert H >= G
    f = [h[s] + g[full ^ s] for s in range(full + 1)]
    opts = [max(f[s] for s in range(full + 1) if s.bit_count() == k) for k in range(n + 1)]
    original_opts = [max(original[s] for s in range(full + 1) if s.bit_count() == k) for k in range(n + 1)]

    def visit(s, path, gains):
        k = len(path)
        assert f[s] <= H + G
        assert 2 * f[s] >= opts[k]
        if 0 < k < n:
            d = max(f[s | (1 << e)] - f[s] for e in range(n) if not (s >> e) & 1)
            assert all(a >= d for a in gains)
            assert f[s] == G + sum(gains)
            stats['branch_nonnegative' if d >= 0 else 'branch_negative'] += 1
            stats['branch_zero'] += d == 0
            for o in range(full + 1):
                if o.bit_count() != k:
                    continue
                u = o | s
                assert f[o] <= H + G
                assert G + f[u] - f[o] >= 0
                if d >= 0:
                    marg = sum(f[s | (1 << e)] - f[s] for e in range(n) if ((o & ~s) >> e) & 1)
                    m = (o & ~s).bit_count()
                    summands = [G + f[u] - f[o], f[s] + marg - f[u], m*d - marg, (k-m)*d, f[s]-G-k*d]
                else:
                    assert f[s] >= H
                    summands = [H+G-f[o], H-G, 2*(f[s]-H)]
                assert min(summands) >= 0 and sum(summands) == 2*f[s]-f[o]
                stats['comparator_checks'] += 1
                slack = 2*f[s]-f[o]
                old = stats['minimum_slack']
                stats['minimum_slack'] = slack if old is None else min(old, slack)
        if k == n:
            order = path[::-1] if reverse else path
            p = 0
            for j, e in enumerate(order, 1):
                p |= 1 << e
                assert 2*original[p] >= original_opts[j]
                # Nonnegative unnormalized baselines transfer without reorientation.
                for baseline in (0, 1, 17):
                    assert 2*(original[p]+baseline) >= original_opts[j]+baseline
                if original[p]:
                    stats['maximum_ratio'] = max(stats['maximum_ratio'], Fraction(original_opts[j], original[p]))
            stats['greedy_orders'] += 1
            return
        choices = [(f[s | (1 << e)] - f[s], e) for e in range(n) if not (s >> e) & 1]
        best = max(a for a, _ in choices)
        if gains:
            assert gains[-1] >= best
        elements = [e for a, e in choices if a == best]
        if not all_ties:
            elements = elements[:1]
        for e in elements:
            visit(s | (1 << e), path + [e], gains + [best])

    visit(0, [], [])
    stats['instances'] += 1
    stats['all_ties_instances'] += all_ties


def random_function(n):
    full = (1 << n) - 1
    # Sums of capped nonnegative modular functions include coverage and rank terms.
    terms = []
    for _ in range(rng.randrange(0, 9)):
        weights = [rng.randrange(0, 6) for _ in range(n)]
        cap = rng.randrange(0, sum(weights)+1)
        multiplier = rng.randrange(0, 4)
        terms.append((weights, cap, multiplier))
    return [sum(mult*min(cap, sum(w[i] for i in range(n) if (s >> i) & 1)) for w, cap, mult in terms) for s in range(full+1)]


for n in range(0, 7):
    zero = [0] * (1 << n)
    verify(zero, zero, all_ties=True)
    q = [s.bit_count() for s in range(1 << n)]
    verify(q, zero, all_ties=True)
    verify(zero, q, all_ties=True)

for case in range(600):
    n = rng.randrange(1, 8)
    h, g = random_function(n), random_function(n)
    verify(h, g, all_ties=(case < 150 and n <= 6))

frozen_witnesses = 0
for filename in ('template-screen.json', 'comparator-screen.json'):
    data = json.loads((Path('evidence/research-pass-2') / filename).read_text())
    for witness in data['exact_witnesses'].values():
        verify([Fraction(x) for x in witness['h']], [Fraction(x) for x in witness['g']])
        frozen_witnesses += 1
witness = json.loads(Path('evidence/research-pass-3/prefix-kernel-screen.json').read_text())['exact_witness']
verify([Fraction(x) for x in witness['h']], [Fraction(x) for x in witness['g']])
frozen_witnesses += 1

lower = []
for n in range(2, 9):
    full = (1 << n) - 1
    q = [n-1 if s & 1 else s.bit_count() for s in range(full+1)]
    f = [q[s]+q[full ^ s] for s in range(full+1)]
    opt = [max(f[s] for s in range(full+1) if s.bit_count() == k) for k in range(n+1)]
    minimum_worst = None
    count = 0
    for order in itertools.permutations(range(n)):
        s = 0
        worst = Fraction(1)
        for k, e in enumerate(order, 1):
            s |= 1 << e
            worst = max(worst, Fraction(opt[k], f[s]))
        assert worst >= Fraction(2*(n-1), n)
        minimum_worst = worst if minimum_worst is None else min(minimum_worst, worst)
        count += 1
    lower.append(dict(n=n, permutations=count, minimum_worst_ratio=str(minimum_worst), formula=str(Fraction(2*(n-1),n))))

snapshot = json.loads(Path('audit/snapshot.json').read_text())
mismatches = [name for name, digest in snapshot['files'].items() if hashlib.sha256(Path(name).read_bytes()).hexdigest() != digest]
assert not mismatches
result = dict(job_id=JOB, snapshot_digest=snapshot['digest'], exact_arithmetic=True,
              seed=250211, frozen_witnesses=frozen_witnesses, stats=stats,
              lower_bound=lower, snapshot_preserved=True, all_checks_pass=True,
              scope='Finite exact falsification and independent proof-step checks only. No owner code imported. Universal correctness and the limiting lower bound are established in audit/math.md, not by this finite computation.')
Path('audit/referee-checks.json').write_text(json.dumps(result, indent=2, default=str)+'\n')
print(json.dumps(result, default=str))
