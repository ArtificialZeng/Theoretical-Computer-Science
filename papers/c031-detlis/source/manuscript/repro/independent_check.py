"""Fresh finite checks; no imports from the candidate or its diagnostics.

Subsequence enumeration is the reference. These checks do not prove universal
correctness, running time, novelty, or conference suitability.
"""
from itertools import product, permutations
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json, hashlib, datetime

COUNTS = dict(inputs=0, subpaths=0, localized_traces=0,
              short_query_thresholds=0, stitching_pivots=0,
              rounded_table_entries=0, aggregate_scores=0,
              compression_steps=0, certified_compressions=0)

def enumerate_chains(a):
    n = len(a)
    cc = []
    for mask in range(1 << n):
        c = tuple(i for i in range(n) if mask >> i & 1)
        if all(a[x] < a[y] for x, y in zip(c, c[1:])):
            cc.append(c)
    return cc

def canonical(cc):
    pp = {}
    for c in cc:
        if c:
            key = c[0], c[-1]
            if key not in pp or (-len(c), c) < (-len(pp[key]), pp[key]):
                pp[key] = c
    return pp

def short_answer(a, l, r, low, high, t):
    # Independently reconstruct the proof's A/B recurrence, using exhaustive
    # predecessor loops rather than a range tree/Fenwick implementation.
    n = len(a)
    lo, hi = 0, n
    while True:
        split = (lo + hi) // 2
        if r <= split: hi = split
        elif l >= split: lo = split
        else: break
    A, B = {}, {}
    for v in range(split-1, lo-1, -1):
        A[v, 1] = (v,)
        for h in range(2, t+1):
            opts = [A[w, h-1] for w in range(v+1, split)
                    if a[w] > a[v] and (w, h-1) in A]
            if opts:
                tail = min(opts, key=lambda c: (a[c[-1]], c))
                A[v, h] = (v,) + tail
    for v in range(split, hi):
        B[v, 1] = (v,)
        for h in range(2, t+1):
            opts = [B[w, h-1] for w in range(split, v)
                    if a[w] < a[v] and (w, h-1) in B]
            if opts:
                head = max(opts, key=lambda c: (a[c[0]], c))
                B[v, h] = head + (v,)
    left, right = {0: ()}, {0: ()}
    for h in range(1, t+1):
        ll = [A[v, h] for v in range(l, split)
              if (v, h) in A and low <= a[v] <= high and a[A[v, h][-1]] <= high]
        rr = [B[v, h] for v in range(split, r)
              if (v, h) in B and low <= a[v] <= high and a[B[v, h][0]] >= low]
        if ll: left[h] = min(ll, key=lambda c: a[c[-1]])
        if rr: right[h] = max(rr, key=lambda c: a[c[0]])
    lv = [a[left[h][-1]] for h in sorted(left) if h]
    rv = [a[right[h][0]] for h in sorted(right) if h]
    assert lv == sorted(lv) and rv == sorted(rv, reverse=True)
    return max((x+y for x in left.values() for y in right.values()
                if not x or not y or a[x[-1]] < a[y[0]]), key=len)

def check_input(a, full_queries):
    n = len(a); cc = enumerate_chains(a); pp = canonical(cc)
    COUNTS['inputs'] += 1
    for c in pp.values():
        for i in range(len(c)):
            for j in range(i, len(c)):
                assert pp[c[i], c[j]] == c[i:j+1]
                COUNTS['subpaths'] += 1
    # Include interval restrictions of GLOBAL paths, not selected-only paths.
    for lo in range(n):
        for hi in range(lo+1, n+1):
            ss = set(range(lo, hi))
            global_traces = {tuple(x for x in c if x in ss) for c in pp.values()} | {()}
            local = {c for (u,v),c in pp.items() if u in ss and v in ss} | {()}
            assert global_traces == local
            COUNTS['localized_traces'] += 1
    if not full_queries: return
    for l in range(n):
        for r in range(l+1, n+1):
            for low in range(-1, 4):
                for high in range(low, 4):
                    feasible = [c for c in cc if all(l <= x < r and low <= a[x] <= high for x in c)]
                    opt = max(map(len, feasible))
                    for t in range(1, n+1):
                        out = short_answer(a,l,r,low,high,t) if r-l>1 else ((l,) if low<=a[l]<=high else ())
                        assert out in feasible
                        if opt <= t: assert len(out) == opt
                        COUNTS['short_query_thresholds'] += 1
                    # Any pivot on any optimal path must admit an exact stitch.
                    for c in feasible:
                        if len(c) != opt: continue
                        for pivot in c:
                            back = max((z for z in feasible if z and z[-1]==pivot), key=len)
                            front = max((z for z in feasible if z and z[0]==pivot), key=len)
                            out = back + front[1:]
                            assert out in feasible and len(out) == opt
                            COUNTS['stitching_pivots'] += 1

