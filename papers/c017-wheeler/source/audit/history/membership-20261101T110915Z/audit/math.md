# Fresh mathematical review

Job: `c017-wheeler-referee-dd13950aae3a` (referee), 2026-11-01 UTC.
Frozen snapshot: `aaa91b59e8425f6cb4943fc3132e3ef9680e93dbb77aad8bca7bfce55d898516`.

**Verdict: accept the exact frozen resolution-paper claim.** The argument gives
a terminating decision procedure for the entire immutable membership question,
including empty transition outputs, and justifies the stated conservative
O(S^13) bound for the decision procedure. The single-pump certificate consequence
and a total computable template bound are also justified. This is an internal
fresh-context mathematical assessment, not external peer review or a formal
truth certificate. No manuscript or PDF was authored in this job.

## Scope and integrity

I read source.md, problem.md, claim.json, the snapshot and its listed inputs,
along with the required policy and referee/contract instructions. The assessment
uses the mathematical arguments and actual primary sources, not the proposer's
assessment of them. I did not read checkpoint.md, state.json, previous audits,
job transcripts, or progress summaries. The more specific fresh-packet restriction
also excluded the supervisor root note. All 13 frozen file hashes and the
snapshot mapping digest matched; see referee-integrity.json. The original
source hash remains
`40fc8e967aeefd233cb62ffd0f70d77e772fafbdeb6086724c4c2ab5f591106d`.

The accepted property is exactly total separation of the reaching languages
I_q in colex, together with a finite partition of each I_q into relatively convex
pieces on which accumulated transition output is weakly monotone in either
orientation. There is no prescribed number of pieces, regular-endpoint
assumption, nonerasure assumption, or restriction on recurrent components.
Terminal outputs are correctly irrelevant to this property. Semantic realization
by another machine, optimal complexity and minimization remain separate tasks.

## Reconstruction and attacks on the proof

1. **Convex incoming blocks.** Once the nonempty I_p are totally separated,
   every word at q is either epsilon (only when q is the initial state) or
   uniquely u a with u in an I_p and delta(p,a)=q. Distinct letters determine
   colex order; for the same letter the state order determines it. Consequently
   these are disjoint convex blocks, ordered by (a,p), after epsilon. Iterating
   gives convex copies I_p z inside I_q. Reversing words shows directly that
   appending the same suffix preserves AND reflects strict and weak colex
   comparisons. The output identity f_q(u z)=f_p(u) omega(p,z) therefore
   transfers comparisons without an output-delay hypothesis, even under erasure.

2. **Regular ranges and global flags.** Relabeling the input graph by output
   words produces exactly the regular range O_p: forgetting input labels creates
   no spurious graph paths. Splitting word edges and retaining epsilon edges is
   effective. Comparing two independent ranges is decided by a finite automaton
   product after reversal: equal-prefix synchronization, a first different
   letter, or a proper-prefix termination exhaust all comparisons. Independent
   choices are appropriate precisely because distinct ordered blocks permit
   every pair of their inputs. This argument does not intersect arbitrary
   rational relations. A violating pair at a state either lies in different
   immediate blocks, giving a seed, or strips one shared final letter and moves
   to a predecessor. The combined input length decreases, so stripping reaches
   a seed. Conversely, every seed violation propagates along every defined
   path. Thus forward reachability from each directional seed set computes
   exactly the globally nondecreasing/nonincreasing flags; no unjustified
   greatest-fixed-point choice is involved.

3. **Strict turns and partition boundaries.** Failure of both weak orientations
   supplies a rising pair and a falling pair. Sorting their at most four inputs,
   removing consecutive equal values, and taking a sign reversal produces a
   strict peak or valley. This reasoning needs only a finite subsequence of
   the total order, not adjacent elements of the infinite domain. In a finite
   convex partition its pieces can be sorted. A strict-turn interval must cross
   a cut between pieces. Strictly separated such intervals cannot use the same
   cut, even when a cut has no endpoint in the domain. Hence infinitely many
   separated turns exclude every finite partition. Nested intervals alone do
   not give this obstruction.

4. **Branching recurrent components.** A cyclic strongly connected component
   other than a directed simple cycle has a vertex r with two distinct internal
   outgoing labeled edges. Determinism gives different first letters, so the
   completed return loops u,v do not commute. Their reversed periodic infinite
   words cannot coincide: if they did, invariance under either period would
   make both rev(u)rev(v) and rev(v)rev(u) the same prefix of that infinite word,
   a contradiction. A sufficiently large common power makes A=u^k and B=v^k
   suffix-incomparable. Move any nonmonotone state's strict turn to r along a
   fixed path. The intervals of alpha_i A B^n then have a fixed separating
   mismatch between rev(A) and rev(B), after the common rev(B)^n. The mismatch
   occurs before either block ends, so arbitrary alpha_i cannot undo separation.
   All output turn signs survive common right concatenation. This proves the
   necessity of global monotonicity in a branching component. If all its states
   are globally monotone, one piece at each state proves sufficiency.

