"""Exact finite checks for the divisor-profile hash lemmas; no asymptotic certification."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, lcm
import json, random
from pathlib import Path

def divs(M): return [d for d in range(2,M+1) if M%d==0]
def dot(u,v,M): return sum(a*b for a,b in zip(u,v))%M
def order(v,M): return lcm(*(M//gcd(M,x) for x in v))
def add3(a,b,c,M): return tuple((x+y+z)%M for x,y,z in zip(a,b,c))
def label(x,M,d): return tuple(a%(M//d) for a in x)

out={'coverage':{},'failures':[]}
# Exhaustive rows and vectors, dimension two, including mixed prime powers.
checks=0
for M in [2,3,4,6,8,12,18]:
    G=list(product(range(M),repeat=2))
    primes=[p for p in divs(M) if all(p%j for j in range(2,p))]
    for v in G:
        d=order(v,M)
        full=sum(dot(u,v,M)==0 for u in G)
        assert full*d==len(G)
        checks+=1
        for p in primes:
            lower=sum(dot(u,v,M)%(M//p)==0 for u in G)
            assert lower*d==len(G)*gcd(d,p)
            checks+=1
out['coverage']['exhaustive_row_marginals']={'moduli':[2,3,4,6,8,12,18],'dimension':2,'identities_checked':checks}
# Exact original-class bucketing, fragmented sublists, and all triple counts.
rng=random.Random(3974)
profile_instances=0
fragmented_classes=0
semantics=0
for M,r in [(4,2),(6,2),(8,2),(12,2)]:
    G=list(product(range(M),repeat=r)); ds=divs(M)
    for repeat in range(4):
        lists=[rng.sample(G,min(12,len(G))) for _ in range(3)]
        buckets=[]
        original_counts=[]
        for S in lists:
            counts={d:Counter(label(x,M,d) for x in S) for d in ds}
            original_counts.append(counts)
            b=defaultdict(list)
            for x in S:
                prof=tuple(1<<(counts[d][label(x,M,d)].bit_length()-1) for d in ds)
                b[prof].append(x)
            buckets.append(b)
        for triple in product(*(b.items() for b in buckets)):
            profiles=[z[0] for z in triple]; U=[z[1] for z in triple]
            ss={d:min(profiles[i][j] for i in range(3)) for j,d in enumerate(ds)}
            n=max(map(len,lists)); R=8; sigma=2
            ell=0
            while any(d**ell*sigma<ss[d]*R for d in ds):ell+=1
            e=next(d for d in ds if d**(ell-1)*sigma<ss[d]*R)
            p=next(p for p in divs(e) if all(p%j for j in range(2,p)))
            q=0
            while p**(q+1)<=R:q+=1
            D=p**q
            assert e**ell*sigma<e*ss[e]*R
            hist=Counter(order(add3(*t,M),M) for t in product(*U))
            for d in ds:
                Td=sum(z for f,z in hist.items() if d%f==0)
                assert Td<=2*ss[d]*n*n
                represented={label(x,M,d) for x in U[0]}
                assert len(represented)*profiles[0][ds.index(d)]<=n
            EF=sum(Fraction(z,d**ell) for d,z in hist.items() if d>1 and e%d==0)
            EZ=sum(Fraction(z*gcd(d,p)**q,d**ell) for d,z in hist.items() if d>1 and e%d==0)
            assert EF<=Fraction(2*len(ds)*sigma*n*n,R)
            assert EZ<=2*len(ds)*sigma*n*n
            if ell>=q:
                rows=[rng.choice(G) for _ in range(ell)]
                k=ell-q
                def pi(x):return (label(x,M,e),tuple(dot(u,x,M) for u in rows[:k]),tuple(dot(u,x,M)%(M//p) for u in rows[k:]))
                def K(x):return (label(x,M,e),tuple(dot(u,x,M) for u in rows))
                H=e**ell//D
                for i in range(3):
                    bycos=defaultdict(set)
                    for x in U[i]:bycos[label(x,M,e)].add(pi(x))
                    assert all(len(vals)<=H for vals in bycos.values())
                    assert len({pi(x) for x in U[i]})<=M*M*n/sigma
                    fragmented_classes+=sum(len([x for x in U[i] if label(x,M,e)==c])<original_counts[i][e][c] for c in bycos)
                # The one-hash support product and exact probe interpretation.
                blocks=[]
                for i in [1,2]:
                    groups=defaultdict(list)
                    for x in U[i]:groups[pi(x)].append(x)
                    blocks.append([v[j:j+sigma] for v in groups.values() for j in range(0,len(v),sigma)])
                zero=(0,)*r
                for x in U[0]:
                    for b2,b3 in product(*blocks):
                        if pi(add3(x,b2[0],b3[0],M))!=pi(zero):continue
                        a=tuple(dot(u,add3(x,b2[0],b3[0],M),M)//(M//p) for u in rows[k:])
                        assert all(dot(u,add3(x,b2[0],b3[0],M),M)%(M//p)==0 for u in rows[k:])
                        q1=(q+1)//2; mu1=a[:q1];mu2=a[q1:]
                        SX=set();SY=set()
                        for y in b2:
                            delta=tuple((dot(u,y,M)-dot(u,b2[0],M))%M for u in rows[k:])
                            assert all(v%(M//p)==0 for v in delta)
                            z=tuple(v//(M//p) for v in delta)
                            SX.add(tuple((z[j]+(mu1[j] if j<q1 else 0))%p for j in range(q)))
                        for y in b3:
                            delta=tuple((dot(u,y,M)-dot(u,b3[0],M))%M for u in rows[k:])
                            z=tuple(v//(M//p) for v in delta)
                            SY.add(tuple((-z[j]-(mu2[j-q1] if j>=q1 else 0))%p for j in range(q)))
                        truth=any(K(add3(x,y,z,M))==K(zero) for y,z in product(b2,b3))
                        assert bool(SX&SY)==truth
                        semantics+=1
            profile_instances+=1
out['coverage']['profile_bucketing']={'moduli':[4,6,8,12],'dimension':2,'original_list_size':12,'input_triples':16,'profile_subinstances':profile_instances,'fragmented_cosets_checked':fragmented_classes,'support_probe_semantics_checked':semantics,'note':'R=8,sigma=2 diagnostic parameters; not asymptotic parameter regime.'}
# Exact parameter inequalities at large n, without constructing enormous lists.
parameter_checks=0
for M in [2,4,6,8,12,18,30,60]:
    ds=divs(M); C=(M-1).bit_length(); eta=min(Fraction(1,18),Fraction(1,8*C))
    for b in [256,1024,4096]:
        n=1<<b; R=1<<((eta.numerator*b)//eta.denominator)
        if R<M:continue
        # Conservative sigma <=sqrt(R) and sigma>=1 suffice for the selection check.
        sigma=1<<(R.bit_length()//2-2)
        for trial in range(50):
            ss={d:1<<rng.randrange(0,b) for d in ds};ss[M]=1<<(b//2)
            ell=0
            while any(d**ell*sigma<ss[d]*R for d in ds):ell+=1
            e=next(d for d in ds if d**(ell-1)*sigma<ss[d]*R)
            p=next(p for p in divs(e) if all(p%j for j in range(2,p)))
            q=0
            while p**(q+1)<=R:q+=1
            assert ell>=q>=1
            assert e**ell*sigma<e*ss[e]*R
            assert p**q*M>=R
            parameter_checks+=1
out['coverage']['parameter_profiles']={'moduli':[2,4,6,8,12,18,30,60],'n_binary_exponents':[256,1024,4096],'profiles_checked':parameter_checks,'note':'Adversarial arbitrary divisor sizes, not necessarily realizable; sigma diagnostic <=sqrt(R).'}
out['status']='all_assertions_passed'
Path('evidence/divisor-hash-tests.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
