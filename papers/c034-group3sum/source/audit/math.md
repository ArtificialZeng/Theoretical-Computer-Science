# Fresh mathematical review

Job: `c034-group3sum-referee-f77368142a77`  
Frozen snapshot: `15a73043f23436b1592a376f95f678e39919b724da29d1fc7773757f6a82f52a`  
Review date: 2026-11-02 UTC. This is an actual fresh internal review, not external
peer review, formal certification, or a claim of statistical independence.

**Verdict: accept the exact frozen resolution-paper claim.** The proof resolves
the immutable original question with the stated randomized, bounded-time witness
algorithm for every fixed exponent bound M. The contribution is substantive.
The separate STOC assessment is **working_paper**; mathematical acceptance does
not establish competitive venue readiness or authorize a released PDF.

## Scope and integrity

I read the skill/referee contract, local publication policy, original source,
precise interpretation, claim, frozen proof and necessary listed code/source
inputs. I did not read checkpoint/state files, earlier job transcripts, earlier
verdicts, or the proposer's self-check/confidence summary. The required supervisor
note was treated only as a source of cautions, not a mathematical verdict. No
other project was inspected and no agent or background worker was started.

I independently hashed every file listed in `audit/snapshot.json`, checked its
canonical mapping digest, and matched the immutable source hash
`f3507a3e5b20d6707750b7e703d5d1c0764d4d5b13ef6b7a4f0001d940c8e8cf`.
No frozen file was changed. The assertion being reviewed includes all products
of cyclic factors dividing M, arbitrary fixed polynomial order bound n^c,
witness recovery, a saving independent of c, and a worst-case random-path time
cap. It is not restricted to Z8, homogeneous prime powers, or detection alone.

## Reconstruction and attempted failure points

1. **Normalization and input size.** Multiplication by M/m maps Z_m injectively
   and homomorphically into Z_M when m divides M. Thus normalization preserves
   and reflects zero sums. Since each nontrivial original factor has size at
   least two, r <= c log_2 n. The enlarged order is at most n^(c log_2 M).
   Arithmetic on the resulting residue vectors costs only a parameter-dependent
   polylogarithmic factor. Deduplication retains one original index per value.
   Empty lists, the trivial group, and bounded n have explicit direct solutions.
   A list of size at most sqrt(n) permits the stated O(n^(3/2) polylog(n)) search.

2. **Original-coset profiles survive fragmentation.** For H_d=G[d], reduction
   modulo M/d is precisely the quotient by H_d in Z_M^r. For each original list,
   the dyadic class size attached to an element is at most its original coset
   size and more than half that size. After restricting to any full profile,
   a list attaining the minimum s_d contributes fewer than 2s_d choices to a
   prescribed H_d coset. Fixing the other two elements proves T_d < 2s_d n^2.
   Separately, the represented original cosets are disjoint and each originally
   contains at least s_(i,d) elements. Their number is therefore at most
   n/s_(i,d), even if a restricted coset has only one remaining element. These
   are different uses of the original counts; neither assumes that restricted
   cosets retain their original sizes. There are at most (1+floor(log_2 n))^(3L)
   triples of profiles. Since M is fixed, this is a polylogarithmic factor.

3. **The discrete selection certificate is sufficient.** Choose the least ell
   for which d^ell sigma >= s_d R simultaneously for all d>1 dividing M. Some
   e fails at ell-1, giving e^ell < e s_e R/sigma. This supplies both the lower
   bounds used in the false-positive analysis and an upper bound on label
   branching in one selected quotient. With original lists larger than sqrt(n),
   s_M > sqrt(n)/2 >= n^(1/4) for n>=16. Consequently
   ell >= (log_M n)/4. For every chosen prime p dividing e,
   q=floor(log_p R) <= eta log_2 n <= (log_M n)/8; hence k=ell-q is nonnegative.
   R>=M ensures q>=1 and D>=2. Also R/M < D <= R. All these comparisons hold
   independently of c and without compatibility assumptions between profiles.

4. **The elementary middle subgroup is valid for mixed exponents.** The quotient
   by H_e is retained in both maps. On ker(pi), its quotient component and the
   first k full rows vanish. Each remaining full row is a multiple of M/p.
   Thus K(ker(pi)) lies in the explicit B congruent to F_p^q. Surjectivity onto
   B is unnecessary: unused middle vertices are harmless. On an H_e coset a
   full row has at most e values, while its reduction modulo M/p has at most
   e/p values. The number of pi labels in that coset is at most e^ell/D.
   Combining the upper certificate with the original-coset count gives fewer
   than M^2 n/sigma labels per restricted list, and at most (M^2+1)n/sigma
   blocks. This deterministic bound holds even for completely dependent rows.

