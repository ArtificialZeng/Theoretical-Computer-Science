"""Replay inputs and audit each record without importing the maintained solver."""
import json
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent

def rows(kind):
    items = [json.loads(s) for s in (HERE/'records'/f'{kind}.jsonl').read_text().splitlines()]
    for i,row in enumerate(items,1):
        assert row['id'] == f'{kind}:{i}' and row['kind'] == kind
    return items

def reach(adj, source):
    seen, todo = {source}, deque([source])
    while todo:
        for target in adj[todo.popleft()]:
            if target not in seen:
                seen.add(target); todo.append(target)
    return seen

def operation(name, args):
    d = len(args[0])
    if name == 'union':
        return [args[0][i] | args[1][i] for i in range(d)]
    if name == 'compose':
        return [sum(1 << j for j in range(d) if any(
            (args[0][i] >> k)&1 and (args[1][k] >> j)&1 for k in range(d))) for i in range(d)]
    assert name == 'closure'
    adj = [[j for j in range(d) if (args[0][i] >> j)&1] for i in range(d)]
    return [sum(1 << j for j in reach(adj,i)) for i in range(d)]

report, observed = {}, {}
low = rows('lower_row'); observed['lower_row']=len(low)
cases = set()
for r in low:
    k, bits, v, i = r['k'],r['matrix_bits'],r['vector'],r['row']
    expected = any((bits >> (i*k+j))&1 and (v>>j)&1 for j in range(k))
    assert all(r[key] == expected for key in ('expected','control','fact','stack'))
    cases.add((k,bits,v))
assert len(cases) == sum(2**(k*k+k) for k in (1,2,3))
for kind in ['selector']:
    items=rows(kind);observed[kind]=len(items)
    for r in items:
        k,bits=r['k'],r['matrix_bits']; v=r['vector']^(1<<r['bit'])
        counts=[sum((bits>>(i*k+j))&1 for j in range(k) if (v>>j)&1) for i in range(k)]
        assert r['counts'] == counts and r['expected'] == [x>0 for x in counts]

inits=rows('bag_init');edits=rows('bag_edit');answers=rows('bag_answer')
for name,items in [('bag_init',inits),('bag_edit',edits),('bag_answer',answers)]:observed[name]=len(items)
groups=defaultdict(list)
for row in answers:groups[row['d'],row['edit']].append(row)
states={r['d']:{(u,v):rel for u,v,rel in r['edges']} for r in inits}
for edit in edits:
    d=edit['d'];edges=states[d];edges[tuple(edit['edge'])]=edit['relation']
    for relation in edges.values():
        assert not any(relation) or (relation[0]&1 and all(not (r&1) for r in relation[1:]))
    adj={ (u,a):[] for u in range(7) for a in range(d)}
    for (u,v),rel in edges.items():
        for a,mask in enumerate(rel):
            adj[u,a].extend((v,b) for b in range(d) if (mask>>b)&1)
    reachable={s:reach(adj,s) for s in adj}
    batch=groups[d,edit['edit']]
    assert len(batch)==49*d*d
    assert len({(tuple(r['source']),tuple(r['target'])) for r in batch})==len(batch)
    for row in batch:
        expected=tuple(row['target']) in reachable[tuple(row['source'])]
        assert row['actual']==row['expected']==expected
        assert row['recomputed_bags']<=5

inits=rows('circuit_init');edits=rows('circuit_edit');answers=rows('circuit_answer')
for name,items in [('circuit_init',inits),('circuit_edit',edits),('circuit_answer',answers)]:observed[name]=len(items)
circuits={r['d']:r['nodes'] for r in inits}
values={d:[r['value'] for r in nodes] for d,nodes in circuits.items()}
groups=defaultdict(list)
for r in answers:groups[r['d'],r['edit']].append(r)
for edit in edits:
    d=edit['d'];nodes=circuits[d];current=values[d];current[edit['leaf']]=edit['value']
    seen={edit['leaf']}
    for gate,node in enumerate(nodes):
        if any(i in seen for i in node['inputs']):seen.add(gate)
        if node['op']:current[gate]=operation(node['op'],[current[i] for i in node['inputs']])
    assert len(seen)-1==edit['affected']
    batch=groups[d,edit['edit']]
    assert {r['gate'] for r in batch}==set(range(8,40))
    for r in batch:assert r['actual']==r['expected']==current[r['gate']]

items=rows('recursion');observed['recursion']=len(items)
for r in items:
    a=b=False;trace=[]
    while True:
        na,nb=b,(r['base'] or a);trace.append([a,b,na,nb])
        if (na,nb)==(a,b):break
        a,b=na,nb
    assert r['trace']==trace and r['summary']==[a,b] and r['rounds']==len(trace)
items=rows('sharing');observed['sharing']=len(items)
for r in items:
    n=r['diamonds'];assert r['call_occurrences']==4*n and r['call_paths']==2**n
    assert r['affected']==9*n and r['expected']==r['actual']==[r['value']]

original=json.loads((HERE/'validation_results.json').read_text())
assert observed==original['record_counts']
assert len(low)==original['lower_bounds']['graph_answers']==12420
assert observed['bag_edit']==original['treeflow']['edits']==108
assert observed['bag_answer']==original['treeflow']['pair_answers']==24696
assert observed['circuit_edit']==original['treeflow']['circuit_edits']==300
assert observed['circuit_answer']==original['treeflow']['circuit_outputs']==9600
assert observed['sharing']==original['sharing']['edits']==24
report={'revision':'treeflow-v2','all_record_ids_unique_and_sequential':True,
        'matrix_vector_instances':len(cases),'replayed_record_counts':observed,
        'status':'all checks passed','method':'reconstructed graph BFS, direct Boolean evaluation, independent circuit operations'}
(HERE/'record_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
