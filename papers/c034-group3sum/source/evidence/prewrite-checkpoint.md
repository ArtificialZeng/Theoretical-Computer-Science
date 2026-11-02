# Checkpoint

Job: c034-group3sum-research-3974e7a3f8f0 (RESEARCH pass 1).
Accumulated research passes: 1 of at most 3. Prior TRIAGE consumed 0; no reset.
Decision: CANDIDATE, kind resolution-paper. Proposer original_status: proved,
subject to the required fresh referee; no acceptance or venue assessment exists.
Previous unresolved triage verdict is preserved in evidence/triage.md and its
provenance. No manuscript/PDF is created or authorized by this proposer verdict.

source.md bytes remain unchanged, SHA256:
f3507a3e5b20d6707750b7e703d5d1c0764d4d5b13ef6b7a4f0001d940c8e8cf.
The exact quantified original remains every fixed M, every compact exponent-
dividing-M abelian group of polynomial order, saving independent of c, charged
witness recovery and bounded randomness. claim.json binds source.md/problem.md.

New substantive artifact: research/divisor-profile-proof.md proposes a complete
randomized algorithm for that original scope. Let eta=min(1/18,
1/(8*ceil(log_2 M))), gamma=0.063 and delta_M=eta*gamma/2. The algorithm has
worst-case O_(M,c)(n^(2-delta_M) polylog(n)) cost, returns only verified witnesses,
and has success >=3/4 on each fixed positive input. It uses the actual prior
Alman-Vassilevska Williams Corollary 26 thin-product algorithm, whose primary
statement was checked and downloaded in intake/primary/2610.06783v1.html.

Core new method: simultaneously bucket elements by ORIGINAL coset sizes for
all annihilator subgroups G[d], d|M. Pick the least ell with d^ell*sigma>=s_d*R
for every nontrivial divisor; choose e violating this at ell-1 and a prime p|e.
The quotient modulo G[e], full-row prefix and reduced-row suffix give both
O_M(n/sigma) blocks and an elementary F_p^q middle. Order-d survival is d^-ell;
the profile/slope inequalities yield E[F]=O_M(sigma*n^2/R) and
E[Z(pi)-Z0]=O_M(sigma*n^2). Observable listing/scanning caps and a random-draw
cap give the bounded-time error guarantee without an uncharged potential oracle.
All polylogarithmically many profile triples and witness scans are charged.
Mixed primes and higher powers follow from the same order identity, not a
narrowed Z8 case or an assumed CRT induction.

Exact finite validation: evidence/divisor-hash-tests.json and
research/verify_divisor_hash.py. Passed 1,698 exhaustive two-dimensional row
identities at M=2,3,4,6,8,12,18; 1,749 profile subinstances from 16 seeded inputs;
352 fragmented-coset checks; 746 support/probe semantic checks; 1,150 diagnostic
large-integer parameter profiles. These tests do not prove the infinite theorem.

Source comparison: evidence/research-pass1-literature.md. Current primary v1 and
author README still have elementary/p^2 scopes. The source's layer-induction
suggestion is prior. No equivalent full resolution was located in bounded
searches; this is not a global novelty certificate. New claimed value is the
all-divisor profile/slope method, subject to fresh critical assessment.

Obstacles/failed routes: fixed-family uniform hashes have order-dependent
survival; blindly importing integer hashes or p^2 induction was not justified.
Fragmented sublists do not preserve lower coset occupancy: the new proof uses
original-list occupancy only to bound numbers of represented original cosets.
See evidence/research-pass1-selfcheck.md for these attacks, the random-bit cap,
call legality, error accumulation and source-extraction diagnostic repairs.
No known gap remains in the proposer's proof; this is not independent review.
The existing thin-product theorem is a cited dependency, not re-proved here.

Next test: fresh referee independently try to falsify the divisor-profile
occupancy bounds, maximum-slope inequalities (1)-(3), all-order survival (5)-(6),
and bounded-time support-product/recovery argument, including mixed-prime M.
Then assess current novelty, nonroutine value and STOC significance against
Theorem 19.17/Open Problem 19.26 and the actual thin-product primitive. The runner
must freeze claim/evidence before that review; no writer may start before actual
accepted full-scope correctness/innovation gates.
