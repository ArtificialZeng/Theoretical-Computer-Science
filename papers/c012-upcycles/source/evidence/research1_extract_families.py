"""Extract and literally recheck every component of the saved Euler models."""
import json
from pathlib import Path
from research1_verify import verify


def extract(label):
    base=Path('evidence/research1-euler')
    meta=json.loads((base/(label+'.encoding.json')).read_text())
    model=json.loads((base/(label+'.model-verification.json')).read_text())
    selected=model['selected_indices']
    aggregate=[0]*2**meta['n']
    cycles=[]
    for component in model['components']:
        vertices=set(component)
        edges=[e for e in selected if meta['tiles'][e-1][:-1] in vertices]
        adj={}
        for e in edges:
            adj.setdefault(meta['tiles'][e-1][:-1],[]).append(e)
        stack=[(min(vertices),None)]
        reverse=[]
        while stack:
            v,e=stack[-1]
            if adj.get(v):
                nxt=adj[v].pop()
                stack.append((meta['tiles'][nxt-1][1:],nxt))
            else:
                stack.pop()
                if e is not None:
                    reverse.append(e)
        tour=reverse[::-1]
        assert len(tour)==len(edges) and set(tour)==set(edges)
        word=''.join(meta['tiles'][e-1][0] for e in tour)
        for i,e in enumerate(tour):
            assert ''.join(word[(i+k)%len(word)] for k in range(meta['n']))==meta['tiles'][e-1]
        literal=verify(word,meta['n'])
        assert literal['diamondicities']==[meta['d']]
        assert literal['diamond_periodic']
        assert max(literal['coverage_counts'])==1
        for i,c in enumerate(literal['coverage_counts']):
            aggregate[i]+=c
        cycles.append(dict(word=word,length=len(word),n=meta['n'],d=meta['d'],
                           covered_words=sum(literal['coverage_counts']),
                           no_internal_repeat=True,edge_tour=tour))
    assert sum(c['length'] for c in cycles)==meta['length']
    assert all(c==1 for c in aggregate)
    out=dict(classification='verified universal partial quasi-family; not a single upcycle',
             n=meta['n'],d=meta['d'],cycles=cycles,coverage_counts=aggregate,
             original_question_resolved=False)
    path=base/(label+'.family-verification.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    return dict(path=str(path),cycles=len(cycles),lengths=[c['length'] for c in cycles])


if __name__=='__main__':
    for label in ['n8d2_xoooxooo','n12d3_period4']:
        print(json.dumps(extract(label)))
