Fresh mathematical referee report

Verdict: ACCEPT the exact frozen three-theorem result-note scope. The original
problem remains unresolved. This is acceptance for the local mathematical
handoff, not human peer review, a priority guarantee, or a venue assessment.

Reviewer job: privacy-interpolation-referee-4ed762972744.
Snapshot: 932c1ba086d51ef9c99afb17ae2046a2a43a19517b9778f2a2a06e751683f641.
The source hash is 9488f12633da72d763b0ad127ff791f002ff7451ea26826a68d35a832f0bad15.
All frozen file hashes and the canonical snapshot digest were recomputed and
matched. I read source.md, problem.md, claim.json, requirements.md, the snapshot
and its listed decisive arguments, code, certificates and source comparison.
I did not consult checkpoint.md, state.json, prior referee reports, owner
transcripts or scheduling summaries. The old unrestricted claim is not being
reopened. No frozen input was modified.

The accepted content is Theorems 1--3 of
evidence/research-excursion-proof.md as submitted: the full positive swapped
triplet frontier, its minimum-budget uniqueness, the sharp global shape
penalty, and the exact necessary-certificate evaluation. Sharpness of the
certificate on swapped triplets means the reservoir coordinate in Theorem 1.
There is no general cap sufficiency, bit-complexity bound, optimal-path
decomposition theorem, or result about every normalized transform-linear rule.
The optional geometric-family comparison was not part of this snapshot or
this acceptance.

1. Reconstructed local speed bounds and binary distance.

For a positive AC path on a compact interval, every coordinate stays uniformly
away from zero. Thus logs are AC, and a budget L gives the two endpoint upper
bounds r_i(t) <= min(p_i exp(Lt),q_i exp(L(1-t))). Differentiating normalization
almost everywhere and bounding the other coordinates also gives
|r_i'| <= L min(r_i,1-r_i). The displayed Phi in the proof has derivative
1/min(x,1-x), including matching one-sided derivatives at 1/2. Its chain rule
therefore yields |(Phi(r_i))'| <= L. In a binary simplex the Phi-linear
monotone path attains the resulting bound. This ingredient is elementary prior
theory; its inclusion supplies a complete proof without invoking Blackwell
sufficiency. Positivity excludes all problematic logarithms and denominators.

2. Theorem 1, including b > 1/2 and every budget.

Since a+b<1 and a<b, one has a<1/2. The scalar distance from a to b is
log(b/a) for b<=1/2, and log(1/[4a(1-b)]) for b>1/2. Applying the preceding
bound to either swapped coordinate forces L>=T*. At the midpoint the two
changing coordinates are each at most a exp(L/2), so every path has reservoir
peak at least max(c,1-2a exp(L/2)). This is a bound on all admissible paths,
without any monotonicity assumption.

I checked the construction for the complete interval T*<=L<=T0. Put
B=exp(L/2), H=1-2aB and use physical time s=Lt, u=exp(s) on the first half.
The fastest scalar decrease g from b is b/u when b<=1/2. When b>1/2 it is
1-(1-b)u until kappa=1/[2(1-b)], followed by K/u with K=1/[4(1-b)]. The
pieces and their first derivatives agree at kappa. For the small-b case set
K=b. Then exp(T*)=K/a and B>=u*=sqrt(K/a). In the large-b case u*>kappa
follows from a<1-b. In both cases aB<1/2 because B<=exp(T0/2)=(a+b)/(2a).

For h=1-au-g(u), the large-b initial piece is exactly cu. On the later
piece h=1-au-K/u, increasing to u* and decreasing thereafter. At u=B,
h(B)-H=aB-K/B>=0. Together with H>=c and h(1)=c, this establishes that
the cap activates at a first crossing u0 and stays active through B. It
also proves h>=c everywhere in this half, so the construction never hits
the simplex boundary. The min/max formula in the submitted proof is
therefore continuous, positive and normalized, with finitely many smooth
pieces, and reaches (H,aB,aB).

The physical-time speed checks are decisive. In the initial large-b phase
the vector is (cu,au,1-(1-b)u): the first two coordinates have derivative
equal to themselves, and the decreasing coordinate has speed 1-r_2<=r_2.
In a later uncapped phase, r_1'=r_1, r_2'=-r_2 and r_0'=r_2-r_1.
The identities r_0+r_0'=1-2r_1 and r_0-r_0'=1-2r_2 are nonnegative,
since both changing coordinates here are at most 1/2. On a capped piece,
r_0'=0 and r_2'=-r_1, with r_2>=r_1 because u<=B. Thus all logarithmic
speeds are at most one in s, hence at most L in t. Reflection in time and
exchange of the changing coordinates preserve these inequalities and join
continuously. The reservoir attains H at the midpoint and never exceeds it.

