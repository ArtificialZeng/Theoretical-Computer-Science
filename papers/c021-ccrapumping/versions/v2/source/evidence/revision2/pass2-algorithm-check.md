# Independent commutativity criterion for checking the explicit algorithm

Research job c021-ccrapumping-research-b9b720512ca2. This elementary
criterion is a validation tool, not a separately claimed innovation.

Combine coefficients of repeated patterns and let c_p=0 for unlisted words.
Then the finite sum f(w)=sum_p c_p [w:p] is permutation-invariant iff
c_p depends only on the Parikh vector of p (including absent patterns).

Proof. The scattered-pattern functions [w:p] are Q-linearly independent
in the sense of finite linear combinations. If a nonzero combination
vanished, take a shortest pattern p with nonzero coefficient and evaluate
at w=p. Longer patterns cannot embed; other patterns of the same length
cannot embed; shorter coefficients are zero. The value is c_p, a
contradiction. For any Parikh vector m,

    sum_(Parikh(p)=m) [w:p] = product_a binom(|w|_a,m_a),

because choosing m_a positions of each letter determines one induced
subsequence word. Thus Parikh-constant coefficients imply invariance.
Conversely, for invariant f evaluate on sorted words as in pass2-proof.md:

    f(w)=sum_(p sorted) c_p product_a binom(|w|_a,m_(p,a)).

Expand each product by the preceding counting identity and use linear
independence. All coefficients in each Parikh class must equal the
coefficient of its sorted representative.

An equivalent sparse finite check is: in every nonzero Parikh class,
all combined coefficients coincide, and the number of distinct supported
patterns is the multinomial |p|!/product_a m_a!. This can be checked in
polynomial bit time without enumerating missing permutations. All-zero
classes disappear. This provides a structurally different oracle against
which to test the reachable/observable commutator algorithm; it does not
use weighted minimization or finite word testing to decide invariance.
The universal CCRA conclusion still depends on the finite-control theorem.

`pass2_algorithm_checks.py` compares this criterion with the supervisor's
explicit WA algorithm and checks its YES constructions and NO certificates
by direct subsequence dynamic programming. Finite checks are supporting
evidence only. The certificate bound tested is the submitted <=2D bound;
no improved bound or additional synthesis claim is introduced.
