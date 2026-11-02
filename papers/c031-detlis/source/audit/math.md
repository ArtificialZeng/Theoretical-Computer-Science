# Fresh mathematical review

Job: `c031-detlis-referee-f280f716946c`.
Frozen snapshot: `76aff8cb1dceada574829e417470dcca336a544f9c08e579f9c49cff43896135`.
Review date: 2026-11-02 UTC.

**Verdict: accept the exact frozen resolution-paper claim.** The dossier proves
a uniform deterministic algorithm for the full uncolored 2D reporting problem
in `source.md`, with overhead
`O((n+m)n^(2/3)log^30(n+m+2))` and additive `O(K)` output cost. This is a
positive resolution of the original existence question, with epsilon=1/3.
The substantive contribution is the implementation and total charge for an
original-background-sensitive canonical-path sampler. The generic sampling
rate, merge/reduce principles, conditional expectation, descendant sums, and
the short-LIS/stitching framework are established tools.

The separate venue assessment is **working_paper**. The full resolution and
substantive algorithmic delta pass this review; the record does not establish
that the advance has the technical depth and breadth needed for a competitive
STOC submission. This is an internal review, not external peer review or a
truth certificate. No manuscript or PDF was made in this job.

## Inputs and integrity

I read the current source, interpretation, claim, snapshot, all listed proof
and diagnostic code, and the relevant statements in the frozen primary-source
texts. I inspected current primary records and additional nearby primary work
online. I did not read checkpoint/state files, earlier audit content, owner
progress, archived claims, or job transcripts. The neutral supervisor routing
note was read only as the applicable input-scope instruction.

All 21 frozen files match their SHA-256 values, and the canonical file-map hash
matches the snapshot digest. `source.md` remains byte-identical, hash
`abb69d3e7246259d6e77733caf7d28a72890a3752a8fc029d1a824a0fa91aa29`.
See `audit/referee-f280f716946c-integrity.json`. The candidate's own finite
diagnostics were inspected but not rerun, since their main functions overwrite
frozen result files. My fresh checks import none of their code.

## Reconstructed decisive argument

1. **Canonical paths and the correct local oracle.** For fixed comparable
   endpoints, take the longest strict chain with lexicographically least index
   sequence. Replacing a subpath by a longer path improves length; replacing
   it by an equal-length lexicographically earlier path improves the whole
   sequence. Replacement is feasible because every inserted point is between
   the subpath endpoints in both coordinates. Hence every subpath is canonical.
   The nonempty trace of any global canonical path on selected vertices is
   exactly the trace of the canonical path between its first and last selected
   vertices. At most d^2 endpoint descriptors suffice, including singletons.
   Repetitions of a selected vertex are always included together.

   Crucially, the endpoint path is computed using *all original vertices in
   the parent index interval*. Every feasible path between those endpoints
   stays there, so this is the global path. Recomputing on the selected set
   would be false, as the dossier's (0,3,1,2,4) example demonstrates. The proof
   does not make that substitution. A rectangle optimum has endpoints u,v;
   their canonical path remains inside that rectangle and is also optimal.
   Thus the sampled family really suffices for every rectangle, independently
   of the number and overlap of supplied queries.

2. **Charged source trees.** For a selected source, a sweep with strict-rank
   Fenwick queries obtains longest source paths. Equal-length predecessor paths
   can be compared by the first unequal children after their LCA in the
   already-built predecessor tree. Parents precede children, so binary lifting
   is available on insertion. These comparisons take O(log n), including ties
   among arbitrary real input values after comparison sorting. The sweep costs
   O(|I|log^2 n) for original interval I, rather than an uncharged global-n scan.
   Keeping only nearest selected ancestors produces a compressed tree with
   exactly the desired traces. Occurrence counts, Euler labels, and descriptors
   cost O(s^2), without storing s-bit incidence vectors for every path.

3. **Relative compression with finite arithmetic.** For input frequency u,
   the bad event is output-frequency error greater than eta(p+u). Bernoulli
   Bernstein gives failure probability at most
   `2 exp(-k eta^2 p/3)` per descriptor. In the displayed derivation,
   `2u+(2/3)eta(p+u) <= (8/3)(p+u)`, so the relaxed constant 1/3 is valid.
   The analytic parameter choice makes the initial sum at most 1/8.

   The rounded integer recurrence U bounds its true conditional probability q
   by `q <= U/D <= q+h/D`: convex averaging preserves the previous error and
   ceiling adds less than one scaled unit. Choosing a minimum upper-score
   occurrence increases the *true* potential by at most M(h-1)/D. Summing gives
   at most `Mk(k-1)/(2D) <= 1/128`. The terminal potential is the integer number
   of bad descriptors and is below one, so it is zero. Exact monotonicity of
   rounded scores is neither needed nor incorrectly assumed.

   All scores are computed, including negative differences: put the difference
   of the two relevant table entries at the target in each selected-source
   tree; a postorder descendant sum gives the contribution to every selected
   vertex. Add across sources. This is the exact dense membership score, not
   a heuristic. Multiplicities enter averaging and output draws; dummies have
   the baseline score. There are O(k^3) table entries and O(k^3) total score/
   update operations. With k<N, D=O(Mk^2), M<=4k^2, and all products and signed
   sums have O(log N) bits up to fixed constants. Constant-many-word or
   elementary polylogarithmic arithmetic suffices. No binomial-sized integer
   or unit-cost probability operation is hidden in the production algorithm.

