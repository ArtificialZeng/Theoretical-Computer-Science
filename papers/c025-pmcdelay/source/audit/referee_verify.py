"""Fresh bounded verifier; standard library only, no owner-code imports.

Literal all-supergraph triangulations are a finite oracle, never part of the
proposed polynomial-time algorithm. Running this file writes only its own
referee result, not frozen inputs. No finite success proves the theorem.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import datetime
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c025-pmcdelay-referee-6970e98c3a2b'
START = time.monotonic()
DEADLINE = START + 150


def check_time():
    if time.monotonic() > DEADLINE:
        raise TimeoutError('Finite verifier ceiling reached; not a mathematical failure')


@lru_cache(None)
def edges_for(n):
    return tuple(combinations(range(n), 2))


@lru_cache(None)
def graph(n, mask):
    adj = [set() for _ in range(n)]
    for i, (v, w) in enumerate(edges_for(n)):
        if mask >> i & 1:
            adj[v].add(w)
            adj[w].add(v)
    return tuple(frozenset(a) for a in adj)


def edge_mask(n, edges):
    es = {tuple(sorted(e)) for e in edges}
    return sum(1 << i for i, e in enumerate(edges_for(n)) if e in es)


def comps(adj, allowed):
    left, result = set(allowed), []
    while left:
        seed = min(left)
        todo, found = [seed], {seed}
        left.remove(seed)
        while todo:
            v = todo.pop()
            new = adj[v] & left
            left.difference_update(new)
            found.update(new)
            todo.extend(new)
        result.append(frozenset(found))
    return result


def hood(adj, vs):
    out = set()
    for v in vs:
        out.update(adj[v])
    return frozenset(out.difference(vs))


def component(adj, v, allowed):
    assert v in allowed
    return next(c for c in comps(adj, allowed) if v in c)


def subsets(vertices, nonempty=False):
    vv = tuple(sorted(vertices))
    for mask in range(int(nonempty), 1 << len(vv)):
        yield frozenset(v for i, v in enumerate(vv) if mask >> i & 1)


def criterion(adj, omega):
    if not omega:
        return False
    boundaries = [hood(adj, c) for c in comps(adj, set(range(len(adj))) - omega)]
    if omega in boundaries:
        return False
    return all(w in adj[v] or any({v, w} <= b for b in boundaries)
               for v, w in combinations(omega, 2))


@lru_cache(None)
def chordal(n, mask):
    # Repeated simplicial deletion is a separate chordality implementation.
    adj = graph(n, mask)
    left = set(range(n))
    while left:
        simplicial = next((v for v in sorted(left)
                           if all(w in adj[u] for u, w in combinations(adj[v] & left, 2))), None)
        if simplicial is None:
            return False
        left.remove(simplicial)
    return True


@lru_cache(None)
def maximal_cliques(n, mask):
    adj = graph(n, mask)
    cliques = [x for x in subsets(range(n), True)
               if all(w in adj[v] for v, w in combinations(x, 2))]
    return frozenset(x for x in cliques if not any(x < y for y in cliques))


@lru_cache(None)
def minimal_completions(n, base):
    candidates = [h for h in range(1 << len(edges_for(n)))
                  if h & base == base and chordal(n, h)]
    minimal = []
    for h in sorted(candidates, key=lambda h: (h.bit_count(), h)):
        if not any(prev & h == prev for prev in minimal):
            minimal.append(h)
    return tuple(minimal)


@lru_cache(None)
def literal_pmcs(n, mask):
    return frozenset(x for h in minimal_completions(n, mask)
                     for x in maximal_cliques(n, h))


def safe_arcs(adj, w, pmcs):
    allv = set(range(len(adj)))
    out = []
    for u in sorted(w):
        x = w | adj[u]
        for b in sorted(w - {u}):
            aa = component(adj, b, allv - (x - {b}))
            na = hood(adj, aa)
            if u in aa | na:
                continue
            uu = component(adj, u, allv - na)
            ss = hood(adj, uu)
            assert u not in ss and b not in ss
            bb = component(adj, b, allv - ss)
            assert u not in bb
            z = x & (ss | bb)
            if z in pmcs:
                out.append((z, u, b, x, ss))
    return out


def connected_checks(n, mask, pmcs, stats):
    adj = graph(n, mask)
    allv = set(range(n))
    if mask == (1 << len(edges_for(n))) - 1:
        assert pmcs == {frozenset(allv)}
        stats['complete_base_cases'] += 1
        return
    separators = [s for s in subsets(allv)
                  if sum(hood(adj, c) == s for c in comps(adj, allv - s)) >= 2]
    fibers = Counter()
    for s in separators:
        cc = comps(adj, allv - s)
        full = [c for c in cc if hood(adj, c) == s]
        selected = full[0]
        union_edges = set()
        selected_cliques = None
        for c in cc:
            vv = sorted(s | c)
            local_edges = [(i, j) for i, v in enumerate(vv) for j, w in enumerate(vv)
                           if i < j and (w in adj[v] or {v, w} <= s)]
            hh = minimal_completions(len(vv), edge_mask(len(vv), local_edges))[0]
            for i, (v, w) in enumerate(edges_for(len(vv))):
                if hh >> i & 1:
                    union_edges.add(tuple(sorted((vv[v], vv[w]))))
            if c == selected:
                selected_cliques = [frozenset(vv[i] for i in z)
                                    for z in maximal_cliques(len(vv), hh)]
        union_mask = edge_mask(n, union_edges)
        assert union_mask in minimal_completions(n, mask), ('gluing', n, mask, sorted(s))
        gamma = min((z for z in selected_cliques if s < z), key=lambda z: tuple(sorted(z)))
        assert gamma in pmcs
        assert full[1] in comps(adj, allv - gamma) and hood(adj, full[1]) == s
        fibers[gamma] += 1
        assert fibers[gamma] <= n
        stats['literal_separator_helpers'] += 1
    arcs = {w: safe_arcs(adj, w, pmcs) for w in pmcs}
    for a in range(n):
        # Includes cut vertices: this is a stronger finite structural test.
        child_adj = tuple(vs - {a} if v != a else frozenset() for v, vs in enumerate(adj))
        child_pmcs = {x for x in subsets(allv - {a}, True) if criterion(child_adj, x)}
        seeds = set()
        for x in child_pmcs:
            lifts = [z for z in (x, x | {a}) if z in pmcs]
            assert lifts, ('lift', n, mask, a, sorted(x))
            seeds.update(lifts)
        seeds.update(s | {a} for s in separators if s | {a} in pmcs)
        assert {w for w in pmcs if a in w} <= seeds
        seen, todo = set(seeds), list(seeds)
        while todo:
            w = todo.pop()
            for z, *_ in arcs[w]:
                if z not in seen:
                    seen.add(z)
                    todo.append(z)
        assert seen == set(pmcs), ('reachability', n, mask, a)
        stats['seed_closures'] += 1
        for omega in pmcs - seeds:
            ca = component(adj, a, allv - omega)
            ss = hood(adj, ca)
            tt = omega - ss
            witnesses = []
            for w, aa in arcs.items():
                smaller = a in w or component(adj, a, allv - w) < ca
                if smaller:
                    witnesses.extend((w, u, b) for z, u, b, x, s in aa
                                     if z == omega and u in ca and b in tt
                                     and omega <= x <= omega | ca and s == ss)
            assert witnesses, ('strong_preimage', n, mask, a, sorted(omega))
            stats['strong_preimages'] += 1


def run():
    stats = Counter()
    digest = hashlib.sha256()
    for n in range(6):
        for mask in range(1 << len(edges_for(n))):
            check_time()
            adj = graph(n, mask)
            exact = literal_pmcs(n, mask)
            recognized = frozenset(x for x in subsets(range(n), True) if criterion(adj, x))
            assert exact == recognized, ('literal_vs_criterion', n, mask)
            stats['literal_graphs'] += 1
            stats['literal_minimal_completions'] += len(minimal_completions(n, mask))
            digest.update(json.dumps([n, mask, sorted([sorted(x) for x in exact])], separators=(',', ':')).encode())
            if n and len(comps(adj, set(range(n)))) == 1:
                stats['connected_graphs'] += 1
                connected_checks(n, mask, exact, stats)
    packet = json.loads((ROOT / 'evidence/pass1-targeted-streaming.json').read_text())
    for row in packet['records']:
        check_time()
        n = row['n']
        adj = graph(n, edge_mask(n, row['edges']))
        expected = {x for x in subsets(range(n), True) if criterion(adj, x)}
        actual = [frozenset(v for v in range(n) if z >> v & 1) for z in row['outputs']]
        assert len(actual) == len(set(actual)) and set(actual) == expected, row['label']
        stats['serialized_cases_checked'] += 1
    return {'job_id': JOB, 'snapshot_digest': json.loads((ROOT/'audit/snapshot.json').read_text())['digest'],
            'at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status': 'passed', 'statistics': dict(stats), 'literal_outputs_digest': digest.hexdigest(),
            'elapsed_seconds': time.monotonic() - START,
            'scope': 'All labelled simple graphs on 0..5 vertices: literal inclusion-minimal chordal completions versus fresh PMC criterion. Connected cases: literal helper gluing, outside witness/fiber, all-vertex lifts, seed closure, and strong endpoint-safe source-preimage witnesses. The frozen 29 serialized output sets are independently checked with the fresh global criterion.',
            'limits': 'Finite exact tests only; neither an asymptotic proof nor a priority certificate. Literal exponential oracles are confined to this verifier. No frozen file is changed.'}


if __name__ == '__main__':
    try:
        result = run()
    except Exception as exc:
        result = {'job_id': JOB, 'status': 'operational_limit' if isinstance(exc, TimeoutError) else 'check_failure',
                  'exception_type': type(exc).__name__, 'detail': str(exc), 'elapsed_seconds': time.monotonic()-START}
    path = ROOT / 'audit/referee-verification.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
    if result['status'] != 'passed':
        raise SystemExit(1)
