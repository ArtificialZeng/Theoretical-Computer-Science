#!/usr/bin/env python3
"""Exact finite-automaton SCC decision prototype; finite controls are not proofs."""
from collections import deque
from functools import cmp_to_key
from itertools import product, combinations
from pathlib import Path
import json
import random

class NFA:
    def __init__(self, count, start, finals, edges):
        self.n, self.start, self.finals, self.edges = count, start, set(finals), edges
    def reverse(self):
        # A fresh start supports multiple old finals, including epsilon acceptance.
        edges = [(b,a,c) for a,b,c in self.edges]
        edges += [(self.n,f,None) for f in self.finals]
        return NFA(self.n+1,self.n,{self.start},edges)
    def append(self, word):
        edges = list(self.edges)
        hub=self.n
        edges += [(f,hub,None) for f in self.finals]
        end=hub
        for c in word:
            edges.append((end,end+1,c)); end+=1
        return NFA(end+1,self.start,{end},edges)
    def eliminate_epsilon(self):
        eps=[[] for _ in range(self.n)]
        raw=[{} for _ in range(self.n)]
        alphabet=set()
        for a,b,c in self.edges:
            if c is None: eps[a].append(b)
            else:
                alphabet.add(c); raw[a].setdefault(c,set()).add(b)
        closures=[]
        for a in range(self.n):
            seen={a}; todo=[a]
            while todo:
                for b in eps[todo.pop()]:
                    if b not in seen: seen.add(b); todo.append(b)
            closures.append(seen)
        trans=[{} for _ in range(self.n)]
        final=set()
        for a in range(self.n):
            if closures[a]&self.finals: final.add(a)
            for c in alphabet:
                targets=set()
                for x in closures[a]:
                    for y in raw[x].get(c,()): targets.update(closures[y])
                if targets: trans[a][c]=targets
        live=set(final)
        changed=True
        while changed:
            changed=False
            for a in range(self.n):
                if a not in live and any(bs&live for bs in trans[a].values()):
                    live.add(a); changed=True
        positive={a for a in range(self.n) if any(bs&live for bs in trans[a].values())}
        return trans,final,live,positive


def singleton(word):
    return NFA(1,0,{0},[]).append(word)


def order_signs(X,Y):
    """Exact attained colex signs for independent x in X, y in Y."""
    x=X.reverse(); y=Y.reverse()
    tx,fx,lx,px=x.eliminate_epsilon()
    ty,fy,ly,py=y.eliminate_epsilon()
    todo=[(x.start,y.start)]; seen=set(); signs=set()
    while todo:
        a,b=todo.pop()
        if (a,b) in seen: continue
        seen.add((a,b))
        if a in fx and b in fy: signs.add(0)
        if a in fx and b in py: signs.add(-1)
        if b in fy and a in px: signs.add(1)
        for c,us in tx[a].items():
            for d,vs in ty[b].items():
                if c==d: todo.extend(product(us,vs))
                elif us&lx and vs&ly: signs.add(-1 if c<d else 1)
    return signs