5. **Simple cycles: necessity.** Unroll the unique internal predecessor for one
   circuit at q. The other children are outside-component blocks or the initial
   singleton. This gives the ordered split I_q=L + I_q c + R. Every finite word
   eventually leaves the descending chain I_q c^n by its length, so no residual
   set is omitted. Its shells are L_n=L c^n and R_n=R c^n, ordered as
   L_0<L_1<...<...<R_1<R_0. In particular the two unions define convex sides.
   If L_0 union L_1 has a strict turn, appending c^(2n) puts its copies in
   levels {2n,2n+1}, giving strictly separated intervals. The same argument
   moves intervals in the decreasing direction on the right. Thus finite
   piecewise monotonicity requires each two-level restriction to have a weak
   global orientation, independently on the two sides.

6. **Simple cycles: sufficiency and effectiveness.** If L_0 union L_1 is
   monotone in one orientation, common-suffix cancellation transfers that SAME
   orientation to every L_n union L_(n+1). When L is nonempty, all levels are
   nonempty, and transitivity through finitely many intermediate levels compares
   any two points. If L is empty there is no condition. The argument applies
   in the reverse level order to R. Thus there are at most two convex monotone
   pieces, without requiring a cut to be represented by a finite word. Each
   two-level restriction is a finite ordered block list: within each I_p z its
   orientation is precisely p's global flag; across blocks it is precisely an
   independent range comparison. The proposed test is therefore both necessary
   and sufficient. Other states on the cycle inherit at most two pieces by
   pulling back q's partition through a fixed path into q. This pullback is
   convex and reflects output comparisons.

7. **Completion and certificates.** After testing all cyclic components, every
   remaining component is a loop-free singleton. In topological order, append
   its finitely many predecessor partitions to its ordered incoming blocks,
   with an initial singleton if present. This gives finite partitions at every
   state. Conversely each rejection after input-order validation has one of the
   separated-turn constructions above. They use a common loop pump and fixed
   bases and therefore satisfy exactly all four first-test conditions, including
   both allowed interval directions. Enumerating a guaranteed finite base turn
   terminates after the independent membership decision. Returning the maximum
   template length on rejection, and zero on acceptance or invalid descriptions,
   defines a total computable B; this is not a circular use of B to decide the
   property. The promised finite trimmed model and the empty-alphabet cases
   are decidable directly. No terminal-output normalization is needed.

8. **Resource bound.** There are m+1 immediate blocks in total. Across one
   representative per simple cycle there are at most m+1 external/initial shell
   blocks: each incoming edge outside its component is encountered once in the
   backward circuit. Doubling them still gives O(S) blocks. Appended paths have
   at most two circuits, so even the loose O(S^2) bound on their output lengths
   is safe. Compared epsilon-NFAs thus have O(S^2) states and original edges.
   There are O(S^2) comparisons. Boolean epsilon-closure tables, live-state
   predicates and enumeration of equal/unequal symbol transition target pairs
   implement each comparison within O(S^10) elementary operations, including
   alphabet size at most S. Indices have O(log S) bits and an original symbol
   identifier has at most S bits, so the stated deliberately loose O(S^13)
   bit-cost bound is consistent with this explicit finite-graph implementation.
   No witness enumeration or Presburger decision is charged to that decision
   bound. No optimality claim is accepted.

## Independent computation actually performed

`python3 audit/referee_checks.py` is a new verifier/control script. It imports
the frozen decision prototype for comparison, but independently constructs
reversed range automata and determinizes by epsilon-closed subsets. Its direct
input runs, partition DP and turn extraction do not call the prototype's run
enumerator, comparator, annular expansion or finite-partition DP.

All checks passed; the complete counts are in referee-checks.json:

- 9,230 independent regular input/output range comparisons agreed.
- 306 input-ordered machines were checked: 210 accepted and 96 rejected.
  The set includes the empty input alphabet, all erasure, 64 initial-on-cycle
  machines on cycles of 2 through 5 states, and 240 machines from a new seed
  with binary/ternary inputs and variable outputs including epsilon.
- 783 finite state lists containing 24,039 runs respected every asserted
  global flag and each accepted piece-count upper bound. The independently
  implemented finite DP was crosschecked on 3,280 ternary value sequences.
- All 96 sampled rejections supplied newly extracted strict-turn pump families;
  the direct verifier checked order, turn and strict interval separation at
  exponents 0 through 5, 15 and 31. There were no depth-bounded inconclusive
  rejections. These finite controls supplement, and do not prove, the all-n
  constructions checked above.
