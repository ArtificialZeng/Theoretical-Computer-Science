"""Standalone exact verifier: no solver, graph, builder, or earlier imports.

Enumerates ALL total words and tests literal compatibility at ALL cyclic
starting indices. Independently checks every pair for an ordinary mismatch.
It reads only a plain witness JSON; no SAT model is trusted.
"""
import hashlib
import itertools
import json
from pathlib import Path
import time


def literal_inverse(word,n,a):
    L=len(word)
    windows=[tuple(word[(i+j)%L] for j in range(n)) for i in range(L)]
    inverse=[]
    counts=[]
    for letters in itertools.product(tuple(str(x) for x in range(a)),repeat=n):
        starts=[]
        for i,window in enumerate(windows):
            if all(c=='*' or c==b for c,b in zip(window,letters)):
                starts.append(i)
        counts.append(len(starts))
        inverse.append(starts[0] if len(starts)==1 else starts)
    ds=sorted({w.count('*') for w in windows})
    periodic=all((word[i]=='*')==(word[(i+n)%L]=='*') for i in range(L))
    return dict(a=a,n=n,length=L,diamondicities=ds,diamond_periodic=periodic,
                length_identity=len(ds)==1 and L==a**(n-ds[0]),
                nontrivial='*' in word and any(c!='*' for c in word) and L>n,
                coverage_counts=counts,unique_start_by_lexicographic_total_word=inverse,
                valid=all(c==1 for c in counts) and len(ds)==1 and periodic and
                      L==a**(n-ds[0]) and L>n and '*' in word and
                      any(c!='*' for c in word))


def pair_certificate(word,n):
    offsets=[]
    failures=[]
    L=len(word)
    for i in range(L):
        for j in range(i+1,L):
            k=next((k for k in range(n) if word[(i+k)%L]!='*' and
                    word[(j+k)%L]!='*' and word[(i+k)%L]!=word[(j+k)%L]),None)
            offsets.append(k)
            if k is None:
                failures.append([i,j])
    return dict(order='i=0..L-1 then j=i+1..L-1',pair_count=len(offsets),
                first_ordinary_conflict_offsets=offsets,failures=failures,
                all_pairs_incompatible=not failures)


def main():
    start=time.monotonic()
    base=Path('evidence/research2-witness')
    data=json.loads((base/'witness.json').read_text())
    word,n,a=data['word'],data['n'],data['a']
    assert set(word)<=set('*01') and a==2 and n==12 and len(word)==512
    inverse=literal_inverse(word,n,a)
    assert inverse['valid'] and inverse['diamondicities']==[3]
    assert sorted(inverse['unique_start_by_lexicographic_total_word']).count(0)==8
    assert all(inverse['unique_start_by_lexicographic_total_word'].count(i)==8 for i in range(512))
    pairs=pair_certificate(word,n)
    assert pairs['pair_count']==130816 and pairs['all_pairs_incompatible']
    # Directly validate every saved pair offset against the serialized word.
    c=0
    for i in range(512):
        for j in range(i+1,512):
            k=pairs['first_ordinary_conflict_offsets'][c]
            assert 0<=k<12 and word[(i+k)%512] in '01' and word[(j+k)%512] in '01'
            assert word[(i+k)%512]!=word[(j+k)%512]
            c+=1
    controls=json.loads(Path('evidence/triage-sanity.json').read_text())['controls'][:2]
    tests=[]
    for control in controls:
        checked=literal_inverse(control['word'],control['n'],2)
        assert checked['valid']
        tests.append(dict(label=control['label'],expected=True,actual=checked['valid']))
    bads=[('bad_n4_bit','101*110*',4),('bad_n4_zero','000*000*',4)]
    ordinary=next(i for i,c in enumerate(word) if c!='*')
    flipped=word[:ordinary]+('1' if word[ordinary]=='0' else '0')+word[ordinary+1:]
    bads.extend([('bad_n12_bit',flipped,12),('bad_n12_all_zero',''.join('*' if c=='*' else '0' for c in word),12)])
    for label,bad,order in bads:
        # A single incompatible pair certificate failure suffices to reject it;
        # also run all-total-word counts for the two source-sized controls.
        conflicts=pair_certificate(bad,order)
        assert not conflicts['all_pairs_incompatible']
        test=dict(label=label,expected=False,actual=False,
                  number_of_compatible_window_pairs=len(conflicts['failures']),
                  first_compatible_pair=conflicts['failures'][0])
        if order==4:
            checked=literal_inverse(bad,order,2)
            assert not checked['valid']
            test['literal_counts_reject']=True
        tests.append(test)
    # Closing windows are checked too: exactly 11 wrap, covering 88 distinct
    # total words that a linear-only check would omit.
    wraps=[i for i in range(512) if i+12>512]
    assert len(wraps)==11
    wrap_words=[i for i,s in enumerate(inverse['unique_start_by_lexicographic_total_word']) if s in wraps]
    assert len(wrap_words)==88
    report=dict(job_id='c012-upcycles-research-456cb4499028',
                verifier='standalone all-words/all-starts literal comparison and separate pairwise ordinary conflicts',
                solver_or_builder_imported=False,all_total_words=4096,all_cyclic_starts=512,
                all_window_pairs=130816,word_sha256=hashlib.sha256(word.encode()).hexdigest(),
                minimum_count=min(inverse['coverage_counts']),maximum_count=max(inverse['coverage_counts']),
                diamondicities=inverse['diamondicities'],diamond_periodic=inverse['diamond_periodic'],
                wildcard_positions_exactly_mod4_zero=all((c=='*')==(i%4==0) for i,c in enumerate(word)),
                wrap_start_count=11,words_unique_to_wrap_starts=88,tests=tests,
                valid_original_scope_witness=True,elapsed_seconds=time.monotonic()-start)
    for name,body in [('inverse-coverage.json',inverse),('pair-conflicts.json',pairs),('standalone-verification.json',report)]:
        (base/name).write_text(json.dumps(body,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':
    main()
