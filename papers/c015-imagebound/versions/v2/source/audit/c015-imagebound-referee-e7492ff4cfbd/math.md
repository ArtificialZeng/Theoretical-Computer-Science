# Fresh mathematical referee report

Job: **c015-imagebound-referee-e7492ff4cfbd**, role referee.
Frozen snapshot: `cb1b52760e44f40d39212ae4e2487e31dff8bbdea70ba237a86a02d321ed9f7e`.
Original source SHA-256:
`7cf4a0de6b28019b0fa2f5e92ea04bee150c74cb9db945e382c75d8379326aa7`.

**Verdict: accept the resolution-paper at its exact frozen scope. Original
status: proved. STOC assessment: working_paper.** These are fresh internal
judgments, not external peer review or a venue decision. Mathematical
acceptance does not certify a manuscript, PDF, release, or STOC readiness.

## Review boundary and scope

I read the required skill/referee instructions, release contract, project
policy and current STOC standard, the phase-start boundary note, source.md,
problem.md, claim.json, snapshot, and relevant snapshot-listed evidence.
I did not read checkpoint.md, state.json, earlier audit reports, transcripts,
archives, or previous confidence/verdicts. Historical and confidence language
inside the required problem/proof packet was not used as evidence. The
unlisted supervisor proof mentioned in the packet was not consulted.
The primary-source checks are recorded separately in this job's literature.md.

The immutable original concerns mortality of arbitrary finite-alphabet NFAs
with the GLOBAL promise |q.w|<=k for every singleton q and every word w.
The frozen full interpretation requires the asymptotically optimal exponent
k+1 for every fixed integer k>=2, on every sufficiently large state size.
It does not add unambiguity or interpret k as growing jointly with n.

The accepted theorem meets exactly that scope. For K=k!, A=1+k(k+1)/2,
N_k=2k+2AK and c_k=K/(2A)^(k+1), every n>=N_k admits a binary strongly
connected incomplete n-state example with mortality threshold at least
c_k*n^(k+1). Together with the known upper bound, this proves
M_k(n)=Theta_k(n^(k+1)). The additional binary and connectivity properties
strengthen the lower bound; they do not restrict the original maximum.
Neither leading-constant optimality nor a bound uniform in growing k is claimed.

## Reconstruction of the decisive proof

Take disjoint queue P of size m>=2 and clock cycles of lengths ell_i>=2.
Letter a rotates each of these sets. Letter b sends p_0 to the packet S of
clock zero positions, permutes P minus {p_0} cyclically, kills each clock's
terminal position, and sends every other clock position to p_0. Put
L=lcm(ell_1,...,ell_k). These rules agree with the frozen tables.

1. **All words satisfy the promise.** Empty sets, all singletons, and all
   translates S.a^t form a family closed under both letters. A packet's
   b-image is either empty or the singleton {p_0}; all its surviving
   components merge at the same port. A singleton's b-image is empty,
   a singleton, or S. Induction over arbitrary words gives the global
   endpoint bound. It is exactly k because p_0.b=S. Repeated forks cannot
   accumulate additional packet support. This is stronger than an outdegree
   check. Strong connectivity follows from rotations to p_0, a b-step into
   the clocks, and a nonterminal clock b-step back to p_0.

2. **The charging identity holds for arbitrary words.** Initially Q.a^t=Q
   and Q.b=P union S. Immediately after any b, the global image has form
   T union cS, where T is a subset of P and c is 0 or 1. Its potential is
   |T|+c, initially m+1. For the next factor a^t b, let alpha indicate
   p_0 in T.a^t. The queue loses alpha points into a new packet; the
   remaining queue points map injectively into P minus {p_0}. The old
   packet contributes p_0 exactly when it is present and has a
   nonterminal component. Calling that indicator epsilon, the new
   potential is |T|+epsilon, and the drop is c-epsilon.

   Hence the potential never increases, and drops by one precisely when
   c=1 and all clocks are terminal. This requires t=-1 modulo every
   ell_i, equivalently L divides t+1; such an interval costs at least L.
   It remains true if alpha=1 and the same b creates a replacement packet.
   A failed attempt creates p_0 outside the image of the queue permutation,
   so it cannot hide an additional decrease through a queue collision.

   A mortal word must contain b. Its initial and terminal a-runs may be
   removed because a is a permutation. Between its first and last b the
   potential must go from m+1 to zero. Exactly m+1 disjoint inter-b
   intervals have a unit drop, proving length >=1+(m+1)L. This rules out
   all shortcut words, rather than only certifying a selected long witness.

3. **Mortality is actually established.** Whenever a packet is present,
   a^(L-1)b lowers the potential by one. If no packet is present but the
   queue is nonempty, rotate any occupied queue position to p_0 and apply
   b. This costs at most m, creates a packet and preserves the potential.
   Perform the killing interval next. There are m+1 drops and at most m
   preliminary forks, giving a mortal word of length <=1+(m+1)L+m^2.
   No coprimality of m and L is needed. Potential zero means the whole
   subset is empty; the procedure does not merely kill one original row.

