# Fresh mathematical referee report

Job: `c017-wheeler-referee-a6cac210b41e`.
Snapshot: `e049cdd6f4851af0fd18969fa672c8ab343b1916120d8417cddc05007f4084bb`.
Verdict: **accept the exact combined frozen resolution-paper scope**.
Original status: **proved**, meaning the original decidability question has a
positive algorithmic resolution. This is an internal mathematical assessment,
not external peer review, a formal truth certificate or conference acceptance.

The original question is membership for all finite trimmed deterministic
subsequential transducers under the literal current-v3 definitions, allowing
partial transitions and erasing outputs. I also reviewed the explicitly added
realizability consequence, the O(S^13) membership bound, and pumped failure
certificates. None is silently removed from the accepted scope.

I checked all 20 frozen file hashes and the canonical snapshot digest. source.md
retains SHA-256 `40fc8e967aeefd233cb62ffd0f70d77e772fafbdeb6086724c4c2ab5f591106d`.
I read the frozen arguments, listed supporting evidence and actual primary
results. I did not read checkpoint.md, state.json, historical audit files or
earlier job transcripts. The mandated supervisor note was treated as context,
not evidence of mathematical acceptance. No agents or other Codex workers were
launched. The assessment below reconstructs the proof from definitions.

## Membership argument

**Input order and recursive blocks.** Pairwise universal colex separation of
regular reaching languages is decidable by reversed-NFA comparisons. When it
holds, every reaching language is convex in the defined-path domain. At q its
immediate blocks are epsilon when q is initial, followed by I_p a, ordered by
letter a and then predecessor state. They are disjoint and convex. Iterating
this statement makes I_p z a convex copy whenever p reads z to q. Appending
the same word preserves and reflects input and output colex comparisons: its
reversal is a common left prefix. This includes erasure and proper-suffix cases.

**Global orientations.** For each weak orientation, mark states with a violating
pair from different immediate blocks. Their ranges are independent regular
languages: forgetting input labels from the output-labeled path automaton is
sound precisely because the two blocks are already strictly ordered. Product
reachability decides a strict output comparison, including equality, epsilon
and unequal-length cases. Forward reachability from the marked states gives
exactly all failures of that orientation. For the converse, strip the common
last letter from any within-block violating pair. The sum of lengths decreases,
so this reaches a seed, rather than relying on an unjustified fixed point.

**Branching recurrence.** A nonsimple cyclic SCC has a vertex with two
different internal outgoing letters. Return paths give noncommuting loops u,v.
Their reversed periodic words differ; otherwise both finite words commute by
the period-shift argument. Large enough equal powers A=u^k, B=v^k have a
mismatch before either ends. A strict turn at any state of the component
transports to that vertex. Appending A B^n preserves the turn and puts
successive triples in strictly separated suffix cylinders, with a fixed
interval direction. A finite convex monotone partition cannot split infinitely
many such intervals. Thus a branching SCC passes exactly when its states are
globally monotone in at least one orientation. The existence of a strict turn
when neither orientation holds follows already on a finite sorted witness set.

**Simple cycles.** Unroll the unique internal predecessor for one complete
cycle c, giving I_q=L + I_q c + R. All other children are external predecessor
blocks or an initial singleton. Repetition yields levels Lc^n in increasing
order, Rc^n in decreasing order, with all left levels before all right levels.
There is no residual finite word in every central copy, by length. The exact
criterion is that L+Lc and Rc+R are each globally weakly monotone, with their
orientations chosen independently. A failed side has a strict turn; shifting
it by c^(2n) yields disjoint intervals on levels 2n and 2n+1. Conversely each
adjacent-level test shifts to every adjacent pair. Transitivity then gives a
single orientation on the entire corresponding side, even if the order has
no actual point at the central cut. There are at most two pieces. External
blocks are tested using their global orientation flags and independent ranges.
This does not replace independent prefix ranges by a bounded word sample.

The nested-turn positive control is consistent with this criterion: its two
sides have opposite orientations and only two pieces, despite infinitely many
turns crossing the same cut. The invalid 'some cyclic turn implies failure'
shortcut is absent. Empty sides, constant sides and an initial state on the
cycle are covered by the decomposition.

**Completion and effectiveness.** Noncyclic singleton SCCs inherit finite
partitions from their immediate predecessors in a topological order. Restriction
and common suffix transport give the result at all states of a passing simple
cycle. Thus the finite SCC tests are necessary and sufficient at every state,
including predecessors and descendants of cyclic components. Terminal words
are correctly unused. Empty alphabets and the epsilon-only instance reduce
to finite cases; an empty-domain convention can be handled separately.

**Resources and certificates.** For the explicit encoding S, there are O(S)
immediate blocks and O(S) annular blocks over the chosen representatives,
O(S^2) comparisons, and comparison NFAs of at most O(S^2) size. Straight
epsilon elimination and pair reachability fit the stated O(S^10) elementary
operations per comparison. The extra factor S for symbol-level bit operations
therefore safely gives O(S^13). This is deliberately loose and concerns
membership only. Each rejection after input order supplies the common-loop
pumped turn just constructed. Enumerating its finite base witness terminates
because existence has been proved. Running the decider first and then this
witness search defines a total computable B(T); no complexity for B is inferred.
The fixed-certificate Presburger translation also uses only constant lengths,
coefficients and moduli after finite orbit/residue decomposition. It contains
no variable multiplication or division by an empty period. No solver was run.

## Realizability argument

