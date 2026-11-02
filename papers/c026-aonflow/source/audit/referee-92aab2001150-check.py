#!/usr/bin/env python3
"""Fresh exact checks. Does not execute or modify the frozen research verifier."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c026-aonflow-referee-92aab2001150'


def edge(u, v):
    return tuple(sorted((u, v)))


def edges(path):
    return frozenset(edge(a, b) for a, b in zip(path, path[1:]))


def reachable(graph_edges, start, removed):
    seen, todo = {start}, [start]
    while todo:
        u = todo.pop()
        for a, b in graph_edges:
            if (a, b) == removed:
                continue
            v = b if a == u else a if b == u else None
            if v is not None and v not in seen:
                seen.add(v)
                todo.append(v)
    return seen


def main():
    snap = json.loads((ROOT/'audit/snapshot.json').read_text())
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == h
               for p, h in snap['files'].items())
    assert hashlib.sha256(json.dumps(snap['files'], sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest() == snap['digest']
    pdf_checks = {}
    for name in ['2602.15015-expanders', 'CKS2005-welllinked', 'CKS2013-AON']:
        p = ROOT/'intake/primary'
        actual = subprocess.run(['pdftotext', '-layout', str(p/(name+'.pdf')), '-'],
                                capture_output=True, text=True, check=True).stdout
        listed = (p/(name+'.txt')).read_text()
        assert re.sub(r'\s+', '', actual) == re.sub(r'\s+', '', listed)
        pdf_checks[name] = True

    # Different fixture from the proposer: duplicate original pairs and shared
    # original endpoints, with unequal rational path amounts.
    raw = [[((0, 1, 2), F(1, 5)), ((0, 3, 2), F(1, 10))],
           [((0, 3, 2), F(1, 5))],
           [((1, 3, 4), F(1, 4)), ((1, 0, 3, 4), F(1, 8))]]
    normalized = [[(edges((10+2*i,)+p+(11+2*i,)), m) for p, m in paths]
                  for i, paths in enumerate(raw)]
    all_edges = sorted(set().union(*(p for paths in normalized for p, _ in paths)))
    for e in all_edges:
        assert sum((m for paths in normalized for p, m in paths if e in p), F()) <= 1
    T, eps = 2, F(1, 8)
    options = []
    for paths in normalized:
        assert sum((m for _, m in paths), F()) < F(1, T)
        opts = [(p, T*m) for p, m in paths]
        opts.append((frozenset(), 1-sum((w for _, w in opts), F())))
        options.append(opts)
    mean_k, probabilities, outcomes, cut_checks = F(), F(), 0, 0
    mean_loads = dict.fromkeys(all_edges, F())
    cut_sets = [frozenset(c) for n in range(3) for c in combinations(all_edges, n)]
    for outcome in product(*options):
        probability = F(1)
        for _, w in outcome:
            probability *= w
        chosen = [p for p, _ in outcome if p]
        probabilities += probability
        mean_k += probability*len(chosen)
        loads = {e: eps*sum(e in p for p in chosen) for e in all_edges}
        assert all(x <= 1 for x in loads.values())
        for e, x in loads.items():
            mean_loads[e] += probability*x/eps
        for cut in cut_sets:
            hit = sum(bool(p & cut) for p in chosen)
            assert eps*hit <= sum((loads[e] for e in cut), F()) <= len(cut)
            cut_checks += 1
        outcomes += 1
    assert probabilities == 1
    assert mean_k == T*sum((m for paths in normalized for _, m in paths), F())
    assert all(x <= T for x in mean_loads.values())

    # Check old occurrence cuts in an actual augmented graph by graph traversal,
    # rather than assuming that the arithmetic owner labels define cuts.
    base = set().union(*(edges(p) for paths in raw for p, _ in paths))
    graph = set(base)
    copies = []
    for i, paths in enumerate(raw):
        s, t = paths[0][0][0], paths[0][0][-1]
        old_s, old_t = 10+2*i, 11+2*i
        graph.update([edge(s, old_s), edge(t, old_t)])
        for j in range(3):
            cs, ct = 100+20*i+2*j, 101+20*i+2*j
            graph.update([edge(cs, old_s), edge(ct, old_t)])
            copies.append((i, cs, ct))
    cut_memberships = []
    for i, paths in enumerate(raw):
        old_edge = edge(paths[0][0][0], 10+2*i)
        side = reachable(graph, 10+2*i, old_edge)
        crossing = [j for j, a, b in copies if (a in side) != (b in side)]
        assert crossing == [i]*3
        cut_memberships.append(crossing)
    feasible_subsets = 0
    for admission in product([0, 1], repeat=len(copies)):
        loads = [sum(x for x, (owner, _, _) in zip(admission, copies) if owner == i)
                 for i in range(3)]
        if max(loads) <= 1:
            assert sum(admission) == len({owner for x, (owner, _, _) in zip(admission, copies) if x})
            feasible_subsets += 1

    # Nonvacuous cut budget: 64 disjoint prepared paths with epsilon=1/4.
    prepared = [frozenset({(2*i, 2*i+1)}) for i in range(64)]
    for count in range(5):
        cut = {next(iter(p)) for p in prepared[:count]}
        assert len(cut) <= F(1, 4)*len(prepared)/4
        hit = sum(bool(p & cut) for p in prepared)
        assert len(prepared)-hit >= F(3, 4)*len(prepared)

    # Product flow -> common distribution: ordered directions consume exactly
    # one half of each unordered product commodity, including self mass.
    product_checks = 0
    for q in [2, 4, 8, 32]:
        for alpha in [F(1), F(1, 2), F(1, 7)]:
            rho = alpha/4
            assert q*alpha/(4*q) == rho
            assert 2*alpha/(4*q) == (alpha/q)/2
            assert (q-1)*alpha/q <= alpha
            product_checks += 1
    for n in [16, 17, 128, 1000, 2**100]:
        b = (n-1).bit_length()
        assert 2**b <= 2*n
        t = 64*(2*n-1).bit_length()
        assert t <= 64*((b+1)+2)
    result = {'job_id': JOB, 'snapshot_digest': snap['digest'],
              'snapshot_integrity': True, 'pdf_text_matches': pdf_checks,
              'independent_sampling_outcomes': outcomes,
              'independent_cut_charge_checks': cut_checks,
              'graph_traversal_bridge_memberships': cut_memberships,
              'admission_subsets_checked': 2**len(copies),
              'bridge_feasible_subsets': feasible_subsets,
              'nonzero_cut_budget_cases': 4,
              'product_distribution_checks': product_checks,
              'all_checks_passed': True,
              'limitations': ['Finite exact diagnostics only; no BJS or CKS implementation.',
                             'The general theorem is assessed by proof and primary sources.']}
    out = ROOT/'audit/referee-92aab2001150-check-results.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
