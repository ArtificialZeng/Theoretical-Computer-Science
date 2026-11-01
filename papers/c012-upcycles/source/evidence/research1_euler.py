"""Exact-cover plus Euler balance on literal partial-word de Bruijn edges.

An edge is a possible n-window tile, with tail=tile[:-1], head=tile[1:].
Exact cover forces the selected tiles to partition A^n. Vertex balance is
necessary for gluing. One connected selected edge component is sufficient,
and an Euler tour is independently expanded before reporting an upcycle.
No arbitrary permutations of positions are used. This is a changed encoding,
not an increase to the initial global-position search's time cap.
"""
import argparse
import itertools
import json
from pathlib import Path
import resource
import subprocess
import time
from research1_sat import JOB, sha
from research1_verify import verify

OUT=Path('evidence/research1-euler')


def build(mask,pinned=None):
    n=len(mask)
    d=mask.count('*')
    L=2**(n-d)
    frames=list(dict.fromkeys(mask[s:]+mask[:s] for s in range(n)))
    tiles=[]
    for frame in frames:
        for bits in itertools.product('01',repeat=n-d):
            letters=iter(bits)
            tiles.append(''.join('*' if c=='*' else next(letters) for c in frame))
    index={tile:i+1 for i,tile in enumerate(tiles)}
    clauses=[]
    for bits in itertools.product('01',repeat=n):
        compatible=[index[''.join('*' if c=='*' else bits[k] for k,c in enumerate(frame))]
                    for frame in frames]
        clauses.append(tuple(compatible))
        clauses.extend((-a,-b) for a,b in itertools.combinations(compatible,2))
    vertices={}
    for e,tile in enumerate(tiles,1):
        vertices.setdefault(tile[:-1],dict(incoming=[],outgoing=[]))['outgoing'].append(e)
        vertices.setdefault(tile[1:],dict(incoming=[],outgoing=[]))['incoming'].append(e)
    for vertex,incidence in vertices.items():
        ids=sorted(set(incidence['incoming']+incidence['outgoing']))
        assert len(ids)<=4
        for bits in itertools.product((0,1),repeat=len(ids)):
            values=dict(zip(ids,bits))
            if sum(values[e] for e in incidence['incoming'])!=sum(values[e] for e in incidence['outgoing']):
                clauses.append(tuple(-e if values[e] else e for e in ids))
    if pinned is not None:
        assert len(pinned)==L
        selected={index[''.join(pinned[(i+k)%L] for k in range(n))] for i in range(L)}
        clauses.extend((e if e in selected else -e,) for e in range(1,len(tiles)+1))
    return clauses,dict(n=n,d=d,length=L,mask=mask,frame_period=len(frames),tiles=tiles,
                        vertices=vertices,variables=len(tiles),clauses=len(clauses),pinned=pinned)


def analyze(meta,selected):
    # Independent expansion of a set of tiles.
    counts=[0]*2**meta['n']
    for e in selected:
        tile=meta['tiles'][e-1]
        holes=[k for k,c in enumerate(tile) if c=='*']
        for bits in itertools.product('01',repeat=len(holes)):
            word=list(tile)
            for k,c in zip(holes,bits):
                word[k]=c
            counts[int(''.join(word),2)]+=1
    assert all(c==1 for c in counts) and len(selected)==meta['length']
    undirected={}
    outgoing={}
    incoming={}
    for e in selected:
        tile=meta['tiles'][e-1]
        a,b=tile[:-1],tile[1:]
        undirected.setdefault(a,set()).add(b)
        undirected.setdefault(b,set()).add(a)
        outgoing.setdefault(a,[]).append(e)
        incoming.setdefault(b,[]).append(e)
    assert all(len(outgoing.get(v,[]))==len(incoming.get(v,[])) for v in undirected)
    unseen=set(undirected)
    components=[]
    while unseen:
        todo=[min(unseen)]
        seen=set(todo)
        while todo:
            v=todo.pop()
            for w in undirected[v]-seen:
                seen.add(w)
                todo.append(w)
        unseen-=seen
        components.append(sorted(seen))
    r=dict(selected_indices=selected,coverage_counts=counts,
           components=components,component_count=len(components),
           component_edge_counts=[sum(meta['tiles'][e-1][:-1] in C for e in selected) for C in map(set,components)])
    if len(components)==1:
        # Hierholzer, recording edge identities and then reading first symbols.
        adj={v:edges[:] for v,edges in outgoing.items()}
        stack=[(min(undirected),None)]
        reversed_edges=[]
        while stack:
            v,edge=stack[-1]
            if adj.get(v):
                nxt=adj[v].pop()
                stack.append((meta['tiles'][nxt-1][1:],nxt))
            else:
                stack.pop()
                if edge is not None:
                    reversed_edges.append(edge)
        tour=reversed_edges[::-1]
        assert len(tour)==len(selected) and set(tour)==set(selected)
        assert all(meta['tiles'][tour[i]-1][1:]==meta['tiles'][tour[(i+1)%len(tour)]-1][:-1]
                   for i in range(len(tour)))
        word=''.join(meta['tiles'][e-1][0] for e in tour)
        literal=verify(word,meta['n'])
        assert literal['valid']
        r.update(euler_tour=tour,upcycle=literal)
    return r