class Machine:
    def __init__(self,n,alphabet,delta,outputs):
        self.n,self.alphabet,self.delta,self.outputs=n,alphabet,delta,outputs
        self._ranges={}
    def path(self,p,w):
        out=''
        for c in w:
            if (p,c) not in self.delta: return None
            out+=self.outputs[p,c]; p=self.delta[p,c]
        return p,out
    def range(self,p,input_labels=False):
        key=p,input_labels
        if key not in self._ranges:
            edges=[]; next_node=self.n
            for (a,c),b in self.delta.items():
                w=c if input_labels else self.outputs[a,c]
                if not w: edges.append((a,b,None)); continue
                at=a
                for j,d in enumerate(w):
                    target=b if j==len(w)-1 else next_node
                    if j!=len(w)-1: next_node+=1
                    edges.append((at,target,d)); at=target
            self._ranges[key]=NFA(next_node,0,{p},edges)
        return self._ranges[key]
    def state_order(self):
        less={}
        for p,r in combinations(range(self.n),2):
            signs=order_signs(self.range(p,True),self.range(r,True))
            if signs not in ({-1},{1}): return None
            less[p,r]=next(iter(signs))
        def cmp(p,r):
            if p==r:return 0
            return less[p,r] if p<r else -less[r,p]
        return sorted(range(self.n),key=cmp_to_key(cmp))
    def blocks(self,q,rank):
        # Blocks are (predecessor, suffix); None predecessor is initial epsilon.
        bs=[(p,a) for (p,a),r in self.delta.items() if r==q]
        bs.sort(key=lambda b:(b[1],rank[b[0]]))
        return ([(None,'')] if q==0 else [])+bs
    def block_range(self,block):
        p,z=block
        if p is None:
            run=self.path(0,z); assert run is not None
            return singleton(run[1])
        run=self.path(p,z); assert run is not None
        return self.range(p).append(run[1])
    def flags(self,order):
        rank={p:i for i,p in enumerate(order)}
        seeds={1:set(),-1:set()}
        cache={}
        for q in range(self.n):
            bs=self.blocks(q,rank)
            for i,j in combinations(range(len(bs)),2):
                pair=bs[i],bs[j]
                if pair not in cache: cache[pair]=order_signs(self.block_range(bs[i]),self.block_range(bs[j]))
                signs=cache[pair]
                if 1 in signs: seeds[1].add(q)
                if -1 in signs: seeds[-1].add(q)
        flags={}
        for e in (1,-1):
            bad=set(seeds[e]); todo=list(bad)
            while todo:
                p=todo.pop()
                for c in self.alphabet:
                    q=self.delta.get((p,c))
                    if q is not None and q not in bad:bad.add(q);todo.append(q)
            flags[e]=[q not in bad for q in range(self.n)]
        return flags
    def sccs(self):
        reach=[]
        for p in range(self.n):
            seen={p}; todo=[p]
            while todo:
                a=todo.pop()
                for c in self.alphabet:
                    b=self.delta.get((a,c))
                    if b is not None and b not in seen:seen.add(b);todo.append(b)
            reach.append(seen)
        seen=set(); components=[]
        for p in range(self.n):
            if p in seen:continue
            cc={q for q in range(self.n) if q in reach[p] and p in reach[q]}
            components.append(cc);seen.update(cc)
        return components
    def monotone_block_list(self,blocks,flags):
        ranges=[self.block_range(b) for b in blocks]
        allowed=[]
        for e in (1,-1):
            if any(p is not None and not flags[e][p] for p,z in blocks):continue
            if any(e in order_signs(ranges[i],ranges[j]) for i,j in combinations(range(len(blocks)),2)):continue
            allowed.append(e)
        return allowed
    def annuli(self,q,cc,rank):
        # Unroll exactly one backward cycle; keep the unique internal block.
        left=[];right=[];cur=q;suffix=''
        for _ in range(len(cc)):
            bs=self.blocks(cur,rank)
            internal=[i for i,(p,z) in enumerate(bs) if p in cc]
            assert len(internal)==1
            i=internal[0]
            extra_left=[(p,z+suffix) for p,z in bs[:i]]
            extra_right=[(p,z+suffix) for p,z in bs[i+1:]]
            left=left+extra_left
            right=extra_right+right
            cur,a=bs[i];suffix=a+suffix
        assert cur==q
        assert self.path(q,suffix)[0]==q
        return left,right,suffix
    def decide(self):
        order=self.state_order()
        if order is None:return {'member':False,'input_order':False}
        rank={p:i for i,p in enumerate(order)}
        flags=self.flags(order); checks=[];bounds={}
        for cc in self.sccs():
            internal=[(p,a,q) for (p,a),q in self.delta.items() if p in cc and q in cc]
            if not internal:continue
            simple=all(sum(p==r for p,a,q in internal)==1 for r in cc)
            if not simple:
                good=all(flags[1][q] or flags[-1][q] for q in cc)
                checks.append({'states':sorted(cc),'type':'branching','pass':good})
                if not good:return {'member':False,'input_order':True,'flags':flags,'checks':checks}
                bounds.update({q:1 for q in cc})
            else:
                q=min(cc);left,right,c=self.annuli(q,cc,rank)
                left2=left+[(p,z+c) for p,z in left]
                right2=[(p,z+c) for p,z in right]+right
                le=self.monotone_block_list(left2,flags)
                re=self.monotone_block_list(right2,flags)
                good=bool(le and re)
                checks.append({'states':sorted(cc),'type':'simple','cycle':c,
                               'left':left,'right':right,'left_orientations':le,
                               'right_orientations':re,'pass':good})
                if not good:return {'member':False,'input_order':True,'flags':flags,'checks':checks}
                bounds.update({r:2 for r in cc})
        while len(bounds)<self.n:
            changed=False
            for q in range(self.n):
                if q in bounds:continue
                predecessors=[p for (p,a),r in self.delta.items() if r==q]
                if all(p in bounds for p in predecessors):
                    bounds[q]=int(q==0)+sum(bounds[p] for p in predecessors);changed=True
            assert changed
        return {'member':True,'input_order':True,'flags':flags,'checks':checks,'piece_bounds':bounds}
    def words(self,limit):
        result=[[] for _ in range(self.n)];layer=[('',0,'')]
        for depth in range(limit+1):
            nxt=[]
            for w,p,out in layer:
                result[p].append((w,out))
                if depth<limit:
                    for a in self.alphabet:
                        if (p,a) in self.delta:
                            nxt.append((w+a,self.delta[p,a],out+self.outputs[p,a]))
            layer=nxt
        for ws in result:ws.sort(key=lambda x:x[0][::-1])
        return result


