"""Driver: sanity checks + Claim 1 + Claim 2 (all 299 patterns), single process, timed."""
import sys, time
sys.path.insert(0, '/private/tmp/claude-503/-Users-mac-Documents-ChatGPT-STOC-----/40ee0f7a-1229-418b-b9f7-ff7898d5b546/scratchpad/indepH')
from cover_bnb import Problem, bnb, full_pattern, box_str
from patterns import all_patterns, to_Js
from fractions import Fraction as F
def run(name, j, Js, c, md=14):
    pr = Problem(j, Js, c); leaves = []
    r = bnb(pr, max_depth=md, record=leaves)
    print(f'{name:28s} j={j} c={c}: {r["status"]:7s} boxes={r["boxes"]} leaves={r["certified"]} '
          f'maxdepth={r["maxdepth"]} searchnodes={r["nodes"]} time={r["time"]:.3f}s'
          + (f'  stuck-box={box_str(r["box"])}' if 'box' in r else ''), flush=True)
    return r, leaves
print('== sanity (expect PROVED) ==')
for j in (1, 2, 3): run('K_3<=2', j, full_pattern(3, j), 2)
print('== sanity (expect FAIL) ==')
for j in (3, 4): run('n=4 c=2 full', j, full_pattern(4, j), 2)
run('n=2 c=1.9 full', 2, full_pattern(2, 2), F(19, 10))
run('n=3 c=1.9 full', 3, full_pattern(3, 3), F(19, 10))
run('n=4 c=2.9 full', 4, full_pattern(4, 4), F(29, 10))
run('t=3 four-item pattern', 4, [(1,2,3),(0,2,3),(0,1,3),(0,1,2)], 2)
print('== Claim 1 ==')
for j in (1, 2, 3, 4):
    r, leaves = run('Claim1 n=4', j, full_pattern(4, j), 3)
    if j == 4:
        for b in leaves: print('    leaf', box_str(b))
print('== Claim 2 (n=5 slots, t=2, c=2) ==')
P = all_patterns(); t0 = time.time(); tot = 0; nb = 0; worst = (0, None)
for j in range(6):
    tj = time.time(); bj = 0; okj = 0
    for e in P[j]:
        pr = Problem(j, to_Js(e), 2); r = bnb(pr, max_depth=22)
        okj += r['status'] == 'PROVED'; bj += r['boxes']
        if r['time'] > worst[0]: worst = (r['time'], e, r['boxes'], r['maxdepth'])
        if r['status'] != 'PROVED': print('   NOT PROVED', e, r)
    print(f'  j={j}: {len(P[j])} patterns, proved {okj}, boxes {bj}, {time.time()-tj:.2f}s', flush=True)
    tot += len(P[j]); nb += bj
print(f'  total {tot} patterns, {nb} boxes, {time.time()-t0:.1f}s; slowest pattern {worst}')
