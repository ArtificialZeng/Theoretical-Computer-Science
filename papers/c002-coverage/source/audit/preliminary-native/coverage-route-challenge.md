# Preliminary native challenge of the rainbow-block route

2026-11-01. Context: native collaboration subagent
`/root/coverage_route_challenge`, assigned by `/root`. This is a fresh pass in
the same model family, not statistical independence, external peer review, a
runner referee job, or a publication acceptance. No `MATH_JOB_ID` was supplied
or invented. Only this preliminary directory was written; no claim, snapshot,
queue state, manuscript, TeX, PDF, or favorable gate flag was created.

**Assessment:** I find no mathematical gap in the proposed all-parameter
existence bound

\[
  \operatorname{disc}(F,k)\le 4kt(kt-1)^2.
\]

The argument addresses every instance of the **frozen qualitative question**
under occurrence-counted sparsity. The deterministic polynomial-time claim is
also supportable with the LP-vertex implementation below. This is a reasoned
preliminary assessment, not acceptance of a frozen candidate or a priority
claim. In particular it does not give the source's sharper dependence on t,k
with its logarithm deleted.

## Reconstruction and attacks

1. **Hall at the correct granularity.** Write q=kt. For any subfamily Q of
large *occurrences*, q|Q| <= sum of their sizes <= t|union Q|. Hence
|union Q| >= k|Q|. Every subcollection of the k copies of each occurrence
has at most k|Q| slots and the same neighbor union as its represented
occurrences Q; ordinary Hall therefore applies to these copied slots.
There are k disjoint representatives for every large occurrence, globally
disjoint even for equal incidence sets. No subtraction of multiplicities is
permitted. Each large occurrence now contains its own full rainbow block,
under every independent choice of block shifts. Its contribution is exactly
one to each color, not merely balanced in expectation. This justifies ignoring
all large occurrences in the subsequent error calculation.

2. **Interaction degree.** A block has at most k items and at most kt=q
incident small occurrences. Each small occurrence has at most q-1 items and
meets at most q-1 blocks, hence contributes at most q-2 other neighbors to a
fixed incident block. The interaction graph has degree at most q(q-2) and
admits H <= (q-1)^2 greedy classes. Repetitions only overcount this bound.
For q=2 the degree is zero: every small occurrence is a singleton. If there
are no large occurrences, singleton blocks give the same valid construction.

3. **The extension is categorical, not itemwise multilinear.** For a fixed
class C, an individual small occurrence S meets at most one active block B.
For color c its expected coverage is

   1-v(S,c)+v(S,c) sum_r p(B,r) z(S,c,r),

where v is the outside avoidance probability and z records whether the
inside portion hits c. Different blocks are independent in this temporary
law; items within a block are deliberately correlated. Multiple items of S
inside B cause no nonlinear dependence on p(B,*). Summing these identities
proves joint affinity throughout the class.

For fixed (B,r), injectivity of the base colors on B gives
sum_c z(S,c,r)=|S intersection B|. As all coefficients and v are
nonnegative and v<=1, the entire coefficient column across **all function
and color rows** has l1 norm at most

   sum_(small occurrences S) |S intersection B|
     = sum_(j in B) deg_small(j) <= t|B| <= q.

The equality counts occurrences, including equal sets assigned to one or
several functions. Counting only affected functions would not establish this
bound. Uniform cyclic shifts initially give equal expectations for every
color: global addition of any color offset is a measure-preserving bijection
of the joint block-shift sample space. This argument includes every within-
block correlation.

4. **The rounding lemma works.** Consider the coordinates that remain
strictly between zero and one. If there are V such coordinates in G
fractional simplexes, then G<=V/2. Freeze all other coordinates. Drop any
value row whose remaining absolute coefficient mass is at most 2q. Every
retained row then has mass >2q, while the total column mass on free
coordinates is at most qV. The number R of retained rows is strictly less
than V/2, so R+G<V. A nonzero direction preserving all retained value rows
and simplex sums exists. Move in either direction to the first boundary,
freezing at least one coordinate. At termination each simplex is a vertex.
A dropped row was exactly at its original target when dropped; later
movement affects only its then-free coordinates, each by absolute amount
at most one. Its final error is at most 2q. A row never dropped has zero
error. There is no accumulation of 2q for repeated drops of a row: each row
is dropped once. Negative coefficients would be harmless if the norm used
absolute values, although this application is nonnegative.

5. **All classes and colors.** Each stage changes a fixed function/color
expectation by at most 2q. At the start its value is common to all colors;
at the end it is actual integral coverage. Summing over H stages and using
the triangle inequality between two colors yields 4qH. The construction
requires no union bound, probability of success, dependence on m, restriction
to prime powers, fixed t/k, feature weight extension, or value-oracle claim.

