"""Independent finite checks; no claim to replace the mathematical proofs."""
import itertools
import json
import random
import platform
import sys
from trace_support import record, close
from pathlib import Path
from treeflow import (BagReference, Circuit, bfs_graph, closure, compose,
                      identity, matrix_product, stack_gadget, union)


def lower_bound_checks():
    cases = graph_checks = fact_checks = stack_checks = selector_transitions = 0
    for k in (1, 2, 3):
        for bits in range(1 << (k*k)):
            matrix = tuple((bits >> (i*k)) & ((1 << k)-1) for i in range(k))
            for vector in range(1 << k):
                expected = matrix_product(matrix, vector, k)
                vertices = ['s'] + [('c', j) for j in range(k)] + [('r', i) for i in range(k)]
                edges = [('s', ('c', j)) for j in range(k) if vector & (1 << j)]
                edges += [(('c', j), ('r', i)) for i in range(k) for j in range(k)
                          if matrix[i] & (1 << j)]
                reachable = bfs_graph(vertices, edges, 's')
                assert tuple(('r', i) in reachable for i in range(k)) == expected
                graph_checks += k
                d = 2*k+2  # zero=0, sigma=1, columns=2.., rows=2+k..
                selector = tuple([1, vector << 2] + [0] * (d-2))
                relation = [1]+[0]*(d-1)
                for j in range(k):
                    relation[2+j] = sum(1 << (2+k+i) for i in range(k)
                                        if matrix[i] & (1 << j))
                product = compose(selector, tuple(relation))
                # Independently explode the three-point CFG and perform BFS.
                facts = [(v, a) for v in range(3) for a in range(d)]
                exploded = [((v, a), (v+1, b)) for v, rel in enumerate((selector, relation))
                            for a in range(d) for b in range(d) if rel[a] & (1 << b)]
                reached = bfs_graph(facts, exploded, (0, 1))
                assert tuple(bool(product[1] & (1 << (2+k+i))) for i in range(k)) == expected
                assert tuple((2, 2+k+i) in reached for i in range(k)) == expected
                fact_checks += k
                for i in range(k):
                    actual_stack = stack_gadget(matrix, vector, i, k)
                    assert actual_stack == expected[i]
                    record('lower_row', k=k, matrix_bits=bits, vector=vector, row=i,
                           expected=expected[i], control=(('r',i) in reachable),
                           fact=((2,2+k+i) in reached), stack=actual_stack)
                    stack_checks += 1
                for j in range(k):
                    changed = vector ^ (1 << j)
                    delta = -1 if vector & (1 << j) else 1
                    counts = [bin(matrix[i] & vector).count('1') for i in range(k)]
                    for i in range(k):
                        counts[i] += delta * bool(matrix[i] & (1 << j))
                    assert tuple(x > 0 for x in counts) == matrix_product(matrix, changed, k)
                    record('selector', k=k, matrix_bits=bits, vector=vector,
                           bit=j, counts=counts, expected=matrix_product(matrix, changed, k))
                    selector_transitions += 1
                cases += 1
    return dict(matrix_vector_cases=cases, graph_answers=graph_checks,
                fact_answers=fact_checks, stack_answers=stack_checks,
                selector_bit_transitions=selector_transitions)


def legal_relation(d, rng):
    if rng.randrange(5) == 0:
        return (0,)*d  # deactivate the complete edge
    return tuple([rng.randrange(1 << d)|1] +
                 [rng.randrange(1 << d)&~1 for _ in range(d-1)])


