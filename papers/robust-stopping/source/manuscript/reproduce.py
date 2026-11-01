#!/usr/bin/env python3
"""Read-only, standard-library reproduction. Prints one JSON object.

Run with python3 -B reproduce.py, without Python's -O flag (assertions check
the certificates). The script never writes the supplied data or evidence.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import random
import sys

from prefix_oracle import optimize as _optimize, linear_oracle
from uniform_frontier import frontier, policy as uniform_policy

def optimize(b, R, p, **kwargs):
    kwargs["max_chord_probes"] = 0
    return _optimize(b, R, p, **kwargs)
from verify_certificates import check_full, check_linear, decode_result

ROOT = Path(__file__).resolve().parent


def main():
    if not __debug__:
        raise SystemExit('Run without -O: assertions are the exact checks.')
    counts = {}
    hashes = {}
    for name in ('oracle-test-cases.json', 'bisection-test-cases.json',
                 'linear-oracle-test-cases.json'):
        path = ROOT/'data'/name
        rows = json.loads(path.read_text())
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        for rec in rows:
            b, R = rec['b'], F(rec['R'])
            if name.startswith('linear'):
                c, f, y = ({int(t): F(v) for t, v in rec[k].items()}
                           for k in ('costs', 'policy', 'y'))
                value = check_linear(b, R, c, f, F(rec['alpha']), y)
            else:
                p = {int(t): F(v) for t, v in rec['p'].items()}
                value = check_full(b, R, p, decode_result(rec['result']))
            assert value == F(rec['value'])
        counts[name] = len(rows)

    signed = 0
    for b in (2, 3):
        for R in (F(3, 2), F(b)):
            for vector in product((-1, 0, 1), repeat=b+1):
                c = {t: F(v) for t, v in enumerate(vector, 1)}
                f, alpha, y, _ = linear_oracle(b, R, c)
                check_linear(b, R, c, f, alpha, y)
                signed += 1

    rng = random.Random(20261031)
    generated = 0
    for j in range(36):
        b = 2+j % 10
        rho = F(b**b, b**b-(b-1)**b)
        R = (rho, rho+F(1, 10**8), F(2), F(b))[j % 4]
        xs = sorted(set(rng.randrange(1, 3*b+7) for _ in range(6)))
        if j % 9 == 0:
            xs.append(10**20+j)
        ws = [rng.randrange(1, 11) for _ in xs]
        p = {x: F(w, sum(ws)) for x, w in zip(xs, ws)}
        p[10**35+j] = F(0)
        check_full(b, R, p, optimize(b, R, p))
        generated += 1

    b, R, p = 3, F(3, 2), {1: F(2, 5), 2: F(3, 5)}
    out = optimize(b, R, p)
    assert check_full(b, R, p, out) == F(39, 20)
    assert out['policy'] == {1: F(1, 4), 3: F(3, 4)}
    # Independent analytic certificates for Proposition 4.
    g = lambda t: sum(v*(x if x < t else b+t-1) for x, v in p.items())
    assert all(g(t) >= 3-F(7, 10)*(t-1) for t in (1, 2, 3))
    assert all(g(t) >= 4-F(6, 5)*(t-1) for t in (2, 3))
    # For t >= 3 g is constant; both affine minorants then decrease.
    restricted = {2: F(1, 2), 3: F(1, 2)}
    assert sum(v*g(t) for t, v in restricted.items()) == F(11, 5)
    assert max(g(t) for t in restricted) == F(14, 5)
    for x in (1, 2):
        assert sum(v*(x if x < t else b+t-1)
                   for t, v in restricted.items()) <= R*x
    assert sum((t-1)*v for t, v in restricted.items()) == F(3, 2)

    fallback = []
    for b, R, p in ((2, F(4, 3), {1: F(1)}),
                    (3, F(3, 2), {1: F(2, 5), 2: F(3, 5)})):
        out = optimize(b, R, p, max_chord_probes=0)
        value = check_full(b, R, p, out)
        assert value == check_full(b, R, p, optimize(b, R, p))
        fallback.append({'b': b, 'value': str(value),
                         'bisection_steps': out['isolation_steps']})
    uniform_checks = 0
    uniform_endpoints = 0
    for b in list(range(2, 23)) + [41, 64]:
        data = frontier(b)
        p_uniform = {x: F(1, b) for x in range(1, b+1)}
        for row in data['segments']:
            lo, hi, j = row['lower'], row['upper'], row['j']
            for r in (lo, (lo+hi)/2, hi):
                u = uniform_policy(b, r, segment=j)
                out = {'policy':u['policy'], 'lam':u['lambda'],
                       'alpha':u['alpha'],
                       'y':{i:u['y'].get(i,F(0)) for i in range(1,b)}}
                assert check_full(b,1+r,p_uniform,out) == u['value']
                if j == b and lo < r < hi:
                    assert len(u['policy']) == b+1
                    assert sum(t>=b for t in u['policy']) == 2
                uniform_checks += 1
            if j < b:
                u=uniform_policy(b,lo,segment=j)
                v=uniform_policy(b,lo,segment=j+1)
                assert u['policy']==v['policy'] and u['value']==v['value']
                uniform_endpoints += 1
    # Evaluate the recorded binary-exact software output under the true model.
    f_observed={1:F(1,4),2:F(3,8),3:F(3,8)}
    p={1:F(2,5),2:F(3,5)}
    direct=lambda t,x: x if t>x else 3+t-1
    observed_cost=sum(v*sum(w*direct(t,x) for x,w in p.items())
                      for t,v in f_observed.items())
    observed_moment=sum((t-1)*v for t,v in f_observed.items())
    assert observed_cost==F(12,5) and observed_moment==F(9,8)
    assert [sum(v*direct(t,x) for t,v in f_observed.items())
            for x in (1,2,3,100)]==[F(3,2),F(3),F(33,8),F(33,8)]
    # Exact separation of expected cost and expected per-horizon ratio.
    f_cost={1:F(1,4),3:F(3,4)}; f_ratio={2:F(1,2),3:F(1,2)}
    g2=lambda t: F(direct(t,1)+direct(t,2),2)
    k2=lambda t: (F(direct(t,1))+F(direct(t,2),2))/2
    assert sum(v*g2(t) for t,v in f_cost.items())==F(15,8)
    assert sum(v*k2(t) for t,v in f_cost.items())==F(21,16)
    assert sum(v*g2(t) for t,v in f_ratio.items())==2
    assert sum(v*k2(t) for t,v in f_ratio.items())==F(5,4)
    assert all(g2(t)+F(3,4)*(t-1)>=3 for t in (1,2,3))
    assert all(k2(t)+F(1,2)*(t-1)>=2 for t in (1,2,3))
    print(json.dumps({'status': 'passed', 'saved_certificates': counts,
                      'data_sha256': hashes, 'generated_signed_ties': signed,
                      'generated_full_certificates': generated,
                      'separation': {'global': '39/20', 'support_level': '14/5',
                                     'best_within_level': '11/5'},
                      'forced_bisection': fallback,
                      'uniform_certificates': uniform_checks,
                      'uniform_endpoint_agreement': uniform_endpoints,
                      'observed_software': {'J':'12/5','moment':'9/8','law':['1/4','3/8','3/8']},
                      'objective_separation': {'cost_optimum':'15/8','ratio_optimum':'5/4','cross_values':['21/16','2']},
                      'scope': 'Exact finite certificate checks; universal claims use the manuscript proofs.'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
