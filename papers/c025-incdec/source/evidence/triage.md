# Bounded TRIAGE evidence

Job: c025-incdec-triage-ff0d5f864af1. Role: triage.
Entry UTC read: 2026-11-01 23:00:23. Main validation completed before
2026-11-01 23:02:20.999990 UTC. No proof-search experiment was run.
Source/model/novelty checks, not mathematical acceptance.

## Inspected evidence

- Read AGENTS.md, publication-policy.json, outer-root-note.md,
  intake/root-handoff.md, intake/source-inputs.json, source.md, checkpoint.md,
  and the shared STOC quality standard. Only the assigned skill/triage reference
  was loaded. No agents, background jobs or other Codex processes were started.
- Both provided primary inputs match their manifest byte counts and SHA256.
  Source.md hash is unchanged. Source PDF text was inspected at Section 1
  pp.2-4 (definitions and table), Section 3 pp.7-9 (algorithm, normalization),
  Proposition 11 pp.14-15, Section 5 pp.20-21 and Appendix B pp.21-22.
- Live publisher page inspected 2026-11-01 UTC:
  https://link.springer.com/article/10.1007/s00236-026-00546-x
  Relevant HTML positions: lines 77-89 for model/algorithm infimum and polynomial
  upper bounds; line 569 for the explicit open deterministic gap. It reports
  publication 14 August 2026. The lower and upper bounds agree with local input.
- Earlier primary version record inspected:
  https://arxiv.org/abs/2508.14516 (submission displayed 20 August 2025).
  The later journal version controls this target.
- Official ESA 2026 page inspected, abstract lines 144-146 and metadata:
  https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.134
  Newer monotone incremental 1.373 bound is a nearby result, not a solution for
  arbitrary h,g. Full proof of that adjacent paper was not audited.
- Bounded live queries: exact article title/authors/year; incremental-decremental
  submodular competitive ratio 2; incremental-decremental 2-competitive 2026;
  exact title Incremental Submodular Maximization: Better Than Greedy.
  No later full resolution was identified in these checked primary records.
  This is open-supported status, not exhaustive novelty or priority certification.
- Read the supplied batch025 screening and source-status-corrections, especially
  screening rows 5-9 and semantic comparison. Did not rerun supplied exhaustive
  diagnostics. Read current registry's 295 lead records programmatically and
  searched incremental/incdec/decremental terms; no matching record was found.
  Semantic scope agrees with preparation: GS/randomized/curvature directions
  overlap this program but do not settle its full all-submodular sharp constant.
  No other project was edited and no new queue state was written.

## Discriminating conclusions

The precise source infimum is unrestricted; polynomial-oracle access is an
additional requested upper-bound requirement. Keep structural and efficient
constants separate. The lower bound is structural, not an oracle-complexity
claim. Normalization and k=0 cause no gap (details in problem.md).

Known equal-total result cannot be a new contribution. The source's coverage
plus modular construction proves tightness of its particular double-greedy
method, not of all deterministic algorithms. An unchanged algorithm cannot
reach 2 on the full class. Static unconstrained submodular maximization does
not provide simultaneous guarantees on every prefix.

No mathematical failed route or research pass was created in this triage.
Algorithmic nesting/extraction is still unresolved. No claim, manuscript,
PDF, audit acceptance or STOC readiness assessment was created.

## One next test for the first bounded RESEARCH pass

Implement exact rational DP with G(S) := [2f(S)>=OPT_|S|] and
R(empty)=true, R(S)=G(S) AND OR_{e in S}R(S\{e}). Record all values,
parent certificates and, separately, reachable good sets with no good one-item
extension. R(E)=false certifies no 2-good chain for that explicit instance;
a dead end alone only rejects the stronger local extension rule.

Bound initial tests to n<=8: (i) source Proposition 11 curvature-1 equal-total
family, (ii) source Proposition 19 coverage/modular family at parameter k=2,3,
with original and swapped h,g and rational g scaling 1/4,1/2,1,2,4;
(iii) at most 200 deterministic-seed weighted coverage pairs, universe <=12,
integer weights 1..5, allowing zero functions and unequal totals. Check tiny
cases by permutation enumeration as a verifier for the DP. Reuse any supplied
identical case certificates rather than recomputing history. Stop generation
on a chain obstruction and verify the explicit table independently.

Successful finite tests prove no universal theorem. A failed local extension
claim is diagnostic only. Use resulting nesting structure to formulate a
polynomial-query constructive invariant without OPT_k access. If no changed
substantive evidence and useful full-scope proof route emerges, stop under the
existing three-pass cap; do not rebrand a subsidiary counterexample as resolution.

## Admission/value assessment

Advance: the exact open-supported uniform sharp-ratio problem is significant
within incremental submodular optimization, with a concrete algorithmic barrier
and independently checkable first diagnostic. A 2-competitive polynomial-oracle
algorithm would match a structural lower bound across every cardinality. This
plausible payoff supports research admission, not a claim of competitive STOC
quality; depth, breadth and actual novelty remain unassessed until a theorem
exists. Publication remains resolution-only. Research passes consumed: 0.