5. **All orders, not just one valuation layer, are charged.** A uniform row on
   Z_M^r maps a vector of order d uniformly onto the subgroup of Z_M of order d.
   One can see this by taking the ideal generated by its coordinates and M;
   its size equals the additive order of the vector. Reduction modulo M/p has
   image size d/gcd(d,p). Independent rows therefore give
   Pr[K(v)=0]=d^(-ell) and
   Pr[pi(v)=0]=gcd(d,p)^q d^(-ell) <= D d^(-ell)
   for nonzero v in H_e. Outside H_e the quotient excludes v. Vectors in H_e
   have order dividing e. Counting exact-order triples using step 2 and then
   the lower certificate gives
   E[F] <= 2L sigma n^2/R and E[Zpi-Z0] <= 2L sigma n^2.
   No independence between these two counts is needed. Each exceeds its
   threshold with probability at most 1/12. Deduplicated lists have Z0<=n^2.
   This is the simultaneous control missing from a naive fixed hash choice.

6. **Probe enumeration does not hide cubic work.** For a fixed x1 and a label
   of list 2, the compatible label of list 3 is determined. Expanding the two
   block ceilings bounds the probe count by
   n C2 + 2n^2/sigma + Zpi/sigma^2.
   The constant, linear, and bilinear terms respectively have exactly those
   bounds, because translation of labels is injective and the bilinear sum
   counts pi-zero triples. Enumeration takes n times the number of list-2
   blocks plus its output, using a sorted label index. On the good event this
   is at most A n^2/sigma, A=M^2+3+24L. The cap is observable during listing;
   evaluating Zpi itself is not part of the algorithm.

7. **Literal support-product semantics and witness scans.** Within each block,
   differences of K-values lie in B. At a probe position the prescribed
   (mu1,mu2) is K(x1)+K(z2)+K(z3), also in B. Equating the two displayed matrix
   membership expressions cancels the representatives and gives exactly
   K(x1+x2+x3)=0. Boolean supports preserve positivity of the integer product.
   Every true triple has a probe and a positive entry. Probes can share a matrix
   position without affecting the argument: every positive probe with no true
   witness contains a distinct nonzero K-zero triple, since a triple determines
   its own x1 and two blocks. Thus the number of failed scans is at most F.
   Direct vector tests in the sorted third block find any true witness and
   preclude false YES answers. The failed-scan cap is observable without knowing
   F; at most one further scan is needed before success or the cap is detected.

8. **The actual matrix theorem applies.** I checked the published Corollary 26
   directly, including its data-structure and prescribed-entry versions. It
   applies to integer matrices with polynomially bounded entries, when
   N>=D^18. Here the entries are 0/1. The frozen construction gives N>=n,
   D<=n^eta<=N^(1/18), and D^(1+gamma)<=N. Its query cap is below
   N^2/sqrt(D), using sigma<=sqrt(R), D>=R/M, and the explicit g0. Therefore
   one deterministic call per nonaborted profile suffices. No new counting
   oracle, unproved group hash, or Exact Triangle reduction is assumed.

9. **Full charged running time.** The actual outer dimension satisfies
   N=O_M(n sqrt(R)/sigma). Since sigma is within a factor two of
   R^(1/2-gamma/4), the call costs
   O_M(n^2 R^(1-gamma)/sigma^2)=O_M(n^2 R^(-gamma/2)).
   Initializing both dense matrices costs O(ND), covered because
   D^(1+gamma)<=N. Setting all their nonzero entries costs
   O(n sqrt(pD) polylog(n)), also below this budget. Listing/sorting the capped
   probes costs O_M(n^2/sigma polylog(n)); the exponent inequality
   1/2-gamma/4 >= gamma/2 holds for gamma=0.063. The capped scans cost
   O((sigma^2 n^2/R+sigma) polylog(n)), with the first term having the same
   R^(-gamma/2) saving. Hash evaluation, sorting, quotient labels, coefficient
   generation, exact rational-power parameter comparisons and original-index
   recovery require polynomial logarithmic overhead. In particular, h and
   sigma can be computed with integer-power comparisons of O_M(log n)-bit
   integers; a real-number operation is not required. Multiplying by all profile
   subinstances leaves O_(M,c)(n^(2-eta gamma/2) polylog(n)). Matrix dimensions
   are polynomial in n, so their word lengths and bit simulation add only
   polylogarithmic overhead. The exponent saving depends on M, not c.

