# Fresh mathematical referee report

Job: `c042-strongrsp-referee-5010e06f0ba2`.
Frozen snapshot: `b8a4224397c4874b51af65e8b82a4b17fef250e6e90513e63334f9d6b3b5e4e9`.
Verdict: **accept the full positive resolution**, with a separate conservative
STOC classification of **working_paper**. This is an actual bounded internal
review, not external peer review or a truth certificate.

## Scope and evidence discipline

I read the immutable source, its interpretation, claim, snapshot, the listed
proof/compiler/literature records and checker sources, and inspected the listed
finite-result records. Every file in the snapshot matched its recorded SHA-256.
No checkpoint, state, earlier referee verdict, job transcript or owner session
was consulted. The required supervisor input was treated as unreviewed input,
not an authority for any mathematical conclusion. No frozen input was edited.

The accepted claim is precisely the quantified all-target assertion in
`source.md`, including arbitrary parallel edges, both zero resources, exact
zero optima, disconnected graphs, arbitrary finite nonnegative real weights,
aspect-independent operation and space bounds, actual reported length bounds,
and deterministic aspect-independent polynomial-time witness queries. It is
not a single-target reduction or a claim of exact original-budget feasibility
for originally infeasible targets. The proof gives deliberately loose universal
exponents a=20, b=100; optimizing them is not needed for this assertion.

## Reconstructed decisive argument

1. **Compression and zero optima.** Cost buckets have a tiny interval of width
   at most eta*C/n and subsequent ratios at most 1+eta/2. A minimum-length
   actual edge per ordered endpoint pair and bucket replaces any original edge
   with length no larger and cost at most (1+eta)c+eta*C/n. Replacing a simple
   feasible path therefore costs at most C'=(1+2eta)C. There are polynomially
   many retained edges M<=min(m,n^2(Jc+1)); a bounded-key balanced map avoids
   an m log m overhead for arbitrary parallel inputs. Cost SSSP restricted to
   retained zero-length edges supplies every original zero optimum, using
   actual edges and a cycle-free parent tree. It can safely supply additional
   relaxed-feasible zero-length paths too.

2. **The static boundary oracle is valid for its stated restricted model.**
   Full vertex blocks, nonnegative clock increments and voluntary ticks are
   essential. Tick seeding bounds each popped label by all its higher-clock
   labels. Thus every candidate from a popped predecessor is a convex
   combination of labels no smaller than that predecessor's current label.
   Heap removals are nondecreasing. All edge/tick Bellman inequalities hold,
   including ignored later-predecessor edges and self-loops. Iterating these
   inequalities with failure assigned to unfinished trajectories proves the
   lower bound against arbitrary policies; bounded convergence is applicable
   because all prices lie in [rho,1+rho]. A selected zero-increment edge points
   to an earlier pop; a positive increment/tick increases the clock sum.
   Therefore the selected policy terminates within N=(2q+1)(n+1) decisions
   and realizes the value. Closed zero-increment classes correctly pay failure,
   rather than a spurious smaller algebraic fixed point.

3. **First-hit comparison and rounded values.** With boundary prices between
   X and alpha*X, stopping a full policy at its first inactive vertex charges
   alpha only once. Continuing stopped policies proves the reverse inequality.
   Whole-vertex monotone boundary tables preserve the causality argument.
   Upward rounding by h0 gives a realizing finite-rank policy of payoff <=Z,
   while every action obeys Z<=E[Z_next]+h0. Applying this residual along the
   exact finite-rank optimal policy proves X<=Z<=X+N*h0. No uniform absorption
   bound for all policies, and no SCC contraction assumption, is being used.

4. **Offline integration and total work.** At each midpoint inactive vertices
   use the earlier endpoint, and active coordinates are clipped between the
   inherited endpoints. Clipping preserves the upper estimate and both time
   and clock monotonicity; no clipped label is asserted to realize a policy.
   Rounded endpoints are ordered by a coordinatewise maximum. The induction
   factor is (1+zeta)^(2h+1), with at most two new factors per midpoint level.
   With zeta=1/[16(2D+1)], the final factor is <=16/15. Parent inactivity
   implies inactivity in both children. At one depth, products of endpoint
   ratios telescope to at most (1+rho)/rho=33. Each coordinate can therefore
   witness only O(D) active intervals, giving O(q^2 D^2) active calls per
   vertex over all depths. Weighting this count by incident degree charges
   all edge scans, including parallel edges. Persistent vertex blocks and
   parent-only activation tests avoid an all-vertex scan in each call.

5. **The probability compiler has a finite implementation.** Relative Poisson
   weights decrease away from a bounded-search mode. Downward dyadic rounding
   accumulates at most H*h error per coordinate; beyond 2U the tail ratios are
   at most 1/2. The stated upper normalizer consequently bounds the true one.
   The lower CDF error is <=tau=2E+h. Taking prefix minima over increasing
   means preserves that bound and stochastic monotonicity. Telescoping CDF
   errors gives total variation <=q*tau per clock. Importantly, the PGF bound
   uses z^k below q and zero at overflow, not a capped nonzero overflow term.
   The specified b=64r makes tau<=1/(2^20 N q). All rounding searches have
   bounded integer domains; no exponential, input-weight logarithm or floor
   is an algorithmic primitive.

