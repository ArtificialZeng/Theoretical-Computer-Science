# Same-worker adversarial check of the proposed proof

Job c037-msthalf-research-d39900f29f79. This is researcher checking, not the
fresh referee required for mathematical, innovation or venue acceptance.

The original pass-3 test was the stronger ultrametric B4 inequality with
rectangle nonemptiness. New supervisor input instead supplied a full-metric
proof program using positive rectangle density. The stronger B4 assertion is
not asserted, refuted or renamed. Full-original resolution follows directly
from the new all-metric theorem if the submitted proof is correct.

## Mathematical attacks and their disposition

- **Insufficiently local density:** the star is obtained inside a SPECIFIC
  set S, not from global average degree. Averaging all ordered disjoint
  r-subsets of S proves exactly the needed induced density for |S|>=2r.
- **Shared path endpoints:** taking a common edge-index parity gives a
  matching. Thus bottom endpoints, top endpoints, and the selected A,B are
  disjoint. Sorting by true length changes neither matching nor overlap.
- **Only a pair of excluded edges:** the argument proves that at least one
  endpoint of each top edge has NO neighbor ANYWHERE in B. It does not merely
  prohibit the same leaf from being adjacent to both endpoints. Triangle
  inequality through two different leaves gives the required stronger fact.
- **Arbitrary scales:** all bottom lengths are at most D0 and all top lengths
  at least D0. The comparison uses D0<=D separately for EACH top edge. No
  bounded aspect ratio or common scale is assumed. One integral pays W once.
- **Ties and zero weights:** D_i>64w_i gives strict endpoint margins even
  for closed interval endpoints and w_i=0. D_i is positive because d is a
  metric on distinct vertices. D ties in the sorted groups are harmless.
- **Wrong tree/order direction:** for nonnegative tree weights, unique
  tree-path length is at most any connecting Euler-walk segment. This is
  y_T<=q, the direction needed to infer d<=q on H-edges. No bottleneck
  metric is used to upper-bound d.
- **Hidden-label algorithm:** H, the mask, d, the benchmark order and T0
  appear only in analysis. Exhaustive candidate selection and the returned
  preorder depend solely on the observed matrix and rational constants.
- **Data-dependent concentration:** E quantifies all rectangles before
  values are chosen. It controls the subsequently selected tree's rectangles
  pointwise, without conditioning independent marks on a chosen tree.
- **Expectation on rare failure or small n:** every possible output has true
  cost at most (n-1)MST, uniformly in arbitrarily large replacement values.
  The explicit repair failure (n-1)beta^(n-2) yields a finite all-n cost
  contribution via the geometric derivative sum. No high-probability claim
  for n=2 from the prior asymptotic proof is assumed.
- **Real p and finite constants:** a rational pi in [p,1/2) can be fixed in
  A_p. All algorithmic thresholds and its integer logarithmic multiplier
  are rational/integer. This leaves only the source's own exact-arithmetic
  model for observations; no numerical approximation certificate is needed.

No mathematical gap was identified by these same-worker attacks. The known
gap list in the submitted full proof is empty, subject to genuine fresh
review. This is a proposed resolution, not the result of that future review.

## New exact finite consistency tests

`interval_packing_check.py`, seed 3703, generated 160 instances of line,
cycle shortest-path, L1 and general weighted-graph shortest-path metrics,
with n=8,12,16,24, arbitrary shuffled orders, widely unequal integer lengths,
and nonuniform nonnegative integer order weights. Every saved instance is
non-ultrametric. Two coordinate sweeps lower order weights while preserving
rectangle counts; this is not a global optimum or exhaustive family search.
There were 28,118 feasibility calls. This suite differs from the pass-2
ultrametric suite and was not run to reconstruct old evidence.

`verify_interval_packing.py` separately checks all true metric triangles and
DIRECTLY enumerates both sides of each disjoint r-by-r rectangle in all saved
instances, rather than reusing the generator's degree-sort minimization.
It checked 2,802,752 rectangles, 778 expensive edges and each exact interval
integral/closed-endpoint overlap identity, as well as the full transfer
inequality. Largest observed interval overlap was 4. These values do not
establish a universal maximum or the infinite theorem.

The generator also exhaustively enumerated every pair mask for n=2,...,6,
33,866 masks in total. For unequal abstract line weights it computes the
repair's walk cost on F and its failure by mask cardinality, and verifies
the claimed expectation and failure upper bounds at p=0,1/3,2/5,49/100 with
exact rational arithmetic. The independent saved-metric verifier does not
reimplement this mask enumeration. These checks confirm the implementation
on the stated finite domain; the analytic coefficient proof establishes the
all-n comparison statement.

Outputs are `interval-packing-check.json` and
`interval-packing-validation.json`. None of these tests is a fresh referee,
a complete computation over all metrics or masks for unbounded n, or evidence
of priority. The main evidence remains the complete written proof.