For each state, the LCP lambda_p of accepted continuation outputs is effectively
computable from a regular range: take any accepted output as a finite prefix
bound and test its prefixes by regular inclusion. Coaccessibility is essential
and supplied by trimming. The normalized edge word is
lambda_p^(-1)(w lambda_r), with normalized terminals defined similarly. Prefix
deletion is justified by the LCP property. All normalized residual ranges have
empty LCP. Consequently equality of normalized residual functions forces equal
defined letters, edge words, terminal data and successor residuals; finite
partition refinement computes exactly that equality. This argument checks
partial continuation domains as well as output values.

A distinct initial state e preserves f(epsilon) as a terminal word and emits
w lambda_r on the first a-edge. Thereafter the normalized quotient is used.
For every nonempty defined u, accumulated output is exactly
H(u)=A_T(u)lambda_delta(s,u), the LCP of all f(uv). At epsilon the accumulated
output stays epsilon. Thus the construction handles a nonempty initial LCP
and initial cycles without introducing an initial output. Merging residuals
before considering convex components is necessary; redundant unary parity is
an exact adverse example for omitting that step.

Canonical state colors have regular reaching languages. After reversal,
color predicates, lex order and shortlex are synchronous regular relations.
The relation E of equal-color endpoints with no differently colored intervening
word is therefore effective by Boolean operations and existential projection.
The stated projection includes arbitrary all-padding continuations after all
free words end; this avoids a hidden existential length bound. Shortlex is a
well-order, so excluding E-equivalent shorter representatives gives one regular
representative per component. Productive genuine-letter cycles decide whether
there are infinitely many components; otherwise their representatives can be
enumerated. These are synchronous relations, not arbitrary rational relations.

E is a convex right-invariant refinement of the canonical colors. Indeed any
word between ua and va ends in a, and its predecessor lies between u and v;
prefix closure and determinism give the required successor color. Definedness,
outputs, final flags and terminal words are constant on a component, making the
finite split C_c well defined. Its reaching languages are exactly the E-classes,
and literal induction shows it computes f and is trimmed.

For necessity, any equivalent Wheeler W partitions D into finitely many convex
state languages. Outside epsilon, each is monochromatic in canonical residual
color. Thus the canonical coloring has finitely many components. Moreover on
each W-state language, H(u)=A_W(u)lambda'_p. Common right append transfers every
monotone piece to H. W's finitely many states and pieces give a global finite
convex partition; separating epsilon handles its exceptional output timing.
Intersecting these pieces with E-classes proves that C_c must pass membership.
This proves soundness of both NO branches. Conversely a passing C_c is the
required equivalent realization. Every construction terminates. No polynomial
realizability bound, minimization or optimality is part of this conclusion.

## Checks actually executed

The new `audit/referee-a6cac210b41e-verify.py` imports the frozen algorithmic
constructors but uses freshly written literal traversal, segmentation and
independent comparison procedures. Its JSON report records:

- 180 complete accessible acyclic instances, 2,223 entire defined paths;
  exact direct input separation and all global flags on the 113 ordered cases
  agree, and finite minimum-piece counts meet the accepted bounds.
- 48 complete finite-domain canonical quotient instances; all 1,146 endpoint
  pairs agree with direct sorted monochromatic runs, the entire representative
  languages agree, and split machines preserve the entire functions.
- All 291 accessible/coaccessible unary one- or two-state models under the
  script's declared finite output/terminal alphabets. A separately derived
  exact unary graph criterion agrees with representative-language finiteness:
  165 YES and 126 NO. There are 9,651 supplementary literal function checks
  through length 37. The unary criterion is that an infinite canonical path
  eventually has a one-state cycle; a finite path always passes.
- Three serialized pump families, 72 instances at n=0..20,37,101,313, replayed
  using fresh literal transition-table evaluation. Both interval directions
  and erasing outputs are covered.

These are finite implementation checks, not proofs of the all-input claims.
The unary test shares normalization and automata constructors; it is not a
second full implementation. No theorem is inferred from absence of a sampled
counterexample. Frozen files were rehashed after the checks and remain unchanged.

## Novelty, significance and remaining gaps

The present bounded primary comparison is recorded in
`audit/referee-a6cac210b41e-literature.md`, including a newly found September
2026 conference publication that still poses both decision problems. Classical
prefix normalization, residual equivalence, the source's LCP identity and
automatic first-order quotient operations are properly credited. Wheeler
language recognition alone does not supply the output criterion.

The independent substantive step is the complete branching-versus-simple-cycle
characterization of an unbounded finite convex partition property. In particular,
the two-side adjacent-shell equivalence and disjoint failure pumping replace an
unbounded partition search by finitely many exact regular-range comparisons.
I find no inspected prior theorem of which this whole step is an elementary
corollary. It resolves the immutable full question, gives a polynomial decision
bound and effective obstruction structure, and supports the useful combined
semantic realizability construction. That is substantive automata-theoretic
value under the project's publication rule. The standard realization ingredients
would not separately warrant another paper.

No unresolved mathematical gap was identified in the exact frozen claim.
The literature screen is bounded, the proof is not formally mechanized, and no
practical performance, optimal exponent, realizability complexity, minimality,
stronger graph convention or STOC quality is certified. These are limitations
of what is asserted, not silently removed parts of the frozen claim. No
manuscript or PDF was authored in this referee job. The structural check-math
result is saved separately; it establishes integrity/provenance only.

Operational note: an initial report patch was rejected because it attempted
delete/add operations on the same path. The fresh report was then written to
this job-specific path and installed as audit/math.md; frozen evidence was not
changed. Web access and source-render glyph warnings were not mathematical data.
