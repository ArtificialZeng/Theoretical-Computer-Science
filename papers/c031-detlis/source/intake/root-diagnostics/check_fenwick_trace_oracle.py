"""Fenwick/LCA implementation of the proposed LOCAL trace oracle.
Exact finite diagnostics against a different quadratic canonical-path DP.
This is one algorithmic primitive, not an end-to-end resolution certificate.
"""
from bisect import bisect_left
from itertools import permutations,product
from pathlib import Path
import random,json,datetime,hashlib
from check_localized_net import paths,traces

class SourceTree:
    def __init__(self,values,lo,hi,source,stats):
        self.lo=lo;self.hi=min(hi,len(values));m=max(0,self.hi-lo);self.m=m;self.stats=stats
        assert lo<=source<self.hi
        self.depth=[0]*m;self.parent=[-1]*m
        self.levels=max(1,m.bit_length());self.up=[[-1]*m for _ in range(self.levels)]
        # Every allocation here depends on the ORIGINAL interval size m, not global n.
        ordered=sorted(values[lo:self.hi]);keys=[]
        for x in ordered:
            if not keys or x!=keys[-1]:keys.append(x)
        ranks=[bisect_left(keys,values[lo+i]) for i in range(m)]
        bit=[-1]*(len(keys)+1);a=source-lo
        def insert_node(v,parent):
            self.parent[v]=parent;self.depth[v]=1 if parent<0 else self.depth[parent]+1;self.up[0][v]=parent
            for j in range(1,self.levels):
                p=self.up[j-1][v];self.up[j][v]=-1 if p<0 else self.up[j-1][p]
                stats['lifting_setup_steps']+=1
        def update(v):
            i=ranks[v]+1
            while i<len(bit):bit[i]=self.better(bit[i],v);i+=i&-i;stats['fenwick_steps']+=1
        def query(r):
            best=-1
            while r:best=self.better(best,bit[r]);r-=r&-r;stats['fenwick_steps']+=1
            return best
        insert_node(a,-1);update(a)
        for v in range(a+1,m):
            p=query(ranks[v]) # strict value predecessor, excluding equal-value ranks
            if p>=0:insert_node(v,p);update(v)
        stats['source_trees']+=1;stats['background_positions_scanned']+=m
        stats['max_per_tree_array_length']=max(stats['max_per_tree_array_length'],m)
    def lift(self,v,steps):
        i=0
        while steps:
            if steps&1:v=self.up[i][v]
            steps>>=1;i+=1;self.stats['lifting_query_steps']+=1
        return v
    def lca(self,a,b):
        if self.depth[a]<self.depth[b]:a,b=b,a
        a=self.lift(a,self.depth[a]-self.depth[b])
        if a==b:return a
        for j in range(self.levels-1,-1,-1):
            self.stats['lifting_query_steps']+=1
            if self.up[j][a]!=self.up[j][b]:a,b=self.up[j][a],self.up[j][b]
        return self.parent[a]
    def better(self,a,b):
        self.stats['key_comparisons']+=1
        if a<0:return b
        if b<0:return a
        if self.depth[a]!=self.depth[b]:return a if self.depth[a]>self.depth[b] else b
        if a==b:return a
        z=self.lca(a,b);target=self.depth[z]+1
        aa=self.lift(a,self.depth[a]-target);bb=self.lift(b,self.depth[b]-target)
        # Global index =lo+local index; addition does not change lexicographic order.
        return a if aa<bb else b
    def path(self,target):
        v=target-self.lo
        if not 0<=v<self.m or self.depth[v]==0:return None
        out=[]
        while v>=0:out.append(self.lo+v);v=self.parent[v]
        return tuple(reversed(out))

def newstats():return {k:0 for k in ['source_trees','background_positions_scanned','max_per_tree_array_length','lifting_setup_steps','lifting_query_steps','fenwick_steps','key_comparisons','trace_vectors','trace_occurrence_visits']}

