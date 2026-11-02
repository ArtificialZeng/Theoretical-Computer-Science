"""Exact finite diagnostics, not an infinite proof or an asymptotic implementation.
Canonical path reference uses quadratic DP. Compression parameters are small
manual fixtures, NOT the deliberately enormous global theorem parameters.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations,combinations
from pathlib import Path
import random,json,hashlib,datetime

def paths(values,lo=0,hi=None):
    hi=len(values) if hi is None else hi
    out={}
    for a in range(lo,hi):
        best={a:(a,)}
        for b in range(a+1,hi):
            choices=[p+(b,) for v,p in best.items() if v<b and values[v]<values[b]]
            if choices:best[b]=min(choices,key=lambda p:(-len(p),p))
        out.update({(a,b):p for b,p in best.items()})
    return out

def traces(pathmap,sample):
    r={0}
    for p in pathmap.values():
        ps=set(p);r.add(sum(1<<i for i,x in enumerate(sample) if x is not None and x in ps))
    return r

def localized_traces(values,sample,lo,hi):
    distinct=sorted({x for x in sample if x is not None});p=paths(values,lo,hi)
    # Empty/singleton traces and all selected-endpoint canonical path traces.
    r={0}
    for x in distinct:r.add(sum(1<<i for i,v in enumerate(sample) if v==x))
    for a in distinct:
        for b in distinct:
            if (a,b) in p:
                ps=set(p[a,b]);r.add(sum(1<<i for i,x in enumerate(sample) if x in ps))
    return r

def compress(sample,trace_list,k,eta):
    assert len(sample)==2*k
    base=2*k; masks=list(sorted(trace_list));counts=[0]*len(masks); aa=[m.bit_count() for m in masks]
    @lru_cache(None)
    def num(a,h,c):
        if h==0:return int(abs(Fraction(c,k)-Fraction(a,base))>eta)
        return a*num(a,h-1,c+1)+(base-a)*num(a,h-1,c)
    h=k;current=Fraction(sum(num(a,h,0) for a in aa),base**h)
    initial=current
    if not initial<1:return None,{'certified_initial_less_than_one':False,'initial':str(initial)}
    result=[]
    for step in range(k):
        candidates=[]
        for x in range(base):candidates.append(sum(num(a,h-1,c+((m>>x)&1)) for a,c,m in zip(aa,counts,masks)))
        x=min(range(base),key=lambda z:candidates[z]);after=Fraction(candidates[x],base**(h-1));assert after<=current
        result.append(sample[x]);counts=[c+((m>>x)&1) for c,m in zip(counts,masks)];h-=1;current=after
    assert current==0
    error=max((abs(Fraction(c,k)-Fraction(a,base)) for c,a in zip(counts,aa)),default=Fraction(0));assert error<=eta
    return result,{'certified_initial_less_than_one':True,'initial':str(initial),'final_potential':str(current),'maximum_frequency_error':str(error),'eta':str(eta),'ranges':len(masks),'table_states':num.cache_info().currsize}

def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();stats={'permutations':0,'paths':0,'subpath_consistency':0,'localized_subset_checks':0,'query_endpoint_checks':0}
    for n in range(1,7):
        for vals in permutations(range(n)):
            pp=paths(vals);stats['permutations']+=1;stats['paths']+=len(pp)
            for p in pp.values():
                for i in range(len(p)):
                    for j in range(i,len(p)):
                        assert pp[p[i],p[j]]==p[i:j+1];stats['subpath_consistency']+=1
            # Exhaustive subsets on the full interval, and interval-local samples.
            for mask in range(1<<n):
                s=[i for i in range(n) if mask>>i&1]
                assert traces(pp,s)==localized_traces(vals,s,0,n);stats['localized_subset_checks']+=1
            for lo in range(n):
                for hi in range(lo+1,n+1):
                    s=list(range(lo,hi));assert traces(pp,s)==localized_traces(vals,s,lo,hi);stats['localized_subset_checks']+=1
            # Every rectangle optimum equals a canonical endpoint path within it.
            for lo in range(n):
                for hi in range(lo+1,n+1):
                    for a in range(n):
                        for b in range(a,n):
                            inside={i for i in range(lo,hi) if a<=vals[i]<=b}
                            brute=max((len(p) for r in range(1,len(inside)+1) for p in combinations(sorted(inside),r) if all(vals[x]<vals[y] for x,y in zip(p,p[1:]))),default=0)
                            canonical=max((len(p) for p in pp.values() if set(p)<=inside),default=0)
                            assert brute==canonical;stats['query_endpoint_checks']+=1
    rng=random.Random(3182026);compression=[];rejected_eta=[]
    cases=[list(range(16)),list(range(15,-1,-1))]+[rng.sample(range(16),16) for _ in range(18)]
    for case,vals in enumerate(cases):
        sample=list(range(16)) if case<10 else [rng.randrange(16) if rng.randrange(8) else None for _ in range(16)]
        ts=traces(paths(vals),sample);assert ts==localized_traces(vals,sample,0,16)
        for eta in [Fraction(1,4),Fraction(3,8),Fraction(1,2),Fraction(5,8)]:
            result,rec=compress(sample,ts,8,eta)
            if result is None:rejected_eta.append({'case':case,'eta':str(eta),'initial':rec['initial']});continue
            assert len(result)==8;compression.append({'case':case,**rec});break
        else:raise AssertionError('No test eta certified')
    # Nontrivial merge tree on equal original intervals, with exact per-path errors.
    merges=[]
    for case in range(4):
        vals=rng.sample(range(32),32);allp=paths(vals);reps=[list(range(i,i+8)) for i in range(0,32,8)];errors=[Fraction(0)]*4;intervals=[(i,i+8) for i in range(0,32,8)]
        while len(reps)>1:
            nxt=[];nerr=[];nint=[]
            for i in range(0,len(reps),2):
                lo,hi=intervals[i][0],intervals[i+1][1];sample=reps[i]+reps[i+1];ts=localized_traces(vals,sample,lo,hi);assert ts==traces(allp,sample)
                out,rec=compress(sample,ts,8,Fraction(1,2));assert out is not None
                bound=max(errors[i:i+2])+Fraction(1,2)
                actual=max(abs(Fraction(sum(x in set(p) for x in out),8)-Fraction(sum(lo<=x<hi for x in p),hi-lo)) for p in allp.values())
                assert actual<=bound;nxt.append(out);nerr.append(bound);nint.append((lo,hi));merges.append({'case':case,'interval':[lo,hi],'actual_error':str(actual),'proved_error_bound':str(bound),**rec})
            reps,errors,intervals=nxt,nerr,nint
        R=set(reps[0]);assert all(set(p)&R for p in allp.values() if Fraction(len(p),32)>errors[0])
    report={'started_at_utc':start,'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'passed_exact_finite_diagnostics','scope':'All permutations through6, all subsets and index intervals for trace/locality, all rank-coordinate rectangles;20 small manual compression fixtures and4 merge trees. Quadratic reference paths; not an asymptotic implementation or infinite proof.','stats':stats,'compression':compression,'uncertified_small_eta_attempts_preserved':rejected_eta,'merge_checks':merges,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':report['status'],'stats':stats,'compression_fixtures':len(compression),'uncertified_eta_attempts':len(rejected_eta),'merge_checks':len(merges)}))
if __name__=='__main__':main()
