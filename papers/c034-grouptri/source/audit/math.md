# Fresh mathematical review: accept the frozen full resolution

Job: c034-grouptri-referee-e6a7f319b8fe.
Snapshot: 05aa22d3dd75b43826bffb43bc7976a87898d16ab67f0597c8e4a686ca39b771.

## Scope and review basis

I accept the exact frozen resolution-paper claim. It proves the immutable
source question for every fixed exponent bound M, all polynomial group-order
constants c, and all compact cyclic-product presentations covered by source.md.
The saving is independent of c. This is an internal fresh review, not external
peer review or a truth certificate. The separate venue assessment is
`working_paper`; mathematical acceptance does not establish STOC readiness.

I checked every frozen file hash and the canonical snapshot digest, read the
original and precise problem statements, both proof dossiers, supplied code
and finite-test records, and the relevant actual primary passages. I ignored
the proposer's confidence statements. I did not consult checkpoint.md,
state.json, earlier reviews, transcripts or progress summaries. I wrote and
ran audit/independent_verifier.py without importing the proposer's code.
No frozen input was changed. The original source SHA256 remains
5e49e9583e24af889c0aa15a1b6dcadb797e1d85f3f467028441af101a677b0e.

## Reconstructed proof and adversarial checks

**Elementary backend.** Majdoddin Theorem 21.3 is a deterministic
elementary-group algorithm with running time
O(p^6 b^(3-epsilon*gamma) log^6 b), constant depending on the fixed
group-order exponent but saving independent of that exponent. Its restriction
p <= b^(epsilon/4) excludes only a fixed finite range for a fixed p.
Corollary 9.1(b), Definition 2.1 and Section 16 give the actual deterministic
instantiation H(1/14,0.077), whose product is 0.0055. Thus the conservative
epsilon_0=1/1000 is legitimate; it does not assume an unproved new oracle.
I read the stated theorem/proof and the matrix-corollary instantiation. As in
an ordinary theorem-dependent proof, acceptance relies on this cited prior
result; I have not formally reverified all its matrix dependencies.

**Capped listing.** Pad to a power-of-two side N. At each entered cube,
construct a fresh complete encoded query whose outer pairs are removed once
their count reaches T. Distinct absence coordinates for the three edge kinds
are essential: a triangle contains exactly one edge of each kind, so no absent
edge can cancel another's marker, including in characteristic two. A positive
cube must emit an output before returning: if no earlier descendant emits,
its entry witness remains active to its leaf. Depth-first execution makes
this argument valid despite changing masks. A finally unsaturated pair could
not have had any witness pruned. Counts therefore equal min(t_ij,T), with
distinct genuine witnesses, including when t_ij=T.

There is no query below b_0, with b_0 comparable to N^alpha. Consequently
p^(d+3) is at most b^C for one fixed C throughout the invocation, even for
large original c. The induced change between logarithmic word sizes is a
fixed factor. At side b there are at most (N/b)^3 queries, charging both
construction and detection in O(N^3 b^(-epsilon_0) polylog n). Summing
downward yields O(n^(3-alpha*epsilon_0) polylog n). Positive leaves have
disjoint tuple domains and each emits, so there are at most Z leaves to scan.
For Z=O(n^(3-theta)), the leaf cost is
O(Z b_0^3 polylog n)=O(n^(3-theta/2) polylog n) at alpha=theta/6.
Negative queries, saturated masks, unequal parts and padding are charged.
This part is valid but is not independently claimed novel.

**Quotient pieces.** Embed every cyclic factor Z_m with m dividing M into
Z_M by multiplying its coordinate by M/m. This is injective, preserves zero
sums, costs O(n^2 log(n+2)) for fixed M,c, and keeps polynomial group order.
For composite M let p be its least prime divisor and q=M/p. Project to
F_p^d and write the condition a_ik+b_kj=c_ij. For
s=2^floor(theta*floor(log_2 n)), L=floor(n/s), and T=L+1, capped listing
gives every light witness and a genuine set of T witnesses for every heavy
pair. Here s=Theta(n^theta), with fixed rounding factors. Even if s=1 for
an enormous finite range, this comparison and its constants remain valid.

The deterministic greedy hitting set has O(s log(n+2)) pivots, since a
remaining set has more than n/s elements. Incidence deletion and an indexed
max heap cost O((n^3/s+n^2+n) log(n+2)), not cubic preprocessing. Assigning
each heavy pair one actual pivot h is crucial. For each h,k, frequency
tables of b_hj-b_kj identify at most r=s^2 high-frequency values. Low-value
scans cost O(|H| n^3/r) plus setup, and their pivot-assignment filter prevents
duplicates. Every other quotient-zero triangle belongs to its unique
high-frequency piece. The complete disjoint partition follows from the
identity a_ik-a_ih=b_hj-b_kj. Sorting only needs a representation order;
it does not require an ordered group.

