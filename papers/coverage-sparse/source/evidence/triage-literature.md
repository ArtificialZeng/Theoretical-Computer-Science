# Bounded primary-literature screen

Job: `coverage-sparse-triage-8c18589f991c`.
Inspected 2026-10-31 Asia/Shanghai (2026-10-30 UTC).
This is a triage screen, not a priority proof or citation audit.

## Primary records inspected

1. Arjun Ramachandra, *Dimension Dependent Correlation Gap Bounds under
   Restricted Independence*, arXiv:2609.02659v1.
   [Primary HTML](https://arxiv.org/html/2609.02659v1),
   [current record](https://arxiv.org/abs/2609.02659).
   Inspected Theorem 2, Section 4.1.1 equations (11)-(12), Section 4.1.2,
   Lemmas 6-7 and equations (14)-(33). The theorem states all-pairs
   asymptotic e/(e-1) tightness with both block counts and block sizes growing.
   Equations (11)-(12) give exactly the normalized Cartesian coverage family.
   Its reduced dual has both within-block and cross-block pair terms;
   equation (24) uses a nonzero cross-block coefficient. That displayed
   certificate does not directly establish tightness when all cross-block
   constraints are deleted. I did not audit that paper's asymptotic proof.
   Locally inspected original: `literature/ramachandra2026.html`;
   relevant extracted content: `evidence/ramachandra2026-excerpts.md`.

2. Paul Dütting, Federico Fusco, Silvio Lattanzi, Ashkan Norouzi-Fard,
   Ola Svensson, Morteza Zadimoghaddam, *The Cost of Consistency:
   Submodular Maximization with Constant Recourse*, arXiv:2412.02492v1.
   [Primary HTML](https://arxiv.org/html/2412.02492v1),
   [record](https://arxiv.org/abs/2412.02492).
   Inspected Section 3.2, Coverage Functions, and the displayed two-sample
   inequality; also checked its link to Lemma 5.4 / Theorem 5.5. It decorrelates
   two groups and obtains 3/4 by a per-feature union calculation. This is a
   known ingredient, and its elementary multi-group extension is a substantial
   overlap risk for presenting our upper-bound argument as a contribution.
   I did not find the full graph-class lower bound in the inspected sections.
   Local original: `literature/cost-consistency2025.html`;
   excerpt: `evidence/cost-consistency2025-excerpts.md`.
   Attempting a v2 HTML URL returned 404; v1 content was accessible. This
   operational failure supplies no mathematical evidence.

3. *Online Submodular Welfare Maximization: Computation is not the Bottleneck*,
   arXiv:2610.16060, found during this job's current search.
   [Primary HTML](https://arxiv.org/html/2610.16060).
   Inspected Sections 1.2 and 3.1 (Definitions 3.1, Lemmas 3.2-3.4,
   Corollaries 3.5-3.6; HTML lines 117-125, 185-229).
   It uses independent uniformly selected faces of k-sided dice on partition
   blocks to realize the same Cartesian coverage polynomial, and explicitly
   discusses alpha_k as an existing single-item correlation-gap factor.
   The inspected claims concern online allocation and restricted bundle
   intersections; they do not state an optimum over graph-tested moment laws.
   Whole-document literal searches for `pairwise` and `color` returned no match;
   this absence is only a search aid, not an equivalence argument. This source
   strengthens the need to restrict any novelty claim to the exact graph-class
   statement and its finite error certificate.

## Search coverage and limitations

Live exact/equivalent-language queries included:

- `"correlation gap" "coverage" "colorable"`
- `"correlation gap" "pairwise" "graph"`
- `"correlation gap" "multi-block" coverage`
- `"coverage" "correlation gap" "partition" "blocks"`
- `"coverage" "correlation gap" "chromatic"`
- `"correlation gap" "edgewise" independence`
- `"coverage" "correlation gap" "k" "blocks"`
- `"correlation gap" "graph-restricted"`
- `"correlation gap" "partial independence"`
- `"correlation gap" "bounded degree"`
- `"block independent" "correlation gap"`
- `"coverage" "correlation gap" "1/k"`
- `"coverage" "correlation gap" "limited independence"`
- `"correlation gap" "chromatic number"`

No directly equivalent full graph-class theorem was identified in this bounded
search. Search snippets were used only to locate primary records. The source
status is `new-question`, not `open-supported`; absence of a match does not
establish novelty. Existing `selection.md` is an earlier same-target screen,
not an independent result. No historical registry was supplied or present
among the project's available top-level artifacts, so cross-project duplicate
checking remains unperformed. No external registry was altered.

Triage decision: advance for a bounded mathematical attack. There is a precise
sharp target and an exact verification route, while contribution size and
novelty remain material risks. No venue-fit or acceptance inference follows.