def probability(a, b, k, h, c, p, eta):
    # Direct binomial sum, independent of the rounded-table recurrence.
    return sum((Q(comb(h,j)*a**j*(b-a)**(h-j), b**h)
                for j in range(h+1)
                if abs(Q(c+j,k)-Q(a,b)) > eta*(p+Q(a,b))), Q(0))

def compression_check(values, sample, p, eta):
    b=len(sample); k=b//2
    pp=canonical(enumerate_chains(values))
    selected=sorted(set(x for x in sample if x is not None))
    desc=[(u,v,pp[u,v]) for u in selected for v in selected if (u,v) in pp]
    masks=[tuple(x is not None and x in path for x in sample) for u,v,path in desc]
    aa=[sum(mask) for mask in masks]; M=len(desc)
    assert M>0
    D=1 << (64*M*k*k-1).bit_length()
    U={}
    for a in range(b+1):
        for c in range(k+1):
            U[a,0,c]=D*int(abs(Q(c,k)-Q(a,b))>eta*(p+Q(a,b)))
        for h in range(1,k+1):
            for c in range(k-h+1):
                U[a,h,c]=(a*U[a,h-1,c+1]+(b-a)*U[a,h-1,c]+b-1)//b
        for h in range(k+1):
            for c in range(k-h+1):
                q=probability(a,b,k,h,c,p,eta)
                assert q <= Q(U[a,h,c],D) <= q+Q(h,D)
                COUNTS['rounded_table_entries']+=1
    counts=[0]*M; output=[]
    initial=sum((probability(a,b,k,k,0,p,eta) for a in aa),Q(0)); current=initial
    for h in range(k,0,-1):
        base=sum(U[a,h-1,c] for a,c in zip(aa,counts))
        delta=[U[a,h-1,c+1]-U[a,h-1,c] for a,c in zip(aa,counts)]
        influence={x:0 for x in selected}
        # Reconstruct selected trees from independently enumerated paths.
        for u in selected:
            nodes=[v for v in selected if (u,v) in pp]
            parent={v:next((x for x in reversed(pp[u,v][:-1]) if x in selected),None) for v in nodes}
            sums={v:0 for v in nodes}
            for j,(src,v,path) in enumerate(desc):
                if src==u: sums[v]+=delta[j]
            for v in reversed(nodes):
                influence[v]+=sums[v]
                if parent[v] is not None: sums[parent[v]]+=sums[v]
        aggregate=[base+(influence[x] if x is not None else 0) for x in sample]
        direct=[sum(U[a,h-1,c+int(mask[x])] for a,c,mask in zip(aa,counts,masks)) for x in range(b)]
        assert aggregate==direct
        COUNTS['aggregate_scores']+=b
        x=min(range(b),key=lambda z:(aggregate[z],z)); output.append(sample[x])
        counts=[c+int(mask[x]) for c,mask in zip(counts,masks)]
        after=sum((probability(a,b,k,h-1,c,p,eta) for a,c in zip(aa,counts)),Q(0))
        assert after<=current+Q(M*(h-1),D)
        current=after; COUNTS['compression_steps']+=1
    if initial<=Q(1,8):
        assert current==0
        COUNTS['certified_compressions']+=1
    return {'values':list(values),'sample':sample,'p':str(p),'eta':str(eta),'initial':str(initial),'terminal':str(current),'certified':initial<=Q(1,8),'output':output}

def main():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    for n in range(1,6):
        for a in product(range(3),repeat=n): check_input(a,True)
    for n in range(1,7):
        for a in permutations(range(n)): check_input(a,False)
    fixtures=[]
    for values in [(0,1,2,3,4,5),(5,4,3,2,1,0),(0,3,1,2,2,4),(1,0,1,0,2,3)]:
        for sample in [[0,1,2,3,4,5,None,2],[0,0,2,2,4,5,None,None]]:
            for p,eta in [(Q(1),Q(1,2)),(Q(1,4),Q(1,4))]:
                fixtures.append(compression_check(values,sample,p,eta))
    result={'job_id':'c031-detlis-referee-f280f716946c','snapshot_digest':'76aff8cb1dceada574829e417470dcca336a544f9c08e579f9c49cff43896135','started_utc':started,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'passed','counts':COUNTS,'fixtures':fixtures,'limits':'Fresh finite checks only. Exhaustive ternary words through length 5 for short reporting and stitching; all permutations through 6 for path identities; 16 manually parameterized compressions. No candidate code imported or rerun. No empirical claim about the asymptotic running time.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','counts':COUNTS}))

if __name__=='__main__': main()
