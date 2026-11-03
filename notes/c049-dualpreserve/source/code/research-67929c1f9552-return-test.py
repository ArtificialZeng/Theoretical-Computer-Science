#!/usr/bin/env python3
"""Exact tests of the new return-edge isolation lemma, not a global bound."""
from pathlib import Path
from itertools import combinations
import importlib.util, json, random, hashlib

fp=Path(__file__).with_name('research-67929c1f9552-flow-test.py')
spec=importlib.util.spec_from_file_location('flowtest',fp)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)

def witnesses(n,edges,pairs):
    beta=[None]*len(edges); ws=[]
    masks,cuts=f.cut_masks(n,edges,pairs)
    for a,out,active in cuts:
        reverse=[i for i,(s,t) in enumerate(pairs) if not(a>>s&1) and a>>t&1]
        inside=[k for k,(u,v) in enumerate(edges) if a>>u&1 and a>>v&1]
        outside=[k for k,(u,v) in enumerate(edges) if not(a>>u&1) and not(a>>v&1)]
        for k in out:
            u,v=edges[k]
            for i in active:
                s,t=pairs[i]
                if f.reach(n,edges,inside,s)>>u&1 and f.reach(n,edges,outside,v)>>t&1:
                    beta[k]=len(reverse) if beta[k] is None else min(beta[k],len(reverse))
                    ws.append((k,i,out,reverse))
    assert [b is not None for b in beta]==[bool(x) for x in masks]
    return beta,ws

def main():
    rng=random.Random(67930);cases=checks=0;rows=[]
    for n in range(3,8):
        for trial in range(8):
            e=[(u,v) for u in range(n) for v in range(n) if u!=v and rng.random()<.4]
            pairs=rng.sample([(u,v) for u in range(n) for v in range(n) if u!=v],min(n,4))
            e=f.prune(n,e,pairs);beta,ws=witnesses(n,e,pairs)
            for k,i,out,rev in ws:
                for mask in range(1<<len(pairs)):
                    if not(mask>>i&1) or any(mask>>j&1 for j in rev):continue
                    aug=e+list({(t,s) for j,(s,t) in enumerate(pairs) if mask>>j&1}-set(e))
                    failed=set(out)-{k};available=set(range(len(aug)))-failed
                    s,t=pairs[i]
                    assert f.reach(n,aug,available,s)>>t&1
                    assert f.reach(n,aug,available,t)>>s&1
                    assert not(f.reach(n,aug,available-{k},s)>>t&1)
                    checks+=1
            rows.append(dict(n=n,p=len(pairs),critical_edges=len(e),
                             beta=beta,high_at_ceil_sqrt=sum(b>int((len(pairs)-1)**.5)+1 for b in beta)))
            cases+=1
    family=[]
    for r,L in [(2,3),(3,2),(4,2)]:
        n,e,pairs=f.chain(r,L);beta,_=witnesses(n,e,pairs)
        cross=[b for b,(u,v) in zip(beta,e) if u<r*L<=v]
        assert all((r-3)**2<=b<=(r-1)**2 for b in cross) if r>=3 else True
        family.append(dict(r=r,L=L,n=n,p=len(pairs),crossings=len(cross),
                           minimum_cross_beta=min(cross),maximum_cross_beta=max(cross)))
    out=dict(job_id=f.JOB,status='declared exact checks passed',
             random_critical_graphs=cases,return_isolation_witness_sample_checks=checks,
             rows=rows,chain_complete_cut_enumeration=family,
             limits='40 seeded graph/demand instances, not exhaustive graph coverage. Every cut and return subset checked within those instances. Three declared chains have complete cut enumeration. No global high-beta edge bound proved.',
             code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('research-67929c1f9552-return-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','random_critical_graphs','return_isolation_witness_sample_checks','chain_complete_cut_enumeration']}),flush=True)

if __name__=='__main__':main()