The strict inequality T*<T0 is valid: on x in ((a+b)/2,b),
min(x,1-x)>a+b-x, while on the remaining part of [a,b] the full-simplex
denominator is at least the fixed-reservoir binary denominator. Integrating
their reciprocal speeds proves the strict comparison. At L=T0 the cap is c
throughout, giving the fixed-reservoir binary geodesic. For L>T0 reuse that
same unit-interval path; its cost stays T0. This covers all larger budgets,
rather than assuming the displayed intermediate construction works there.

At L=T*, each changing coordinate saturates the integral Phi speed bound.
The integral of its nonnegative speed deficit is zero, so its Phi derivative
is forced to be +T* or -T* almost everywhere. The two coordinates, and then
the normalized reservoir, are uniquely determined as continuous functions.
Existence was already proved, so this is genuine uniqueness of the fixed-time
path, not just uniqueness of a curve image. The displayed minimum-budget
peaks follow by substituting exp(T*/2); they exceed c because T*<T0.
The boundary b=1/2 is consistent in both formulas. The strict hypotheses
exclude a=b and c=0; no limiting endpoint is silently added.

3. Theorem 2 and its quantified sharpness.

For an affine coordinate, its positive-ratio log speed increases with q_i/p_i;
its negative-ratio log speed increases as q_i/p_i decreases. At endpoint
distance eta, the two bounding functions in the proof are consequently valid.
They meet at t=1/2, with the increasing-coordinate envelope larger before
that point. Their integral is exactly B_eta=2 log((exp(eta)+1)/2).
For p!=q the affine maximum speed D(t) is continuous and bounded below by
a positive number: any nonconstant affine coordinate supplies such a lower
bound on the compact interval. The normalized cumulative length map thus
has a C1 inverse. Its reparameterization has cost equal to the affine length,
stays coordinate-monotone and stays inside the endpoint box. Dividing by
Lambda>=eta proves both claimed upper bounds without presuming general
optimal-path attainment.

For every eta>0 choose E=exp(eta) and 0<a<=1/(2E). Then b=aE<=1/2,
c=1-a-b>0, and Theorem 1 gives unrestricted Lambda=eta. Each restricted
class fixes the equal-endpoint reservoir. Dividing the other two coordinates
by m=a+b reduces the restricted optimum to the binary swapped pair
(1/(E+1),E/(E+1)), whose Phi distance is B_eta. Its binary optimal path
satisfies both restrictions, so the same example attains equality for both
ratios. Splitting c into any n-2 positive fixed-proportion coordinates
preserves the unrestricted log-speed construction; both restrictions force
each split coordinate constant. This proves attainment in every n>=3.
For n=2 the unrestricted binary optimal path already satisfies both
restrictions. Ratios concern eta>0; there is no 0/0 claim at p=q or n=1.
The limit of B_eta/eta is two. This is the price relative to the actual
unrestricted optimum, not merely relative to endpoint distance.

4. Theorem 3 and exact arithmetic complexity.

Summing the endpoint upper envelopes over i!=j and using normalization gives
r_j(t)>=1-S_j(exp(Lt)); maximizing proves the necessary certificate.
The assumed endpoint ratios imply S_j(1)=1-p_j and S_j(Z)=1-q_j.
Thus C_j>=max(p_j,q_j); existence is not inferred from this bound.

For v=z^2, branch changes are at the rational values Zq_i/p_i in [1,Z^2].
Each cell is A z+B/z, with A,B>=0. Its endpoint squared values are rational,
and the only possible interior minimum has v=B/A and squared value 4AB.
When either coefficient vanishes, endpoint evaluation suffices. Squaring
does not change the order because the function is nonnegative. Tied events
can be transferred together; including the skipped event of j merely
subdivides a cell without changing the answer. One common ratio sort and a
linear scan per j prove exactly the submitted arithmetic-operation bounds.
There is no unit-cost claim for bit lengths. At Z=1 the endpoint condition
forces p=q; the degenerate interval evaluates directly to
R_j=(1-p_j)^2. The frozen implementation handles this case.

For the swapped reservoir the exterior cells minimize at the endpoints,
with value a+b, while the middle cell is az+Za/z and has minimum
2a sqrt(Z). Therefore C_0=max(c,1-2a sqrt(Z)). Equality with the true
minimum peak follows from Theorem 1. This does not make the certificate
sufficient for arbitrary endpoints.

5. Independent exact checks actually performed.

