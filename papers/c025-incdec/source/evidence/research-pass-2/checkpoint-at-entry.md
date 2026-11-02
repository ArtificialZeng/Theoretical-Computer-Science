# RESEARCH pass 1 checkpoint

Job: c025-incdec-research-393eb62fad16. Decision: continue bounded research.
Original status: unresolved. Candidate kind: none. This is assigned research
pass 1 of at most 3; entry TRIAGE recorded 0 consumed. Runner owns counters;
no scheduling/usage/revision/failure counter was reset or edited. The entry
checkpoint is preserved at evidence/research-pass-1/checkpoint-at-entry.md.

Immutable source SHA256 remains
12956c470e37f8a548f510c7eb1781eda7b961999c5fa1163df43b56513b45a4.
Full arbitrary unequal-total all-cardinality scope remains unchanged, as do
the distinction C_struct <= C_poly and the polynomial-oracle requirement.
Nearest primary bounds remain structural lower 2 and efficient upper
1+e/(e-1); equal totals and the source double-greedy tightness are known.
Current bounded primary refresh found no full resolution; see literature.md
under evidence/research-pass-1. This is not a priority certificate.

New exact evidence: code/chain_dp.py tabulates 255 coverage/modular instances,
n<=8: 55 mandatory/source-derived scaled cases and 200 seeded coverage pairs.
Every input admits a complete 2-good chain. All subset values, good thresholds,
reachability, parent edges, backward viability, and chains are stored in
chain-tables.json; 195 instances n<=6 also enumerate all permutations. The
separate code/verify_chain_evidence.py recomputes every table from its input
description and verifies certificates exactly. Finite tests prove no general
chain theorem.

Failed route: every reachable good set extends is FALSE. There are 122 local
dead ends in 10 inputs. A minimal n=3 exact weighted-coverage witness with
h=0 has g=[0,12,4,13,5,12,9,13], f=[13,9,12,5,13,4,12,0], and
OPT=[13,13,12,0]. Prefix {a} is good but both extensions fail; c,b,a is a
complete good chain. See local-obstruction.md and independent-verification.json.
This intermediate counterexample does not disprove the original question.

Changed full-scope route: actual-gain bidirectional greedy maintains L subset T
and maximizes f(L+e)-f(L) or f(T-e)-f(T), appending left or prepending right.
This differs from the source algorithm and uses O(n^2) value queries. It has
nonnegative, nonincreasing selected gains, and its left/right boundaries have
values at least g(E)/h(E). These elementary facts do not prove ratio 2 for
unequal totals. Both side tie priorities pass all 255 exact inputs (510 runs,
worst ratio 7/4). A general-function LP screen completes n=3..6: 4688 successful
numerical optimizations, no positive f(O)-2f(prefix). Another 90-second screen
at n=7 completes only a partial 21-word prefix / 2435 LP calls. It is incomplete;
solver nonfindings are floating screening, never exact class nonexistence.

Proof lead: trace-dual.json and compact-dual.json contain coefficientwise
verified rational dual certificates for ONE six-item trace RLLRRL, prefix
{1,2}, comparator {0,5}. The compact certificate uses 17 aggregate inequalities,
including choices after the assessed prefix. It is no general theorem. See
route-status.md for definitions, limits and operational failures. The exact
unresolved kernel is the net-greedy ratio-2 inequality at arbitrary n,k,h,g;
this sufficient lemma is not asserted equivalent to the original question.

One next test for pass 2: derive a general-n telescoping certificate for
f(O)<=2f(S_k) under the actual-gain greedy comparisons, using the tracked
comparator O_i=(O union L_i) intersection T_i and cardinality excess
|O_i|-k. Start from compact-dual.json, allow future choices, and seek a
nonnegative rational combination of monotonicity/submodularity and greedy
inequalities that holds for every trace/membership pattern. Use bounded exact
dual synthesis to attack any proposed formula before calling it a proof.
A complete proof would settle both constants with the known lower bound 2;
a method counterexample only rejects this route. Two passes remain under the
configured cap, subject to the runner's actual accounting.

No claim.json, acceptance/readiness metadata, manuscript or PDF was created.
Only a fully resolved substantive original result may become a candidate.