def trace_oracle(values,sample,lo,hi,stats):
    assert all(x is None or lo<=x<hi for x in sample), "sample occurrences must belong to the original interval"
    m=max(0,min(hi,len(values))-lo);real=sorted(x for x in sample if x is not None and lo<=x<min(hi,len(values)))
    selected=[]
    for x in real:
        if not selected or x!=selected[-1]:selected.append(x)
    d=len(selected);occ=[]
    for x in sample:
        if x is None or not lo<=x<min(hi,len(values)):occ.append(-1)
        else:
            z=bisect_left(selected,x);assert selected[z]==x;occ.append(z)
    selected_rank=[-1]*m
    for j,x in enumerate(selected):selected_rank[x-lo]=j
    out=[tuple(0 for _ in sample)]
    for j in range(d):out.append(tuple(int(z==j) for z in occ))
    for a in selected:
        tree=SourceTree(values,lo,hi,a,stats);near=[-1]*m
        for v in range(m):
            if tree.depth[v]:near[v]=v if selected_rank[v]>=0 else (-1 if tree.parent[v]<0 else near[tree.parent[v]])
        for b in selected:
            v=b-lo
            if not tree.depth[v]:continue
            flags=[False]*d
            while v>=0:
                z=selected_rank[v];assert z>=0;flags[z]=True
                p=tree.parent[v];v=-1 if p<0 else near[p]
            # Explicit occurrence vector: O(s) word work, NOT repeated giant-integer ORs.
            out.append(tuple(int(z>=0 and flags[z]) for z in occ));stats['trace_occurrence_visits']+=len(sample)
    assert len(out)<=len(sample)**2+len(sample)+1
    stats['trace_vectors']+=len(out)
    return out

def vector_masks(vectors):return {sum(int(b)<<i for i,b in enumerate(v)) for v in vectors}

def main():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();stats=newstats();checks={'permutation_inputs':0,'tied_value_inputs':0,'source_interval_endpoint_paths':0,'trace_multisets':0,'large_background_small_intervals':0}
    def check_paths(vals):
        n=len(vals)
        for lo in range(n):
            for hi in range(lo+1,n+1):
                ref=paths(vals,lo,hi)
                for a in range(lo,hi):
                    tree=SourceTree(vals,lo,hi,a,stats)
                    for b in range(lo,hi):assert tree.path(b)==ref.get((a,b));checks['source_interval_endpoint_paths']+=1
    for n in range(1,7):
        for vals in permutations(range(n)):check_paths(vals);checks['permutation_inputs']+=1
    for n in range(1,6):
        for vals in product(range(3),repeat=n):check_paths(vals);checks['tied_value_inputs']+=1
    for n in range(1,6):
        for vals in permutations(range(n)):
            pp=paths(vals)
            for mask in range(1<<n):
                sample=[i for i in range(n) if mask>>i&1]
                got=vector_masks(trace_oracle(vals,sample,0,n,stats));assert got==traces(pp,sample);checks['trace_multisets']+=1
    rng=random.Random(11431)
    for n in [8,16,31,64]:
        for _ in range(30):
            vals=rng.choices(range(max(2,n//2)),k=n);pp=paths(vals)
            lo=rng.randrange(n);hi=rng.randrange(lo+1,n+1)
            sample=[rng.randrange(lo,hi) if rng.randrange(5) else None for _ in range(12)]
            assert vector_masks(trace_oracle(vals,sample,lo,hi,stats))==traces(pp,sample);checks['trace_multisets']+=1
    # Same small primitive against a much larger background: no n-sized per-source arrays.
    vals=rng.sample(range(4096),4096)
    for lo,hi in [(2000,2016),(4080,4112)]:
        sample=[lo,lo+1,lo+3,lo+3,min(hi,len(vals))-1,None,4100 if hi>4100 else None]
        local=newstats();got=vector_masks(trace_oracle(vals,sample,lo,hi,local));reference=traces(paths(vals,lo,min(hi,len(vals))),sample);assert got==reference
        assert local['max_per_tree_array_length']<=min(hi,len(vals))-lo
        checks['large_background_small_intervals']+=1
    report={'started_at_utc':started,'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'passed_exact_fenwick_LCA_local_oracle_checks','scope':'Efficient canonical-path primitive checked against separate quadratic DP. All permutations through6, all ternary words through5, all selected subsets through5,120 tied/repeated/dummy random fixtures and2 interval-local allocation fixtures. Does not certify whole range-LIS theorem, infinite complexity or novelty.','checks':checks,'instrumentation':stats,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('fenwick-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':report['status'],'checks':checks,'instrumentation':stats}))
if __name__=='__main__':main()
