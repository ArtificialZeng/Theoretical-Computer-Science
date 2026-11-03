#!/usr/bin/env python3
"""Exact finite attempted selector sharing; a failed merge is not a theorem."""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import deque
import hashlib,json,time
JOB='c049-dualpreserve-research-2396269cbd5d'
PREFIX='research-2396269cbd5d'
spec=spec_from_file_location('energy',Path(__file__).with_name(PREFIX+'-energy-test.py'))
energy=module_from_spec(spec);spec.loader.exec_module(energy)

def base(k):
    t=2*3**k+1;A=[sum(((b>>j)&1)*3**j for j in range(k)) for b in range(2**k)]
    assert all(a==b for a in A for b in A if any((a+b-2*c)%t==0 for c in A))
    inv=(t+1)//2;match=[]
    for z in range(t):match.append([(((z-a)*inv)%t,t+((z+a)*inv)%t) for a in A])
    ed={e for row in match for e in row}
    assert len(ed)==t*len(A)
    assert all(u==x or (u,y) not in ed for row in match for u,v in row for x,y in row)
    return t,A,match

def build(k,groups,share_left,share_right):
    t,A,match=base(k);D=len(A);names={};edges=[];idx={};wit=[]
    def vertex(name):
        if name not in names:names[name]=len(names)
        return names[name]
    U=[vertex(('u',i)) for i in range(t)];W=[vertex(('w',i)) for i in range(t)]
    def add(u,v):
        if u==v:return None
        if (u,v) not in idx:idx[u,v]=len(edges);edges.append((u,v))
        return idx[u,v]
    for row in match:
        for u,v in row:add(U[u],W[v-t])
    left=[];right=[]
    for i,row in enumerate(match):
        left.append([vertex(('a',i if j==0 or not share_left else i%groups,j)) for j in range(D)])
        right.append([vertex(('b',i if j==D-1 or not share_right else i%groups,j)) for j in range(D)])
    # Names distinguish all endpoints from internal shared states by position.
    for i,row in enumerate(match):
        a=left[i];b=right[i]
        for j,(u,v) in enumerate(row):add(a[j],U[u]);add(W[v-t],b[j])
        for j in range(D-1):add(a[j],a[j+1]);add(b[j],b[j+1])
    for i,row in enumerate(match):
        for j,(u,v) in enumerate(row):
            F=[]
            if j<D-1:F.append(idx[left[i][j],left[i][j+1]])
            if j:F.append(idx[right[i][j-1],right[i][j]])
            wit.append((i,j,idx[U[u],W[v-t]],left[i][0],right[i][-1],F))
    return len(names),edges,wit,t,D

def reach(adj,s,t,fail):
    seen={s};queue=[s]
    for u in queue:
        if u==t:return True
        for v,e in adj[u]:
            if e not in fail and v not in seen:seen.add(v);queue.append(v)
    return False

def main():
    start=time.monotonic();rows=[]
    for k in (2,3,4):
        t=2*3**k+1
        for groups in (t,max(1,t//2),max(1,t//4),1):
            for left,right in ((True,False),(False,True),(True,True)):
                if groups==t and (left,right)!=(True,True):continue
                n,ed,wit,p,D=build(k,groups,left,right)
                adj=[[] for _ in range(n)]
                for e,(u,v) in enumerate(ed):adj[u].append((v,e))
                checked=0;failure=None
                for i,j,e,s,tgt,F in wit:
                    before=reach(adj,s,tgt,set(F));after=reach(adj,s,tgt,set(F)|{e})
                    checked+=1
                    if not before or after:
                        failure={'matching':i,'position':j,'core_edge_index':e,'source':s,'target':tgt,
                                 'failed_edge_indices':F,'reachable_before':before,'reachable_after_removing_core_edge':after}
                        break
                passed=failure is None
                E=None
                if passed and n<=1200:E=energy.path_reverse(n,ed)[0]
                rows.append({'k':k,'matching_count':p,'matching_size':D,'groups':groups,
                    'shared_left':left,'shared_right':right,'n':n,'m':len(ed),'all_core_witnesses':len(wit),
                    'witness_checks_until_first_failure':checked,'all_specified_core_witnesses_survive':passed,
                    'first_failed_witness':failure,'energy_when_computed':E,
                    'energy_over_n_p_plus_1':None if E is None else str(energy.Fraction(E,n*(p+1))),
                    'compulsory_core_energy_lower_bound_if_all_witnesses_survive':
                        str(energy.Fraction((p*D)**2,2*p)) if passed else None})
                result={'job_id':JOB,'status':'in progress','rows':rows,
                    'limits':'Only specified periodic same-position identifications and inherited witnesses tested. Failure of an inherited witness does not prove that core edge is no longer compulsory by some other witness. No asymptotic obstruction or preserver result.'}
                Path(__file__).with_name(PREFIX+'-sharing-results.json').write_text(json.dumps(result,indent=2)+'\n')
    result['status']='declared finite sharing tests complete';result['elapsed_seconds']=time.monotonic()-start
    result['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_name(PREFIX+'-sharing-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cases':len(rows),'all_inherited_witnesses_survive':sum(r['all_specified_core_witnesses_survive'] for r in rows),'elapsed_seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
