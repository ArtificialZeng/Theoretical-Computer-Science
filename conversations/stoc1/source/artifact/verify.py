"""Exhaustive finite validation; all numeric paper results originate here."""
import itertools as it
import json
import pathlib
from collections import defaultdict
from viable import Decoder, vocabulary

HERE = pathlib.Path(__file__).resolve().parent
ALPHABET = b'()[]'

def oracle(prefix):
    stack = []
    for c in prefix:
        if c in b'([': stack.append(c)
        elif c in b')]':
            if not stack or (stack.pop(), c) not in [(40,41),(91,93)]: return False
        else: return False
    return True

def nfa(matrix):
    m=len(matrix); edges=defaultdict(lambda:defaultdict(set)); final={'boundary','done'}
    def edge(q,c,r):edges[q][c].add(r)
    # Universal block. Share its initial boundary with the test prefix.
    for k in range(m):
        q='boundary' if k==0 else ('b',k)
        for c in '01':edge(q,c,('b',k+1))
    edge(('b',m),'#',('u',0))
    for k in range(m):edge(('u',k),'a',('u',k+1))
    edge(('u',m),'!','boundary')
    # Before witness selection, only the bit position is retained.
    for j in range(1,m+1):
        q='boundary' if j==1 else ('e',j-1)
        if j<m:
            for c in '01':edge(q,c,('e',j))
        edge(q,'1',('c',j,m-j))
        for k in range(m-j,0,-1):
            for c in '01':edge(('c',j,k),c,('c',j,k-1))
        edge(('c',j,0),'#',('r',j,0))
        for i in range(m):edge(('r',j,i),'a',('r',j,i+1))
        for i in range(1,m+1):
            if matrix[i-1][j-1]:edge(('r',j,i),'?','done')
    # Independently calculate coaccessibility, not a completion cutoff.
    reverse=defaultdict(set)
    for q,trans in edges.items():
        for targets in trans.values():
            for r in targets:reverse[r].add(q)
    live=set(final); frontier=list(final)
    while frontier:
        for q in reverse[frontier.pop()]:
            if q not in live:live.add(q);frontier.append(q)
    return edges,final,live

def run(edges,text):
    states={'boundary'}
    for c in text:states=set().union(*(edges[q].get(c,set()) for q in states)) if states else set()
    return states

def main():
    vocab=vocabulary()
    expected=[bytes(v) for length in range(1,5) for v in it.product(ALPHABET,repeat=length)]
    assert vocab==expected
    prefix_count=bit_count=0
    for length in range(7):
        for raw in it.product(ALPHABET,repeat=length):
            prefix=bytes(raw)
            with Decoder() as d:
                assert d.commit(prefix)==oracle(prefix)
                actual,_=d.mask()
            want=sum(1<<i for i,v in enumerate(vocab) if oracle(prefix+v))
            assert actual==want,(prefix,actual,want)
            prefix_count+=1;bit_count+=len(vocab)
    depths=[0,1,4,16,64,256,1024,4096]
    depth_rows=[]
    for depth in depths:
        prefix=b'(['*(depth//2)+(b'(' if depth%2 else b'')
        with Decoder() as d:
            assert d.commit(prefix)
            actual,copied=d.mask()
            want=sum(1<<i for i,v in enumerate(vocab) if oracle(prefix+v))
            assert actual==want
            depth_rows.append({'depth':depth,'copied_words':copied})
    matrix_count=probes=live_prefixes=0
    for m in range(1,4):
        for entries in it.product(range(2),repeat=m*m):
            matrix=[entries[i*m:(i+1)*m] for i in range(m)]
            edges,final,live=nfa(matrix);matrix_count+=1
            for v in it.product(range(2),repeat=m):
                text=''.join(map(str,v))+'#'
                for i in range(1,m+1):
                    actual=bool(run(edges,text+'a'*i+'?') & final)
                    want=any(a and b for a,b in zip(matrix[i-1],v))
                    assert actual==want,(matrix,v,i)
                    probes+=1
                trace=text+'a'*m+'!'
                # Check all prefixes on two consecutive blocks as well.
                for k in range(len(trace*2)+1):
                    assert run(edges,(trace*2)[:k]) & live
                    live_prefixes+=1
    result={'vocabulary_size':len(vocab),'max_token_length':4,
            'dyck_prefixes':prefix_count,'dyck_mask_bits':bit_count,
            'depth_mask_bits':len(depths)*len(vocab),'false_positives':0,'false_negatives':0,
            'matrices':matrix_count,'matrix_probes':probes,
            'universal_live_prefix_checks':live_prefixes,'depth_rows':depth_rows,
            'scope':'finite correctness and operation counts; no serving or model benchmarks'}
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    rows=[('Dyck vocabulary / maximum length',f'{len(vocab)} / 4'),
          ('All byte prefixes of length at most 6',f'{prefix_count:,}'),
          ('Exhaustively compared mask bits',f'{bit_count:,}'),
          ('Additional depth-test mask bits',f'{len(depths)*len(vocab):,}'),
          ('Matrices of orders 1 through 3',f'{matrix_count:,}'),
          ('Exact matrix-row probes',f'{probes:,}'),
          ('Universal-prefix liveness checks',f'{live_prefixes:,}'),
          ('False-positive / false-negative bits','0 / 0'),
          ('Stack depths in operation test','0--4,096'),
          ('64-bit row words copied at each depth',str(depth_rows[0]['copied_words']))]
    tex='\\begin{table}[t]\n\\caption{Actual deterministic validation coverage. Depth tests use eight specified depths; the interval does not denote exhaustive depth coverage. No timing values are inferred.}\\label{tab:validation}\n\\small\n\\begin{tabularx}{\\columnwidth}{@{}Xr@{}}\\toprule\nCheck & Count\\\\\\midrule\n'
    tex+='\n'.join(a+' & '+b+'\\\\' for a,b in rows)
    tex+='\n\\bottomrule\\end{tabularx}\n\\end{table}\n'
    (HERE/'validation_table.tex').write_text(tex)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
