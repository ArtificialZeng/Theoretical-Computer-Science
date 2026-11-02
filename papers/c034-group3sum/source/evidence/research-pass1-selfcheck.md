# Proposer's adverse self-check (not fresh review)

Job c034-group3sum-research-3974e7a3f8f0. Full proof:
research/divisor-profile-proof.md. Exact finite regression script/output:
research/verify_divisor_hash.py, evidence/divisor-hash-tests.json.

* Fragmentation attack: lower coset occupancy is false after intersecting
  profiles. The proof uses lower occupancy ONLY in original lists, to bound
  the NUMBER of represented original cosets. Upper occupancy continues to
  hold under intersection. Tests explicitly exercised 352 fragmented cosets.
* Mixed-prime attack: the final reduced row has kernel rate gcd(d,p)/d,
  rather than always p/d. The proof upper bounds that rate by p/d and sums
  all exact orders d|e; it does not require all such d divisible by p.
* Resource attack: row choice does not enumerate triples or evaluate F.
  Expectations select a high-probability event; observable probe-output and
  failed-scan caps make every random path obey the time bound.
* Randomness attack: rejection sampling can take unbounded time. The explicit
  24*r*ell attempt cap contributes failure probability <=1/12, added to two
  <=1/12 Markov tails, preserving success >=3/4 on each fixed positive input.
* Error accumulation attack: fix one input witness and its deterministic profile.
  Existential detection needs that profile to succeed; there is no erroneous
  union bound over polylogarithmically many positive subinstances. Every YES
  is checked using original group addition and original list membership.
* Matrix legality: proof checks D<=N^(1/18), query count<=N^2/sqrt(D),
  D^(1+gamma)<=N and initialization cost ND, with explicit M-dependent padding.
  Quotient vectors remain compact; no huge quotient table is constructed.
* Scope: quotient subgroups G[d] include every divisor of arbitrary fixed M;
  higher prime powers and mixed primes use the same identities. No special
  case replaces the immutable original. delta_M is independent of c.

Exact coverage: 1,698 row identities over all two-dimensional rows/vectors for
M in {2,3,4,6,8,12,18}; 1,749 profile subinstances from 16 deterministic-seed
list inputs, 746 support/probe product checks, and 1,150 arbitrary divisor-size
parameter profiles at n=2^256,2^1024,2^4096 where the diagnostic range applies.
These finite checks do NOT certify the infinite theorem, probability bound,
novelty, or the cited thin matrix algorithm. Those are mathematical proof and
source-dependency obligations, documented in the proof packet.

Preserved route history: naive fixed-family hashing is obstructed by the source's
order-dependent survival rates. A direct layer-by-layer extension would need
multiple size potentials and cannot be assumed from the p^2 theorem. The new
profile/slope route avoids that unproved induction; no universal impossibility
or new lower bound is inferred. No failed mathematical counterexample was found.

Operational extraction diagnostics: BeautifulSoup was unavailable; switched to
standard-library HTMLParser. Early text matching hit mentions rather than the
Corollary 26 heading; corrected to the heading beginning 'Let N', and inspected
the resulting exact theorem. Neither diagnostic is mathematical evidence.

No known gap remains in the proposer's full argument after this self-check.
This is not independent review or acceptance. Most decisive next step: a fresh
referee should try to falsify inequalities (1)-(3), all-order survival (5)-(6),
and the capped support-product/witness interface before assessing current novelty
and significance. No manuscript or PDF is authorized by this packet alone.
