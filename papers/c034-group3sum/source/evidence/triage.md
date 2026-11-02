# Bounded triage evidence

Job: c034-group3sum-triage-7cb7e5c1a226. Date: 2026-11-02 UTC.
Decision: **advance**. Candidate: **none**. Original: **unresolved**.
This admits research, not a mathematical result, audit acceptance or manuscript.

## Sources actually inspected

1. [Majdoddin, arXiv:2610.17420v1](https://arxiv.org/abs/2610.17420v1).
   Frozen PDF: intake/primary/2610.17420v1.pdf; extracted text:
   intake/primary/2610.17420v1-pdf.txt. SHA256 of the PDF independently
   rechecked as a536921aea8fe16830262db76c624593c5815094ae495ef5afce8c761d1c3d2e.
   Inspected Section 19 Model, printed pp.65-66; Theorem 19.17 and embedding,
   pp.76-77; light/heavy proof, pp.77-82; Open Problem 19.26 and proposed
   induction, pp.82-83; Remark 20.6, p.86; Definition 2.1/Lemma 2.2, pp.10-11.
   Local text line positions: 3620-3670, 4257-4632, 4788-4794, 493-549.
2. [Current arXiv record](https://arxiv.org/abs/2610.17420), retrieved this
   job around 16:02 UTC: submission history displays v1 only, dated 12 October
   2026. The abstract's claimed group scope stops at elementary and p^2 groups.
3. [Author's current groups README](https://raw.githubusercontent.com/Majdoddin/formal-math/main/groups/README.md),
   opened live this job. Also inspected intake/Majdoddin-groups-current-README.md
   and intake/Majdoddin-current-repository-check.json. The preserved pinned
   repository inspection is at commit 63e9490d3b5d62bf8b9f7f0a8103b0e409564a9d.
   The README explicitly limits its formalization: running times and call
   legality are not formalized. No Lean build or fresh repository-tree audit
   was performed in this job. Missing formalization does not reopen prior claims.
4. [Alman and Vassilevska Williams, arXiv:2610.06783](https://arxiv.org/abs/2610.06783),
   current abstract record opened. The matrix interface was inspected through
   Majdoddin's explicit statement and Lemma 2.2 reduction. This is not an
   independent proof audit of the original thin-matrix theorem.

Bounded live search terms: '3SUM bounded exponent abelian groups',
'19.26 3SUM', '3SUM abelian Majdoddin', '3SUM Z_8 algorithm', and
'3SUM finite abelian groups algorithm 2026', including exact-phrase variants.
No full resolution was located. Only primary sources support this decision;
aggregator snippets were leads, not evidence. This is a limited search and
cannot certify global priority or absence of an unindexed follow-up.

## Cheapest discriminating check and nearest comparison

The source's p^2 theorem is stated for exponent *dividing* p^2 and explicitly
embeds every Z_p coordinate into Z_(p^2) by multiplication by p. Therefore
Z_4^d x F_2^d is already covered. The open-example list contradicts that theorem
on this example; the general target is still well-defined. A paper on that
example would rediscover prior work. The first genuinely uncovered diagnostic
is Z_8^d; resolving it alone would not resolve source.md.

The p^2 proof partitions the triples into seven light cases and polylogarithmically
many heavy size buckets. Its actual row-selection argument uses a computable
weighted potential in the light case and two complementary count/estimator
regimes in the heavy case. Thus listing residue classes and calling the p^2
algorithm independently is not yet a costed extension method. The source already
suggests higher-layer induction; that idea itself is prior.

The target delta is a uniform saving for every fixed exponent M independent
of c, covering higher prime powers and mixed primes. The coordinate embedding
in problem.md preserves the original full scope; it is only a normalization.
The plausible substantive payoff is a reusable composition method that closes
this gap and, via the source's Remark 20.6, reaches every group-representable
fixed coordinate relation. Whether the eventual proof is nonroutine and
STOC-significant remains unassessed; open status alone does not establish either.

## First bounded research test and falsification route

Derive a layer-extension invariant, testing p^3 (p=2) first. A source-style
branch must bound the middle group by D, blocks by O_M(n/sigma), grouping triples
Z(pi) by O_M(sigma*n^2), and surviving nonzero triples F by
O_M(sigma*n^2/D), together with subquadratic computable row selection.
Charge the sum over all branches, compatible class triples, calls, scans and
witness recovery; show the invariant composes over all prime-power and CRT
layers. The sufficient bounds are a proposed test interface, not established
higher-layer facts. Check adverse heavy distributions and carry-dependent
targets symmetrically with attempts to prove the bounds. An inequality failure
rejects that route, not the unconditional existence of another algorithm.

No proof/counterexample search or new algorithm experiment was run in triage.
There is no full resolution, subsidiary theorem claim or failed proof presented
as a lower bound. A positive full proof still needs an actually justified
primitive, fresh correctness/innovation review and the separate STOC assessment.

## Preserved state and limits

Read intake/root-handoff.md before scientific inspection and read
outer-root-note.md, AGENTS.md, publication-policy.json, checkpoint.md and the
shared STOC quality standard. The parent reports a mathematical comparison
against 446 registered leads with no semantic duplicate; this job did not
independently inspect that external registry. No scheduling state was edited.
Research passes observed: 0; consumed here: 0; cap unchanged: 3.
No agents, background workers, manuscript, PDF, external contact or upload.
The real clock was checked at entry (16:01:53 UTC), before the last source
validation batch (16:02:33 UTC), and at the transition to finalization
(16:03:52 UTC). After that transition only records and consistency validation
were completed; no additional scientific test was started.
