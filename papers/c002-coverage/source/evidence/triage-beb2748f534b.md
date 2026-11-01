# Bounded triage evidence

Job: `c002-coverage-triage-beb2748f534b`.
Inspected 2026-11-01 Asia/Shanghai (2026-10-31 UTC).
Decision: **advance**, candidate kind **none**, original status **unresolved**.
This is admission to bounded research, not candidate acceptance.

## Primary literature actually inspected

1. [Avila, Rohwedder, Wennmann, current arXiv record](https://arxiv.org/abs/2602.09948).
   Live landing page identifies v3, revised 2026-07-01; no v4 is listed.
   Local v3 full text: `literature/source.txt`. Inspected Theorem 3,
   Definition 4 and Section 1.3, printed pp.4-5. It gives a logarithmic size
   factor and discusses removing it. It does not settle the frozen
   qualitative question in those passages.
2. [Official ESA proceedings record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.139).
   Live page verifies the actual article number 139, publication 2026-08-25,
   19 pages, and abstract retaining dependence on log n. Full text reused
   from the freshly downloaded official input, `literature/publisher-source.txt`.
   Inspected Theorem 3/Definition 4, p.139:4; Section 1.3, p.139:5;
   Lemma 9, p.139:6; Section 5/Lemma 23, pp.139:12-13.
   This last section already uses interaction graph classes and Beck-Fiala
   row dropping, so those are not independent innovations of the proposal.
   Existing publisher receipt records PDF SHA-256
   `9aa69876e42ce14087dbe76b97caf56e9dff1b09ae914854cc5279920aac8505`.
   The current landing metadata is consistent with that input; this job did
   not independently redownload or certify the entire version comparison.
3. [Hollender, Manurangsi, Meka, Suksompong](https://arxiv.org/abs/2509.09252).
   Live page still lists v2 (2025-09-29). Local full text
   `literature/hollender-nonadditive.txt`, Definition 13, Question 14 and
   Theorem 15, PDF p.10, inspected directly. Their sparsity counts
   influenced functions and their question concerns arbitrary 1-Lipschitz
   functions, hence it is broader than this project's structural coverage
   target. A coverage-only bound cannot be advertised as its resolution.
4. [Dupré la Tour and Fujii](https://arxiv.org/abs/2509.16802).
   Live record still lists v1 (2025-09-20). Local full text introduction and
   abstract, `literature/dupre-fujii-nonadditive.txt`, inspected. The general
   non-additive bound depends on the number of functions and restricts k
   to prime powers; the inspected result does not resolve this target.
5. [Wennmann's author publication list](https://leo-wennmann.github.io/).
   Live inspected 2026 entries include the ESA coverage paper; no later
   resolving coverage paper is listed there. This limited list cannot
   exclude independent work by other authors.

## Current search coverage and its limits

Web searches executed in this job included:

- `"2602.09948" non additive discrepancy polynomial`
- `"Non-Additive Discrepancy" "Beck-Fiala"`
- `"coverage functions" "discrepancy" "size-independent"`
- `"coverage functions" "discrepancy" "size independent"`
- `"non-additive discrepancy" "Hall"`
- `"coverage" "discrepancy" "Beck-Fiala" polynomial`
- `"coverage" "Beck-Fiala" "rainbow"`
- `"non-additive discrepancy" polynomial bound 2026`
- `"coverage functions" "discrepancy" Hall rounding`

Relevant hits led back to the inspected ESA/arXiv paper and precursor
records. No inspected primary result giving the required size-independent
polynomial was found. Search snippets and aggregators were not used as
mathematical evidence. This is a bounded literature screen, not a priority
certificate. A global historical claim registry was not supplied within
the project; this job makes no global duplicate-clearance claim. The local
route and native challenge concern the same target and are not separate
contributions or fresh acceptance.

## Cheapest discriminating mathematical test

New independently implemented script: `evidence/triage_first_test.py`.
Command: `python3 evidence/triage_first_test.py`.
Result: `evidence/triage_first_test.json`, all assertions passed.

It checks all multisets of at most three nonempty incidence subsets on
n=1..4, for t=1,2 and k=2,3 whenever the occurrence-degree bound holds,
plus six explicit fixtures. Repeated subsets are retained as distinct
occurrences; alternating function tags include repeated subsets across
functions. Fixtures include multiple items of a small occurrence inside
one rainbow block, repeated large occurrences, overlapping large
occurrences mixed with small occurrences, and k=4. Empty feature lists
and unused items are covered by the enumerated cases. Nonuniform rational
shift laws test the categorical identity beyond the uniform starting law.

Counts: 1,208 family/parameter cases, 113 Hall subfamilies, 107 large
occurrences, 17,066 exact affine identities, 11,165 coefficient columns,
182 repeated-occurrence cases, and 14 same-block intersections. Arithmetic
uses `fractions.Fraction`. The test verifies Hall representatives,
interaction-degree/class bounds, direct expectation versus affine
expression, and column l1<=kt. It does not implement the final rounding
algorithm or prove a theorem for unbounded inputs. No counterexample to
these tested route components was found in this precisely bounded range.

## Admission assessment and one next test

Source status is an open-supported direction, not a verified worldwide open
problem designation. The precise all-parameter target and the decisive
first test are available. The proposed change from item variables to
disjoint categorical rainbow blocks could protect all large occurrences
while balancing the small ones; if valid and new, size independence for
this structural non-additive class has plausible substantive value.
The worse polynomial 4kt(kt-1)^2 would answer source.md, but would not retain
the sharper t,k exponents of the ESA bound.

No triage obstruction was found that warrants parking. Actual full
correctness, current novelty, and nonroutine significance remain open
review tasks. Standard Hall and LP tools alone do not establish innovation.
The outer preliminary favorable assessment was not treated as acceptance.
No manuscript, PDF, candidate, audit acceptance, or scheduler mutation was
created. Original source hash is unchanged.

**One next test:** independently prove or refute the proposed all-parameter
categorical block-rounding argument, focusing on the multiple-choice
rounding lemma's 2kt error per class and its telescoping across at most
(kt-1)^2 classes. A counterexample to that route is not automatically a
counterexample to source.md. Retain exact obstructions or failed-route
records and recheck primary novelty before any candidate submission.
