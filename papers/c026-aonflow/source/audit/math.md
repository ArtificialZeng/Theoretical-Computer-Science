# Fresh mathematical review

Verdict: **accept**, for the exact frozen resolution-paper claim.
Original status assessed: **proved**, using the specified published BJS and CKS
theorems. This is an internal mathematical review, not external peer review or
a truth certificate. Venue assessment is separately **working_paper**.

Job: c026-aonflow-referee-92aab2001150.
Snapshot: 573d5e72b132c0772447265073b14686ec1c85b65a6c5a6769030620d3e0eadd.
Review date: 2026-11-02 UTC.

## Packet and scope

I read source.md, problem.md, claim.json, audit/snapshot.json and the evidence
listed there, together with the required policies and actual primary results.
I did not read checkpoint.md, state.json, previous audit verdicts, job transcripts
or progress logs, and did not create another agent/process worker. All frozen
hashes and the canonical snapshot digest match. Fresh PDF text extraction agrees
with the supplied text for all three listed primary papers.

The reviewed assertion concerns every finite undirected unit-edge-capacity graph
with indexed terminal pairs. It selects distinct original pairs, routes one
splittable unit for each, and respects capacity one. Its ratio is

    C log(k+2) exp(C sqrt(log log(k+4))).

The algorithm has a uniform polynomial running-time and random-bit bound, always
returns feasible output, and attains the ratio with probability at least 3/4.
This is the full positive source question, including the k-sensitive parameter.
No restricted graph class, augmented congestion, fractional admission, or
subsidiary-lemma disproof is substituted for it.

## Reconstruction of the new reduction

1. Separate endpoint occurrences by unit pendant edges. Extending/projecting
   original unit flows preserves OPT. Shared original vertices and indexed
   duplicates cause no problem. Coincident endpoints can be admitted freely.
   With N at least the normalized encoding length, k <= ceil(log2 N) permits
   exact enumeration of at most 2N admission subsets, each tested by a compact
   rational flow LP. Thus the other branch may use log N = O(k).

2. Fix an optimum fractional admission flow of value F and cancel cycles.
   Split each commodity into pieces of mass at most 1/T, with
   T = 64 ceil(log2(2N)). There are at most TF+k pieces and polynomially many
   fragments; tiny positive rational masses do not create denominator-many
   copies. Independently choosing a path from each piece with probabilities
   T times fragment masses gives E[K]=TF and E[Z_e]<=T.

3. The stated lower/upper Chernoff estimates apply to independent piece
   indicators, even for pieces belonging to the same original pair. Their
   union bound is below 1/32. The bounded dyadic sampler perturbs the joint
   law by at most 1/64: interval lattice counts differ by less than one and
   marginal total variation distances add. Hence the explicitly checked
   event K>=TF/2 and all Z_e<=4T has probability greater than 61/64.
   On failure a single connected original pair remains a feasible answer.
   On success, each selected path copy carries epsilon=1/(4T) feasibly.

4. Weight each new copy endpoint by one, everything else by zero. BJS
   Theorem 3.1 applies with total integral weight 2K and
   phi=epsilon/(8 Gamma(2K)). It removes at most epsilon K/4 edges.
   For disconnected inputs its construction can be applied componentwise
   with this same global phi; sum a Gamma(a)<=2K Gamma(2K). Zero-weight
   components are vacuous. This is an implementation of the quoted theorem
   for its stated input class, not a new decomposition hypothesis.

5. For the fixed prepared paths, epsilon times the number hit by cut edges
   is at most their aggregate load on those edges, and thus at most |C|.
   At least 3K/4 complete copy pairs survive. In a component U, work in
   the induced graph G*[U], exactly as BJS guarantees. Restoring internal
   cut edges, if any, does not make component edge sets overlap.
   For q surviving endpoints, demand phi/q on each unordered pair has
   marginal at most phi. Dividing by phi is A-respecting. All-demand
   expansion therefore provides the required congestion-one product flow,
   even after endpoint deletion changes the product denominator.

6. Apply the uniform CKS matching-rounding theorem with alpha=phi<=1.
   Summing over edge-disjoint components gives at least
   3 c0 K/(128 T Gamma(2K)) >= 3 c0 F/(256 Gamma(2K)) unit copy demands.
   The original source occurrence edge of each indexed pair remains a
   bridge in the FULL augmented graph. All source copies of that pair
   lie on one side, all corresponding sink copies on the other. Two
   selected copies would each contribute one unit across this capacity-one
   cut, which is impossible even for splittable flows. Projection therefore
   gives the same number of distinct feasible original admissions.

7. K<=k(T+1) and the non-enumeration branch has T=O(k), hence 2K=O(k^2).
   The stated Gamma becomes log(k+2) exp(O(sqrt(log log(k+4)))), which is
   log^(1+o(1)) k. F>=OPT, and freely admitted coincident pairs preserve the
   guarantee. Compact LPs, rational path decomposition, bounded categorical
   sampling, augmentations, rounding and projection have polynomial size and
   arithmetic bit complexity. Fixed overhead constants are not input advice.

## The CKS correction and its hypotheses

CKS2005 Theorem 3.1 states exactly the required uniform edge-flow-linked
matching theorem, with unit admission and no congestion augmentation. The
candidate is invoking this published theorem as an algorithmic dependency;
it is not invoking CKS2013 Theorem 3.8 verbatim on an arbitrary component.
The former theorem's footnote requires stronger clustering, so I also checked
the corrected journal proof in Section 3.4 rather than ignoring the footnote.