6. **Events cover the correct optimum.** For an uncovered feasible target,
   let Lstar be the optimum in the retained graph at budget C'. Its largest
   edge lies in [Lstar/n,Lstar]. One edge-local grid event lies between Lstar
   and (1+eta/2)Lstar. This uses the compressed optimum, not an invalid lower
   bound on a shortened representative of the original optimum. At this event,
   each clock's total rounded mean on a fixed optimal path is <=q(1-2eta).
   The Chernoff exponent is q[-log(1-d)-d]>=q*d^2/2, d>=2eta. With the
   selected q the two ideal tails total <1/512. Compiled-law mismatch on at
   most n edges is <=2nq*tau<=2^-19. Hence the first accepted event exists:
   (16/15)(rho+1/512+2^-19)-rho<1/16. No true C-feasible target is lost.

7. **Actual deterministic witnesses.** One fresh full static solve at the
   accepted event is query work. It gives V=Z-rho with initial V<=1/16+2^-20
   and E[V_next]<=V under the selected pointer. With two H variables initially
   1/8, the conservative PGF implies the potential V+H_l+H_c is a
   supermartingale when overflow receives potential 1. The finite arithmetic
   enclosure routine has excess <=2h per H; choosing a surviving outcome by
   its upper score incurs <=4h per decision. N*h<=2^-20 keeps the potential
   below 3/4. Tick actions have the same property. The rank reaches source
   within N decisions, giving actual original edges, not merely a value label.
   If length exceeded (1+8eta)L_t, the rounded-mean lower bound would force
   H_l>(1/8)exp(q[log z+(1-z)/z]-log z)>1. Here
   log z+(1-z)/z>= (1-z)^2/2 and q*(8eta)^2/18>log 8. The same reasoning
   bounds cost by (1+8eta)C'. This contradicts the maintained potential.
   Cycle erasure preserves both bounds. Finally
   (1+8eta)(1+eta)<=1+epsilon and
   (1+8eta)(1+2eta)<=1+epsilon for eta=epsilon/1000.

8. **Numerical and resource implementation.** I checked the log-tail direction
   x0>=x, the overflow/underflow guards using h<=H<=1, the small-argument
   Horner absolute-error bound, and squaring-error propagation. For b>=32,
   the stated 2^(5b+32) error amplification still leaves error <2^-20b;
   adding 2^-10b is an upper enclosure before the final upward dyadic round.
   Stored numbers have O(p) dyadic precision, while the finite log series has
   only O(p) terms and polynomial rational encoding length, where
   p=O(log(n+2)+log(1/eta+2)). No power with exponent Theta(1/eta) is stored
   as an unrounded rational. Sorting only M*J events gives log E=O(p).
   Combining the activity count with the q^4 static cost gives
   O((m+n)eta^-12 p^8), within the claimed loose universal exponents.
   Persistent storage, probability tables, and static scratch fit the same
   larger bound. Query work is polynomial in n and 1/epsilon since
   M<=n^2(Jc+1); scratch is bounded by the allowed near-linear space.
   Output-walk storage is O(nq), followed by a vertex-stack cycle erasure.

The E=0, one-event and two-event cases use only zero-length SSSP or endpoint
solves and satisfy the same estimates. Originally infeasible targets need not
be distinguished exactly; every reported witness still meets the relaxed
cost bound. An unreachable target has failure value 1 and cannot pass the
acceptance threshold. Empty source paths and zero-cost cycles are covered.

## Independent checks actually performed

`audit/referee-checks.py` imports no frozen checker. It implements a fresh
ordered oracle and compares it with synchronous finite-horizon Bellman DP
initialized at failure. Exact Fraction arithmetic passed 64 cases and 624
active-state comparisons at n=4, q=2,3, with arbitrary joint laws, closed
classes, self-loops, an extremely small probability, whole-vertex boundary
prices, upward rounding, policy payoffs, ranks and all-action residuals.
Four fresh monotone sequences also passed 576 state checks of the rounded
clipped recursion, including inactive blocks, against the synchronous
reference. Results and reproduction code are in `audit/referee-checks.json`
and `audit/referee-checks.py`. These finite tests support but do not establish
the universal proof or a production running-time claim. No full algorithm
execution at the enormous prescribed q, formalization, or independent human
review is claimed. The frozen Decimal exponential checks remain numerical
smoke tests; my enclosure assessment uses the analytic bounds above.

## Current prior work, contribution, and limits

On 2026-11-03 UTC I directly refreshed the primary arXiv HTML statements and
the current unversioned record, which identifies 29 October v2 as current.
The precise comparisons and an additional offline-SSSP primary result found
in this review are recorded in `audit/referee-literature.md`.

The Poisson clock DP and conditional-expectation potential are prior work;
recursive offline activation and multiplicative counting are also prior work.
The accepted new step is a costed nonadditive, vertex-closed first-hit oracle
with bounded positive prices, finite-rank rounding and clipping, integrated
with local scale events to solve all targets at once. The cited ordinary-SSSP
theorems neither state that stopped stochastic contract nor supply the required
all-target RSP algorithm. The single-target bottleneck reduction also does not
give the aggregate bound. Thus the result is not an elementary restatement or
routine corollary of the nearest verified theorems. It resolves an explicitly
identified numerical-aspect barrier for a classical constrained-path problem.

No equivalent full resolution was identified in the bounded current primary
search. This is not an exhaustive priority certificate. No correctness or
original-scope gap remains identified in the frozen claim after this review.
The separate STOC assessment remains conservative: the epsilon dependence is
very loose, the principal architectures are imported, a general method beyond
this clock model is not established, and the dossier still needs concise
submission exposition. These are venue-strength and presentation limitations,
not a silent narrowing of the accepted theorem.
