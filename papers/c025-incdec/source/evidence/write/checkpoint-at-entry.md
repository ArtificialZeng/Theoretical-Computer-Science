# RESEARCH pass 3 checkpoint — proposed complete resolution

Job c025-incdec-research-76b5f4e5209a. Assigned final research pass 3 of cap 3;
runner counters are unchanged. Decision proposed: candidate, resolution-paper,
original_status proved, subject to actual fresh mathematical/innovation review.
No acceptance, STOC assessment, manuscript, PDF, or external action is created.
The entry checkpoint is preserved in evidence/research-pass-3/checkpoint-at-entry.md.
Source remains immutable, SHA256
12956c470e37f8a548f510c7eb1781eda7b961999c5fa1163df43b56513b45a4.

The assigned bidirectional kernel f(O)<=f(L)+G+|O|d is FALSE. A new prefix-only
LP formulation found an exact eight-item weighted-coverage witness after 522
calls. It has maximal trace L(0),R(1),L(2), comparator O={1,3}, L={0,2},
G=5/29,H=24/29,f(L)=19/29,f(O)=1,d=2/29, giving residual gap 1/29.
Every input hypothesis and maximal choice is rationally checked. A greedy
completion still has factor-2 prefixes; this only kills the intermediate kernel,
not the bidirectional algorithm or original question. See research-progress.md,
prefix-kernel-screen.json, and exact-verification.json in evidence/research-pass-3.
Earlier limited certificates and nonfindings are preserved without alteration.

A changed full-scope algorithm avoids the failed kernel: compare H=h(E) and
G=g(E). If H>=G, greedily maximize actual F(P+e)-F(P) on ONE growing prefix,
even after gains turn negative. Otherwise swap h/g, construct that greedy order,
and return its reverse. Fixed deterministic tie breaking and O(n^2) oracle cost
are explicit. The all-n proof is evidence/research-pass-3/oriented-greedy-proof.md.
For its H>=G orientation, greedy gains a_i are nonincreasing. For |O|=|P_k|=k
and d=a_{k+1}>=0, monotonicity of h gives F(O)<=F(O union P_k)+G, while
submodularity and maximality give F(O union P_k)<=F(P_k)+kd and
kd<=F(P_k)-G. Hence F(O)<=2F(P_k). If d<0, the decreasing tail gives
F(P_k)>=H, so F(O)<=H+G<=2F(P_k). Endpoints, reversal, normalization,
zero objectives and all ties are included. This resolves the arbitrary-pair
all-cardinality oracle upper bound at 2. The source's coverage-star lower
bound 2(n-1)/n for every permutation is reproduced for all n, proving both
C_struct=C_poly=2. No theorem about the abandoned bidirectional method is needed.

The proof has explicit nonnegative-summand coefficient identities. Exact tests
on 261 instances include source equal-total/lower-bound/source-algorithm
adversaries, all prior witnesses, the new residual witness, and zero/empty cases.
A separate arbitrary-table numerical LP attack found no violation in 492 calls
at n=3..8; these are numerical diagnostics, not the universal proof. The separate
standard-library exact checker verifies diagnostic tables, coefficient identities
and the known lower family; it is not a fresh referee or a formal proof assistant.

Current primary comparison is evidence/research-pass-3/literature.md. The nearest
verified full-pair source remains upper 1+e/(e-1), lower 2; the ESA 1.373 result
is different and unrestricted in efficiency. No complete equivalent was found
in the bounded search. The proposed substantive delta is closing the entire
sharp deterministic gap with a new endpoint-oriented actual-objective rule,
not improving a restricted class. The short proof's novelty, substantive value,
and STOC depth/breadth still require actual fresh review. No venue-readiness
label or numerical acceptance chance is inferred.

One next test: a fresh referee should independently audit the complete proof's
union-loss inequality, sign split, endpoint reversal, oracle reading and
matching lower bound against the frozen source/problem, then check generic
additive-nonmonotonicity antecedents before judging novelty/substantive value
and the separate STOC criteria. This requests review, not another research pass.
