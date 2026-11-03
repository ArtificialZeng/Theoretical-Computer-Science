"""Bounded exact implementation attacks; the universal theorem is a written proof.

Run from the project directory. No subprocesses, network, or background work.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import random

ROOT = Path(__file__).resolve().parent
JOB = 'c037-msthalf-research-d39900f29f79'


def rectangle_min(d, w, r):
    n = len(d)
    t = [0]
    for x in w:
        t.append(t[-1] + x)
    adj = [sum(1 << j for j in range(n)
               if j != i and d[i][j] <= abs(t[i] - t[j])) for i in range(n)]
    least = r*r
    for aa in combinations(range(n), r):
        mask = sum(1 << a for a in aa)
        ds = sorted((adj[b] & mask).bit_count()
                    for b in range(n) if not (mask >> b & 1))
        least = min(least, sum(ds[:r]))
    return least


def mst(d):
    n = len(d)
    have = {0}
    cost = 0
    while len(have) < n:
        length, _, b = min((d[a][b], a, b) for a in have
                           for b in range(n) if b not in have)
        cost += length
        have.add(b)
    return cost


def make_metric(n, family, rng):
    if family == 'line':
        x = [0]
        for _ in range(n-1):
            x.append(x[-1] + rng.choice([1, 2, 17, 10000]))
        return [[abs(a-b) for b in x] for a in x]
    if family == 'L1':
        pts = [(i, rng.randrange(20), rng.choice([0, 10000])) for i in range(n)]
        return [[sum(abs(a-b) for a,b in zip(x,y)) for y in pts] for x in pts]
    inf = 10**15
    d = [[0 if i == j else inf for j in range(n)] for i in range(n)]
    for i in range(n):
        j = (i+1) % n
        d[i][j] = d[j][i] = rng.choice([1, 3, 101, 100000])
    if family == 'graph':
        for i,j in combinations(range(n),2):
            if rng.randrange(5) == 0:
                d[i][j] = d[j][i] = min(d[i][j], rng.choice([2, 19, 10007]))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d


def metric_suite():
    rng = random.Random(3703)
    records = []
    calls = 0
    for n in [8, 12, 16, 24]:
        for family in ['line', 'cycle', 'L1', 'graph']:
            for trial in range(4):
                raw = make_metric(n, family, rng)
                order = list(range(n))
                rng.shuffle(order)
                d = [[raw[i][j] for j in order] for i in order]
                settings = [(2,1), (2,2)]
                if n <= 12:
                    settings.append((3,2))
                for r,h in settings:
                    w = [d[i][i+1] for i in range(n-1)]
                    for _ in range(2):
                        indices = list(range(n-1))
                        rng.shuffle(indices)
                        for i in indices:
                            low, high = 0, w[i]
                            while low < high:
                                mid = (low+high)//2
                                w[i] = mid
                                calls += 1
                                if rectangle_min(d,w,r) >= h:
                                    high = mid
                                else:
                                    low = mid+1
                            w[i] = low
                    actual = rectangle_min(d,w,r)
                    assert actual >= h
                    records.append(dict(n=n, family=family, trial=trial,
                                        r=r, required=h, minimum=actual,
                                        d=d, weights=w))
    return records, calls


def repair_suite():
    """All masks for n=2,...,6; worst line-walk costs bound repaired trees."""
    out = []
    for n in range(2,7):
        pairs = list(combinations(range(n),2))
        lookup = {e:i for i,e in enumerate(pairs)}
        by_k = [[0,0,0] for _ in range(len(pairs)+1)]
        a = [1, 100, 2, 10000, 3][:n-1]
        for mask in range(1 << len(pairs)):
            def good(i,j):
                return not (mask >> lookup[tuple(sorted((i,j)))] & 1)
            coefficients = [1]*(n-1)
            ok = True
            for i in range(n-1):
                if good(i,i+1):
                    continue
                xs = [x for x in range(n) if x not in (i,i+1)
                      and good(i,x) and good(i+1,x)]
                if not xs:
                    ok = False
                    break
                x = min(xs, key=lambda x:(i-x if x<i else x-i-1,x))
                extra = range(x,i) if x<i else range(i+1,x)
                for j in extra:
                    coefficients[j] += 2
            k = mask.bit_count()
            by_k[k][0] += 1
            if ok:
                by_k[k][2] += sum(x*y for x,y in zip(a,coefficients))
            else:
                by_k[k][1] += 1
        checks = []
        for p in [F(0),F(1,3),F(2,5),F(49,100)]:
            m = len(pairs)
            failure = sum(F(row[1])*p**k*(1-p)**(m-k)
                          for k,row in enumerate(by_k))
            cost = sum(F(row[2])*p**k*(1-p)**(m-k)
                       for k,row in enumerate(by_k))
            alpha = (1-p)**2
            assert failure <= (n-1)*(1-alpha)**(n-2)
            assert cost <= (1+4/alpha)*sum(a)
            checks.append(dict(p=str(p),failure=str(failure),
                               expected_walk_cost_on_F=str(cost)))
        out.append(dict(n=n, masks=1<<len(pairs), weights=a, checks=checks))
    return out


if __name__ == '__main__':
    records,calls = metric_suite()
    result = dict(job_id=JOB, seed=3703, arithmetic='exact integers/rationals',
                  scope='Sampled general metrics and coordinate minima only; not a universal computational proof.',
                  records=records, feasibility_calls=calls, repair_masks=repair_suite())
    (ROOT/'interval-packing-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(metric_witnesses=len(records), feasibility_calls=calls,
                          repair_masks=sum(x['masks'] for x in result['repair_masks']))))
