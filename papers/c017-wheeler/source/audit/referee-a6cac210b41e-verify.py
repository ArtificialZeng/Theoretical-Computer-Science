#!/usr/bin/env python3
"""Fresh referee controls; finite checks supplement the written proof only."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

M = load('frozen_membership', 'evidence/check_membership.py')
R = load('frozen_realizability', 'evidence/research-2-check-realizability.py')

def all_paths(edges, terminals, depth):
    # Literal traversal, independently implemented; includes undefined-terminal paths.
    result = {}
    stack = [('', 0, '')]
    while stack:
        word, state, output = stack.pop()
        result[word] = (state, output,
                        None if terminals[state] is None else output + terminals[state])
        if len(word) == depth:
            continue
        for a, edge in enumerate(edges[state]):
            if edge is not None:
                target, emitted = edge
                stack.append((word + str(a), target, output + emitted))
    return result

def machine(edges):
    delta = {(p, str(a)): e[0] for p, row in enumerate(edges)
             for a, e in enumerate(row) if e is not None}
    outputs = {(p, str(a)): e[1] for p, row in enumerate(edges)
               for a, e in enumerate(row) if e is not None}
    return M.Machine(len(edges), ''.join(str(a) for a in range(len(edges[0]))),
                     delta, outputs)

def pieces(values):
    # Independent shortest-path segmentation of the whole finite value list.
    distance = [0] + [len(values) + 1] * len(values)
    for end in range(1, len(values) + 1):
        for start in range(end):
            signs = {(values[i] > values[i-1]) - (values[i] < values[i-1])
                     for i in range(start+1, end)} - {0}
            if len(signs) <= 1:
                distance[end] = min(distance[end], distance[start] + 1)
    return distance[-1]

def finite_case(edges, terminal):
    direct = all_paths(edges, terminal, len(edges)-1)
    ordered = sorted(direct, key=lambda w: w[::-1])
    colors = [direct[w][0] for w in ordered]
    compressed = [c for i, c in enumerate(colors) if i == 0 or colors[i-1] != c]
    separated = len(compressed) == len(set(compressed))
    T = machine(edges)
    decision = T.decide()
    assert decision['input_order'] == separated
    assert decision['member'] == separated  # Every reaching set is finite.
    for q in range(len(edges)):
        if not separated:
            break
        values = [direct[w][1][::-1] for w in ordered if direct[w][0] == q]
        assert decision['flags'][1][q] == all(x <= y for x, y in zip(values, values[1:]))
        assert decision['flags'][-1][q] == all(x >= y for x, y in zip(values, values[1:]))
        assert pieces(values) <= decision['piece_bounds'][q]
    return len(direct), separated

def exact_finite_quotient(edges, terminal):
    ce, ct, prefixes, _ = R.onward(edges, terminal)
    direct = all_paths(edges, terminal, len(edges)-1)
    canonical = all_paths(ce, ct, len(edges)-1)
    assert set(direct) == set(canonical)
    for w in direct:
        assert direct[w][2] == canonical[w][2]
        if w:
            assert canonical[w][1] == direct[w][1] + prefixes[direct[w][0]]
    ordered = sorted(canonical, key=lambda w: w[::-1])
    groups = []
    index = {}
    for w in ordered:
        if not groups or canonical[groups[-1][-1]][0] != canonical[w][0]:
            groups.append([])
        groups[-1].append(w)
        index[w] = len(groups)-1
    expected = sorted([min((w[::-1] for w in group), key=lambda w: (len(w), w))
                       for group in groups], key=lambda w: (len(w), w))
    E, reps_automaton, _ = R.component_relation(ce)
    reps = R.finite_language(reps_automaton)
    assert reps == expected
    pairs = 0
    for u, v in itertools.product(ordered, repeat=2):
        assert E.accepts(R.convolution(u[::-1], v[::-1])) == (index[u] == index[v])
        pairs += 1
    qe, qt = R.quotient(ce, ct, E, reps)
    split = all_paths(qe, qt, len(edges)-1)
    assert {w: r[2] for w, r in direct.items()} == {w: r[2] for w, r in split.items()}
    assert machine(qe).decide()['member']
    return pairs, len(groups)

def trimmed_unary(edges, terminal):
    reached = set()
    q = 0
    while q not in reached:
        reached.add(q)
        if edges[q][0] is None:
            break
        q = edges[q][0][0]
    if len(reached) != len(edges):
        return False
    live = {p for p, t in enumerate(terminal) if t is not None}
    while True:
        new = live | {p for p, row in enumerate(edges)
                      if row[0] is not None and row[0][0] in live}
        if new == live:
            return len(live) == len(edges)
        live = new

def unary_case(edges, terminal):
    ce, ct, _, _ = R.onward(edges, terminal)
    # Independent exact criterion for a unary functional graph: eventual
    # canonical color has a finite convex refinement iff its eventual cycle
    # has one state. A finite chain also always has a finite refinement.
    seen = {}
    q = 0
    while q not in seen and ce[q][0] is not None:
        seen[q] = len(seen)
        q = ce[q][0][0]
    expected = ce[q][0] is None or len(seen) - seen[q] == 1
    E, rep_automaton, _ = R.component_relation(ce)
    reps = R.finite_language(rep_automaton)
    assert (reps is not None) == expected
    old = all_paths(edges, terminal, 37)
    new = all_paths(ce, ct, 37)
    assert {w: r[2] for w, r in old.items()} == {w: r[2] for w, r in new.items()}
    if reps is not None:
        qe, qt = R.quotient(ce, ct, E, reps)
        assert machine(qe).decide()['member']
    return expected, len(old)

def main():
    snapshot = json.loads((ROOT / 'audit/snapshot.json').read_text())
    mismatches = [f for f, h in snapshot['files'].items()
                  if hashlib.sha256((ROOT / f).read_bytes()).hexdigest() != h]
    assert not mismatches
    rng = random.Random(202611013411)
    # Replay frozen serialized pump families using literal transition tables,
    # with fresh held-out indices and no call to the supplied witness checker.
    families = json.loads((ROOT / 'evidence/exact-certificates.json').read_text())['certificates']
    certificate_instances = 0
    for family in families:
        edges = {(e['from'], e['input']): (e['to'], e['output'])
                 for e in family['transitions']}
        def literal(word):
            q, output = family['initial'], ''
            for a in word:
                q, emitted = edges[q, a]
                output += emitted
            assert q == family['target_state']
            return output[::-1]
        for n in list(range(21)) + [37, 101, 313]:
            words = [t['x'] + t['y'] * n + t['z'] for t in family['templates']]
            next_words = [t['x'] + t['y'] * (n+1) + t['z'] for t in family['templates']]
            u, v, w = [x[::-1] for x in words]
            x, y, z = [literal(x) for x in words]
            assert u < v < w
            assert x < y > z if family['turn'] == 'peak' else x > y < z
            if family['interval_direction'] == 'increasing':
                assert w < next_words[0][::-1]
            else:
                assert next_words[2][::-1] < u
            certificate_instances += 1
    finite_count = finite_words = ordered_count = quotient_pairs = 0
    for case in range(180):
        n = 1 + case % 6
        k = 1 + case % 3
        edges = []
        for p in range(n):
            row = []
            for a in range(k):
                target = p+1 if a == 0 else rng.choice([None] + list(range(p+1, n)))
                if p == n-1:
                    target = None
                row.append(None if target is None else
                           (target, rng.choice(('', '0', '1', '01', '110', '001'))))
            edges.append(row)
        terminal = [rng.choice(('', '0', '10', '001')) for _ in edges]
        words, ordered = finite_case(edges, terminal)
        finite_count += 1
        finite_words += words
        ordered_count += ordered
    quotient_counts = []
    for case in range(48):
        n = 1 + case % 4
        edges = []
        for p in range(n):
            row = []
            for a in range(2):
                target = p+1 if a == 0 else rng.choice([None] + list(range(p+1, n)))
                if p == n-1:
                    target = None
                row.append(None if target is None else
                           (target, rng.choice(('', '0', '1', '01', '110'))))
            edges.append(row)
        terminal = [rng.choice(('', '0', '10')) for _ in edges]
        pairs, count = exact_finite_quotient(edges, terminal)
        quotient_pairs += pairs
        quotient_counts.append(count)
    unary_total = unary_yes = unary_replays = 0
    for n in (1, 2):
        for targets in itertools.product(range(-1, n), repeat=n):
            present = [p for p, t in enumerate(targets) if t >= 0]
            for outputs in itertools.product(('', '0', '10'), repeat=len(present)):
                output_map = dict(zip(present, outputs))
                edges = [[None if targets[p] < 0 else (targets[p], output_map[p])]
                         for p in range(n)]
                for terminal in itertools.product((None, '', '0', '10'), repeat=n):
                    if not trimmed_unary(edges, terminal):
                        continue
                    yes, replays = unary_case(edges, terminal)
                    unary_total += 1
                    unary_yes += yes
                    unary_replays += replays
    assert all(hashlib.sha256((ROOT / f).read_bytes()).hexdigest() == h
               for f, h in snapshot['files'].items())
    result = {
        'job_id': 'c017-wheeler-referee-a6cac210b41e',
        'snapshot_digest': snapshot['digest'],
        'status': 'all fresh checks passed',
        'frozen_files_checked': len(snapshot['files']),
        'serialized_pump_families_replayed': len(families),
        'serialized_pump_instances_replayed': certificate_instances,
        'fresh_pump_indices': list(range(21)) + [37, 101, 313],
        'finite_acyclic_membership_cases': finite_count,
        'finite_acyclic_complete_path_count': finite_words,
        'finite_acyclic_input_ordered_cases': ordered_count,
        'complete_finite_convex_quotient_cases': len(quotient_counts),
        'complete_finite_component_relation_pairs': quotient_pairs,
        'finite_component_counts': quotient_counts,
        'exhaustive_trimmed_unary_cases': unary_total,
        'unary_yes': unary_yes,
        'unary_no': unary_total-unary_yes,
        'supplementary_unary_literal_function_checks': unary_replays,
        'limitations': 'Fresh direct traversal/segmentation checks are finite. Unary finiteness comparison uses a separately derived exact graph criterion but the frozen normalization and automata constructors. These controls do not replace the all-input mathematical proof or certify novelty.'
    }
    target = ROOT / 'audit/referee-a6cac210b41e-checks.json'
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'finite_component_counts'}))

if __name__ == '__main__':
    main()
