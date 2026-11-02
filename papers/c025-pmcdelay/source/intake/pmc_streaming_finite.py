"""Finite correctness/charging test; NOT an implementation of the delay bound.

For tiny inputs minimal separators are deliberately enumerated by all subsets.
The theorem proposal instead requires the known polynomial-delay primitive.
No timing of this script supports a polynomial-delay asymptotic assertion.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from collections import Counter, deque
import datetime
import hashlib
import json
import random
import networkx as nx

from pmc_atom_neighborhood import bits, neighborhood, components, is_pmc, neighbors

ROOT = Path(__file__).resolve().parent


def nxgraph(adj):
    g = nx.Graph()
    g.add_nodes_from(range(len(adj)))
    g.add_edges_from((u, v) for u in range(len(adj)) for v in bits(adj[u]) if u < v)
    return g


def adjacency(g):
    nodes = sorted(g.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    adj = [0] * len(nodes)
    for u, v in g.edges():
        adj[idx[u]] |= 1 << idx[v]
        adj[idx[v]] |= 1 << idx[u]
    return tuple(adj)


def separators(adj):
    allv = (1 << len(adj)) - 1
    for s in range(allv):
        full = [c for c in components(adj, allv ^ s) if neighborhood(adj, c) == s]
        if len(full) >= 2:
            yield s, full


def extension(adj, sep, full):
    """Construct the proposed helper by saturating sep inside every block."""
    n = len(adj)
    allv = (1 << n) - 1
    g = nxgraph(adj)
    saturated_union = nx.Graph()
    saturated_union.add_nodes_from(range(n))
    block_selected = None
    for c in components(adj, allv ^ sep):
        block = g.subgraph(list(bits(c | sep))).copy()
        block.add_edges_from(combinations(list(bits(sep)), 2))
        tri, _ = nx.complete_to_chordal_graph(block)
        assert nx.is_chordal(tri)
        saturated_union.add_edges_from(tri.edges())
        if c == full[0]:
            block_selected = tri
    assert nx.is_chordal(saturated_union)
    cliques = sorted((sum(1 << v for v in s) for s in nx.chordal_graph_cliques(block_selected)))
    gamma = next(s for s in cliques if s != sep and (s & sep) == sep)
    assert is_pmc(adj, gamma)
    outside = components(adj, allv ^ gamma)
    witnesses = [c for c in outside if neighborhood(adj, c) == sep]
    assert full[1] in witnesses
    return gamma, full[1], sorted(tuple(sorted(e)) for e in saturated_union.edges())


@lru_cache(None)
def generate(adj):
    n = len(adj)
    allv = (1 << n) - 1
    expected = frozenset(s for s in range(1, 1 << n) if is_pmc(adj, s))
    if all(adj[v] == (allv ^ (1 << v)) for v in range(n)):
        assert expected == {allv}
        return {'outputs': (allv,), 'phase_counts': [1, 0, 0], 'helpers': (),
                'child_count': 0, 'max_helper_fiber': 0, 'processed_queue': 0,
                'all_prefix_counts_valid': True}
    a = next(v for v in reversed(range(n)) if len(components(adj, allv ^ (1 << v))) == 1)
    remaining = [v for v in range(n) if v != a]
    child = tuple(sum(1 << j for j, w in enumerate(remaining) if adj[v] >> w & 1)
                  for v in remaining)
    child_result = generate(child)
    out = []
    known = set()
    phase_counts = [0, 0, 0]

    def emit(s, phase):
        if s not in known:
            assert s in expected
            known.add(s)
            out.append(s)
            phase_counts[phase] += 1

    child_lifts = []
    for number, x in enumerate(child_result['outputs'], 1):
        lifted = sum(1 << remaining[j] for j in bits(x))
        valid = [s for s in [lifted, lifted | (1 << a)] if is_pmc(adj, s)]
        assert valid
        assert all((s & ~(1 << a)) == lifted for s in valid)
        for s in valid:
            emit(s, 0)
        assert len(out) >= number
        child_lifts.append((x, tuple(valid)))
    helpers = []
    fibers = Counter()
    # All-subsets discovery is a finite oracle replacement, not the proposed
    # polynomial-delay separator implementation.
    for r, (s, full) in enumerate(separators(adj), 1):
        gamma, outside, tri_edges = extension(adj, s, full)
        emit(gamma, 1)
        fibers[gamma] += 1
        assert fibers[gamma] <= n
        helpers.append((s, gamma, outside))
        assert r <= n * len(out)
        candidate = s | (1 << a)
        if is_pmc(adj, candidate):
            emit(candidate, 1)
    required_seed = set(known)
    queue = deque(out)
    popped = set()
    while queue:
        s = queue.popleft()
        assert s not in popped
        popped.add(s)
        assert len(popped) <= len(out)
        ns, _ = neighbors(adj, s, expected)
        for t in sorted(ns):
            if t not in known:
                emit(t, 2)
                queue.append(t)
    assert known == expected, {'adj': adj, 'a': a, 'missing': sorted(expected - known)}
    assert len(out) == len(set(out))
    return {'outputs': tuple(out), 'phase_counts': phase_counts, 'helpers': tuple(helpers),
            'child_count': len(child_result['outputs']), 'max_helper_fiber': max(fibers.values(), default=0),
            'processed_queue': len(popped), 'all_prefix_counts_valid': True,
            'recursive_lift_projection_injective': True, 'source_closure_complete': True}


def direct_triangulations(adj):
    """Independent literal-definition check on n<=5: all chordal supergraphs."""
    g = nxgraph(adj)
    nonedges = sorted(nx.non_edges(g))
    minimal = []
    found = set()
    for mask in sorted(range(1 << len(nonedges)), key=lambda x: (x.bit_count(), x)):
        if any((prev & mask) == prev for prev in minimal):
            continue
        h = g.copy()
        h.add_edges_from(nonedges[i] for i in bits(mask))
        if nx.is_chordal(h):
            minimal.append(mask)
            found.update(sum(1 << v for v in c) for c in nx.chordal_graph_cliques(h))
    return found, len(minimal)


def run():
    records = []
    digest = hashlib.sha256()
    direct_count = 0
    direct_triangulation_count = 0
    cases = []
    for index, g in enumerate(nx.graph_atlas_g()):
        if len(g) and nx.is_connected(g):
            cases.append((f'atlas-{index}', g))
    rng = random.Random(20261101)
    # Held-out here only with respect to the preceding <=7 atom screen;
    # these are not a fresh-context independence claim.
    for n in [8, 9]:
        for trial in range(30):
            p = [0.22, 0.5, 0.78][trial % 3]
            g = nx.gnp_random_graph(n, p, seed=rng.randrange(1 << 32))
            if nx.is_connected(g):
                cases.append((f'random-{n}-{trial}', g))
    for label, g in cases:
        adj = adjacency(g)
        result = generate(adj)
        n = len(adj)
        if n <= 5:
            direct, count = direct_triangulations(adj)
            assert direct == set(result['outputs'])
            direct_count += 1
            direct_triangulation_count += count
        item = {'input': label, 'n': n, 'edges': sorted(tuple(sorted(e)) for e in g.edges()),
                'output_count': len(result['outputs']), 'outputs': result['outputs'],
                'phase_counts': result['phase_counts'], 'helper_count': len(result['helpers']),
                'helper_pairs': result['helpers'], 'max_helper_fiber': result['max_helper_fiber'],
                'queue_count': result['processed_queue'], 'all_count_invariants_checked': True}
        digest.update(json.dumps(item, sort_keys=True, separators=(',', ':')).encode())
        records.append(item)
    packet = {'created_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'original_status': 'unresolved', 'candidate_kind': 'none',
              'root_proposal_finite_verification_only': True,
              'scope': 'Full output correctness and helper/lift/queue counting for specified finite inputs; no asymptotic timing claim.',
              'separator_oracle': 'Brute-force all subsets, deliberately NOT a polynomial-delay implementation.',
              'triangulation_primitive': 'Installed NetworkX MCS-M; direct all-supergraph audit only for n<=5.',
              'networkx_version': nx.__version__, 'case_count': len(records),
              'atlas_connected_instances': sum(x['input'].startswith('atlas') for x in records),
              'additional_held_out_random_instances': sum(x['input'].startswith('random') for x in records),
              'literal_definition_graphs': direct_count,
              'literal_minimal_triangulations': direct_triangulation_count,
              'records_digest': digest.hexdigest(), 'records': records}
    dest = ROOT / 'pmc-streaming-finite.json'
    dest.write_text(json.dumps(packet, indent=2) + '\n')
    print(json.dumps({k: packet[k] for k in ['case_count', 'atlas_connected_instances',
        'additional_held_out_random_instances', 'literal_definition_graphs', 'literal_minimal_triangulations', 'records_digest']}))
    print(json.dumps({'packet_sha256': hashlib.sha256(dest.read_bytes()).hexdigest(),
                      'file': str(dest)}))


if __name__ == '__main__':
    run()
