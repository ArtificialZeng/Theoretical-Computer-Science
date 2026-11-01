# Fresh mathematical referee report

Job: `c002-coverage-referee-3e90f78a9294`.
Snapshot: `26d2a64f317984b35b49212bdc46529ccb7f19bc1be1b5e471d28d308d18456e`.
Review date: 2026-11-01 Asia/Shanghai (2026-10-31 UTC).

**Verdict: accept the exact frozen resolution-paper candidate.** The proof
establishes `disc <= 4kt(kt-1)^2` for every allowed parameter tuple in the
immutable question. Its deterministic polynomial-time strengthening also
passes in the explicitly stated input model. The structural reduction has
substantive mathematical value relative to the primary results inspected.
This is a local fresh model review, not external peer review or a truth
certificate. No manuscript or PDF was authored in this job.

## Scope and frozen evidence

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, the
listed proof, code, exact diagnostic output and cited source material, plus
the required project policy/instructions. I did not read checkpoint or
scheduling state, an earlier review, owner confidence, intake handoffs or
historical transcripts. All 16 frozen files and the canonical snapshot
digest were independently rehashed and matched; see
`audit/referee-integrity.json`. No frozen input was changed.

The target counts every tagged feature occurrence in each item's total
degree, including equal incidence subsets within or across functions. It
requires one polynomial independent of n and m for all positive n,m,t and
all k>=2. The candidate supplies exactly this, without restricting feature
rank, the number of features, t, k, or the incidence family. The extra time
claim measures explicitly listed incidences and item slots, with binary
k,t. Empty color classes are allowed. The source's deduplicated-union
notation remains a separately flagged ambiguity; the original covering
universes and singleton example support the frozen occurrence reading.
The review neither changes that convention nor uses it to manufacture a
counterexample. Arbitrary weights and influence-only sparsity are outside
the immutable target and are not claimed.

## Reconstruction and adversarial checks

Write q=kt>=2. Each of the following steps is established for all finite
inputs; the finite diagnostics below are supplementary.

1. **Large occurrences and Hall's quantifier.** For any subfamily Q of
   occurrences of size at least q, incidence counting gives
   `q|Q| <= t|union Q|`. Thus its neighborhood has at least k|Q| items.
   For an arbitrary subset X of k demand copies per occurrence, let Q
   be the represented occurrences. Then `|N(X)|>=k|Q|>=|X|`. This checks
   subsets containing only some copies as well as whole demand groups.
   Hall therefore supplies pairwise disjoint k-item blocks, one inside
   every large occurrence. Multiplicity is correctly included throughout.

2. **Protected blocks and symmetry.** Partition the remaining items into
   singletons. The k cyclic shifts of a full block give every color to
   that block in every state. Consequently every large feature contributes
   one to each color for every possible choice of all states, even if it
   also meets other blocks. Initially independent uniform shifts are
   invariant under a simultaneous color rotation, giving a common
   expectation mu_i for all colors of each function. This uses block
   independence, and never requires independence of items in one block.

3. **Interaction classes.** A block meets at most |B|t<=q occurrences.
   A small occurrence has at most q-1 items, hence adds at most q-2 other
   blocks as neighbors of a block it meets. The simple graph degree is
   at most q(q-2), including repeated incidence sets by overcounting.
   It has at most `(q-1)^2` greedy classes. Each small occurrence meets
   at most one block of a given class. At q=2 all small features are
   singletons, so the graph is edgeless and the bound H=1 remains valid.

4. **Affine categorical extension.** Hold all laws outside a class fixed.
   For a small feature e meeting class block B, let v_e,c be its outside
   miss probability and z_e,c(r) its hit indicator inside B in state r.
   Its hit probability is precisely
   `1-v_e,c + v_e,c sum_r p_B,r z_e,c(r)`.
   Distinct items of B have distinct colors, so
   `sum_c z_e,c(r)=|e intersect B|`, even for a multi-item intersection.
   The nonnegative matrix obtained by summing over tagged features obeys
   `sum_(i,c) A_((i,c),(B,r)) <= sum_(j in B) degree_small(j) <= q`.
   This is the critical column estimate: it counts incidence multiplicity,
   not merely the number of affected functions, and has no hidden factor
   from the number of colors or features.

5. **Rounding lemma.** The submitted self-contained argument is valid.
   With V strictly fractional coordinates, every fractional simplex has
   at least two such coordinates, giving at most V/2 group equations.
   After dropping rows of residual absolute mass <=2D, the column bound
   implies strictly fewer than V/2 surviving rows. Hence a nonzero
   null direction exists, preserving all retained equations and simplex
   sums, and a bounded move fixes at least one further coordinate. A row
   stays exactly at its target until its single deletion; all subsequent
   movement costs at most its then-residual mass, <=2D. Errors do not
   accumulate across nullspace moves. D=0, zero coordinates, fixed groups,
   odd V and threshold equality cause no exception. This is the known
   multiple-choice theorem, not an innovation of this packet.