def bag_checks(seed=20261031):
    rng = random.Random(seed)
    # Triangle chain with a balanced, branching width-two decomposition.
    bags = [(2,3,4), (1,2,3), (3,4,5), (0,1,2), (4,5,6)]
    children = [[1,2], [3], [4], [], []]
    universe = sorted({(u,v) for bag in bags for u in bag for v in bag})
    owners = {e: next(i for i,b in enumerate(bags) if set(e) <= set(b)) for e in universe}
    counts = dict(edits=0, pair_answers=0, circuit_edits=0, circuit_outputs=0)
    for d in (1, 2, 3):
        edges = {e: legal_relation(d, rng) for e in universe}
        record('bag_init', d=d, bags=bags, children=children,
               edges=[[u,v,list(rel)] for (u,v),rel in edges.items()])
        reference = BagReference(bags, children, edges, owners, d)
        for edit in range(36):
            e = rng.choice(universe)
            changed_bags = reference.update(e, legal_relation(d, rng))
            assert changed_bags <= 3
            record('bag_edit', d=d, edit=edit, edge=e,
                   relation=reference.edges[e], changed_bags=changed_bags)
            exploded = [((u,a),(v,b)) for (u,v),rel in reference.edges.items()
                        for a in range(d) for b in range(d) if rel[a] & (1 << b)]
            vertices = [(u,a) for u in range(7) for a in range(d)]
            for u in range(7):
                for a in range(d):
                    reached = bfs_graph(vertices, exploded, (u,a))
                    for v in range(7):
                        rel, ix = reference.evaluate(pin=(u,v))
                        assert reference.last_recomputed <= 5
                        for b in range(d):
                            actual = bool(rel[ix[u,a]] & (1 << ix[v,b]))
                            assert actual == ((v,b) in reached)
                            record('bag_answer', d=d, edit=edit, source=[u,a], target=[v,b],
                                   expected=((v,b) in reached), actual=actual,
                                   recomputed_bags=reference.last_recomputed)
                            counts['pair_answers'] += 1
            counts['edits'] += 1
    # Shared acyclic relation circuit; both insertions and deletions are present.
    for d in (1,2,4):
        c = Circuit()
        leaves = [c.add(value=tuple(rng.randrange(1 << d) for _ in range(d))) for _ in range(8)]
        for i in range(32):
            ins = rng.sample(range(len(c.nodes)), 2)
            if i % 3 == 0:
                c.add(closure, (ins[0],))
            else:
                c.add(compose if i % 2 else union, ins)
        record('circuit_init', d=d, nodes=[{'op':op.__name__ if op else None,
               'inputs':ins, 'value':c.values[i]} for i,(op,ins) in enumerate(c.nodes)])
        for edit in range(100):
            leaf = rng.choice(leaves)
            value = tuple(rng.randrange(1 << d) for _ in range(d))
            affected = c.update(leaf, value)
            record('circuit_edit', d=d, edit=edit, leaf=leaf, value=value, affected=affected)
            fresh = []
            for op, ins in c.nodes:
                index = len(fresh)
                fresh.append(c.values[index] if op is None else op(*(fresh[j] for j in ins)))
            assert fresh == c.values
            for gate in range(8,len(c.nodes)):
                record('circuit_answer', d=d, edit=edit, gate=gate,
                       expected=fresh[gate], actual=c.values[gate])
            counts['circuit_edits'] += 1
            counts['circuit_outputs'] += len(c.nodes)-len(leaves)
    return counts


def recursive_checks():
    # A mutually recursive SCC. Removing its only base path must kill the cycle.
    results = []
    for case,base in enumerate((True, False, True)):
        a = b = False
        rounds = 0
        trace = []
        while True:
            na, nb = b, (base or a)
            rounds += 1
            trace.append([a,b,na,nb])
            if (na, nb) == (a,b):
                break
            a,b = na,nb
        assert (a,b) == (base,base)
        record('recursion', case=case, base=base, trace=trace, summary=[a,b], rounds=rounds)
        results.append({'base':base, 'summary_a':a, 'summary_b':b, 'rounds':rounds})
    return results


def sharing_checks():
    checks = []
    for diamonds in range(1,9):
        c = Circuit()
        ident = c.add(value=(1,))
        leaf = c.add(value=(0,))
        summary = leaf
        for _ in range(diamonds):
            left = c.add(compose,(c.add(compose,(ident,summary)),ident))
            right = c.add(compose,(c.add(compose,(ident,summary)),ident))
            to_left = c.add(compose,(c.add(compose,(ident,left)),ident))
            to_right = c.add(compose,(c.add(compose,(ident,right)),ident))
            summary = c.add(union,(to_left,to_right))
        for edit,value in enumerate((1,0,1)):
            affected = c.update(leaf,(value,))
            assert c.values[summary] == (value,)
            assert affected == 9*diamonds
            row = dict(diamonds=diamonds, edit=edit, value=value,
                       call_occurrences=4*diamonds, call_paths=2**diamonds,
                       affected=affected, expected=[value], actual=c.values[summary])
            record('sharing', **row)
            checks.append(row)
    return dict(edits=len(checks), maximum_affected=max(r['affected'] for r in checks))


if __name__ == '__main__':
    report = dict(revision='treeflow-v2', seed=20261031,
                  lower_bounds=lower_bound_checks(), treeflow=bag_checks(),
                  recursion=recursive_checks(), sharing=sharing_checks(),
                  scope='finite correctness checks, not repository performance measurements')
    report['record_counts'] = close()
    Path(__file__).with_name('runtime.json').write_text(json.dumps(dict(
        python=sys.version, implementation=platform.python_implementation(),
        platform=platform.platform(), command=' '.join([Path(sys.executable).name]+sys.argv)),indent=2)+'\n')
    Path(__file__).with_name('validation_results.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
