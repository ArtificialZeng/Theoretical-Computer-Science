# TRIAGE checkpoint

Job: c025-incdec-triage-ff0d5f864af1. Decision: advance to bounded RESEARCH.
Original status: unresolved. Candidate kind: none. Research passes remain 0/3;
no usage/revision/failure counter or scheduling state was reset or edited.

The original sharp deterministic ratio is open-supported by the current
Acta Informatica source, Section 5 pp.20-21. Verified baselines are structural
lower bound 2 (Proposition 11) and polynomial upper bound 1+e/(e-1)
(Corollary 2). Equal totals already have ratio 2 (Proposition 17).
The existing double-greedy method has a matching 1+e/(e-1) worst case
(Proposition 19/Corollary 20), so a 2-upper-bound route must change the method.

Precise quantifiers and definitions are in problem.md. Crucial model point:
the source infimum over algorithms is not explicitly efficiency-restricted.
Keep C_struct and C_poly distinct; the requested polynomial value-oracle
construction is additional. A polynomial 2-algorithm settles both. An oracle
lower bound alone does not settle the structural source question. Normalizing
nonnegative baselines and adding k=0 preserve the worst-case sharp constants.

Evidence: evidence/triage.md and evidence/triage-validation.json. Both source
inputs match their manifest. Source.md remains byte-identical. Live primary
publisher/ESA records were checked. Adjacent ESA2026 1.373 incremental result
only addresses the monotone incremental setting, not arbitrary paired functions.
No equivalent full resolution was found in the bounded search; priority is not
certified. Current registry and supplied screening were checked, without rerunning
exhaustive diagnostics. No proof experiment or failed research route occurred.

Obstacle: no universal 2-good-chain theorem or polynomial extraction algorithm
is known here. Accessibility of every good set is stronger than existence of
one complete good chain. A local dead end is not a disproof of the original.

One next test: in the first <=25-minute RESEARCH pass, implement the exact
rational Boolean-lattice reachability DP for 2-good sets on n<=8 coverage pairs,
including source equal-total and tight-double-greedy adversaries, swapped roles
and unequal scales; cap additional seeded weighted-coverage cases at 200.
Record complete tables and DP/permutation checks. Distinguish R(E)=false from
failure of a stronger local extension rule, then seek a polynomial constructive
invariant without OPT_k access. Full bounds are in evidence/triage.md. Finite
success is evidence only; diagnostic counterexamples are not publication outputs.

No candidate, manuscript/PDF, acceptance metadata or readiness verdict exists.
Preserved intake summaries are in evidence/pretriage-problem.md and
evidence/pretriage-checkpoint.md. Full original scope and publication/STOC
gates are unchanged.
