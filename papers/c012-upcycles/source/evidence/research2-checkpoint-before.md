# Checkpoint

Job `c012-upcycles-research-cfe911474960`, RESEARCH pass 1, 2026-11-01.
Decision: **continue**. Candidate kind **none**; original status **unresolved**.
One research pass consumed; two remain under the three-pass ceiling. No
claim.json, fresh referee, manuscript or PDF. No agents/background workers.

## Immutable scope and current literature

The original still asks whether ANY nontrivial finite-alphabet upcycle with
constant d>=2 exists. Finite exclusions do not answer it negatively. `problem.md`
retains the exact interpretation. `source.md` SHA256 remains
`773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac`.
Current publisher Question 9.2/Remark 6.6 and arXiv v3 still support open status.
The current author-cited code repository and 2025 tori Sections 8–9 were also
inspected; no equivalent full resolution was located. Quasi-families and Euler
ideas are prior concepts. No method/finite-result priority is certified. See
`evidence/research1-results.md` and saved primary-source web confirmations.

## New decisive evidence

Exact global-position XOR CNFs passed pinned source n4d1/n8d1 controls, three
intentional bad pins and all 64 fixed-frame n4 assignments. All eight admitted
n8d2/d3 mask classes are UNSAT (each <1.52 seconds, cap 60). Together with the
source's exclusion of the ninth d3 class, this exhausts those finite binary
cases. Every target certificate passed the separate Python LRAT/RUP checker.
All CNFs, metadata, logs and proofs remain in `evidence/research1-sat/`.

Failure analysis separated balanced subcube tiling from cyclic overlap.
All four d2 classes admit independently expanded balanced tilings; all four
tested d3 classes are UNSAT even in that relaxation, with checked certificates.
`research1-relaxation-proof-checks.json` and its models contain the exact scope.
Private-orientation Fourier constraints alone still allow 57/8/16/15 normalized
local codes, so that attempted simpler obstruction failed; code/counts retained.

Changed method: select n-tiles giving an exact cube partition and equal in/out
degree at each literal partial-(n-1)-word vertex. Connectedness is sufficient
and necessary for one Euler tour/upcycle; the full elementary encoding argument
is in `research1-results.md`. Pinned known controls recover verified tours.
The adjacent-star n8d2 frame is UNSAT even before connectedness; its certificate
passed. The period-4 n8d2 frame has a four-component balanced model, four cycles
of length 16. Initial global-position UNSAT excludes a connected version.

The changed n12d3 period-4 test is SAT for exact cover plus vertex balance:
2048 selectors, 37376 clauses, 512 selected tiles, 22 components (21 length 24,
one length 8). `research1_extract_families.py` independently reconstructs each
closed word and expands ALL windows to an all-one 4096-entry total count array.
This is a multiple-cycle quasi-family, NOT an upcycle or original resolution.
Its model/family files are under `evidence/research1-euler/`.

## Obstacles, limits and one next test

Connectivity of a new n12d3 tile selection remains untested. Current models
cannot be joined merely by reordering disconnected edges. The fixed-frame
kernel is sufficient for a positive original answer, not equivalent to the
unrestricted existential question. No timeouts occurred; no larger raw SAT cap
was used. All failed routes/operational issues and actual usage are retained
in `evidence/research1-usage.json`; triage records remain intact.

Next pass: implement guarded connectivity cuts on the n12d3 period-4 Euler
exact-cover CNF. First benchmark connected n4d1 SAT and the certified n8d2
period-4 negative control. Limit to 20 refinement rounds, 180 total solver-wall
seconds and <=30 seconds per call. For a component vertex set S avoiding the
selected zero-word root edge r, add for each possible internal edge e:
(not y_r) OR (not y_e) OR (OR y_f over edges leaving S). Both guards are needed;
a connected solution retaining r/e must leave S. Preserve cuts and certificates.
Any connected model must yield a literal 512-character n12d3 upcycle and an
independent all-one 4096-entry coverage array, with recomputed length, d and
periodicity. If this stagnates, park or justify a structural change; do not
increase caps blindly. Full-resolution novelty/significance review remains
mandatory before any publication candidate.
