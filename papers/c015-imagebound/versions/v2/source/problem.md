# Frozen question and precise interpretation

Original input: source.md, preserved verbatim. SHA-256:
7cf4a0de6b28019b0fa2f5e92ea04bee150c74cb9db945e382c75d8379326aa7.
Triage job c015-imagebound-triage-104fc05d5d7d, 2026-11-01.

## Model and quantifiers

An automaton A=(Q,Sigma,Delta) has |Q|=n>=1, a finite nonempty alphabet,
and relations Delta_a subset Q x Q. There are no designated initial or final
states. For S subset Q, S.w is the union of all endpoints of w-labelled paths
from S; q.w abbreviates {q}.w, and S.epsilon=S. Missing transitions are allowed.
The global k-image promise is

    for every q in Q and every w in Sigma*, |q.w| <= k.

It does not merely constrain one-letter outdegree and does not bound path
multiplicity. A word is mortal if Q.w is empty; A is incomplete precisely when
such a word exists. Write mu(A)=min{|w|:Q.w=empty} for incomplete A, and

    M_k(n)=max mu(A)

over all such n-state incomplete globally k-image-bounded automata and finite
alphabets. Repeated letter relations are redundant, so this maximum is over
a finite set of possibilities up to names. No strong connectivity,
unambiguity, determinism or alphabet-size restriction is imposed.

The assigned full fixed-parameter tightness reading is

    for every fixed integer k>=2 there are c_k>0 and N_k such that
    for every n>=N_k, M_k(n) >= c_k n^(k+1).

Together with the source upper bound this means M_k(n)=Theta_k(n^(k+1))
for every fixed k>=2. Constants and thresholds may depend on k. A family on
sizes n_j with bounded ratios n_(j+1)/n_j suffices: add isolated states with
no outgoing edges to fill intervening sizes without changing a positive
mortality threshold. An arbitrarily sparse family alone does not suffice.

The source's literal final question is only “Is this bound tight?” and does
not explicitly specify these asymptotic quantifiers. The fixed-k hierarchy
is the interpretation explicitly frozen in source.md by the user, not a
quotation of a fully quantified conjecture from the paper. We do not change
it. The elementary bound M_k(n)<=2^n-1 rules out reading n^(k+1) as jointly
tight for all growing k. The k=1 partial-DFA case is known quadratic
calibration, outside the proposed new contribution.

Logically a single fixed-k improved upper bound refutes the displayed universal
tightness assertion. The user's publication requirement is stronger: answer
the full fixed-k hierarchy, either by all-k matching constructions or a
genuinely uniform sharper upper-bound theorem covering that hierarchy.
An isolated k=2 result is recorded only as partial work under this policy.

## Nearest prior results and status

Kiefer and Ryzhikov, MFCS 2025, DOI 10.4230/LIPIcs.MFCS.2025.62,
Section 2 pp.62:2–3 defines the semiautomaton/matrix model; Section 7
pp.62:14–15 defines the global image bound and proves the two-state killing
criterion (Lemma 12); Section 9 p.62:16 states the n^(k+1) bound and asks
tightness. Latest arXiv version observed: 2504.13784v2, 2025-07-23.

The usual proof explains the extra factor n: after a prefix, any original
state has at most k current images; its reachable subset orbit has at most
B(n,k)=sum_{j=0}^{min(k,n)} binomial(n,j) elements. A shortest suffix killing
that image has length at most B(n,k)-1. Killing original rows successively
gives at most n(B(n,k)-1)=O_k(n^(k+1)). This is a routine explanation,
not a new result.

Root's cycle-reset benchmark gives only Omega_k(n^k). Local proof and complete
finite checks are in evidence/clock-baseline.md and its code/results. General
NFA mortality, finite rational matrix semigroup mortality and bounded
ambiguity have different hypotheses; see evidence/literature.md.

Source status: open-supported for research under the assigned reading.
No equivalent resolution was found in the bounded primary-source checks of
2026-11-01; this is not an exhaustive novelty or priority certification.
The c003-compress target concerns complete deterministic strongly connected
synchronizing automata and a distinguished-state pair-merging threshold;
its objects, quantifiers and objective differ. No full historical registry
comparison is claimed where that registry was unavailable.

## Triage proposal and decision (historical)

Nearest result: O_k(n^(k+1)) upper bound versus the routine n^k clock lower
bound. Proposed delta: a rigorously mortal sequential queue plus k-cycle clock
forcing a linear number of long simultaneous-clock events, for every k.
The exact transition table, potential lemma and nine-model bounded first test
are frozen in evidence/next-test.md. This is a plausible full-scope route,
not an established construction or novelty claim. If it is an elementary known
composition without substantive independent innovation, park it under policy.

Decision: advance to bounded research; original unresolved, candidate_kind=none.
No manuscript/PDF is authorized by this triage.

## Research pass 1: proposed full resolution, pending fresh review

Job c015-imagebound-research-337b679e5617 leaves all definitions and quantifiers
above unchanged. Its complete proposed proof is evidence/research-proof.md.
For K=k!, A=1+k(k+1)/2, c_k=K/(2A)^(k+1) and N_k=2k+2Ak!, it proves:
for every k>=2 and every n>=N_k there exists a binary strongly connected
incomplete globally k-image-bounded n-state NFA with mortality threshold at
least c_k*n^(k+1). Together with the known upper bound this yields the whole
frozen fixed-k hierarchy M_k(n)=Theta_k(n^(k+1)).

The general construction, for m>=2 and clock lengths ell_i>=2, has threshold
between 1+(m+1)*lcm(ell_i) and that number plus m^2. The new proof identifies
the exact all-word support invariant, a potential charging m+1 disjoint clock
events, constructive mortality without gcd(m,L)=1, and an elementary
pairwise-coprime clock choice for every sufficiently large n.

The current comparison is evidence/research-literature.md. In particular the
known deterministic queue/tail mechanism is acknowledged; the proposed delta
is the compressed clock packet preserving the global image bound while
retaining a linear number of costly events. The September 2026 quadratic
matrix-mortality preprint assumes joint spectral radius<=1, which fails here
for k>=2, and does not supply a resolution of this question.

This is a resolution-paper proposal with no mathematical gap presently known
to the proposer. Correctness, current novelty and substantive significance
still require the normal frozen fresh referee. No acceptance or manuscript
authorization follows from this research record.