For product demand alpha/q, put rho=alpha/4 on the q matching endpoints.
Use alpha/(4q) in each ordered direction and retain the diagonal amount
locally. Each terminal sends rho to the same uniform distribution, and the
two directions on an unordered commodity use half its product routing.
Thus the combined common-distribution flow uses at most half capacity.
This supplies the conclusion of journal Lemma 3.4 used by Section 3.4.
Nice-instance tree feasibility and root separation are used there to obtain
this common distribution, not by the subsequent clustering/min-cut arguments.

I identified an omission in the dossier's *reconstruction* of that prior proof:
discarding pairs at the residual weight-less-than-one tree does not alone
ensure that every external tagging contact lies in a cluster. This does not
change the quoted CKS2005 theorem or the new reduction. For clarity, the
following standard completion verifies coverage in this application's leaf
terminal setting:

* Root the grouping spanning tree at a zero-weight nonterminal. Positive
  terminal weights are on degree-one vertices; reused connector vertices
  therefore have weight zero. If total rho-mass is below one, route one
  arbitrary pair, which already gives the required constant-times-q-rho bound.
* Otherwise apply Lemma 3.3. Absorb its final residual tree, of unowned
  mass less than one, into the last extracted cluster. That cluster meets
  the residual tree at its extraction root. Each earlier extracted cluster
  meets the entire subsequently remaining tree at at most its own extraction
  root. Consequently full coverage still has pairwise cluster intersections
  of at most one vertex and induced clusters remain edge-disjoint.
* Owned receiving masses are now between one and three. Each cluster has
  fewer than 3/rho positive terminals, so greedy pair selection discards at
  most 6/rho pairs per chosen pair and retains Omega(q rho) pairs. This
  changes only an absolute constant in the cited uniform rounding bound.
  All external contacts now belong to a cluster. Shared vertices carry
  no receiving mass and use the journal's explicit shared-node tagging rule.

The rest of the journal argument uses: connected clusters of receiving mass
at least one; the center and single-source min-cut facts of Lemmas 3.9 and
3.12; the tagging lemma 3.13; constant-degree conflict selection; and the
edge-disjoint transit-tree pairing of Lemma 3.14. These hypotheses hold here.
In particular, earlier separating edges before the first external/shared
contact are bridges of the ROUNDING INPUT graph. Disjoint receiving supports
permit composition with the common-distribution flows at load at most 1/2.
The preliminary unit-commodity routes have load at most one on nonbridges
and at most 3/2 on bridges. After simple-path cycle removal a bridge is
used by a unit commodity either with its whole unit or not at all. Its
integer load is below two and thus at most one (Lemma 3.10).

This checks exact congestion one. It establishes no nonuniform rounding
claim. The coverage explanation completes a sketch of an existing cited
dependency; it does not repair, weaken or replace an important new theorem
of the candidate. No frozen file was changed. The dossier also mislocates
CKS2005 Theorem 3.1 as printed p.5; the supplied author PDF has it on PDF
page 7 of 10. Use the theorem number and correct pagination in future writing.

## Independent checks actually run

audit/referee-92aab2001150-check.py uses a different exact rational path fixture
from the research verifier. It checks sampling marginals over 18 outcomes,
1,422 cut-charge cases, actual augmented-graph bridge separation by traversal,
512 copy-admission subsets, a nonzero cut-budget fixture, common-distribution
scaling, the small-k arithmetic, all frozen hashes, and PDF/text consistency.
All checks passed. It does not implement BJS or CKS or exhaust graph inputs.
The general conclusion rests on the argument and the stated primary theorems,
not on these finite diagnostics. The frozen research script was read but not
executed, because its main function overwrites a frozen evidence file.

## Novelty, value and limitations

The primary comparison and access record is
audit/referee-92aab2001150-literature.md. BJS2026 still explicitly records the
O(log^2 k) baseline and leaves the full near-logarithmic AON guarantee open.
CKS2005 already provides uniformization, endpoint duplication and exact
matching rounding; none is newly credited here. Anand2026 improves a
decomposition tool but does not provide the original-scope admission theorem.
No equivalent full resolution was located in this bounded current search;
this is not a priority certificate.

The substantive delta is a full general-graph, congestion-one approximation
improvement, through an admission-preserving transfer that pays for cuts
against a fixed feasible family and cancels the uniform path scale in the
rounding yield. Keeping the old occurrence cuts is essential to the final
distinct-admission guarantee. This supplies the missing interface rather
than merely replacing an overhead bound inside the prior adaptive recursion.
Its ingredients are known and the proof is short, but the uniform polynomial
algorithm and nearly one logarithmic exponent of improvement give substantive
independent mathematical value. I do not reject it merely for shortness or
reclassify it as a subsidiary result.

No unresolved mathematical gap remains for this exact theorem relative to
the cited dependencies. The actual release_gate.py check-math command passed
for this snapshot and referee job; it checks integrity/provenance, not truth.
Writing/release artifact gates have not been performed in this referee
phase. The separate STOC assessment remains working_paper: technical depth
of the new composition and consequences beyond this AON improvement are
uncertain, and presentation needs to distinguish the prior theorem from its
reconstruction and state the coverage convention clearly. Acceptance of
mathematics does not certify STOC competitiveness or authorize submission.
