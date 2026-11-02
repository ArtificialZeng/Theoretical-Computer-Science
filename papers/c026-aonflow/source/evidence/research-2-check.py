#!/usr/bin/env python3
"""Exact finite diagnostics for the uniform-copy proof; not a full AON solver."""
from fractions import Fraction as Q
from itertools import product, combinations
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c026-aonflow-research-02dec8252283'
SOURCE = '7241936e887e814eebe18f891cfe9d90c883ee0298057dfc8bbdd2344501e29e'


def ceil(x):
    return -(-x.numerator // x.denominator)


def edge(u, v):
    return tuple(sorted((u, v)))


def path_edges(path):
    return frozenset(edge(u, v) for u, v in zip(path, path[1:]))


def split(paths, T):
    result, current, mass = [], [], Q(0)
    for path, amount in paths:
        while amount:
            take = min(amount, Q(1, T) - mass)
            current.append((path, take))
            mass += take
            amount -= take
            if mass == Q(1, T):
                result.append(current)
                current, mass = [], Q(0)
    if current:
        result.append(current)
    return result


def prepare_fixture():
    # Duplicate first two original pairs, plus shared original endpoints.
    raw = [([(0, 1, 3), (0, 2, 3)], [Q(1, 4), Q(1, 4)]),
           ([(0, 2, 3)], [Q(1, 4)]),
           ([(1, 3, 4)], [Q(1, 4)])]
    pairs = []
    for i, (paths, masses) in enumerate(raw):
        s, t = 5 + 2*i, 6 + 2*i
        pairs.append([(path_edges((s,) + p + (t,)), a)
                      for p, a in zip(paths, masses)])
    return pairs


def finite_uniformization():
    pairs = prepare_fixture()
    edges = sorted(set().union(*(p for ps in pairs for p, _ in ps)))
    x = [sum((a for _, a in ps), Q(0)) for ps in pairs]
    F = sum(x, Q(0))
    assert F == 1
    for e in edges:
        assert sum((a for ps in pairs for p, a in ps if e in p), Q(0)) <= 1
    totals = {'sampling_outcomes': 0, 'cut_checks': 0, 'T_results': []}
    for T in range(1, 5):
        pieces = [(i, piece) for i, ps in enumerate(pairs) for piece in split(ps, T)]
        assert len(pieces) == sum(ceil(T*a) for a in x)
        assert len(pieces) <= T*F + len(pairs)
        options = []
        for owner, piece in pieces:
            opts = [(owner, p, T*a) for p, a in piece]
            null = 1 - sum((a for _, _, a in opts), Q(0))
            if null:
                opts.append((owner, frozenset(), null))
            assert sum((a for _, _, a in opts), Q(0)) == 1
            options.append(opts)
        ek, ee, probability, good = Q(0), dict.fromkeys(edges, Q(0)), Q(0), Q(0)
        for outcome in product(*options):
            weight = Q(1)
            for _, _, p in outcome:
                weight *= p
            selected = [(owner, path) for owner, path, _ in outcome if path]
            K = len(selected)
            counts = {e: sum(e in path for _, path in selected) for e in edges}
            probability += weight
            ek += weight*K
            for e in edges:
                ee[e] += weight*counts[e]
            if K >= T*F/2 and all(z <= 4*T for z in counts.values()):
                good += weight
                eps = Q(1, 4*T)
                # All singleton and two-edge deletion sets, plus empty deletion.
                for size in range(3):
                    for cut_tuple in combinations(edges, size):
                        cut = set(cut_tuple)
                        hit = sum(bool(path & cut) for _, path in selected)
                        cut_load = eps*sum(counts[e] for e in cut)
                        assert eps*hit <= cut_load <= len(cut)
                        if len(cut) <= eps*K/4:
                            assert K-hit >= Q(3, 4)*K
                        totals['cut_checks'] += 1
            totals['sampling_outcomes'] += 1
        assert probability == 1
        assert ek == T*F
        assert all(v <= T for v in ee.values())
        totals['T_results'].append({'T': T, 'pieces': len(pieces),
                                    'exact_good_event_probability': str(good)})
    # Tiny weights create one piece, not denominator-many pieces.
    tiny = Q(1, 2**300)
    tiny_pieces = split([(frozenset({(0, 1)}), tiny)], 1024)
    assert len(tiny_pieces) == 1
    totals['tiny_mass_denominator_bits'] = tiny.denominator.bit_length()
    return totals


def bounded_dyadic_sampler():
    cases = 0
    for denominator in range(2, 19):
        for first in range(denominator+1):
            for second in range(denominator-first+1):
                probs = [Q(first, denominator), Q(second, denominator),
                         Q(denominator-first-second, denominator)]
                for B in [2, 5, 9]:
                    size = 2**B
                    counts = [0, 0, 0]
                    for u in range(size):
                        cumulative = Q(0)
                        for j, p in enumerate(probs):
                            cumulative += p
                            if Q(u, size) < cumulative:
                                counts[j] += 1
                                break
                    actual = [Q(c, size) for c in counts]
                    assert sum(actual) == 1
                    assert all(abs(a-p) <= Q(1, size) for a, p in zip(actual, probs))
                    tv = sum((abs(a-p) for a, p in zip(actual, probs)), Q(0))/2
                    assert tv <= Q(len(probs), size)
                    cases += 1
    return {'rational_distribution_and_bit_cases': cases,
            'denominators': [2, 18], 'bit_counts': [2, 5, 9]}


def bridge_cut():
    # On a cut consisting of one old occurrence edge, every selected copy of
    # that original pair has endpoints on opposite sides, thus contributes 1.
    tested, feasible = 0, 0
    owners = [0, 0, 0, 1, 1, 2]
    for bits in product([0, 1], repeat=len(owners)):
        loads = [sum(b for b, i in zip(bits, owners) if i == j) for j in range(3)]
        is_feasible = all(load <= 1 for load in loads)
        if is_feasible:
            assert len({i for b, i in zip(bits, owners) if b}) == sum(bits)
            feasible += 1
        tested += 1
    return {'copy_subsets': tested, 'old_bridge_feasible_subsets': feasible,
            'limitation': 'Exact cut arithmetic, not a complete graph LP feasibility test.'}


def parameter_checks():
    assert Q(8, 9)**320 < Q(1, 64)
    assert Q(27, 256) < Q(1, 8)  # e<3 suffices for the upper-tail bound
    count = 0
    for N in [16, 17, 31, 32, 1024, 2**80]:
        b = (N-1).bit_length()
        T = 64*((2*N-1).bit_length())
        assert T >= 320
        assert Q(N, 8**T) < Q(1, 64)
        assert 2**b <= 2*N
        for k in [b+1, 2*b+1, 1000*b]:
            assert T <= 64*(k+2)
            assert 2*k*(T+1) <= 2*k*(64*(k+2)+1)
            count += 1
    return {'parameter_cases': count, 'minimal_T': 320,
            'individual_tail_budgets_less_than': '1/64',
            'sampling_total_variation_budget_at_most': '1/64',
            'good_event_probability_greater_than': '61/64'}


def main():
    digest = hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
    assert digest == SOURCE
    data = {'job_id': JOB, 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
            'arithmetic': 'exact fractions.Fraction', 'source_sha256': digest,
            'source_unchanged': True, 'uniformization': finite_uniformization(),
            'dyadic_sampling': bounded_dyadic_sampler(), 'admission_bridge': bridge_cut(),
            'parameters': parameter_checks(), 'all_checks_passed': True,
            'limits': ['No implementation of BJS decomposition or CKS rounding',
                       'No exhaustive graph domain; one explicit feasible path fixture',
                       'Finite diagnostics do not certify the proposed infinite theorem',
                       'Full algorithmic proof is in research-2-uniform-copy-resolution.md']}
    dest = ROOT/'evidence/research-2-check-results.json'
    dest.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
