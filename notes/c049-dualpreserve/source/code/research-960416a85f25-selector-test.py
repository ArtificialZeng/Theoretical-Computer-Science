#!/usr/bin/env python3
"""Bounded COMPLETE alternative-witness search on specified shared selectors.

All 0/1/2 edge-fault sets are enumerated. DAG edge dominators compute every
edge critical for any diagonal demand. A second implementation directly
deletes the reported edge and checks reachability of each saved witness.
This is finite evidence about a subsidiary construction, not a full result.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import datetime, hashlib, json, subprocess, time
ROOT=Path(__file__).resolve().parent
PREFIX='research-960416a85f25'
JOB='c049-dualpreserve-research-960416a85f25'
spec=spec_from_file_location('sharing',ROOT/'research-2396269cbd5d-sharing-test.py')
sharing=module_from_spec(spec);spec.loader.exec_module(sharing)

def reachable(n,ed,s,t,failed):
    adj=[[] for _ in range(n)]
    for e,(u,v) in enumerate(ed):
        if e not in failed:adj[u].append(v)
    seen={s};todo=[s]
    for u in todo:
        for v in adj[u]:
            if v not in seen:seen.add(v);todo.append(v)
    return t in seen

def run_case(k,groups,left,right):
    n,ed,wit,p,D=sharing.build(k,groups,left,right)
    P=[None]*p
    for i,j,e,s,t,F in wit:P[i]=(s,t)
    c=p*D
    data=f'{n} {len(ed)} {p} {c}\n'+''.join(f'{u} {v}\n' for u,v in ed)+''.join(f'{s} {t}\n' for s,t in P)
    started=time.monotonic()
    run=subprocess.run([str(ROOT/(PREFIX+'-allfault'))],input=data,text=True,capture_output=True,timeout=40,check=True)
    result=json.loads(run.stdout)
    assert result['fault_sets']==1+len(ed)+len(ed)*(len(ed)-1)//2
    for w in result['witnesses']:
        s,t=P[w['demand']];F=set(w['faults']);e=w['edge']
        assert e not in F and len(F)<=2
        assert reachable(n,ed,s,t,F)
        assert not reachable(n,ed,s,t,F|{e})
    # The literal dense-core ratio keeps the ENTIRE original ambient n.
    result.update(k=k,groups=groups,shared_left=left,shared_right=right,
                  elapsed_seconds=time.monotonic()-started,matching_size=D,
                  ambient_n=n,core_vertex_count=2*p,
                  density_ratio_numerator=c*c,
                  density_ratio_denominator=n*(p+1)*(2*p),
                  edges=ed,demands=P,
                  scope='All <=2 edge failures and all diagonal demands in this saved DAG. Every saved critical witness independently checked by BFS. A noncritical core edge has no alternate witness for these demands in this finite graph.')
    return result

def main():
    start=time.monotonic();rows=[]
    result={'job_id':JOB,'status':'in progress','rows':rows,'limits':'Specified finite shared-selector DAGs only. No asymptotic DENSITY result or original-scope resolution.'}
    for k in (1,2):
        t=2*3**k+1
        for groups,left,right in [(t,True,True),(1,True,False),(1,False,True),(1,True,True),(max(1,t//2),True,True)]:
            now=datetime.datetime.now(datetime.timezone.utc)
            assert now < datetime.datetime(2026,11,3,21,30,tzinfo=datetime.timezone.utc)
            try:row=run_case(k,groups,left,right)
            except subprocess.TimeoutExpired:
                row={'k':k,'groups':groups,'shared_left':left,'shared_right':right,'status':'per-case 40-second timeout; no classification inferred'}
            rows.append(row)
            result['elapsed_seconds']=time.monotonic()-start
            (ROOT/(PREFIX+'-selector-results.json')).write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps({key:row.get(key) for key in ['k','groups','shared_left','shared_right','n','m','core_edges','critical_core_edges','critical_all_edges','elapsed_seconds','status']}),flush=True)
    result['status']='declared finite cases complete'
    result['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['cpp_sha256']=hashlib.sha256((ROOT/(PREFIX+'-allfault.cpp')).read_bytes()).hexdigest()
    (ROOT/(PREFIX+'-selector-results.json')).write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