4. **The parameter choice covers every n.** For each n>=N_k set
   M=K floor((n-k)/(AK)), ell_i=1+iM, and
   m=n-k-(A-1)M. Then m>=M>=n/(2A) and M>=2. The state count is exactly
   n. If a divisor d divides two clock lengths, it is coprime to M and
   divides j-i. A prime divisor of d would be at most k-1, hence would
   divide K and M, a contradiction. Thus the clock lengths are pairwise
   coprime and L=product ell_i>=k! M^k. It follows that
   (m+1)L>=k! M^(k+1)>=c_k*n^(k+1). No prime distribution assumption,
   sparse subsequence, padding, or changed alphabet hypothesis is used.

5. **The upper bound is justified at the same scope.** Successively kill
   the images of the n original states. Every continuation of one such
   image is still the image of its original singleton, so the global
   promise bounds its size by k throughout. A shortest killing suffix
   cannot repeat a nonempty subset; its length is at most
   D=sum_{j=1}^{min(k,n)} binomial(n,j). Encode a nonempty subset by its
   increasing list, padded to length k with repetitions of its maximum;
   this is an injection into Q^k. Therefore D<=n^k and the concatenated
   word has length <=n^(k+1). Empty rows remain empty under continuation.
   This argument reproduces the known upper bound and is not credited as new.

I found no essential correctness, quantifier, degeneracy, or scope gap.
The assumptions m>=2 and ell_i>=2 are used explicitly, including in the
connectivity and first-b calculations. The proof avoids counting paths as
distinct endpoints and avoids assuming that singleton mortality alone
implies global mortality.

## Independent exact checks actually performed

The new `verify.py` in this job's audit directory imports no frozen checker.
It regenerates the transition relations as integer bitmasks and explores
complete singleton and full-set subset closures. It also validates saved
distance tables by transition equality, edge inequalities, and a predecessor
at the preceding distance for every non-root vertex. This supplies a local
distance certificate in addition to its independently generated BFS.

- All nine serialized intake certificates were checked against the fresh
  transition rules, singleton closures, global graphs and exact distances.
- All 18 frozen research cases were replayed, including every saved graph
  edge and the saved mortal words. The nine original shortest lengths are
  48, 91, 181, 63, 123, 243, 78, 155, 301.
- Another 43 parameter cases, absent from those 18 records, were checked.
  They include k=1 calibration, k=5 packets, repeated and noncoprime clock
  lengths, and gcd(m,L)>1. The general theorem is not inferred from them.
- Across the 61 cases, every abstract queue subset and packet indicator,
  and every a-phase residue modulo lcm(m,L), were tested: 277,168 potential
  transitions, including 5,044 simultaneous kill-and-replacement events.
  Constructive mortality and underlying strong connectivity passed too.
- There were 1,181 exact arithmetic samples for k=2,...,20, including
  threshold values and full floor periods for the smaller k. These support
  implementation checks of the parameter formulas, not the infinite proof.

`verification.json` records the cases and results. All frozen file hashes
and the canonical snapshot digest were independently recomputed and matched.
No original source, claim, snapshot, frozen proof, code or certificate was
modified. Existing active math/innovation review bytes were copied to this
job's `prior-active-audits/` without consulting their contents before the
fresh reports were installed. Their hashes are recorded in verification.json.

## Novelty, value and limitations

The nearest verified prior constructions and current follow-ups are compared
in this job's literature.md. The source [MFCS 2025 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.62)
poses this precise endpoint-support tightness direction; its main unresolved
complexity question is a different question about unambiguous automata.
The deterministic queue and physical-tail mechanism are established prior
work, as directly checked in [Ryzhikov, Section 4](https://arxiv.org/html/2405.19622v4)
and [Ananichev's Lemma 2.1](https://arxiv.org/pdf/1701.07954).
Neither CRT alone nor the old sequential-delay mechanism is new here.

The substantive delta is the shared compressed packet together with its
all-word closure and collision-free potential. It realizes L units of delay
using sum(ell_i) clock states and forces a linear number of such delays
without multiplying that clock-state cost. The known physical-tail theorem
does not imply that replacement preserves the global promise or prevents
shortcut mortality. The exact invariant and charging identity supply those
missing facts and yield the optimal exponent at every fixed k, even with
two letters and strong connectivity. This is sufficient substantive new
mathematical value for the resolution-only gate; it is not merely a finite
witness, an elementary restatement of a cited theorem, or a restricted-model
substitute for the original problem.

The fresh finite literature screen found no equivalent hierarchy resolution
among the checked primary records. It is not exhaustive priority assurance.
The finite-rational-semigroup and joint-spectral-radius hypotheses in the
inspected later results fail for the construction, since b^(2r) has k^r
ordinary return paths from p_0 to itself. Those results do not supersede it.

The accepted result does not determine optimal constants, give running-time
lower bounds, resolve unambiguous mortality, or establish broad applications.
Those omissions are not gaps in the frozen theorem. They do limit the case
for a major general-theory advance. The separate STOC assessment consequently
uses **working_paper**, with uncertainty about importance and technical depth
and a weak demonstrated breadth case. No manuscript or PDF was authored in
this referee job. Future writing and artifact release require their own gates.

## Structural handoff check

The required release_gate.py check-math command passed on the installed fresh
audit with the frozen snapshot and actual referee job ID. This checks integrity
and workflow provenance, not mathematical truth or venue quality. The exact
command result is retained in this job's completion.json.