10. **Worst-case random paths and quantifiers.** Uniform coefficient rejection
    sampling has expected at most 2r ell attempts. The 24r ell cap fails with
    probability at most 1/12 by Markov, coupled to unlimited uniform sampling.
    Together with the two 1/12 tails above, a fixed witness's deterministic
    profile succeeds with probability at least 3/4. One need not union-bound
    over all profile subinstances: on a positive input fix one witness before
    randomness; reaching its profile is unnecessary if an earlier witness was
    already found. Every profile has a deterministic listing, scanning, and
    random-bit cap on every execution. Negative inputs cannot produce a false
    witness. Thus this is a bounded-time, per-fixed-input, one-sided-error
    algorithm, at the full frozen scope.

## Independent finite evidence

I wrote `audit/referee-verifier.py` from the definitions, importing no proposer
code and preserving the frozen test output. Its literal support matrices check
all entries before consulting their probe positions. The completed exact checks
are recorded in `audit/referee-verifier-results.json`:

- 778 full-row and 1,382 reduced-row output distributions over nine moduli;
- 4,622 complete original-profile subinstances and their order potentials;
- 144 support instances, 45,932 literal matrix entries and 13,244 probes;
- 3,036 false-positive probes, with their total bounded by distinct false
  triples in each instance.

These checks include mixed moduli, prime powers, fragmented profiles, odd and
even middle dimensions, zero/full-prefix cases and nonsurjective hash images.
They are finite regression evidence. They neither prove asymptotic running time
nor establish novelty. I did not run a formal assistant or reimplement the
published thin-matrix algorithm. The argument above supplies the asymptotic and
probabilistic verification; the existing algorithmic theorem supplies that call.

## Prior results, current novelty and value

The actual primary positions checked were Majdoddin's arXiv:2610.17420v1,
Model, Lemmas 19.6–19.7, Theorem 19.17, Corollary 19.25, Open Problem 19.26,
and Lemmas 20.3–20.4/Remark 20.6; and Alman–Vassilevska Williams,
arXiv:2610.06783v1, Section 4.1, Corollary 26. The former already handles
exponent dividing p^2; its embedding includes Z4^d times F2^d. The ordinary
support construction and matrix primitive are inherited, not new contributions.
The suggested layer-induction goal is also prior. The accepted new part is the
simultaneous original-coset profiles and extremal divisor certificate: it balances
all orders with one elementary middle group, without recursive layer enumeration.
The earlier statements do not supply that certificate or the resulting all-M
algorithm. This is a new algorithm for the entire missing bounded-exponent class,
not an elementary corollary or an isolated diagnostic counterexample.

As a consequence already anticipated by Remark 20.6, this closes the sufficient
tractability direction for every fixed abelian-group-representable finite
coordinate relation, uniformly in its logarithmic dimension constant. I checked
the finite-quotient argument in Lemma 20.3(d) and the witness-preserving translation
in Lemma 20.4(a): for fixed P the representing finite group and its exponent are
fixed, while its d-fold power has polynomial order. This consequence is routine
from the accepted group theorem and the cited lemmas; it is not a second new
method or a dichotomy for nonrepresentable relations.

The live arXiv record still displayed only v1 and the live author's group README
still described the p^2 scope. A bounded fresh search also found and checked
Chan–Itakura–Ma–Yu, arXiv:2610.42012v1 (30 October 2026), Theorem 2.3 and
Sections 2.2/3. Its reductions concern integer inputs and use random-prime
residues and carry-free encodings; they do not state or immediately give the
bounded-torsion theorem. No full-scope equivalent was found. Search terms,
primary URLs and limitations are recorded in `audit/referee-literature.md`.
This is a bounded current novelty assessment, not proof of universal priority.

## Final mathematical judgment and limits

The original scope is resolved, the randomized correctness and all main costs
are accounted for, and no unresolved mathematical gap was found. The qualitative
extension to every bounded exponent and its generic representation consequence
provide substantive new mathematical value. Accept the frozen claim unchanged.

The review relies on the cited published algorithmic theorem as ordinary prior
work; it is not a fresh proof of that theorem. Novelty screening cannot exclude
unindexed/unpublished equivalents. No manuscript, layout, citation-completeness
audit, or external submission was performed. These limits do not weaken the
accepted mathematical scope. The separate working_paper label records real
uncertainty about competitive STOC technical depth and broader impact, not a
claim that any manuscript or artifact gate has already passed.