4. **Global error and total construction cost.** Base blocks and both
   children of a merge have equal original size and equal representative
   cardinality. Thus their original frequencies and representative frequencies
   average with identical weights. Compression of a possibly empty global
   trace is covered by the endpoint oracle; an empty trace remains empty.
   Induction gives
   `|r-phi| <= ((1+eta)^j-1)(phi+p)`.
   With eta=1/(16H), at most H levels give error factor below 1/15. Every
   root path of length at least t has phi>=p=t/N and positive representative
   frequency. Deduplication and discarding dummies only at the end preserve
   this hit property.

   Per merge the cost is O(|I|k log^2 n+k^3 polylog n). Parent intervals are
   disjoint at each level, giving O(Nk log^3 n) for the background term. There
   are fewer than N/k merge nodes, giving O(Nk^2 polylog n) for tables and
   scores. This explicit accounting is the central algorithmic point. It does
   not assume a subset-only oracle or enumerate all global endpoint paths.
   For t=ceil(n^(2/3)), k=O(n^(1/3)log^3 n), the cost is
   O(n^(5/3)polylog n). The parameter cube root is obtained by integer search.

5. **All query lengths and output.** I reconstructed the short routine's
   minimum-peak A and maximum-base B recurrences. A feasible chain's internal
   indices/values lie between its endpoints; the range filters therefore check
   every boundary. Joining requires a strict value inequality. The extremal
   left peaks increase with length and the extremal right bases decrease, so
   the proposed binary search is valid. Zero-length and one-sided candidates
   handle empty sides. Every returned handle is feasible, and when the query
   optimum is <=t the optimum split is among those examined. There is no use
   of an invalid long-query output as an optimum.

   For each sampled r lying in a query, longest forward and backward endpoint
   paths lie in that query by the same endpoint-box argument. They meet only
   at r. If r is on a canonical optimum, the maximum feasible stitch is
   optimal. One of the short and long routines therefore handles every query,
   including threshold equality. Only final winners are expanded, by stored
   parent/state links, giving additive O(K). Losing paths are never expanded.

6. **Uniform and degenerate cases.** Equal real values receive equal ranks
   and never follow each other. Empty and singleton ranges, n=1, m=0, repeated
   representatives, all-dummy nodes, and arbitrary overlaps are covered. Static
   range trees store attained finite records, with flags for infeasible states.
   Addresses, counts, parameter calculations, and arithmetic have polynomial
   size. If k>=N, using all points for stitching is valid and charged because
   n<=k=O(n^(1/3)log^3 n) on that branch. This branch condition justifies the
   asymptotic bound even though its constants make the fallback extensive.
   Combining the deterministic short cost, net cost, and endpoint-query cost
   fits the frozen log^30 bound. The result covers reporting, not only lengths,
   and its epsilon is independent of n,m, values, and LIS lengths.

No substantive mathematical correction to the frozen proof was needed in
these reconstructions. I found no remaining correctness or scope gap.

## Independent finite checks actually run

`python3 audit/referee-f280f716946c-check.py` passed. Its independent reference
enumerates increasing subsequences, rather than importing the submitted DP,
Fenwick oracle, or compression implementation. It checked:

- 1,236 inputs: all ternary words through length 5 and all permutations through
  length 6; 35,318 canonical subpath identities and 21,850 interval-trace cases.
- 330,120 short-query/threshold cases over ternary inputs, including value
  boundaries beyond the data and empty answers; 88,758 optimal stitching pivots.
- 2,160 rounded-table states against direct rational binomial sums, and 512
  aggregate scores against dense membership sums, over 16 manual compression
  fixtures with duplicates/dummies and 64 successive draw choices.

Eight compression fixtures have initial potential <=1/8 and finish with zero
bad traces. The other eight are retained without a certified zero-bad claim;
only their recurrence, scoring and potential-increase identities are asserted.
These finite checks do not implement the huge uniform-parameter construction
and do not prove the theorem or benchmark its asymptotic cost. The universal
argument above, rather than finite success, grounds the correctness decision.
The script and full exact results are retained next to this report.

