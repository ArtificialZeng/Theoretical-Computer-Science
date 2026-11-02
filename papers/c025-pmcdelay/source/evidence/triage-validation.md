# Bounded triage validation

Job: c025-pmcdelay-triage-d83ce6e9a5e9. Role: triage.
Dispatch 2026-11-01 22:58:21 UTC; first actual clock read 23:00:23 UTC.
Scientific validation completed before the 23:02:21 UTC main-test deadline.
Decision: **advance** to bounded research. Candidate none; original unresolved.
This record is intake validation, not a fresh mathematical or venue review.

## Integrity and preserved state

Read project AGENTS.md, publication-policy.json, outer-root-note.md,
intake/root-handoff.md, source-inputs.json, checkpoint and problem, skill main
and only the triage phase reference, and the required STOC quality standard.
All six local PDF/text inputs match both SHA-256 and byte count in the input
manifest. The original source hash matches state.json:
30ba523462232346f8c2d671825d32d790edcd9362f00b8eec84a58e11d4e5cc.
No source, intake artifact, state counter or frozen file was modified.
Entry checkpoint and problem are preserved alongside this record.
state.json at entry has research_passes=0, revisions=0. No research pass,
subagent, external Codex process, background worker or exhaustive rerun occurred.

## Primary source/model checks, retrieved 2026-11-01 UTC

- [Berge--Limouzy--Schivre, 2610.19850](https://arxiv.org/abs/2610.19850):
  live primary history lists latest v3, 20 October 2026. Inspected supplied
  matching text: Theorem 1, printed pp.6 and43 (total output-linear bound),
  Section1.4 p.8 (delay left open), Lemma1 p.12 (separator delay O(n^3)),
  Lemmas11/12 p.17 (recursive lifts/containing-vertex seeds), Algorithm3 p.31,
  Theorem11/Corollary3 p.42 (reachability from all required seeds).
  No statement there permits replacing the full seed family by one arbitrary
  PMC. Its batched recursive algorithm gives no worst-case inter-output delay.
- [Kenig, 2610.24856](https://arxiv.org/abs/2610.24856): live history lists v1,
  17 October 2026. Supplied Theorem1.1 p.2 covers constrained size-at-most-k
  enumeration with delay 2^{O(k^3)}n^4 log n, including initial/final waiting.
  This is parameterized delay; substituting n for k is not polynomial.
- [IPEC2025.21](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2025.21):
  primary publisher record and matching supplied text cover triconnected planar
  graphs. Inspected abstract/introduction and Proposition29 on p.21:14.
  That proposition already uses a minimal triangulation saturating a separator
  and a maximal clique on the other full-component side. Thus the helper
  extension has an identifiable prior analogue; new value cannot rest on
  asserting that construction alone is novel.

The local PDFs are supplied research inputs; no manuscript was authored.
The underlying minimal-triangulation primitive and separator endpoint delay
contracts still require direct primitive-level scrutiny in research, as already
flagged in the source-input manifest. Their existing citations are not a
completed independent proof audit.

## Bounded current equivalent search

Web queries actually run:
1. "potential maximal cliques" "polynomial delay" 2026
2. "Output-linear time enumeration of potential maximal cliques"
3. "potential maximal cliques" "incremental" "delay"
4. "potential maximal cliques" "polynomial-delay" enumeration 2026
   -site:paperpeel.com -site:mdpi.com

No primary general all-size polynomial-delay resolution was identified in
these bounded results. Primary source histories were opened, not inferred
from snippets. Nonprimary aggregators and ordinary maximal-clique results
were not treated as evidence. This is **open-supported**, not a priority
certificate or exhaustive literature audit. The handoff reports a bounded
semantic registry comparison finding no identical earlier project among 295
leads. This worker did not independently inspect other projects or claim to
repeat that comparison. Follow-up/equivalence checks remain necessary before
any eventual novelty claim.

## Admission and precise unresolved kernel

The model is precise and preserves all original quantifiers, including empty,
complete and disconnected inputs, initial/final waits and permitted exponential
space. Known total-time, parameterized-size and restricted-class algorithms
leave a genuine scope gap. The source's required seeds and polynomial
neighborhood align with the proposed streaming schedule at the statement
level. This supports a bounded attack; it does not establish correctness.

The key proof obligation is whether deterministic polynomial helper production
with fiber<=n, injective child lifts and complete neighborhood seeds together
support simultaneous E(j)<=Q(n)j and T<=Q(n)K, with an additive polynomial
recurrence, and whether buffering then preserves every delay boundary. Check
an actual polynomial separator enumerator, not the finite checker's subset
oracle. The root's finite evidence was read, not reproduced or promoted to a
proof. The failed atom-neighborhood route remains failed and is not a disproof.

A full resolution could strengthen a graph-enumeration primitive used in exact
triangulation/treewidth methods. The conversion's nonroutine character and
STOC competitiveness are unresolved review questions. No candidate, audit
acceptance, readiness label, manuscript or PDF is justified by this triage.
