#!/usr/bin/env python3
"""Exact serialized families plus finite replay; all-n justifications are in the note."""
from itertools import combinations
from pathlib import Path
import json
from check_membership import Machine, singleton, order_signs


def verify_family(name,T,x,pump,kind,direction):
    decision=T.decide()
    assert decision['input_order'] and not decision['member']
    q=T.path(0,x[0])[0]
    assert all(T.path(0,w)[0]==q for w in x)
    assert T.path(q,pump)[0]==q
    replay=list(range(12))+[17,31,257]
    for n in replay:
        words=[w+pump*n for w in x]
        outs=[T.path(0,w)[1] for w in words]
        assert words[0][::-1]<words[1][::-1]<words[2][::-1]
        if kind=='peak':assert outs[0][::-1]<outs[1][::-1]>outs[2][::-1]
        else:assert outs[0][::-1]>outs[1][::-1]<outs[2][::-1]
        nxt=[w+pump*(n+1) for w in x]
        if direction=='increasing':assert words[2][::-1]<nxt[0][::-1]
        else:assert nxt[2][::-1]<words[0][::-1]
    return {'name':name,'state_count':T.n,'alphabet':T.alphabet,'initial':0,
            'finals':list(range(T.n)),'terminal_outputs':'all empty',
            'transitions':[{'from':p,'input':a,'to':q,'output':T.outputs[p,a]}
                           for (p,a),q in sorted(T.delta.items())],
            'target_state':q,'templates':[{'x':w,'y':pump,'z':''} for w in x],
            'turn':kind,'interval_direction':direction,'replayed_n':replay,
            'decision':decision,'all_n_proof':'evidence/research-1-adversarial.md'}


def main():
    # Validate the range comparator independently on ALL finite binary languages
    # with words of length <=2 (128 languages, 16384 ordered pairs).
    words=['','0','1','00','01','10','11']
    from check_membership import NFA
    def finite_language(ws):
        edges=[];at=1;finals=[]
        for w in ws:
            cur=at;at+=1;edges.append((0,cur,None))
            for c in w:
                edges.append((cur,at,c));cur=at;at+=1
            finals.append(cur)
        return NFA(at,0,finals,edges)
    languages=[[w for j,w in enumerate(words) if bits>>j&1] for bits in range(128)]
    nfas=[finite_language(ws) for ws in languages]
    for i,X in enumerate(languages):
        for j,Y in enumerate(languages):
            expected={(-1 if x[::-1]<y[::-1] else 1 if x[::-1]>y[::-1] else 0) for x in X for y in Y}
            assert order_signs(nfas[i],nfas[j])==expected
    certificates=[]
    # A two-state branching SCC, rather than a one-state morphism-only example.
    delta={(p,a):int(a) for p in range(2) for a in '01'}
    outputs={e:('1' if e[1]=='0' else '0') for e in delta}
    T=Machine(2,'01',delta,outputs)
    # Start with the complement valley at state 0: 000<10<0010.
    # Return loops u=0,v=10 have distinct first letters. A=00,B=1010
    # are suffix-incomparable. Append A, then B^n to the base valley.
    certificates.append(verify_family('branching_two_state',T,
                       ['00000','1000','001000'],'1010','valley','increasing'))
    # Simple cycle, increasing annular side, unbounded regular predecessor range.
    delta={(0,'0'):1,(0,'1'):2,(1,'0'):1,(1,'1'):2,(2,'1'):2}
    outputs={(0,'0'):'0',(0,'1'):'',(1,'0'):'0',(1,'1'):'',(2,'1'):'0'}
    T=Machine(3,'01',delta,outputs)
    certificates.append(verify_family('simple_cycle_left_unbounded_prefix',T,
                       ['1','001','11'],'11','peak','increasing'))
    # Simple cycle, decreasing annular side, state-dependent erasure.
    delta={(0,'0'):1,(0,'1'):2,(0,'2'):2,(2,'0'):1,(1,'0'):1}
    outputs={(0,'0'):'',(0,'1'):'',(0,'2'):'1',(2,'0'):'',(1,'0'):'0'}
    T=Machine(3,'012',delta,outputs)
    certificates.append(verify_family('simple_cycle_right_erasing',T,
                       ['100','200','10'],'00','peak','decreasing'))
    result={'finite_language_comparator_pairs':16384,'finite_language_universe':words,
            'certificates':certificates,'status':'all exact assertions and finite replays passed',
            'limits':'Finite replays are implementation controls. All-n certificates follow the written structural argument; this is not a fresh referee audit.'}
    Path(__file__).with_name('exact-certificates.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'comparator_pairs':16384,'certificate_families':len(certificates),'status':'passed'}))

if __name__=='__main__':main()