6. **Telescoping with changing coefficients.** Apply that lemma with D=q
   to each class. Its infinity error is <=2q in every (i,c) coordinate.
   Matrices are recomputed with the actual outside marginals; they need
   not agree across classes. The functional Phi on full block-law vectors
   is the same at consecutive stages. Previously rounded point masses
   and still-uniform later laws remain a valid product-law definition.
   At the end Phi equals literal coverage. Thus
   `|f_i(T_c)-mu_i|<=2qH`, and pairwise color differences are <=4qH,
   proving the exact frozen polynomial. This is an analytic proof for
   all parameters, not an extrapolation from search.

7. **Constructive claim.** If k>=n, distinct colors on all items give
   discrepancy <=t with polynomial-size output labels. Otherwise k<n,
   and replacing t by the actual degree d (or 1 if zero) keeps all
   expanded dimensions polynomial in explicit input size and only
   strengthens the displayed bound. Matching has at most n demand
   copies; actual class count is at most n. At each class the outside
   miss factors are 0, 1, or `(k-a)/k`, so coefficients have a common
   denominator dividing k^n and polynomial bit length. The verified
   rational rounding theorem applies. The alternative LP-vertex
   implementation also uses submatrices of the fixed class matrix and
   fixed polynomial-length targets; it avoids assuming arbitrary
   repeated rational null directions have a bit-complexity bound.
   Empty functions can be discarded. Unused items, zero features and
   very large binary t introduce no difficulty.

I found no unresolved mathematical gap, counterexample, circular use of a
lemma, unjustified limiting step or dependence on an unproved conjecture.

## Independent computational evidence

I wrote `audit/referee_verify.py` without importing or executing the
researcher's implementation, which would overwrite frozen output. It ran
successfully with exact `fractions.Fraction` arithmetic and seed 391057.
The result is `audit/referee-verification.json`:

- All seven serialized certificates were independently checked for the
  partition, protected witnesses, cyclic coloring, literal coverage,
  interaction classes and stated bound.
- All 4,111 subfamilies of their large features were checked for Hall
  expansion, including the family with twelve large occurrences.
- 24 uniform, nonuniform and partly deterministic block-law cases were
  checked by enumerating literal colorings (6,900 states). Their 45 class
  affine matrices and 291 columns passed. Coefficients were obtained by
  enumerating outside states, independently of the submitted product-of-
  miss-factors implementation. Additional held-out partitions included
  every nonempty item subset and repeated subsets with distinct tags.
- 160 small signed-rational grouped matrices were checked for the rounding
  inequality by complete enumeration of integral choices, without a
  floating-coordinate or nullspace implementation.

No full product enumeration was attempted for the two largest fixtures.
These finite tests are diagnostics, not a certificate of the infinite
theorem or of the algorithm's asymptotic running time.

## Current novelty and substantive significance

Primary records and current searches are recorded in
`audit/referee-literature.md`. The nearest coverage result is
[Avila--Rohwedder--Wennmann, ESA 2026, Theorem 3](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.139),
with logarithmic size dependence; its Section 5 already contains the
independent-class/rounding architecture. The exact grouped matrix lemma
is [Glaßer--Reitwießner--Witek, FSTTCS 2011, Theorem 2](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2011.55),
attributed there to Doerr--Srivastav (2003). Hall matching, greedy coloring
and the rounding theorem are standard and receive no novelty credit.

The substantive delta is a compatible choice space for both halves of
the nonlinear problem: all large features are identically balanced under
every allowed state choice, while small features retain low-column-mass
affine extensions over the same states. Neither Hall allocation alone
nor the grouped linear theorem proves that compatibility. In particular,
freezing arbitrary colors on witnesses can impose size-dependent bias on
small features, and rounding witness items separately can destroy their
rainbow property. The categorical construction and incidence estimate
resolve both obstructions simultaneously. It is not a parameter
substitution in the nearest theorem or a new label for its rounding lemma.

The resulting removal of every instance-size parameter at fixed t,k is
a qualitative change for an unrestricted nonlinear coverage class, and
it is achieved constructively. This warrants publication-level value for
the exact frozen question despite the coarse O(t^3 k^3) dependence. I
therefore do not classify the result as a routine elementary corollary.
This assessment does not imply STOC suitability or acceptance, a sharp
bound, a resolution for general Lipschitz/influence-sparse functions, or
removal of the logarithm while retaining the earlier t,k exponents.

The current bounded primary-source screen found no equivalent full
resolution or the categorical reduction. It cannot certify worldwide
priority or exclude unindexed/new work. The broader papers inspected
do not imply this all-color, occurrence-degree-only conclusion. Those
ordinary search limits do not leave a mathematical gap in the proof.

**Remaining mathematical/scope gaps: none.** Acceptance is bound only to
the exact snapshot above. A substantive change to the claim or decisive
evidence requires a new freeze and fresh review. The structural
`check-math` result is recorded separately; it validates hashes and role
provenance, not this mathematical judgment.

The required `release_gate.py check-math .` was actually run after the fresh
acceptance records were written. It exited 0 with `ok=true`, the snapshot
digest above, and this referee job ID. See `audit/referee-gate.json`.