- The three serialized frozen certificates were checked from their transition
  tables by fresh direct runs at exponents 0 through 32, 127 and 1024 (105
  family instances). The eight named controls were additionally called without
  running the evidence-writing main routines; the nested-turn positive control
  is correctly accepted. No frozen evidence was rewritten.

## Current primary-source comparison and value

Primary sources were rechecked live on 2026-11-01, with these limits:

- [D'Agostino and Paradiso, arXiv:2606.29405v3](https://arxiv.org/html/2606.29405v3),
  Sections 2.1/2.2, Definitions 4/5, and Section 4, match the frozen model and
  identify its membership decision as unresolved. The
  [current version history](https://arxiv.org/abs/2606.29405) still lists v3,
  13 August 2026. The candidate addresses precisely that machine property.
- [Becker et al., Optimal Wheeler Language Recognition, arXiv:2306.04737v2](https://arxiv.org/abs/2306.04737),
  primary abstract: O(mn) recognition asks whether a DFA's accepted language
  has a Wheeler presentation. This is a different predicate and contains no
  output-partition decision in the inspected statement.
- [D'Agostino, Martincigh and Policriti, Ordering Regular Languages: A Danger Zone](https://ceur-ws.org/Vol-3072/paper5.pdf),
  Definition 1 and the discussion following it, pp. 4-5, give the known
  graph/input-order baseline with stronger initial-state/input-consistency
  conventions. The present proof derives its blocks directly and does not
  assume those conventions.
- [Filiot, Lhote and Reynier, Lexicographic Transductions of Finite Words,
  MFCS 2025, article 50](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.50),
  official abstract/metadata, concerns exponential-growth transductions and
  MSO set interpretations, rather than this order condition. I do not claim
  a full-text exclusion of every potentially relevant technique.
- An additional primary search hit, [Pin and Weil, The wreath product principle
  for ordered semigroups](https://www.irif.fr/~jep/PDF/WreathProduct.pdf),
  Sections 2.1 and 3.1, uses the length-preserving product order on words and
  structurally ordered transducers. Proposition 3.1 is a sufficient
  order-preservation statement in that model; it does not decide the present
  finite convex colex partition property.
- The auxiliary fixed-certificate note's periodic-output/Presburger reduction
  is valid on inspection: residue alignment yields A B^n C, and character
  positions use only linear terms and fixed congruences. The original Cooper
  URL timed out during direct fetching; an alternate primary scan was available
  without machine-readable text. This access limitation is not mathematical
  evidence. General quantifier elimination and the required constant-modulus
  syntax were independently verified in [Haase et al., ICALP 2024 article 142,
  Section 2 and Corollary 3.2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.142/LIPIcs.ICALP.2024.142.pdf).
  Inside-out elimination with Boolean duality covers mixed quantifiers; its
  single-block exponential bound is not transferred to the whole verifier.
  This routine auxiliary fact is not a dependency of the membership algorithm
  or a basis for the innovation verdict.

Fresh queries included exact Wheeler-transducer membership/decidability terms;
finite-state or sequential transducers with piecewise monotonicity;
lexicographic monotonicity/decidability; rational string-function monotonicity;
and order-preserving sequential transducers. Third-party summaries and old-v2
criticisms were not used as premises. No equivalent resolution was identified
in the inspected current primary sources. This is a bounded literature result,
not an exhaustive priority guarantee.

The input-order comparisons and automata reachability are routine ingredients.
The substantive independent step is the complete recurrent-component criterion:
branching forces one global orientation, whereas a simple cycle permits a
persistent central cut and is decided by exactly two adjacent-shell tests.
It turns the unbounded, endpoint-unrepresented partition quantifier into finitely
many exact independent-range comparisons and produces disjoint pump obstructions
on rejection. The nested-turn example shows why ordinary cyclic-turn pumping
does not already imply this criterion. None of the inspected prior results
supplies that reduction. This is a full decision theorem for a specified
recently proposed class, with structural explanations of its positive and
negative instances; it is not an elementary restatement of input-order
recognition or a toy subclass. That is substantive theoretical value at the
scope claimed. It establishes no practical indexing speedup, optimal bound,
STOC suitability, external acceptance or result on equivalent realization.

## Final assessment

Original scope resolved: yes, positively. Correctness: passes the reconstructed
proof and independent attacks above. Novelty/value: passes the stated policy
within the documented bounded primary-source comparison. Remaining mathematical
gaps: none identified. No claim or decisive frozen evidence was changed. The
required innovation assessment is in innovation.json. The separate check-math
gate checks integrity and role provenance only; its actual result is recorded
in referee-check-math.json. Future writing and release remain separate phases.
