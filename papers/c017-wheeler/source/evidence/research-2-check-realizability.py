#!/usr/bin/env python3
"""Exact automatic convex quotient prototype. Finite controls are not a proof.

No bounded enumeration is used to answer finiteness: that answer comes from
cycle detection in an explicitly constructed regular representative language.
The existing membership prototype is used only after constructing the quotient.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json
import random
import sys

PAD = '#'


class DFA:
    def __init__(self, alphabet, rows, finals):
        self.alphabet = tuple(alphabet)
        self.rows = rows
        self.finals = set(finals)
        self.index = {a: i for i, a in enumerate(self.alphabet)}

    def accepts(self, word):
        q = 0
        for a in word:
            q = self.rows[q][self.index[a]]
        return q in self.finals


def build(alphabet, start, step, final):
    states = [start]
    ids = {start: 0}
    rows = []
    for q in states:
        row = []
        for a in alphabet:
            r = step(q, a)
            if r not in ids:
                ids[r] = len(states)
                states.append(r)
            row.append(ids[r])
        rows.append(row)
    return DFA(alphabet, rows, [i for i, q in enumerate(states) if final(q)])


def minimize(A):
    colors = [int(q in A.finals) for q in range(len(A.rows))]
    while True:
        ids = {}
        new = []
        for q, row in enumerate(A.rows):
            key = (q in A.finals, tuple(colors[r] for r in row))
            if key not in ids:
                ids[key] = len(ids)
            new.append(ids[key])
        if new == colors:
            break
        colors = new
    reps = {c: colors.index(c) for c in set(colors)}
    return build(A.alphabet, colors[0],
                 lambda c, a: colors[A.rows[reps[c]][A.index[a]]],
                 lambda c: reps[c] in A.finals)


def combine(A, B, predicate):
    assert A.alphabet == B.alphabet
    return minimize(build(A.alphabet, (0, 0),
        lambda q, a: (A.rows[q[0]][A.index[a]], B.rows[q[1]][B.index[a]]),
        lambda q: predicate(q[0] in A.finals, q[1] in B.finals)))


def project(A, track):
    """Existential projection, including witnesses longer than retained words.

    Convolutions admit trailing all-PAD columns. After letter projection and
    subset construction, saturate finals backwards under all-PAD columns.
    This performs the regular right quotient by all-PAD*, so a witness can
    outlast every free variable. It is not a bound on the witness length.
    """
    images = {a: a[:track] + a[track+1:] for a in A.alphabet}
    alphabet = tuple(dict.fromkeys(images.values()))
    choices = {b: [A.index[a] for a in A.alphabet if images[a] == b]
               for b in alphabet}
    P = build(alphabet, frozenset({0}),
              lambda qs, b: frozenset(A.rows[q][i] for q in qs for i in choices[b]),
              lambda qs: bool(qs & A.finals))
    pad = P.index[(PAD,) * len(alphabet[0])]
    finals = set(P.finals)
    while True:
        more = finals | {q for q, row in enumerate(P.rows) if row[pad] in finals}
        if more == finals:
            break
        finals = more
    return minimize(DFA(P.alphabet, P.rows, finals))


def compare(c, a, b):
    if c or a == b:
        return c
    if a == PAD:
        return -1
    if b == PAD:
        return 1
    return -1 if a < b else 1


def convolution(*words):
    return [tuple(w[i] if i < len(w) else PAD for w in words)
            for i in range(max(map(len, words), default=0))]


def reversed_color_machine(edges):
    """Exact reversal DFA: state is the transformation q -> delta(q,rev(w))."""
    n = len(edges)
    k = len(edges[0])
    alphabet = tuple(str(i) for i in range(k))
    states = [tuple(range(n))]
    ids = {states[0]: 0}
    rows = []
    for t in states:
        row = []
        for a in range(k):
            u = tuple(-1 if edges[q][a] is None else t[edges[q][a][0]]
                      for q in range(n))
            if u not in ids:
                ids[u] = len(states)
                states.append(u)
            row.append(ids[u])
        rows.append(row)
    return alphabet, rows, [t[0] for t in states]


def tuple_predicate(edges, arity, predicate, comparisons=()):
    sigma, color_rows, labels = reversed_color_machine(edges)
    alphabet = tuple(product(sigma + (PAD,), repeat=arity))
    # (DFA states on each tape, ended bits, comparison signs)
    start = ((0,) * arity, (False,) * arity, (0,) * len(comparisons))
    def step(q, column):
        if q is None:
            return None
        states, ended, signs = q
        if any(e and a != PAD for e, a in zip(ended, column)):
            return None
        ns = tuple(s if a == PAD else color_rows[s][int(a)]
                   for s, a in zip(states, column))
        ne = tuple(e or a == PAD for e, a in zip(ended, column))
        nc = tuple(compare(c, column[i], column[j])
                   for c, (i, j) in zip(signs, comparisons))
        return ns, ne, nc
    def final(q):
        if q is None:
            return False
        states, ended, signs = q
        return predicate(tuple(labels[s] for s in states), ended, signs)
    return minimize(build(alphabet, start, step, final))


def component_relation(edges):
    # A different color lies strictly between endpoints (in either direction).
    bad = tuple_predicate(edges, 3,
        lambda cs, es, ss: all(c >= 0 for c in cs) and cs[2] != cs[0]
                          and ss[0] == ss[1] and ss[0] != 0,
        ((0, 2), (2, 1)))
    bad_pair = project(bad, 2)
    same = tuple_predicate(edges, 2,
                          lambda cs, es, ss: cs[0] == cs[1] and cs[0] >= 0)
    E = combine(same, bad_pair, lambda same, bad: same and not bad)
    # Shortlex(v)<shortlex(u): if one tape ends first its word is shorter;
    # otherwise the lexicographic sign decides. Store the length comparison by
    # a separate DFA because the ended bits alone lose simultaneous endings.
    alphabet = E.alphabet
    def slstep(q, col):
        if q is None:
            return None
        ends, length, lex = q
        if any(e and a != PAD for e, a in zip(ends, col)):
            return None
        if not length and (col[0] == PAD) != (col[1] == PAD):
            length = -1 if col[1] == PAD else 1  # length(v) vs length(u)
        return (tuple(e or a == PAD for e, a in zip(ends, col)), length,
                compare(lex, col[1], col[0]))
    short = minimize(build(alphabet, ((False, False), 0, 0), slstep,
        lambda q: q is not None and (q[1] < 0 or q[1] == 0 and q[2] < 0)))
    has_smaller = project(combine(E, short, lambda a, b: a and b), 1)
    domain = tuple_predicate(edges, 1, lambda cs, es, ss: cs[0] >= 0)
    reps = combine(domain, has_smaller, lambda dom, smaller: dom and not smaller)
    return E, reps, {'bad_triple_states': len(bad.rows),
                     'bad_pair_states': len(bad_pair.rows),
                     'component_relation_states': len(E.rows),
                     'representative_states': len(reps.rows)}


def finite_language(A):
    # Restrict to genuine letters: convolution padding is not part of a word.
    letters = [i for i, a in enumerate(A.alphabet) if PAD not in a]
    live = set(A.finals)
    while True:
        more = live | {q for q, row in enumerate(A.rows)
                       if any(row[i] in live for i in letters)}
        if more == live:
            break
        live = more
    if 0 not in live:
        return []
    color = {}
    def cyclic(q):
        color[q] = 1
        for i in letters:
            r = A.rows[q][i]
            if r not in live:
                continue
            if color.get(r) == 1 or color.get(r, 0) == 0 and cyclic(r):
                return True
        color[q] = 2
        return False
    if cyclic(0):
        return None
    result = []
    todo = [(0, '')]
    while todo:
        q, w = todo.pop()
        if q in A.finals:
            result.append(w)
        for i in letters:
            r = A.rows[q][i]
            if r in live:
                todo.append((r, w + A.alphabet[i][0]))
    return sorted(result, key=lambda w: (len(w), w))


def lcp(words):
    u = words[0]
    for v in words[1:]:
        j = 0
        while j < min(len(u), len(v)) and u[j] == v[j]:
            j += 1
        u = u[:j]
    return u


def onward(edges, terminal):
    n, k = len(edges), len(edges[0])
    prefixes = []
    for p in range(n):
        todo = deque([(p, '')]); seen = {p}
        while todo:
            q, out = todo.popleft()
            if terminal[q] is not None:
                prefixes.append(out + terminal[q]); break
            for item in edges[q]:
                if item is not None and item[0] not in seen:
                    r, w = item; seen.add(r); todo.append((r, out + w))
        else:
            raise ValueError('Non-coaccessible state')
    while True:
        new = []
        for p in range(n):
            options = [prefixes[p]]
            if terminal[p] is not None:
                options.append(terminal[p])
            options += [w + prefixes[r] for item in edges[p]
                        if item is not None for r, w in [item]]
            new.append(lcp(options))
        if new == prefixes:
            break
        prefixes = new
    norm = [[None if item is None else
             (item[0], (item[1] + prefixes[item[0]])[len(prefixes[p]):])
             for item in edges[p]] for p in range(n)]
    nt = [None if terminal[p] is None else terminal[p][len(prefixes[p]):]
          for p in range(n)]
    colors = [0] * n
    while True:
        ids = {}; new = []
        for p in range(n):
            key = (nt[p], tuple(None if item is None else
                               (item[1], colors[item[0]]) for item in norm[p]))
            if key not in ids:
                ids[key] = len(ids)
            new.append(ids[key])
        if new == colors:
            break
        colors = new
    reps = [colors.index(c) for c in range(max(colors) + 1)]
    ce = [[None if item is None else
           (colors[item[0]] + 1, item[1] + prefixes[item[0]]) for item in edges[0]]]
    ct = [terminal[0]]
    for p in reps:
        ce.append([None if item is None else (colors[item[0]] + 1, item[1])
                   for item in norm[p]])
        ct.append(nt[p])
    # Remove normalized classes not reached after a nonempty word.
    reached = [0]
    for p in reached:
        for item in ce[p]:
            if item is not None and item[0] not in reached:
                reached.append(item[0])
    ids = {p: i for i, p in enumerate(reached)}
    ce = [[None if item is None else (ids[item[0]], item[1]) for item in ce[p]]
          for p in reached]
    ct = [ct[p] for p in reached]
    return ce, ct, prefixes, colors


def run(edges, terminal, word):
    q, out = 0, ''
    for a in word:
        item = edges[q][int(a)]
        if item is None:
            return None
        q, x = item; out += x
    return q, out, None if terminal[q] is None else out + terminal[q]


def quotient(edges, terminal, E, reps):
    qe, qt = [], []
    for rep in reps:
        q = run(edges, terminal, rep[::-1])[0]
        row = []
        for a, item in enumerate(edges[q]):
            if item is None:
                row.append(None); continue
            encoding = str(a) + rep
            matches = [i for i, r in enumerate(reps)
                       if E.accepts(convolution(encoding, r))]
            assert len(matches) == 1
            row.append((matches[0], item[1]))
        qe.append(row); qt.append(terminal[q])
    assert reps[0] == ''
    return qe, qt


def main():
    from check_membership import Machine
    controls = [
        ('redundant_unary_parity', [[(1, '')], [(0, '')]], ['', ''], True, True),
        ('source_floor_length', [[(1, '')], [(0, '0')]], ['', ''], False, False),
        ('initial_cycle_nonempty_lcp', [[(0, '0')]], ['0'], True, True),
        ('binary_identity', [[(0, '0'), (0, '1')]], [''], True, True),
        ('binary_erasure', [[(0, ''), (0, '')]], [''], True, True),
        ('binary_complement', [[(0, '1'), (0, '0')]], [''], True, False),
        ('partial_terminal_unary_parity', [[(1, '')], [(0, '')]], ['', None], False, False),
        ('only_empty_word', [[None, None]], ['01'], True, True),
        ('empty_input_alphabet', [[]], ['1'], True, True),
        ('partial_delayed_terminal', [[(0, ''), (1, '')], [None, None]], [None, '01'], True, True),
        ('suffix_coloring_split', [[(1, ''), (1, '')], [(1, ''), (1, '')]], [None, ''], True, True),
        ('finite_domain_needs_convex_splitting',
         [[(1, ''), (1, '')], [(2, ''), (2, '')], [None, None]],
         ['', '', ''], True, True),
        ('binary_length_with_nonempty_lcp', [[(0, '0'), (0, '0')]], ['0'], True, False),
    ]
    reports = []
    literal_checks = h_checks = relation_checks = successor_checks = 0
    rng = random.Random(6172012)
    for name, edges, terminal, expected_finite, expected_member in controls:
        ce, ct, prefixes, colors = onward(edges, terminal)
        E, Rep, sizes = component_relation(ce)
        reps = finite_language(Rep)
        finite = reps is not None
        assert finite == expected_finite, (name, finite)
        k = len(edges[0]); sigma = ''.join(str(i) for i in range(k))
        words = [''.join(w) for d in range(8) for w in product(sigma, repeat=d)]
        defined = []
        for w in words:
            old = run(edges, terminal, w); new = run(ce, ct, w)
            assert (old is None) == (new is None)
            if old is None:
                continue
            assert old[2] == new[2]; literal_checks += 1
            if w:
                assert new[1] == old[1] + prefixes[old[0]]; h_checks += 1
            defined.append((w, new[0]))
        # Exhaust all pairs in the finite displayed domain for separation
        # falsification. A contrary-color between witness disproves E exactly;
        # absence in this finite window alone does not establish E.
        ordered = sorted(defined, key=lambda p: p[0][::-1])
        for _ in range(min(1500, max(1, len(ordered)**2))):
            i, j = sorted((rng.randrange(len(ordered)), rng.randrange(len(ordered))))
            u, cu = ordered[i]; v, cv = ordered[j]
            related = E.accepts(convolution(u[::-1], v[::-1]))
            if related:
                assert cu == cv and all(c == cu for _, c in ordered[i:j+1])
            if cu != cv or any(c != cu for _, c in ordered[i:j+1]):
                assert not related
            assert related == E.accepts(convolution(v[::-1], u[::-1]))
            # Trailing padding must never change relation truth.
            assert related == E.accepts(convolution(u[::-1], v[::-1]) + [(PAD, PAD)]*3)
            relation_checks += 1
        record = {'name': name, 'lambda': prefixes, 'normalized_colors': colors,
                  'canonical_states': len(ce), 'finite_convex_components': finite,
                  'component_representatives_reversed': reps, **sizes}
        if finite:
            qe, qt = quotient(ce, ct, E, reps)
            for w in words:
                old = run(edges, terminal, w); new = run(qe, qt, w)
                assert (old is None) == (new is None)
                assert old is None or old[2] == new[2]
                if new is not None:
                    matches = [i for i, r in enumerate(reps)
                               if E.accepts(convolution(w[::-1], r))]
                    assert matches == [new[0]]; successor_checks += 1
            delta = {(p, str(a)): item[0] for p, row in enumerate(qe)
                     for a, item in enumerate(row) if item is not None}
            outputs = {(p, str(a)): item[1] for p, row in enumerate(qe)
                       for a, item in enumerate(row) if item is not None}
            decision = Machine(len(qe), sigma, delta, outputs).decide()
            assert decision['member'] == expected_member, (name, decision)
            record['membership'] = decision['member']
            record['quotient_edges'] = qe
            record['quotient_terminal'] = qt
        else:
            record['membership'] = 'not run: exact infinite representative language'
        reports.append(record)
    # Held-out complete finite domains: direct sorted maximal runs give an
    # independent exact answer for EVERY pair and the entire representative
    # language. These data were not used to design the statement.
    finite_complete = []
    for case in range(20):
        n = 1 + case % 5
        k = 1 + case % 2
        sigma = ''.join(str(i) for i in range(k))
        edges = []
        for p in range(n):
            row = []
            for a in range(k):
                if p == n-1 or rng.randrange(4) == 0:
                    row.append(None)
                else:
                    row.append((rng.randrange(p+1, n), rng.choice(('', '0', '1', '01', '10'))))
            edges.append(row)
        terminal = [rng.choice(('', '0', '1', '10')) for _ in range(n)]
        ce, ct, _, _ = onward(edges, terminal)
        E, Rep, sizes = component_relation(ce)
        reps = finite_language(Rep)
        assert reps is not None
        words = [''.join(w) for d in range(n) for w in product(sigma, repeat=d)]
        defined = sorted([w for w in words if run(ce, ct, w) is not None],
                         key=lambda w: w[::-1])
        groups = []; group_of = {}
        last = None
        for w in defined:
            c = run(ce, ct, w)[0]
            if c != last:
                groups.append([]); last = c
            groups[-1].append(w); group_of[w] = len(groups)-1
        exact_reps = sorted([min((w[::-1] for w in g), key=lambda r: (len(r), r))
                             for g in groups], key=lambda r: (len(r), r))
        assert reps == exact_reps
        for u, v in product(defined, repeat=2):
            assert E.accepts(convolution(u[::-1], v[::-1])) == (group_of[u] == group_of[v])
            relation_checks += 1
        qe, qt = quotient(ce, ct, E, reps)
        for w in words:
            old = run(edges, terminal, w); new = run(qe, qt, w)
            assert (old is None) == (new is None)
            assert old is None or old[2] == new[2]
            literal_checks += 1
        finite_complete.append({'case': case, 'original_states': n,
                                'domain_size': len(defined), 'components': len(reps), **sizes})
    # Deliberately OMIT canonical merging: redundant parity has infinite
    # components. This is an exact adverse control for the invalid shortcut.
    raw = [[(1, '')], [(0, '')]]
    raw_E, raw_Rep, raw_sizes = component_relation(raw)
    assert finite_language(raw_Rep) is None
    # Explicit projection whose only witness is longer than the free word.
    # u is empty, v is a nonempty unary word. Projection must accept empty u.
    alph = tuple(product(('0', PAD), repeat=2))
    witness = build(alph, (False, False, False),
        lambda q, col: (q[0] or col[0] != PAD,
                        q[1] or col[1] != PAD,
                        q[2] or col[1] == PAD and col[0] != PAD),
        lambda q: not q[0] and q[1] and not q[2])
    projected = project(witness, 1)
    assert projected.accepts([])
    report = {'job_id': 'c017-wheeler-research-98a17f8eb2fd', 'status': 'passed',
              'controls': reports, 'held_out_complete_finite_domains': finite_complete,
              'whole_function_checks': literal_checks,
              'H_identity_checks': h_checks, 'automatic_relation_checks': relation_checks,
              'component_successor_checks': successor_checks,
              'unmerged_redundant_parity_infinite': True,
              'longer_existential_witness_for_empty_free_word': True,
              'limits': 'Exact finite automata decide representative finiteness and quotient transitions for the listed controls. Direct input checks stop at length 7. No general runtime bound, automatic proof certification, or fresh referee verdict is claimed.'}
    path = Path(__file__).with_name('research-2-realizability-check.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'controls': len(controls),
                      'whole_function_checks': literal_checks,
                      'automatic_relation_checks': relation_checks,
                      'component_successor_checks': successor_checks}))


if __name__ == '__main__':
    main()