## Current primary comparisons and contribution assessment

Primary records and actual nearby theorem statements were checked on
2026-11-02. No equivalent full deterministic 2D reporting algorithm was
identified in this bounded check; this is not a certificate of exhaustive
priority. The comparison record is `audit/referee-f280f716946c-literature.md`.

- [Karthik C. S. and Rahul, arXiv:2404.04795v2](https://arxiv.org/abs/2404.04795v2),
  Theorems 1 and 5, Section 3 and Section 7: randomized square-root overhead,
  deterministic short-query primitive, stitching, and the explicit
  derandomization question. The candidate retains their framework and is
  slower than their randomized bound; its advance is deterministic
  subquadratic time for their full 2D reporting model.
- [Har-Peled and Sharir, arXiv:0909.0717v2](https://arxiv.org/abs/0909.0717v2),
  Theorem 2.11 and Lemma 2.15: the inverse-p sample scale and deterministic
  relative approximation cost are already known. There is no new generic
  sample-size theorem here. The candidate supplies the implicit path oracle
  and its background-sensitive global charge, which those bounds alone do not
  implement.
- [Bagchi et al., deterministic geometric stream sampling](https://arxiv.org/abs/cs/0307027),
  frozen conference version Section 2, Lemma 2.2 and Observations 2.3--2.4:
  merge/reduce and deterministic nets assume a subsystem oracle whose time is
  bounded in the selected subset size. The candidate instead pays |I|s at a
  merge and proves the sum of those costs using disjoint index backgrounds.
  Treating that cost as a free subset oracle would invalidate the result;
  the frozen argument does not do so.
- [Tao, Sheng and Pei, SIGMOD 2011](https://www.cse.cuhk.edu.hk/~taoyf/paper/sigmod11-skip.pdf),
  Section 4.1, Theorem 1 and Lemmas 1--2, already link consistent paths of
  dimension two and small covers. Section 4.2 uses randomized ordering and a
  bounded-degree cost analysis. Existence of a small cover is not the new step.
- [Alon, Chechik and Cohen, ICALP 2019](https://doi.org/10.4230/LIPIcs.ICALP.2019.12),
  Lemma 2 and Section 1.3: generic explicit path hitting is standard, and the
  paper itself distinguishes that from efficiently identifying the critical
  family. It does not provide the candidate's original-interval LIS oracle.
- [Gawrychowski, Gorbachev and Kociumaka, ESA 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/html/LIPIcs.ESA.2025.74/LIPIcs.ESA.2025.74.html),
  Theorem 1.3 and Section 5, and
  [Korogi, arXiv:2610.20983v1](https://arxiv.org/abs/2610.20983v1),
  Introduction and Theorem 1.1, concern index-interval reporting. Their stated
  query interfaces do not apply an independent value interval to all internal
  points. Neither result was silently treated as a weaker baseline in its own
  1D scope.
- A new adverse lead was checked:
  [Ben-Eliezer and Even, arXiv:2610.25467v1](https://arxiv.org/html/2610.25467v1),
  Claim 6.7 and Appendix A.2, give monotone-pattern detection with preprocessing
  `2^(O(h^2)) O(n log^(3h)n)` and query time `(O(log n))^(3h^2)` for pattern
  length h. That is not a uniform polynomial-saving all-length LIS reporting
  theorem. Recent directed shortcut constructions were also screened at the
  statement/model level; reachability shortcuts do not themselves preserve a
  canonical longest chain inside every query rectangle.

The result is more than an elementary invocation of a known epsilon-net
theorem: the selected traces depend on unselected original points, and the
proof provides both their exact representation and a subquadratic accounting
of the extra background work. This is a concrete, useful algorithmic advance
on the full original question. Generic sampling and tree summation should
remain explicitly attributed, rather than inflated into separate innovations.

The case for *STOC* is less established. The exponent remains above the
randomized square-root benchmark, no tight deterministic lower bound or new
consequence for a second problem is proved, and much of the mechanism adapts
standard machinery. These are real depth/breadth concerns. They justify the
conservative working_paper assessment while leaving the full mathematical
resolution and substantive specialized algorithm intact. No numerical
acceptance chance is inferred.

## Disposition

Accept this frozen snapshot as `resolution-paper`, original status `proved`.
Keep the separate `working_paper` assessment. The next authorized workflow
step, after a passing structural check-math gate, is the ordinary writing job
with the user-specified author and all later artifact gates. This referee job
does not draft, publish, upload, submit, or contact anyone.
