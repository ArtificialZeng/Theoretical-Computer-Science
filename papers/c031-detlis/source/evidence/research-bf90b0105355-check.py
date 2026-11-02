"""New interval-parameterized forest/rounding checks for research pass 2.

Production scores use only rounded integers and selected-source trees.
Quadratic paths, Fractions, and dense score sums are verifier work only.
Manual parameters exercise compression; they are not the uniform theorem's
conservative parameters. No existing diagnostic is run or overwritten.
"""
from pathlib import Path
import sys, json, random, hashlib, datetime
from fractions import Fraction
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'intake/root-diagnostics'))
from check_fenwick_trace_oracle import SourceTree, newstats

COUNTS = dict(local_fixtures=0, source_paths=0, trace_memberships=0,
              candidate_scores=0, growth_steps=0, table_states=0,
              negative_deltas=0, certified=0, uncertified=0, merge_nodes=0,
              invariant_checks=0, all_dummy=0)

def reference_paths(values, lo, hi):
    out = {}
    for u in range(lo, min(hi, len(values))):
        best = {u: (u,)}
        for v in range(u+1, min(hi, len(values))):
            options = [p+(v,) for w,p in best.items() if values[w] < values[v]]
            if options:
                best[v] = min(options, key=lambda p: (-len(p), p))
        out.update({(u,v):p for v,p in best.items()})
    return out

def forests(values, sample, lo, hi):
    assert all(x is None or lo <= x < min(hi,len(values)) for x in sample)
    selected = sorted(set(x for x in sample if x is not None))
    rank = {x:j for j,x in enumerate(selected)}
    occ = [rank.get(x,-1) for x in sample]
    d, size = len(selected), max(0,min(hi,len(values))-lo)
    weight = [occ.count(j) for j in range(d)]
    result, traces, stats = [], [], newstats()
    for u in selected:
        tree = SourceTree(values,lo,hi,u,stats)
        near = [-1]*size
        for v in range(size):
            if tree.depth[v]:
                near[v] = rank[lo+v] if lo+v in rank else (
                    -1 if tree.parent[v]<0 else near[tree.parent[v]])
        parent, nodes, count = [-1]*d, [], [0]*d
        for j,x in enumerate(selected):
            v=x-lo
            if not tree.depth[v]: continue
            nodes.append(j)
            pv=tree.parent[v]
            parent[j]=-1 if pv<0 else near[pv]
            assert parent[j]<j
            count[j]=weight[j]+(0 if parent[j]<0 else count[parent[j]])
        children=[[] for _ in selected]
        for j in nodes:
            if parent[j]>=0: children[parent[j]].append(j)
        tin,tout=[-1]*d,[-1]*d
        stack=[(rank[u],False)]; clock=0
        while stack:
            v,done=stack.pop()
            if done: tout[v]=clock; continue
            tin[v]=clock; clock+=1
            stack.append((v,True))
            stack.extend((x,False) for x in reversed(children[v]))
        ids=[]; sid=len(result)
        for v in nodes:
            ids.append(len(traces)); traces.append((sid,v,count[v]))
        result.append((nodes,parent,tin,tout,ids))
    assert stats['max_per_tree_array_length']<=size
    return selected,occ,result,traces,stats

def compress(values,sample,lo,hi,p,eta,records):
    k=len(sample)//2; b=2*k
    selected,occ,ff,traces,stats=forests(values,sample,lo,hi)
    COUNTS['local_fixtures']+=1
    M,d=len(traces),len(selected)
    if not M:
        COUNTS['all_dummy']+=1
        return [None]*k
    D=1 << (64*M*k*k-1).bit_length()
    def bad(a,c):
        return int(abs(Fraction(c,k)-Fraction(a,b))>eta*(p+Fraction(a,b)))
    U=[]
    for a in range(b+1):
        rows=[[D*bad(a,c) for c in range(k+1)]]
        for h in range(1,k+1):
            prev=rows[-1]
            rows.append([(a*prev[c+1]+(b-a)*prev[c]+b-1)//b
                         for c in range(k-h+1)])
        U.append(rows)
    # Independent exact oracle is never consulted by production choices.
    @lru_cache(None)
    def exact(a,h,c):
        if h==0: return bad(a,c)
        return a*exact(a,h-1,c+1)+(b-a)*exact(a,h-1,c)
    for a in range(b+1):
        for h in range(k+1):
            for c in range(k-h+1):
                q=Fraction(exact(a,h,c),b**h)
                assert q<=Fraction(U[a][h][c],D)<=q+Fraction(h,D)
                COUNTS['table_states']+=1
    ref=reference_paths(values,lo,hi)
    direct_members=[]
    for sid,v,a in traces:
        nodes,parent,tin,tout,ids=ff[sid]
        u=selected[nodes[0]]
        path=set(ref[u,selected[v]])
        assert a==sum(x in path for x in sample if x is not None)
        for j,x in enumerate(selected):
            assert (tin[j]>=0 and tin[j]<=tin[v]<tout[j])==(x in path)
            COUNTS['trace_memberships']+=1
        direct_members.append([x in path if x is not None else False for x in sample])
        COUNTS['source_paths']+=1
    counts=[0]*M; output=[]
    current=Fraction(sum(exact(a,k,0) for _,_,a in traces),b**k)
    initial=current
    for h in range(k,0,-1):
        B=0; influence=[0]*d
        for nodes,parent,tin,tout,ids in ff:
            acc=[0]*d
            for j in ids:
                _,v,a=traces[j]; c=counts[j]
                zero,one=U[a][h-1][c:c+2]
                delta=one-zero; COUNTS['negative_deltas']+=delta<0
                B+=zero; acc[v]+=delta
            for v in reversed(nodes):
                if parent[v]>=0: acc[parent[v]]+=acc[v]
            for v in nodes: influence[v]+=acc[v]
        scores=[B+(0 if j<0 else influence[j]) for j in occ]
        direct=[sum(U[a][h-1][counts[j]+int(direct_members[j][x])]
                    for j,(_,_,a) in enumerate(traces)) for x in range(b)]
        assert scores==direct
        COUNTS['candidate_scores']+=b
        chosen=min(range(b),key=lambda x:(scores[x],x))
        rank=occ[chosen]
        for j,(sid,v,a) in enumerate(traces):
            nodes,parent,tin,tout,ids=ff[sid]
            hit=rank>=0 and tin[rank]>=0 and tin[rank]<=tin[v]<tout[rank]
            counts[j]+=hit
        output.append(sample[chosen])
        after=Fraction(sum(exact(a,h-1,counts[j]) for j,(_,_,a) in enumerate(traces)),b**(h-1))
        assert after<=Fraction(scores[chosen],D)
        assert after<=current+Fraction(M*(h-1),D)
        current=after; COUNTS['growth_steps']+=1
    certified=initial<=Fraction(1,8)
    COUNTS['certified' if certified else 'uncertified']+=1
    if certified:
        assert current==0
        assert all(abs(Fraction(counts[j],k)-Fraction(a,b))<=eta*(p+Fraction(a,b))
                   for j,(_,_,a) in enumerate(traces))
    records.append({'lo':lo,'hi':hi,'background_size':max(0,min(hi,len(values))-lo),
                    'k':k,'M':M,'initial_exact_potential':str(initial),
                    'terminal_bad_count':str(current),'certified':certified,
                    'max_local_array':stats['max_per_tree_array_length'],
                    'D_bits':D.bit_length()})
    return output

