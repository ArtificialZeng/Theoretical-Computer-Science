"""Independently (Fractions) verify that a reported cover at an exact interior point p satisfies
(N1),(N2) and covers the cube -- i.e. that the relaxation genuinely cannot certify there."""
from fractions import Fraction as F
from math import floor
import sys; sys.path.insert(0, "/private/tmp/claude-503/-Users-mac-Documents-ChatGPT-STOC-----/40ee0f7a-1229-418b-b9f7-ff7898d5b546/scratchpad/indepH")
from brute import exp_dist, hamming
def verify(j, Js, c, p, cover):
    c = F(c); N = 1 << j
    assert all(0 < x < 1 for x in p)
    covered = 0
    for i, J in enumerate(Js):
        r = len(J); pv = [p[k] for k in J]
        Up, Um = cover[i]
        Up = [y for y in range(1 << r) if Up >> y & 1]; Um = [y for y in range(1 << r) if Um >> y & 1]
        for U in (Up, Um):
            if U:
                assert exp_dist(U, r, pv) > c / 2, (i, U)
        if Up and Um:
            assert min(hamming(a, b) for a in Up for b in Um) > c
        for x in range(N):
            y = sum(((x >> k) & 1) << t for t, k in enumerate(J))
            if y in Up or y in Um:
                covered |= 1 << x
    assert covered == (1 << N) - 1
    return True
cases = [
 ('t3 c=2', 4, [(1,2,3),(0,2,3),(0,1,3),(0,1,2)], 2, ['3/8','121/256','1/4','49/128'], [(1, 128), (16, 8), (4, 32), (8, 16)]),
 ('n4 c2 j3', 3, [(0,1,2)]*4, 2, ['79/256','31/64','81/256'], [(1, 128), (18, 0), (4, 32), (72, 0)]),
 ('n4 c2 j4', 4, [(0,1,2,3)]*4, 2, ['3/16','31/64','121/256','23/128'], [(43, 16384), (388, 0), (8208, 1024), (39488, 0)]),
 ('n2 c1.9 j2', 2, [(0,1)]*2, F(19,10), ['123/256','1/2'], [(1, 8), (2, 4)]),
 ('n3 c1.9 j3', 3, [(0,1,2)]*3, F(19,10), ['9/128','13/32','125/256'], [(1, 232), (6, 16), (0, 0)]),
 ('n4 c2.9 j4', 4, [(0,1,2,3)]*4, F(29,10), ['117/256','31/128','25/64','119/256'], [(1, 59520), (2, 5120), (20, 512), (256, 104)]),
]
for name, j, Js, c, p, cov in cases:
    print(name, verify(j, Js, c, [F(x) for x in p], cov))
