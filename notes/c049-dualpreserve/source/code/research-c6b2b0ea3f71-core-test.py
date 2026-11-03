#!/usr/bin/env python3
"""Exact finite checks of induced-matching selector; asymptotic proof is in math.md.
Does not certify random-demand expansion or original preserver theorem by search.
"""
from pathlib import Path
from collections import defaultdict,deque
from itertools import product
import hashlib,json,time
JOB='c049-dualpreserve-research-c6b2b0ea3f71'

def sphere_base(dim,b):
    layers=defaultdict(list)
    for v in product(range(b),repeat=dim):layers[sum(x*x for x in v)].append(v)
    r=max(layers,key=lambda x:(len(layers[x]),-x))
    base=2*b; A=sorted(sum(x*base**i for i,x in enumerate(v)) for v in layers[r])
    M=2*base**dim+1
    assert all(a==c or a+c!=2*z for a in A for c in A for z in A)
    assert all(a==c or (a+c-2*z)%M for a in A for c in A for z in A)
    match=[[] for _ in range(M)];inv2=(M+1)//2
    for z in range(M):
        for a in A:
            x=((z-a)*inv2)%M;y=(x+a)%M;match[z].append((x,M+y))
    edge_set={e for ms in match for e in ms}
    assert len(edge_set)==M*len(A)
    for ms in match:
        assert len({u for u,v in ms})==len(A)==len({v for u,v in ms})
        assert all((u,v2) not in edge_set for u,v in ms for u2,v2 in ms if u!=u2)
    return M,A,match

def build(M,match):
    ed=[];idx={};core=[];s=[];t=[];left=[];right=[];wit=[];n=2*M
    def add(u,v):
        assert u!=v and (u,v) not in idx
        idx[u,v]=len(ed);ed.append((u,v));return len(ed)-1
    for ms in match:
        for u,v in ms:core.append(add(u,v))
    for ms in match:
        a=list(range(n,n+len(ms)));n+=len(ms)
        b=list(range(n,n+len(ms)));n+=len(ms)
        left.append(a);right.append(b);s.append(a[0]);t.append(b[-1])
        for k,(u,v) in enumerate(ms):add(a[k],u);add(v,b[k])
        for k in range(len(ms)-1):add(a[k],a[k+1]);add(b[k],b[k+1])
    hub=n;n+=1
    for j,a in enumerate(left):add(a[-1],left[j+1][0] if j+1<M else hub)
    for dest in t:add(hub,dest)
    for j,ms in enumerate(match):
        for k,(u,v) in enumerate(ms):
            failed=[idx[left[j][k],left[j][k+1] if k+1<len(ms) else (left[j+1][0] if j+1<M else hub)]]
            if k:failed.append(idx[right[j][k-1],right[j][k]])
            wit.append((j,k,idx[u,v],failed))
    assert len(ed)==5*M*len(match[0])
    assert n==2*M+2*M*len(match[0])+1
    return n,ed,core,s,t,left,right,wit

def reachable(adj,source,failed):
    seen={source};todo=[source]
    for u in todo:
        for v,k in adj[u]:
            if k not in failed and v not in seen:seen.add(v);todo.append(v)
    return seen

def main():
    rows=[];total=0;start=time.monotonic()
    for dim,b in [(2,2),(3,2),(3,3)]:
        M,A,ms=sphere_base(dim,b);n,ed,core,s,t,left,right,wit=build(M,ms)
        adj=[[] for _ in range(n)];radj=[[] for _ in range(n)]
        for k,(u,v) in enumerate(ed):adj[u].append((v,k));radj[v].append((u,k))
        reach_count=0
        for x in s:
            R=reachable(adj,x,set());assert all(y in R for y in t);reach_count+=M
        witness_counts=[];minimum_sources=M;minimum_targets=M
        for j,pos,e,fail in wit:
            assert t[j] in reachable(adj,s[j],set(fail))
            R=reachable(adj,s[j],set(fail)|{e});assert t[j] not in R
            out=[k for k,(u,v) in enumerate(ed) if u in R and v not in R]
            assert e in out and len(out)<=3 and set(out)-{e}<=set(fail)
            sx=sum(x not in R for x in s);tx=sum(y in R for y in t)
            assert sx>=len(A)-3 and tx>=len(A)-3
            minimum_sources=min(minimum_sources,sx);minimum_targets=min(minimum_targets,tx)
            # Every prefix/suffix edge on the unique surviving route is mandatory.
            allowed=set(range(len(ed)))-set(fail)
            seen=reachable(adj,s[j],set(fail));co=reachable(radj,t[j],set(fail))
            route_edges=[k for k,(u,v) in enumerate(ed) if k in allowed and u in seen and v in co]
            expected=pos+1+1+1+(len(ms[j])-pos-1)
            assert len(route_edges)==expected # unique selector path, no alternative edge
            witness_counts.append(len(fail));total+=1
        rows.append(dict(dim=dim,digit_bound=b,modulus=M,progression_free_set=A,
                         matching_count=M,core_minimum_degree=len(A),n=n,m=len(ed),
                         core_edges=len(core),all_source_target_reachability_checks=reach_count,
                         mandatory_core_witnesses=len(wit),one_failure_witnesses=witness_counts.count(1),
                         two_failure_witnesses=witness_counts.count(2),
                         minimum_outside_sources_on_witness_cuts=minimum_sources,
                         minimum_inside_targets_on_witness_cuts=minimum_targets))
        print(json.dumps(rows[-1]),flush=True)
    result={'job_id':JOB,'status':'all declared finite checks passed','rows':rows,
            'mandatory_core_witnesses':total,'elapsed_seconds':time.monotonic()-start,
            'limits':'Three exact sphere-selector instances only. All matching edges and all original source/target combinations checked. No exhaustive graph search, no finite random-demand expansion claim, and no original-scope resolution.',
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('research-c6b2b0ea3f71-core-results.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
