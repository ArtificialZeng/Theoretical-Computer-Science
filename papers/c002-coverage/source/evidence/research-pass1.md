# Bounded research record, pass 1

Job: `c002-coverage-research-8e44b8ae65fb`.
Started 2026-10-31 21:28:51 UTC (2026-11-01 Asia/Shanghai).
Ceiling: 25 minutes, one process, no delegated/background workers.
Original `source.md` is unchanged; expected SHA-256:
`b79ed29f77420ec62a957e727b934deb6b9435b41ed86deaa2c8d77c01b66f9d`.

## New mathematical artifact

`research/proof.md` gives an all-parameter argument for
4kt(kt-1)^2 and explains rational explicit-input constructivity.
The assigned uncertain step is proved there: the multiple-choice lemma
has error 2D from one-time row deletion, and the coverage expectations
telescope across <=(kt-1)^2 classes with pairwise error <=4kt per class.
This is new project evidence; no finite absence of a counterexample is
used as an infinite proof.

## Symmetric challenges and corrected attribution

- Every subset of the Hall demand copies is checked in the proof, rather
  than asserting Hall merely for full occurrence groups.
- The graph degree calculation counts tagged occurrences and allows
  several items of one feature in a block.
- The affine column identity counts colored items inside a block, rather
  than assuming feature/block intersection size one.
- Rounding is support preserving on categorical coordinates; every
  nonintegral group has at least two nonintegral coordinates, including
  groups that already have zero coordinates. The light-row threshold
  includes equality. One deletion bounds the entire later row movement.
- Class coefficients change from stage to stage. Each stage compares
  consecutive values of the same coverage-expectation functional, which
  justifies telescoping without a common fixed matrix across classes.
- q=2, unused items, no features, equal incidence subsets, and k>=n are
  covered explicitly. Finite code checks will supplement these arguments.
- The exact 2||A||_1 multiple-choice theorem was identified as known:
  Doerr--Srivastav (2003), explicitly stated as Theorem 2, p.58, in the
  primary FSTTCS 2011 paper by Glaßer--Reitwießner--Witek. The rounding
  lemma is accordingly credited, not presented as an innovation.

## Failed routes and operational limits

- **Observed access failure:** urllib download of the official FSTTCS
  2011 PDF failed with a name-resolution error in the command sandbox.
  The primary PDF was accessible through the web tool and its Theorem 2
  was inspected there. No local PDF download is claimed; this access
  failure is not a mathematical obstruction.
- **Rejected justification:** repeated exact null directions by themselves
  do not prove polynomial bit complexity. The proof uses the known
  rational algorithm or fixed-input rational LP vertices instead.
- **Scope excluded by original instruction:** literal deduplicated subset
  unions do not represent the immutable question; no artificial t=1
  counterexample on that different reading is offered.

## Exact finite diagnostics and decision

`evidence/research_rounding_check.py` was run successfully with the standard
library. Its result is `evidence/research_rounding_check.json`:

- 385 generic signed-rational rounding cases, including threshold equality,
  zero columns, fixed/zero coordinates, and nonuniform probability laws;
- 7,571 complete coverage constructions, including every multiset of <=3
  nonempty subsets on n=1..4 with t=1,2, k=2,3 and every two-function
  occurrence tagging, seven serialized structured fixtures, and 180 seeded
  larger families up to n=24;
- 18,268 rounding calls, 48,507 floating moves, 1,888 moves with retained
  value constraints, 94,208 one-time row deletions, 17,883 class stages and
  186,772 affine row checks;
- 956 large occurrences, 180 same-block multiple-item intersections,
  1,263 repeated-occurrence cases and 7,424 direct product enumerations of
  the initial expectations.

All assertions passed in 13.919 seconds. The seven fixtures contain exact
incidences, blocks, classes, returned colors, coverage values and stage
drifts for inspection. The tests verify the described finite ranges only.
They do not prove an infinite theorem or certify novelty.

`literature/research-primary-comparison.md` records the current primary
checks, newly recognized known lemma and bounded novelty limits. No
equivalent full coverage resolution was found in the inspected sources.
The complete proof plus categorical witness reduction supports proposing
a **resolution-paper candidate**, original_status=proved as a submitted
mathematical claim, for the exact original question. Actual fresh review
is still required for correctness, novelty and substantive significance;
there is no self-acceptance or claim of external review.

One next test: a fresh referee should try to invalidate the categorical
witness reduction (especially equations (3)--(5)), its original-scope
coverage, and its claimed independent value relative to the ESA 2026
Lemma 23 and the known multiple-choice theorem. Routine/known work must
be rejected even if the proof is correct.

No manuscript, authored PDF, audit verdict, or scheduling state was changed.

Final structural validation confirmed all 15 claim inputs are existing,
nonempty project-relative files, the exact contract keys and proposer ID
match, and the original source hash is unchanged. A separate direct recount
of every serialized fixture checked item degrees, literal function/color
values, large-feature rainbow coverage and its recorded discrepancy.
The checkpoint is 477 words. Actual bounded usage and operational events
are retained in `evidence/research-usage.json`; unavailable token accounting
is not estimated or represented as a mathematical result. The runner owns
freezing and the next fresh-referee dispatch.
