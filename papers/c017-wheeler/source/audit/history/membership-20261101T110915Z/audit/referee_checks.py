#!/usr/bin/env python3
"""Fresh referee controls. No modification of frozen inputs; no proof by sampling."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('candidate', ROOT/'evidence/check_membership.py')
candidate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(candidate)


def run(delta, outputs, word):
    q, out = 0, []
    for a in word:
        if (q, a) not in delta:
            return None
        out.append(outputs[q, a])
        q = delta[q, a]
    return q, ''.join(out)


def enumerate_runs(n, alphabet, delta, outputs, depth):
    rows = [[] for _ in range(n)]
    layer = [('', 0, '')]
    for d in range(depth+1):
        nxt = []
        for w, q, out in layer:
            rows[q].append((w, out))
            if d < depth:
                for a in alphabet:
                    if (q, a) in delta:
                        nxt.append((w+a, delta[q, a], out+outputs[q, a]))
        layer = nxt
    for row in rows:
        row.sort(key=lambda x: x[0][::-1])
    return rows


def pieces(values):
    # Shortest-path DP with monotone-run starts. Prefix optimum is nondecreasing.
    dp = [0]
    up_start = down_start = 0
    for i, value in enumerate(values):
        if i and values[i-1] > value:
            up_start = i
        if i and values[i-1] < value:
            down_start = i
        dp.append(1+min(dp[up_start], dp[down_start]))
    return dp[-1]


def brute_pieces(values):
    dp = [0]+[len(values)+1]*len(values)
    for j in range(1, len(values)+1):
        for i in range(j):
            v = values[i:j]
            if all(x <= y for x,y in zip(v,v[1:])) or all(x >= y for x,y in zip(v,v[1:])):
                dp[j] = min(dp[j], dp[i]+1)
    return dp[-1]


def reversed_dfa(n, delta, outputs, target, input_labels=False):
    """Independent subset construction for the reversed input/output range."""
    eps = {q:set() for q in range(n)}
    labeled = {q:{} for q in range(n)}
    chars = set()
    count = n
    for (p,a),q in delta.items():
        label = a if input_labels else outputs[p,a]
        prev = q
        if not label:
            eps[q].add(p)
        for i,c in enumerate(label[::-1]):
            nxt = p if i == len(label)-1 else count
            if nxt == count:
                eps[count] = set()
                labeled[count] = {}
                count += 1
            labeled[prev].setdefault(c,set()).add(nxt)
            chars.add(c)
            prev = nxt
    def close(states):
        result = set(states)
        todo = list(states)
        while todo:
            for r in eps[todo.pop()]:
                if r not in result:
                    result.add(r)
                    todo.append(r)
        return frozenset(result)
    start = close({target})
    todo = [start]
    transitions = {}
    finals = set()
    while todo:
        states = todo.pop()
        if states in transitions:
            continue
        if 0 in states:
            finals.add(states)
        transitions[states] = {}
        for c in chars:
            dest = close(set().union(*(labeled[q].get(c,set()) for q in states)))
            if dest:
                transitions[states][c] = dest
                if dest not in transitions:
                    todo.append(dest)
    live = set(finals)
    while True:
        more = {p for p,ts in transitions.items() if any(q in live for q in ts.values())}
        if more <= live:
            break
        live |= more
    return start, transitions, finals, live


def signs(dfa1, dfa2):
    s1,t1,f1,l1 = dfa1
    s2,t2,f2,l2 = dfa2
    todo = [(s1,s2)]
    seen = set()
    result = set()
    while todo:
        p,q = todo.pop()
        if (p,q) in seen:
            continue
        seen.add((p,q))
        if p in f1 and q in f2:
            result.add(0)
        if p in f1 and any(r in l2 for r in t2[q].values()):
            result.add(-1)
        if q in f2 and any(r in l1 for r in t1[p].values()):
            result.add(1)
        for a,r in t1[p].items():
            for b,s in t2[q].items():
                if a == b:
                    todo.append((r,s))
                elif r in l1 and s in l2:
                    result.add(-1 if a < b else 1)
    return result


def reachable(n,delta):
    reached = {0}
    while True:
        extra = {q for (p,a),q in delta.items() if p in reached}
        if extra <= reached:
            return len(reached) == n
        reached |= extra


def strict_turn(row):
    compressed = []
    for w,out in row:
        if not compressed or out != compressed[-1][1]:
            compressed.append((w,out))
    for a,b,c in zip(compressed,compressed[1:],compressed[2:]):
        x,y,z = a[1][::-1],b[1][::-1],c[1][::-1]
        if x < y > z or x > y < z:
            return [a[0],b[0],c[0]]
    return None


def return_path(start, target, cc, delta):
    queue = [(start,'')]
    seen = {start}
    for q,w in queue:
        if q == target:
            return w
        for (p,a),r in sorted(delta.items()):
            if p == q and r in cc and r not in seen:
                seen.add(r)
                queue.append((r,w+a))
    raise AssertionError('SCC return path absent')


def verify_new_rejection(delta,outputs,base,pump):
    direction = None
    for k in list(range(6))+[15,31]:
        ws = [w+pump*k for w in base]
        rs = [run(delta,outputs,w) for w in ws]
        assert all(r is not None and r[0] == rs[0][0] for r in rs)
        a,b,c = [w[::-1] for w in ws]
        assert a < b < c
        x,y,z = [r[1][::-1] for r in rs]
        assert x < y > z or x > y < z
        ns = [(w+pump*(k+1))[::-1] for w in base]
        current = 1 if c < ns[0] else -1 if ns[2] < a else 0
        assert current != 0
        if direction is None:
            direction = current
        assert direction == current


def check_machine(n, alphabet, delta, outputs, depth, counters):
    T = candidate.Machine(n, alphabet, delta, outputs)
    d = T.decide()
    inp = [reversed_dfa(n,delta,outputs,q,True) for q in range(n)]
    ordered = True
    for p,q in itertools.combinations(range(n),2):
        attained = signs(inp[p],inp[q])
        assert attained == candidate.order_signs(T.range(p,True),T.range(q,True))
        ordered &= attained in ({-1},{1})
        counters['independent_regular_comparisons'] += 1
    assert ordered == d['input_order']
    out = [reversed_dfa(n,delta,outputs,q) for q in range(n)]
    for p,q in itertools.combinations_with_replacement(range(n),2):
        assert signs(out[p],out[q]) == candidate.order_signs(T.range(p),T.range(q))
        counters['independent_regular_comparisons'] += 1
    if not ordered:
        return False
    counters['input_ordered_machines'] += 1
    counters['accepted_machines' if d['member'] else 'rejected_machines'] += 1
    rows = enumerate_runs(n,alphabet,delta,outputs,depth)
    for q,row in enumerate(rows):
        values = [o[::-1] for w,o in row]
        up = all(a <= b for a,b in zip(values,values[1:]))
        down = all(a >= b for a,b in zip(values,values[1:]))
        assert not d['flags'][1][q] or up
        assert not d['flags'][-1][q] or down
        k = pieces(values)
        if d['member']:
            assert k <= d['piece_bounds'][q], (delta, outputs, q, k, d)
        counters['finite_state_lists'] += 1
        counters['finite_runs'] += len(row)
    for test in d['checks']:
        if test['type'] == 'simple' and len(test['states']) > 1:
            counters['multistate_simple_cycle_checks'] += 1
    if not d['member']:
        test = d['checks'][-1]
        cc = set(test['states'])
        witnessed = False
        if test['type'] == 'branching':
            r = next(p for p in cc if sum(x==p and q in cc for (x,a),q in delta.items()) > 1)
            base = strict_turn(rows[r])
            if base is not None:
                loops = [a+return_path(q,r,cc,delta) for (p,a),q in sorted(delta.items()) if p==r and q in cc]
                u,v = loops[:2]
                for power in range(1,len(u)+len(v)+2):
                    A,B = u*power,v*power
                    if not A.endswith(B) and not B.endswith(A):
                        break
                else:
                    raise AssertionError('Noncommuting loops remained suffix-comparable')
                verify_new_rejection(delta,outputs,[w+A for w in base],B)
                witnessed = True
        else:
            q = min(cc)
            c = test['cycle']
            anchor = rows[q][0][0]+c
            sides = [[],[]]
            for w,outword in rows[q]:
                root = w
                level = 0
                while root.endswith(c):
                    prefix = root[:-len(c)]
                    r = run(delta,outputs,prefix)
                    if r is None or r[0] != q:
                        break
                    root = prefix
                    level += 1
                if level <= 1:
                    sides[int(root[::-1] > anchor[::-1])].append((w,outword))
            for side in sides:
                base = strict_turn(side)
                if base is not None:
                    verify_new_rejection(delta,outputs,base,c+c)
                    witnessed = True
                    break
        counters['new_rejection_pump_controls' if witnessed else 'rejections_without_depth_bounded_turn'] += 1
    return True


def main():
    counters = dict.fromkeys(['independent_regular_comparisons','input_ordered_machines',
        'accepted_machines','rejected_machines','finite_state_lists','finite_runs',
        'multistate_simple_cycle_checks','new_rejection_pump_controls',
        'rejections_without_depth_bounded_turn'],0)
    dp_tests = 0
    for size in range(8):
        for values in itertools.product(range(3),repeat=size):
            assert pieces(values) == brute_pieces(values)
            dp_tests += 1
    # Empty alphabets and complete erasure; arbitrary terminal outputs are irrelevant.
    check_machine(1,'',{}, {},0,counters)
    check_machine(1,'0',{(0,'0'):0},{(0,'0'):''},30,counters)
    # Initial state lies on cycles of 2 through 5 states. Labels ensure input order.
    for size in range(2,6):
        alphabet = ''.join(str(j) for j in range(size))
        delta = {(p,str((p+1)%size)):(p+1)%size for p in range(size)}
        for seed in range(16):
            rng = random.Random(97000+100*size+seed)
            outputs = {e:rng.choice(('', '0','1','01','100','0001')) for e in delta}
            assert check_machine(size,alphabet,delta,outputs,45,counters)
    # New seed; ternary input and variable output words, including epsilon.
    rng = random.Random(60117017)
    attempts = accepted_order = 0
    while accepted_order < 240 and attempts < 16000:
        attempts += 1
        size = rng.choice((2,3,4))
        alphabet = rng.choice(('01','012'))
        delta = {(p,a):q for p in range(size) for a in alphabet
                 if (q:=rng.randrange(-2,size)) >= 0}
        if not reachable(size,delta):
            continue
        outputs = {e:rng.choice(('', '0','1','2','02','110','0012')) for e in delta}
        if check_machine(size,alphabet,delta,outputs,8 if alphabet=='01' else 6,counters):
            accepted_order += 1
    certs = json.loads((ROOT/'evidence/exact-certificates.json').read_text())['certificates']
    certificate_replays = 0
    indices = list(range(33))+[127,1024]
    for cert in certs:
        delta = {(e['from'],e['input']):e['to'] for e in cert['transitions']}
        outputs = {(e['from'],e['input']):e['output'] for e in cert['transitions']}
        for n in indices:
            words = [t['x']+t['y']*n+t['z'] for t in cert['templates']]
            rs = [run(delta,outputs,w) for w in words]
            assert all(r is not None and r[0] == cert['target_state'] for r in rs)
            a,b,c = [w[::-1] for w in words]
            assert a < b < c
            x,y,z = [r[1][::-1] for r in rs]
            assert (x < y > z) if cert['turn']=='peak' else (x > y < z)
            nxt = [(t['x']+t['y']*(n+1)+t['z'])[::-1] for t in cert['templates']]
            assert (c < nxt[0]) if cert['interval_direction']=='increasing' else (nxt[2] < a)
            certificate_replays += 1
    result = {'job_id':'c017-wheeler-referee-dd13950aae3a','status':'passed',
        'seed':60117017,'random_attempts':attempts,'random_input_ordered':accepted_order,
        'dp_crosschecks':dp_tests,'counts':counters,
        'certificate_families':len(certs),'certificate_indices':indices,
        'certificate_replays':certificate_replays,
        'limits':'Subset-construction range comparisons and direct run/finite partition controls independently check the prototype and witnesses. Finite sampling does not establish the theorem or all-n assertions; these are reviewed by proof in audit/math.md.'}
    (ROOT/'audit/referee-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