def main():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    rng=random.Random(9031031); records=[]
    # Narrow intervals far inside a large background: no whole-n source arrays.
    values=[rng.randrange(9) for _ in range(2048)]
    for lo,hi in [(1500,1516),(2032,2064),(500,524)]:
        sample=[rng.randrange(lo,min(hi,len(values))) if rng.randrange(4) else None
                for _ in range(16)]
        compress(values,sample,lo,hi,Fraction(1),Fraction(1,2),records)
    # Nontrivial small tolerances are retained even if initial potential is too
    # large. Growth/table/score identities still apply; no zero-bad claim then.
    for values in [list(range(16)),list(range(15,-1,-1)),
                   [rng.randrange(5) for _ in range(16)]]:
        for p,eta in [(Fraction(1,4),Fraction(1,4)),(Fraction(1),Fraction(1,2))]:
            sample=[rng.randrange(16) if rng.randrange(5) else None for _ in range(16)]
            compress(values,sample,0,16,p,eta,records)
    compress(values,[None]*16,4,12,Fraction(1),Fraction(1,2),records)
    # Full multi-interval, multi-level merge with original backgrounds and
    # arbitrary multiplicities. Conservative manual tolerance is intentional.
    for n in [45,64]:
        values=[rng.randrange(11) for _ in range(n)]
        N=64; k=8; p=Fraction(1); eta=Fraction(1,2)
        global_paths=list(reference_paths(values,0,n).values())
        layer=[(lo,lo+k,[j if j<n else None for j in range(lo,lo+k)],0)
               for lo in range(0,N,k)]
        while len(layer)>1:
            next_layer=[]
            for q in range(0,len(layer),2):
                lo,mid,left,depth=layer[q]; mid2,hi,right,depth2=layer[q+1]
                assert mid==mid2 and depth==depth2
                before=len(records)
                out=compress(values,left+right,lo,hi,p,eta,records)
                assert len(records)==before or records[-1]['certified']
                for path in global_paths:
                    phi=Fraction(sum(lo<=x<hi for x in path),hi-lo)
                    r=Fraction(sum(x in path for x in out if x is not None),k)
                    E=(1+eta)**(depth+1)-1
                    assert abs(r-phi)<=E*(phi+p)
                    COUNTS['invariant_checks']+=1
                next_layer.append((lo,hi,out,depth+1)); COUNTS['merge_nodes']+=1
            layer=next_layer
    # Exact uniform parameter arithmetic across small and enormous n, with no
    # floating roots or allocating a uniform-parameter table in the fallback.
    params=[]
    for n in [1,2,3,17,2**30+7,2**90+1,2**180+13]:
        lo,hi=0,n
        while lo<hi:
            mid=(lo+hi)//2
            if mid**3>=n*n: hi=mid
            else: lo=mid+1
        t=lo; N=1<<(n-1).bit_length(); L=(N+1).bit_length(); H=L+1
        lower=512*N*256*H*H*L
        target=(lower+t-1)//t
        k=1<<(target-1).bit_length()
        assert (t-1)**3<n*n<=t**3
        assert k*t>=lower and k<2*(lower+t)
        assert (1+Fraction(1,16*H))**H-1<Fraction(1,15)
        params.append({'n':str(n),'t':str(t),'k_bits':k.bit_length(),'fallback':k>=N})
    report={'job_id':'c031-detlis-research-bf90b0105355','started_utc':started,
            'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status':'passed','counts':COUNTS,'records':records,'uniform_parameters':params,
            'limits':'Finite manually parameterized diagnostics; exact/direct oracles are verification only. Not an asymptotic benchmark, infinite proof, novelty verdict, or fresh referee review.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('research-bf90b0105355-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'passed','counts':COUNTS,'parameter_cases':len(params)}))

if __name__=='__main__': main()
