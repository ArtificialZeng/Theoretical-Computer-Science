"""Cheap triage checks, not a search for an unknown d>1 upcycle.

Run: python3 evidence/triage_sanity.py > evidence/triage-sanity.json
Only standard library; outputs reproducible literal checks and safe mask orbits.
"""
import hashlib
import itertools
import json
import re
from pathlib import Path


def literal(u, n, a=2):
    counts = [0] * (a ** n)
    ds = []
    for i in range(len(u)):
        w = [u[(i+k) % len(u)] for k in range(n)]
        holes = [k for k, c in enumerate(w) if c == '*']
        ds.append(len(holes))
        for replacement in itertools.product(range(a), repeat=len(holes)):
            expanded = w.copy()
            for k, c in zip(holes, replacement):
                expanded[k] = str(c)
            index = 0
            for c in expanded:
                index = a*index + int(c)
            counts[index] += 1
    d = ds[0] if len(set(ds)) == 1 else None
    nontrivial = '*' in u and any(c != '*' for c in u)
    length_ok = d is not None and len(u) == a**(n-d)
    unique = all(c == 1 for c in counts)
    return dict(length=len(u), n=n, a=a, diamondicities=sorted(set(ds)),
                nontrivial=nontrivial, length_identity=length_ok,
                missing=sum(c == 0 for c in counts),
                multiply_covered=sum(c > 1 for c in counts),
                coverage_min=min(counts), coverage_max=max(counts),
                valid=unique and nontrivial and length_ok and len(u) > n)


def pairwise(u, n):
    for i in range(len(u)):
        for j in range(i+1, len(u)):
            if not any(u[(i+k) % len(u)] != '*' and
                       u[(j+k) % len(u)] != '*' and
                       u[(i+k) % len(u)] != u[(j+k) % len(u)]
                       for k in range(n)):
                return False
    return True


def rotations(s):
    return [s[k:]+s[:k] for k in range(len(s))]


def orbit(s):
    return set(rotations(s) + rotations(s[::-1]))


def period(s):
    return next(m for m in range(1, len(s)+1)
                if len(s) % m == 0 and s == s[:m]*(len(s)//m))


def curtained(s):
    return any(all(s[i] == '*' or s[len(s)-k+i] == '*'
                   for i in range(k)) for k in range(1, len(s)+1))


def masks(n, d):
    classes = {}
    for holes in itertools.combinations(range(n), d):
        s = ''.join('*' if k in holes else '.' for k in range(n))
        canonical = min(orbit(s))
        classes.setdefault(canonical, set()).add(s)
    result = []
    for s, members in sorted(classes.items()):
        m = period(s)
        pane = s[:m]
        result.append(dict(mask=s, orbit_size=len(members), period=m,
                           passes_source_8_7=any(not curtained(t)
                                                for t in rotations(pane))))
    assert sum(c['orbit_size'] for c in result) == len(list(itertools.combinations(range(n), d)))
    return dict(n=n, d=d, raw_masks=sum(len(v) for v in classes.values()),
                dihedral_classes=result)


def main():
    text = Path('intake/paper.txt').read_text()
    block = text.split('Proof. Each of the following cyclic partial words')[1].split('The computer search')[0]
    examples = ['001*110*'] + [re.sub(r'\s+', '', s).replace('⋄', '*')
                             for s in re.findall(r'\(([^()]*)\)', block)]
    assert len(examples) == 8
    controls = []
    for i, u in enumerate(examples):
        n = 4 if i == 0 else 8
        r = literal(u, n)
        assert r['valid'] and pairwise(u, n)
        controls.append(dict(label=f'source_example_{i}', word=u, **r))
    bad = [('flipped_ordinary', '101*110*', 4),
           ('doubled_good', '001*110*'*2, 4),
           ('linear_upword_read_cyclically', '**0111', 3),
           ('degenerate_single_wildcard', '*', 4)]
    for label, u, n in bad:
        r = literal(u, n)
        assert not r['valid']
        controls.append(dict(label=label, word=u, **r))
    exhaustive = []
    for bits in itertools.product('01', repeat=6):
        u = ''.join(bits[:3])+'*'+''.join(bits[3:])+'*'
        r = literal(u, 4)
        assert r['valid'] == pairwise(u, 4)
        if r['valid']:
            exhaustive.append(u)
    xor_clauses = [(1,2,-3), (-1,-2,-3), (1,-2,3), (-1,2,3)]
    rows = []
    for x,y,z in itertools.product([False, True], repeat=3):
        values = [None,x,y,z]
        sat = all(any(values[abs(t)] if t>0 else not values[abs(t)]
                      for t in c) for c in xor_clauses)
        assert sat == (z == (x != y))
        rows.append(dict(x=x,y=y,z=z,clauses_hold=sat))
    print(json.dumps(dict(job_id='c012-upcycles-triage-8176c8933a92',
        classification='sanity checks; no unknown-parameter SAT searches run',
        source_sha256=hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        controls=controls,
        all_64_fixed_frame_n4_assignments_agree=True,
        n4_valid_fixed_frame_assignments=exhaustive,
        xor_truth_table=rows,
        masks=[masks(8,2), masks(8,3)]), indent=2))


if __name__ == '__main__':
    main()
