# Routine reset-clock calibration

Job c015-imagebound-triage-104fc05d5d7d. No novelty claim.

Take k disjoint cycles of lengths ell_i>=2; a rotates each. Let S contain
their zero vertices, D their last vertices. Under b, each vertex in D has
empty image and every other vertex has image S.

Before the first b, a singleton remains a singleton. Every nonempty b-image
of any subset is exactly S. Subsequently an image has form S.a^t, with one
vertex per cycle, until it is reset to S or killed by b. These forms are
closed under both letters. This proves the global all-word image bound k,
not merely the one-step branching bound.

From Q, a preserves Q and the first b gives S. From S, a^t b kills exactly
when t=-1 modulo every ell_i, whose least nonnegative solution is L-1 for
L=lcm(ell_i). An unsuccessful b resets the same S and cannot improve this
minimum. Thus the shortest mortal word is b a^(L-1) b, length L+1.
Pairwise coprime comparable lengths give a routine order n^k lower bound
for fixed k. It does not supply the extra factor n in the question.

The supervisor's named batch015 code/results were not present inside this
project, so these local controls were independently recreated from the
explicit transition rule. Run from project root:

    python3 evidence/check_clock_baseline.py

The script exhausts closure seeded by every singleton, then complete BFS
from Q. It checks closure on every letter edge, saves all reachable masks
and Q-distances, and reconstructs a shortest word. BFS layers cover all
shorter words via their subset images; no search cap or heuristic pruning
is used. The domains are finite subsets of the full 2^n power set.

| Cycle lengths | n | Max row image | Row closure | Q closure | Minimum |
|---|---:|---:|---:|---:|---:|
| (3,5) | 8 | 2 | 24 | 17 | 16 |
| (2,3,5) | 10 | 3 | 41 | 32 | 31 |
| (3,4,5) | 12 | 3 | 73 | 62 | 61 |
| (5) | 5 | 1 | 6 | 7 | 6 |

Data: evidence/clock-baseline-results.json. These four exact observations
calibrate the general argument only; no arbitrary NFA classification was run.
