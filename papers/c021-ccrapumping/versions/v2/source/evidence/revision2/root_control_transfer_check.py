"""Finite controls for the unaccepted finite-control unipotent extension."""
from collections import deque
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json


def identity(d):
    return [[F(i == j) for j in range(d)] for i in range(d)]


def multiply(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b, scale=F(1)):
    return [[x+scale*y for x,y in zip(row,other)] for row,other in zip(a,b)]


def power(a, n):
    result=identity(len(a))
    while n:
        if n & 1:
            result=multiply(result,a)
        a=multiply(a,a)
        n//=2
    return result


def unipotent_power(a, exponent):
    """Finite binomial polynomial, applicable to every tested UT3 matrix."""
    d=len(a);nil=add(a,identity(d),F(-1));term=identity(d)
    answer=identity(d);coefficient=F(1)
    for j in range(1,d):
        term=multiply(term,nil)
        coefficient*=F(exponent-j+1,j)
        answer=add(answer,term,coefficient)
    assert power(nil,d)==[[0]*d for _ in range(d)]
    return answer


LETTERS=[[[F(1),F(b),F(b)],[F(0),F(1),F(1)],[F(0),F(0),F(1)]] for b in (0,1)]


def matrix(word):
    value=identity(3)
    for b in word:
        value=multiply(LETTERS[b],value)
    return value


def reachable(start, transitions):
    seen={start};todo=[start]
    while todo:
        q=todo.pop()
        for row in transitions:
            if row[q] not in seen:
                seen.add(row[q]);todo.append(row[q])
    return seen


def verify(transitions):
    n=len(transitions[0]);reach=[reachable(q,transitions) for q in range(n)]
    components={frozenset(v for v in range(n) if v in reach[q] and q in reach[v]) for q in range(n)}
    component=min((c for c in components if c<=reach[0] and all(row[q] in c for q in c for row in transitions)),key=lambda c:tuple(sorted(c)))
    states=sorted(component);renaming={q:i for i,q in enumerate(states)};s=len(states)
    letters=[tuple(renaming[row[q]] for q in states) for row in transitions]
    initial=tuple(range(s));words={initial:()};todo=deque([initial])
    while todo:
        current=todo.popleft()
        for a,row in enumerate(letters):
            nxt=tuple(row[x] for x in current)
            if nxt not in words:
                words[nxt]=words[current]+(a,);todo.append(nxt)
    t=min(words,key=lambda f:(len(set(f)),len(words[f]),words[f]));rank=len(set(t));N=factorial(rank)
    e=words[t]*N

    def control(word):
        f=initial
        for a in word:
            f=tuple(letters[a][x] for x in f)
        return f

    E=control(e);R=set(E)
    assert len(R)==rank and all(E[q]==q for q in R)
    base=matrix(e);inverse=unipotent_power(base,F(-1));blocks=[]
    for a in (0,1):
        word=e+(a,)+e;f=control(word)
        assert set(f)==R and {f[q] for q in R}==R
        returning=word*N;actual=control(returning)
        assert all(actual[q]==q for q in R)
        B=matrix(returning);U=unipotent_power(B,F(1,N))
        assert U==multiply(multiply(base,LETTERS[a]),base)
        assert multiply(multiply(inverse,U),inverse)==LETTERS[a]
        blocks.append(B)
    assert multiply(*blocks)!=multiply(*reversed(blocks))
    return s,rank,len(words),len(e)


def main():
    counts={};maxima={'semigroup':0,'e_length':0};ranks={}
    for n in (1,2,3):
        count=0
        for flat in product(range(n),repeat=2*n):
            s,rank,size,length=verify([flat[:n],flat[n:]])
            count+=1;maxima['semigroup']=max(maxima['semigroup'],size);maxima['e_length']=max(maxima['e_length'],length)
            ranks[(s,rank)]=ranks.get((s,rank),0)+1
        assert count==n**(2*n)
        counts[n]=count
    upper=[[1,1],[0,1]];lower=[[1,0],[1,1]]
    bad=multiply(upper,lower)
    assert sum(bad[i][i] for i in range(2))==3
    result={'verified':True,'complete_binary_control_DFAs':counts,'total':sum(counts.values()),'bottom_SCC_and_rank_histogram':{str(k):v for k,v in ranks.items()},'maxima':maxima,'checks':['complete finite control transformation semigroup','minimum rank and idempotent e','all return blocks fix the same image states','exact UT3 root/inverse recovery of original letters','noncommuting recovered witness matrices'],'generator_only_promise_counterexample':'Two unipotent 2x2 generators have product trace3, not unipotent','scope':'Finite controls for a new unaccepted all-word-unipotent generalization. No fresh referee acceptance or all-register theorem is certified.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
