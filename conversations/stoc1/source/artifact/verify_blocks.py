"""Finite independent set-oracle checks plus logical compiled table payloads."""
from pathlib import Path
from itertools import product
from array import array
import json
from block_index import BlockIndex
from viable import lib

HERE=Path(__file__).resolve().parent

def step(active,edges):
    return {j for i in active for j in edges[i]}
def output(active,labels):
    result=set()
    for i in active:result.update(labels[i])
    return sum(1<<i for i in result)
def edges_from_rows(rows,s):return [{j for j in range(s) if (r>>j)&1} for r in rows]

def validate():
    queries=pushes=pops=0
    label_rows={0:[5,6],1:[8,3]}
    label_sets={q:edges_from_rows(rows,4) for q,rows in label_rows.items()}
    for packed in range(256):
        trans={c:[(packed>>(c*4+i*2))&3 for i in range(2)] for c in range(2)}
        edges={c:edges_from_rows(rows,2) for c,rows in trans.items()}
        for initial in range(4):
            for b in [1,2]:
                index=BlockIndex(trans,label_rows,2,b,4)
                # Explicit persistent parent stack, compared with independent set transitions.
                stack=[initial]
                def walk(active,depth):
                    nonlocal queries,pushes,pops
                    for q in range(2):
                        assert index.mask(stack[-1],q)==output(active,label_sets[q]);queries+=1
                    if depth==5:return
                    for c in range(2):
                        old=stack[-1];stack.append(index.push(old,c));pushes+=1
                        next_active=step(active,edges[c])
                        assert stack[-1]==sum(1<<i for i in next_active)
                        walk(next_active,depth+1)
                        stack.pop();pops+=1;assert stack[-1]==old
                walk({i for i in range(2) if (initial>>i)&1},0)
    # A larger fixed classifier: exhaust all 256 active sets for every b.
    s=8;trans={0:[(1<<i)|(1<<((i+1)%s)) for i in range(s)],1:[1<<((3*i+1)%s) for i in range(s)]}
    labels={0:[1<<i for i in range(s)],1:[1<<((i+3)%s) for i in range(s)]}
    payload=[];larger=0
    for b in [1,2,3,4,8]:
        index=BlockIndex(trans,labels,s,b,8)
        for active in range(1<<s):
            aset={i for i in range(s) if active>>i&1}
            for c in range(2):
                want=step(aset,edges_from_rows(trans[c],s))
                assert index.push(active,c)==sum(1<<i for i in want);larger+=1
            for q in range(2):
                assert index.mask(active,q)==output(aset,edges_from_rows(labels[q],8));larger+=1
        payload.append({'block_bits':b,'groups':len(index.groups),'payload_words':index.payload_words,'payload_bytes':index.payload_words*8,'query_group_lookups':len(index.groups),'push_group_lookups':len(index.groups)})
    return {'exhaustive_nfas':256,'initial_sets_per_nfa':4,'prefix_depth_limit':5,'block_choices':[1,2],'mask_comparisons':queries,'push_comparisons':pushes,'pop_restorations':pops,'larger_classifier_comparisons':larger,'payload_rows':payload,'rust_allocated_mask_words':lib.viable_mask_table_words(),'rust_allocated_mask_payload_bytes':8*lib.viable_mask_table_words()}

def dyck_compile_growth():
    result=[]
    for L in range(1,6):
        vocab=[bytes(p) for k in range(1,L+1) for p in product(b'()[]',repeat=k)]
        B=(len(vocab)+63)//64;num_rows=1<<(L+1);table=array('Q',[0])*(num_rows*B)
        for h in range(1,num_rows):
            depth=h.bit_length()-1;base=[(h>>j)&1 for j in reversed(range(depth))]
            for i,token in enumerate(vocab):
                stack=base.copy();ok=True
                for c in token:
                    if c==40:stack.append(0)
                    elif c==91:stack.append(1)
                    elif not stack or stack.pop()!=(0 if c==41 else 1):ok=False;break
                if ok:table[h*B+i//64]|=1<<(i%64)
        binary=table.tobytes();assert len(binary)==num_rows*B*8
        result.append({'L':L,'vocabulary_size':len(vocab),'valid_classes':num_rows-1,'allocated_rows':num_rows,'words_per_row':B,'payload_bytes':len(binary)})
        if L==4:assert len(binary)==lib.viable_mask_table_words()*8
    return result

if __name__=='__main__':
    r=validate();r['dyck_compilation_growth']=dyck_compile_growth()
    (HERE/'block_results.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
