"""Failed local-only Fourier obstruction: reproducible exact finite check.

Only subsets of ordinary coordinates unique to one frame orientation are used.
Each must have zero sign sum across its four selected tiles. Normalizing one
tile to 00000 is valid for this local subcube-tiling relaxation, by translating
the total cube; it is NOT a cyclic-word coordinate symmetry.
"""
import itertools
import json
from pathlib import Path


def main():
    out=[]
    for mask in ['***.....','**.*....','**..*...','*.*.*...']:
        n=len(mask)
        frames=list(dict.fromkeys(mask[s:]+mask[:s] for s in range(n)))
        ordinary=[{i for i,c in enumerate(f) if c!='*'} for f in frames]
        O=sorted(ordinary[0])
        private=[set(S) for k in range(1,len(O)+1) for S in itertools.combinations(O,k)
                 if sum(set(S)<=T for T in ordinary)==1]
        local=[sum(1<<O.index(i) for i in S) for S in private]
        good=[]
        for other in itertools.combinations(range(1,32),3):
            C=(0,)+other
            if all(sum((x&s).bit_count()%2 for x in C)==2 for s in local):
                good.append(C)
        out.append(dict(mask=mask,ordinary_coordinates=O,
                        private_subsets=[sorted(S) for S in private],
                        normalized_local_codes=len(good),examples=good[:5]))
    return out


if __name__=='__main__':
    result=main()
    previous=json.loads(Path('evidence/research1-private-fourier-initial.json').read_text())
    assert json.loads(json.dumps(result))==previous
    print(json.dumps(result,indent=2))