**Carries and missing edges.** On a piece, put alpha_i=a_ih,
beta_j=b_hj and tau_k equal to its frequency slot. Every present edge obeys
a_ik=alpha_i+tau_k, b_kj=beta_j-tau_k, c_ij=alpha_i+beta_j. This edgewise
assertion is stronger than just knowing that all its triangles are zero.
Lift the potentials coordinatewise to Z_M and subtract them on the three
edge kinds with the stated signs. Each present residual is divisible by p,
and the potentials cancel exactly in A'+B'-C'=A+B-C. No homomorphic section
is assumed. Division pZ_M -> Z_q is well-defined and injective as an additive
group map, including when p divides q. This resolves the non-split carry
case rather than assuming it away. Slots absent at k create no incident
present edges, so their arbitrary potential causes no assertion.

The three separate Z_q markers exclude every absent edge in the resulting
complete instance. Signs are on the actual plus-sum edge labels, so the third
edge marker is +1 before conversion to the A+B=C convention. Kernel calls
have the original side bound n and dimension d+3, hence polynomial group
order with an adjusted fixed c. Repeated lifting adds only three coordinates
per layer. The argument does not call an algorithm on tiny sides while
retaining an uncharged large dimension.

**Whole algorithm and cost induction.** Check light and low-frequency
exceptions in the original group, then solve every explicit kernel instance.
Every original zero triangle is quotient-zero and is covered. The gauge
identity and the masks prevent false positives. Besides capped listing, the
costs are (n^3/s+n^2), (s n^2+n^3/s), s^3 n^2 for materialization, and
s^3 n^(3-delta_q) for all recursive calls, each with fixed polylog factors.
Constructing every edge, arithmetic on all coordinates, dictionaries,
potentials, division, masks and control costs fit these charges.

For theta=delta_q/12 the available savings include
epsilon_0*delta_q/72, theta, 1-theta, 1-3theta, and 3delta_q/4.
All are at least the first. Taking
delta_M=epsilon_0*delta_q/144=delta_q/144000 leaves positive slack for
every fixed polylogarithm. At primes delta_M=1/1000. Thus the displayed
formula (1/1000)*(1/144000)^(Omega(M)-1) follows by finite induction.
Its value depends on M and not c. All loops use explicit polynomial storage
and logarithmic-word indices. The algorithm itself uses the input dimension,
not a supplied numerical c. Empty parts, the trivial group and n<=1 are
handled directly; fixed-p exceptional ranges and cutoff rounding are finite
and can be brute-forced with constants depending only on the fixed parameters.

## Independent finite checks and their limits

audit/independent-checks.json records 512 capped-listing instances;
676,333 exhaustive one-coordinate gauge/kernel cases for composite M<=36
and every proper prime divisor; 3,548,440 complete-input mask cases;
360 seeded graph decompositions in dimensions 1--3 and sides 1--6, with
6,850 explicit kernel instances; and 2,047 exact rational cost ledgers for
2<=M<=2048. The script uses independently selected witness subsets and
separate exact brute-force relations. It imports no supplied test code.
These are finite semantic checks, not fast implementation benchmarks or
proofs of the infinite theorem. The infinite result rests on the argument
above. A fresh PDF extraction also confirms the frozen source PDF's relevant
theorem locations and hash; marker checks alone prove no theorem.

## Novelty, value, and verdict

See audit/current-literature.md for current primary records, exact comparisons
and bounded search limits. The capped-listing principle, hitting/frequency
decomposition, and its potential equations are prior tools. The innovation
accepted here is the complete algorithmic extension step: obtain that structure
without its cubic fresh-input initialization, exploit its edgewise gauges to
solve arbitrary non-split kernel instances, and preserve a saving through every
fixed exponent with all materialization charged. Neither the elementary-group
backend nor the literal prior decomposition theorem supplies this full result
on its own. The former fails to filter kernel-zero projections; the latter
has cubic construction and does not state a group-extension algorithm. The
source's restricted p^2 propositions leave both dense and residue-diverse
inputs untreated. The new step covers those inputs without a promise.

This is a substantive qualitative extension across an infinite class of
compact group presentations and a reusable quotient/kernel algorithmic
principle, rather than a small computational example or a restricted p^2
corollary. The mathematics uses elementary identities once the right structure
is available; I do not assign novelty to those identities separately or claim
a new matrix primitive. The bounded independent primary comparison found no
equivalent full extension theorem. I accept substantive innovation at this
scope, with ordinary bounded-search priority limitations. The strongest case
is conceptual closure, not exponent improvement or practical performance.

No mathematical gap in the submitted scope was identified. No claim or proof
repair was made in this review. Verdict: **accept**, original status **proved**,
candidate kind **resolution-paper**. The separate assessment remains
**working_paper**: technical depth and broad STOC consequences are uncertain,
and no external venue decision or acceptance probability is asserted. Writing
still requires a separately assigned phase. After these fresh audits were
written, the required `release_gate.py check-math` command completed with exit
code 0 and `ok=true` for this snapshot and referee job. Its actual output is
retained in audit/check-math.json. This verifies structure and provenance only.