def run(label,mask,cap=30,pinned=None):
    OUT.mkdir(exist_ok=True)
    clauses,meta=build(mask,pinned)
    cnf=OUT/(label+'.cnf');proof=OUT/(label+'.lrat');log=OUT/(label+'.log')
    encoding=OUT/(label+'.encoding.json')
    with cnf.open('w') as f:
        f.write(f'p cnf {meta["variables"]} {len(clauses)}\n')
        for c in clauses:
            f.write(' '.join(map(str,c))+' 0\n')
    encoding.write_text(json.dumps(meta,indent=2)+'\n')
    cmd=['/opt/homebrew/bin/cadical','--check','--lrat','--no-binary','-t',str(cap),str(cnf),str(proof)]
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    start=time.monotonic()
    with log.open('w') as f:
        try:
            code=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=cap+2).returncode
        except subprocess.TimeoutExpired:
            code=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result=dict(job_id=JOB,label=label,n=meta['n'],d=meta['d'],mask=mask,
                status='SAT' if code==10 else 'UNSAT' if code==20 else 'unknown',
                returncode=code,cap_seconds=cap,elapsed_seconds=time.monotonic()-start,
                child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                variables=meta['variables'],clauses=meta['clauses'],cnf=str(cnf),
                proof=str(proof),log=str(log),encoding=str(encoding),
                cnf_sha256=sha(cnf),proof_sha256=sha(proof),
                scope='exact subcube partition plus balanced literal-overlap graph; connectedness checked on models')
    if code==10:
        values={}
        for line in log.read_text().splitlines():
            if line.startswith('v '):
                for x in map(int,line[2:].split()):
                    if x:
                        values[abs(x)]=x>0
        assert all(any(values[abs(x)]==(x>0) for x in c) for c in clauses)
        selected=[e for e in range(1,len(meta['tiles'])+1) if values[e]]
        checked=analyze(meta,selected)
        model=OUT/(label+'.model-verification.json')
        model.write_text(json.dumps(checked,indent=2)+'\n')
        result.update(model_verification=str(model),component_count=checked['component_count'],
                      verified_upcycle='upcycle' in checked)
    path=OUT/(label+'.result.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['benchmark','n8','n12'])
    args=parser.parse_args()
    if args.mode=='benchmark':
        data=json.loads(Path('evidence/triage-sanity.json').read_text())
        for c in data['controls'][:2]:
            mask=''.join('*' if x=='*' else '.' for x in c['word'][:c['n']])
            r=run('benchmark_'+c['label'],mask,10,c['word'])
            assert r['status']=='SAT' and r['verified_upcycle']
        r=run('bad_flip_n4','...*',10,'101*110*')
        assert r['status']=='UNSAT'
    elif args.mode=='n8':
        for mask in ['**......','*...*...']:
            label='n8d2_'+mask.replace('*','x').replace('.','o')
            run(label,mask,30)
    else:
        run('n12d3_period4','...*'*3,60)