def min_pieces(values):
    # Independent interval DP, not the SCC recurrence. Exact for the finite list.
    n=len(values);dp=[0]+[n+1]*n
    for start in range(n):
        up=down=True
        for end in range(start,n):
            if end>start:
                up &= values[end-1]<=values[end]
                down &= values[end-1]>=values[end]
            if not (up or down):break
            dp[end+1]=min(dp[end+1],dp[start]+1)
    return dp[-1]


def accessible(delta,n):
    seen={0};todo=[0]
    while todo:
        p=todo.pop()
        for a in '01':
            q=delta.get((p,a))
            if q is not None and q not in seen:seen.add(q);todo.append(q)
    return len(seen)==n


def check_finite(T,decision,limit):
    if not decision['input_order']:return None
    ws=T.words(limit); finite=[]
    for q,samples in enumerate(ws):
        values=[o[::-1] for w,o in samples]
        up=all(a<=b for a,b in zip(values,values[1:]))
        down=all(a>=b for a,b in zip(values,values[1:]))
        assert not decision['flags'][1][q] or up
        assert not decision['flags'][-1][q] or down
        k=min_pieces(values)
        if decision['member']:assert k<=decision['piece_bounds'][q],(q,k,decision)
        finite.append({'state':q,'samples':len(samples),'pieces':k,
                       'up':up,'down':down})
    return finite


def controls():
    records=[]
    for name,outs,expected in [('identity',['0','1'],True),('erasing',['',''],True),
          ('ordered_variable',['0','11'],True),('complement',['1','0'],False),
          ('length_only',['0','0'],False),('mixed_erasure',['','1'],False)]:
        T=Machine(1,'01',{(0,'0'):0,(0,'1'):0},{(0,'0'):outs[0],(0,'1'):outs[1]})
        d=T.decide();assert d['member']==expected,(name,d)
        f=check_finite(T,d,9)
        records.append({'name':name,'decision':d,'finite':f})
    delta={(0,'0'):1,(0,'1'):2,(2,'0'):1,(1,'0'):1}
    outputs={e:('0' if e==(1,'0') else '') for e in delta}
    T=Machine(3,'01',delta,outputs);d=T.decide();assert d['member']
    finite=check_finite(T,d,12);assert finite[1]['pieces']==2
    records.append({'name':'nested_turn_positive','decision':d,'finite':finite})
    # Unary one-state and a three-state cycle with erasure/variable outputs.
    T=Machine(1,'0',{(0,'0'):0},{(0,'0'):'10'});d=T.decide();assert d['member']
    records.append({'name':'unary','decision':d,'finite':check_finite(T,d,30)})
    return records


def main():
    results={'controls':controls(),'exhaustive':[],'random':{},'scope':
        'Exact NFA decision prototype. Finite sample and DP comparisons are controls, not a proof of the infinite theorem.'}
    total=members=rejects=input_pass=0
    for n in (1,2):
        count=good=bad=ip=0
        for table in product(range(-1,n),repeat=2*n):
            delta={(p,a):table[2*p+j] for p in range(n) for j,a in enumerate('01') if table[2*p+j]>=0}
            if not accessible(delta,n):continue
            dummy=Machine(n,'01',delta,{e:'' for e in delta})
            if dummy.state_order() is None:continue
            for vals in product(('','0','1'),repeat=len(delta)):
                T=Machine(n,'01',delta,dict(zip(delta,vals)))
                d=T.decide();check_finite(T,d,7)
                count+=1;good+=d['member'];bad+=not d['member'];ip+=d['input_order']
        results['exhaustive'].append({'states':n,'input_ordered_output_tables':count,
                                     'members':good,'nonmembers':bad,'word_length_control':7})
        total+=count;members+=good;rejects+=bad;input_pass+=ip
    rng=random.Random(1701001);count=good=bad=ip=0;attempts=0
    while count<600:
        attempts+=1;n=rng.choice((3,4,5))
        delta={(p,a):r for p in range(n) for a in '01' if (r:=rng.randrange(-1,n))>=0}
        if not accessible(delta,n):continue
        T=Machine(n,'01',delta,{e:rng.choice(('','0','1','00','01','10','11','001')) for e in delta})
        d=T.decide()
        if not d['input_order']:continue
        check_finite(T,d,8);count+=1;good+=d['member'];bad+=not d['member'];ip+=d['input_order']
    results['random']={'seed':1701001,'attempts':attempts,'input_ordered_tables':count,
                       'members':good,'nonmembers':bad,'states':[3,4,5],
                       'output_words':['','0','1','00','01','10','11','001'],
                       'word_length_control':8,'all_states_final':True}
    Path(__file__).with_name('membership-check.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'controls':len(results['controls']),'exhaustive':results['exhaustive'],
                      'random':results['random'],'status':'all checks passed'}))

if __name__=='__main__':main()
