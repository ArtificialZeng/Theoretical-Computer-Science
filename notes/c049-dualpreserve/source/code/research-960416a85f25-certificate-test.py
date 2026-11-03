#!/usr/bin/env python3
"""Exact bounded validation of the fully shared selector theorem in math.md."""
from pathlib import Path
import importlib.util, json, subprocess, hashlib, time
ROOT=Path(__file__).resolve().parent;PRE='research-960416a85f25'
spec=importlib.util.spec_from_file_location('sharing',ROOT/'research-2396269cbd5d-sharing-test.py')
sharing=importlib.util.module_from_spec(spec);spec.loader.exec_module(sharing)

def perfect(t,edges,excluded):
    adj=[[] for _ in range(t)]
    for e,(u,v) in enumerate(edges):
        if e not in excluded:adj[u].append((v-t,e))
    match=[None]*t
    def aug(u,seen):
        for v,e in adj[u]:
            if v in seen:continue
            seen.add(v)
            if match[v] is None or aug(match[v][0],seen):match[v]=(u,e);return True
        return False
    for u in range(t):assert aug(u,set())
    return {x[1] for x in match}

def main():
    rows=[];start=time.monotonic()
    for k in (1,2):
        n,ed,wit,t,D=sharing.build(k,1,True,True);core=ed[:t*D]
        P0=[None]*t
        for i,j,e,s,tgt,F in wit:P0[i]=(s,tgt)
        S=[s for s,tgt in P0];T=[tgt for s,tgt in P0]
        A={v for u,v in ed if u in S and v>=2*t and v not in S}
        B={u for u,v in ed if v in T and u>=2*t and u not in T}
        assert len(A)==len(B)==1;a=next(iter(A));b=next(iter(B))
        u0=[next(v for u,v in ed if u==s and v<2*t) for s in S]
        wlast=[next(u for u,v in ed if v==tgt and u<2*t) for tgt in T]
        assert len(set(u0))==len(set(wlast))==t
        ui={u:i for i,u in enumerate(u0)};wj={w:j for j,w in enumerate(wlast)}
        core_pairs=[(ui[u],wj[v]) for u,v in core]
        assert all(i!=j for i,j in core_pairs)
        M1=perfect(t,core,set());M2=perfect(t,core,M1)
        assert len(M1)==len(M2)==t and not M1&M2
        for mode in ('diagonal','restore_every_core'):
            P=[(i,i) for i in range(t)]
            if mode=='restore_every_core':P+=core_pairs
            P=list(dict.fromkeys(P));pset=set(P)
            keep=set(M1|M2)
            keep.update(e for e,(u,v) in enumerate(ed[:t*D]) if (ui[u],wj[v]) in pset)
            keep.update(e for e,(u,v) in enumerate(ed) if u in S or v in T or (u==a and v<t) or (v==b and t<=u<2*t))
            assert len(keep)<=8*t+len(P)
            data=f'{n} {len(ed)} {t} {len(P)}\n'+''.join(f'{u} {v} {int(e in keep)}\n' for e,(u,v) in enumerate(ed))
            data+=' '.join(map(str,S))+'\n'+' '.join(map(str,T))+'\n'+''.join(f'{i} {j}\n' for i,j in P)
            checked=json.loads(subprocess.run([str(ROOT/(PRE+'-verify'))],input=data,text=True,capture_output=True,timeout=30,check=True).stdout)
            assert checked['preserves']
            assert checked['fault_sets']==1+len(ed)+len(ed)*(len(ed)-1)//2
            rows.append(dict(k=k,n=n,m=len(ed),matching_size=D,matching_count=t,demand_mode=mode,p=len(P),retained_edge_count=len(keep),kept_edges=sorted(keep),edges=ed,source_vertices=S,target_vertices=T,demands_by_indices=P,verification=checked))
            print(json.dumps({key:rows[-1][key] for key in ['k','n','m','p','demand_mode','retained_edge_count','verification']}),flush=True)
    result={'job_id':'c049-dualpreserve-research-960416a85f25','status':'all declared exact certificate comparisons passed','rows':rows,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cpp_sha256':hashlib.sha256((ROOT/(PRE+'-verify.cpp')).read_bytes()).hexdigest(),'limits':'Finite verification of the specified family only; the general family proof is in math.md. No resolution of source.md or novelty certification.'}
    (ROOT/(PRE+'-certificate-results.json')).write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
