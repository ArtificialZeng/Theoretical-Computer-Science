"""Exact bounded diagnostic for a positive all-PMC enumeration program.

The target remains a full polynomial-delay algorithm on every finite graph.
This tests only the Definition20 neighborhood and a clique-separator repair.
No queue job, admission, proof audit or manuscript is implied.
"""
from pathlib import Path
from itertools import combinations
import json
import hashlib
import datetime
import networkx as nx

ROOT = Path(__file__).resolve().parent


def bits(x):
    while x:
        t = x & -x
        yield t.bit_length() - 1
        x ^= t


def neighborhood(adj, s):
    ans = 0
    for v in bits(s):
        ans |= adj[v]
    return ans & ~s


def components(adj, s):
    ans = []
    while s:
        todo = s & -s
        c = 0
        while todo:
            c |= todo
            s &= ~todo
            todo = neighborhood(adj, todo) & s
        ans.append(c)
    return ans


def component(adj, v, allowed):
    assert (allowed >> v) & 1
    seen = 1 << v
    todo = seen
    while todo:
        todo = neighborhood(adj, todo) & allowed & ~seen
        seen |= todo
    return seen


def is_pmc(adj, omega):
    if not omega:
        return False
    allv = (1 << len(adj)) - 1
    reach = list(adj)
    for c in components(adj, allv ^ omega):
        nc = neighborhood(adj, c)
        if nc == omega:
            return False
        for v in bits(nc):
            reach[v] |= nc
    return all((omega & ~(reach[v] | (1 << v))) == 0 for v in bits(omega))


def neighbors(adj, omega, pmcs):
    r"""Literal source recipe where the X-close separator is defined.

    For b,u in omega, u!=b and nonadjacent: A is the b-component
    after deleting X\{b}; require u outside N[A]. S=N(C_u(G-N(A))).
    Keep X intersect (S union C_b(G-S)), and check the global PMC criterion.
    """
    allv = (1 << len(adj)) - 1
    ans = set()
    witness = {}
    for u in bits(omega):
        x = omega | adj[u]
        for b in bits(omega & ~((1 << u) | adj[u])):
            a = component(adj, b, allv & ~(x & ~(1 << b)))
            na = neighborhood(adj, a)
            if ((a | na) >> u) & 1:
                continue
            cu = component(adj, u, allv & ~na)
            sep = neighborhood(adj, cu)
            assert sep & ((1 << b) | (1 << u)) == 0
            cb = component(adj, b, allv & ~sep)
            assert not (cb >> u) & 1
            target = x & (sep | cb)
            if target in pmcs:
                ans.add(target)
                witness[target] = {'u': u, 'b': b, 'X': x, 'A': a, 'S': sep}
    return ans, witness


def clique_separators(adj):
    n = len(adj)
    allv = (1 << n) - 1
    found = []
    for s in range(1, allv):
        if all((s & ~(adj[v] | (1 << v))) == 0 for v in bits(s)):
            if len(components(adj, allv ^ s)) >= 2:
                found.append(s)
    return found


def run():
    summaries = {}
    all_failures = []
    atom_failures = []
    atom_records = []
    input_digest = hashlib.sha256()
    atlas = nx.graph_atlas_g()
    for index, graph in enumerate(atlas):
        n = len(graph)
        if n == 0 or not nx.is_connected(graph):
            continue
        adj = [0] * n
        edges = sorted(tuple(sorted(e)) for e in graph.edges())
        input_digest.update(json.dumps([index, n, edges], separators=(',', ':')).encode())
        for u, v in edges:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        pmcs = set(s for s in range(1, 1 << n) if is_pmc(adj, s))
        arcs = {}
        witnesses = {}
        for s in pmcs:
            arcs[s], witnesses[s] = neighbors(adj, s, pmcs)
        dg = nx.DiGraph()
        dg.add_nodes_from(pmcs)
        dg.add_edges_from((s, t) for s, ts in arcs.items() for t in ts)
        scc = sorted([sorted(c) for c in nx.strongly_connected_components(dg)])
        seps = clique_separators(adj)
        atom = not seps
        row = summaries.setdefault(str(n), {'connected_instances': 0, 'atom_instances': 0,
            'all_scc_failures': 0, 'atom_scc_failures': 0, 'pmcs': 0, 'arcs': 0})
        row['connected_instances'] += 1
        row['atom_instances'] += int(atom)
        row['pmcs'] += len(pmcs)
        row['arcs'] += sum(map(len, arcs.values()))
        if len(scc) != 1:
            row['all_scc_failures'] += 1
            record = {'atlas_index': index, 'n': n, 'edges': edges, 'PMCs': sorted(pmcs),
                'clique_separators': seps, 'SCCs': scc,
                'arcs': {str(s): sorted(ts) for s, ts in arcs.items()},
                'arc_separator_witnesses': {str(s): {str(t): w for t, w in ws.items()}
                    for s, ws in witnesses.items()}}
            all_failures.append(record)
            if atom:
                row['atom_scc_failures'] += 1
                atom_failures.append(record)
        if atom:
            atom_records.append({'atlas_index': index, 'n': n, 'edges': edges,
                'PMC_count': len(pmcs), 'SCC_count': len(scc)})
    out = {'created_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'original_status': 'unresolved', 'candidate_kind': 'none',
        'hypothesis_tested': 'Definition20 PMC digraph is strongly connected on connected graphs with no clique separator.',
        'source': '2610.19850v3 Definition20 p29, PDF visually inspected; proper close-separator endpoint conditions retained.',
        'input_domain': 'All connected nonempty instances in the installed NetworkX graph_atlas_g dataset; no independently verified isomorphism completeness claim.',
        'networkx_version': nx.__version__, 'library_atlas_count': len(atlas),
        'connected_input_sha256': input_digest.hexdigest(), 'summary_by_n': summaries,
        'first_general_failure': all_failures[0] if all_failures else None,
        'atom_failure_count': len(atom_failures), 'atom_failures': atom_failures,
        'all_atom_instance_records': atom_records,
        'limits': 'Finite diagnostic only; neither an infinite connectivity proof nor a full polynomial-delay algorithm. A method obstruction is not the original question.'}
    dest = ROOT / 'pmc-atom-neighborhood.json'
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'summary_by_n': summaries, 'first_general_failure': out['first_general_failure'],
        'atom_failure_count': len(atom_failures), 'first_atom_failure': atom_failures[0] if atom_failures else None,
        'packet_sha256': hashlib.sha256(dest.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    run()