I wrote audit/referee_verify.py without importing either frozen path generator
or consumer. It checks the serialized coefficient functions after scaling
quadratic inequalities to [0,1], using endpoint signs and the discriminant
condition for an interior vertex. It verifies positivity, normalization,
joins, the complete continuous-cell speed inequalities, the reservoir cap,
the midpoint and reflected endpoint, and the applicable budget bounds.
All 657 small-b and 210 large-b paths passed: 1,824 half-cells and 5,472
coordinate cells, including 79 degenerate cells. Sixteen records are exactly
at their minimum feasible budget and 63 at the constant-reservoir boundary.
These counts describe finite evidence, not parameter coverage of a theorem.

For the certificate algorithm I loaded only the frozen all_certificates
implementation with its main function disabled, so no frozen files were
rewritten. A fresh oracle reconstructs every interval from a midpoint and
evaluates branches directly rather than maintaining the sweep's sums.
On 233 newly chosen endpoint pairs in dimensions 2 through 8, three rational
budgets each produced 3,483 exact coordinate comparisons, all matching.
This includes identical endpoints, ties, exact endpoint budgets and highly
unequal masses. Results and input hashes are in audit/referee-exact-checks.json.
The universal statements rest on the preceding analytic reconstruction.

6. Source comparison and contribution judgment.

The primary passages and access limits actually inspected are recorded in
audit/referee-sources.json. [BCSZ Proposition 2.1](https://arxiv.org/html/1810.12518v2)
is the known factor-two general extension theorem.
[Dong--Roth--Su Theorem 2.10 and Proposition 2.15](https://arxiv.org/html/1905.02383v3)
give Blackwell comparison and the continuous-group Laplace limit. Their
unrestricted-reachability consequences are background, not an accepted new
contribution here. The binary calculation and affine length bound are also
credited ingredients.

[Lemmens--Roelands Theorems 4.3 and 5.1](https://aif.centre-mersenne.org/item/10.5802/aif.2932.pdf)
concern cone Thompson geodesics; Theorem 5.2 concerns Hilbert distance on
a section. In particular the reciprocal two-point spectrum criterion does
not apply as a normalized-simplex uniqueness theorem to ratios {1,E,1/E}.
The candidate's saturation proof supplies its stated uniqueness directly.
[The SoCG polygonal definitions](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.82/LIPIcs.SoCG.2025.82.html)
likewise distinguish endpoint maximum symmetrization from path length.

The preserved Qiu primary HTML explicitly normalizes in Definition 6 and
proves the factor-two accounting in Proposition 3 and Appendix B.5;
its [current abstract record](https://arxiv.org/abs/2601.09946) was checked.
[Liu--Qiu Section 5.2 and Appendix E](https://arxiv.org/html/2609.14125v1)
explicitly calibrate pre-normalization budgets and use standard envelopes.
Neither inspected construction states the optimized mandatory peak over all
admissible paths. Normalization may change coordinate shape, so these results
are not contradicted by the frozen theorem. The candidate correctly avoids
that inference. The [NeurIPS shape paper](https://papers.neurips.cc/paper_files/paper/2022/file/9c84feb75eae1ef6389f31b3ef050b6a-Paper-Conference.pdf)
has a different geometric-estimation meaning of shape in its inspected
abstract and introduction.

A fresh search additionally found
[Fernandez de Bobadilla et al., arXiv:2609.38382v1](https://arxiv.org/html/2609.38382v1).
Its Proposition 6 and Theorem 8 give a one-sided instantaneous cost
F_infty(p,v)=max_{v_i<0}|v_i|/p_i and optimized endpoint quasi-distance.
Here the instantaneous cost is max(F_infty(p,v),F_infty(p,-v)), before
optimizing paths. Symmetrizing an already optimized quasi-distance is a
different operation: for a=1/16,b=3/4 the endpoint maximum is log(12),
whereas the present minimum budget is log(16). The inspected statements
do not give the all-budget cap frontier or the shape penalty.

No equivalent constrained frontier or exact shape-penalty theorem was found
in this bounded comparison. This is not proof of priority; older constrained
control and function-algebra literature were not exhaustively searched.
The sweep and binary ingredients alone would be insufficient as a new note.
The combined result does qualify: it optimizes a meaningful excursion
objective over all paths at every feasible budget in the minimal dimension
where shape restrictions cost anything, and then identifies the exact worst
restriction cost over all endpoints and all higher dimensions, with positive
attaining examples for every eta. This is stronger than an isolated affine
obstruction or a relabeling of unrestricted reachability. A credible use is
to quantify the additional privacy budget required by endpoint-range design
constraints, and to certify an unavoidable transient output probability.
These are one coherent subsidiary contribution and should stay together.

There are no unresolved mathematical gaps in the exact frozen claims found
by this review. The original general question and its full interpolation-family
comparison remain outside the accepted scope. Proceed to writing only that
scope, retaining the stated credit and limitations and the required later
release gates. No manuscript or PDF was created in this referee job.