6. **Polynomial arithmetic is repairable, not an obstruction.** Use explicit
incidence input. For k>=n assign different colors to all items: each color
class is empty or a singleton, and all function values on singletons are
at most t. Thus the huge binary-encoded-k case is trivial. Otherwise k<n,
and replace the input t bound by the maximum actual occurrence degree if
needed. Matching, graph construction, and at most n nonempty graph classes
have polynomial size.

At the start of processing a class all its block laws are still uniform;
previous classes are integral and future classes uniform. Therefore the
outside probabilities are products of factors 0, 1, or (k-a)/k with at
most n factors, and have O(n log k) bits before summing occurrences.
Each class's coefficient matrix is fixed. Keep retained equations equal
to the original target A p_uniform throughout that class. With fixed
coordinates in {0,1}, every subsequent polytope uses subsets of that fixed
rational matrix and its fixed targets. A rational LP vertex can be found
in polynomial time, with polynomial determinant bounds on its bit length.
Since R+G<V, any such vertex must fix another coordinate; repeat drops and
vertex selection until integral. At most the original number of coordinates
can become fixed and at most the original number of rows can be dropped.
This avoids any unsupported claim that repeatedly taking arbitrary rational
null directions automatically controls intermediate denominators. No exact
LP coloring implementation was certified in this preliminary pass.

## Independent finite evidence

`challenge_identities.py` was written without reading or importing the
root checker. It uses exact `Fraction` arithmetic, a separate augmenting-path
matching implementation, direct joint enumeration of outside shifts (rather
than the same product formula used in the sketch), and nonuniform rational
outside laws. The three fixed and forty seeded fixtures include k=2,3,4,
t=1,...,4, repeated tagged sets, and multiple items of one feature inside a
block. All assertions passed: 43 families, 22 large occurrences, 30 Hall
subfamilies, 1,449 feature/class/color affine identities, 641 whole-matrix
column bounds, 15 families with repeated incidence sets, and 6 tests with
multiple same-block items. Initial cyclic symmetry was also checked by direct
enumeration. The JSON records these limited counts. This checker does not
test polynomial runtime or establish the universally quantified theorem;
the preceding proof reconstruction is the evidence for those claims.

## Primary-source comparison, novelty and value

I read the original cached arXiv full text, especially printed pp.3--5 and
Section 5/Lemma 23, and checked the decisive passages in the publisher text.
The [ESA paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.139)
already has item interaction classes and dropped-row Beck--Fiala rounding.
Thus neither mechanism should be advertised as independently new here.
The added step is disjoint Hall witnesses plus a categorical extension that
keeps those witnesses rainbow while the remaining discrepancy is rounded.
The source's discussion separately raises its size logarithm and its extra
t,k dependence. The proposed polynomial settles the frozen qualitative
size-independence question, not the sharper quantitative question with the
source's t,k exponents retained.

I also checked the actual Question 14 in
[Hollender--Manurangsi--Meka--Suksompong v2](https://arxiv.org/abs/2509.09252v2):
its t-influence-sparse, 1-Lipschitz setting includes broader functions. The
current route handles its unweighted-coverage subclass because Lipschitzness
at the empty set bounds a single item's covered features in each function.
It gives no resolution for arbitrary such functions. I inspected the other
concurrent [Dupré la Tour--Fujii source](https://arxiv.org/abs/2509.16802v1)
for a competing sparse coverage implication and found none.

Bounded live exact-title/author searches and combinations of coverage,
non-additive discrepancy, Hall, rainbow blocks, size independence, and
multiple-choice Beck--Fiala did not expose an equivalent result. Search
results mostly returned the source and its two precursors; this is weak
negative evidence, not an exhaustive current citation search or proof of
priority. The Hall and rounding ingredients individually are standard. The
composition looks like a coherent short structural observation with a
meaningful qualitative payoff if still unpublished; simplicity alone would
not make an open-question resolution worthless. Conversely this preliminary
pass does not establish substantial novelty or STOC-level importance. The
bound has cubic k,t growth, and the source remains quantitatively much
stronger for many parameter ranges.

Metadata correction only: cached arXiv v3 frontmatter prints ESA DOI .137,
which now belongs to a different paper. The verified coverage publication
is DOI **10.4230/LIPIcs.ESA.2026.139**, volume 388, pp.139:1--139:19. This
does not undermine the arXiv mathematical source or change the frozen target.

**Next boundary:** the runner researcher should formalize the exact theorem
and explicit-representation algorithm, freeze them with their evidence, and
obtain a genuinely fresh correctness/novelty/value review. This report may
serve as adversarial evidence for that process; it must not be relabeled as
the publication acceptance required by the user.
