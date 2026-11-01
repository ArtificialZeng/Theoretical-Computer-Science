# Full fixed-parameter mortality hierarchy: research proof packet

Proposer job: c015-imagebound-research-337b679e5617. This is a mathematical
evidence record for a proposed resolution, not an accepted paper or referee
report. The original question is the unchanged source.md, interpreted exactly
as in problem.md. The frozen transition rule originates in evidence/next-test.md;
the supervisor supplied the all-parameter argument in
intake/root-queue-clock/queue-clock-proof.md. The present pass checks and spells
out that argument, including the mortality procedure and every-n quantifiers.

## Statement

Let M_k(n) be the maximum shortest mortal-word length over incomplete n-state
NFAs with a finite alphabet and |q.w| <= k for every state q and every word w.
For every integer k >= 2, put

    K = k!,  A = 1 + k(k+1)/2,
    N_k = 2k + 2AK,  c_k = K/(2A)^(k+1).

For every integer n >= N_k there is a binary, strongly connected such NFA
with shortest mortal-word length at least c_k n^(k+1). Consequently

    c_k n^(k+1) <= M_k(n) <= n^(k+1)     (n >= N_k),

so M_k(n) = Theta_k(n^(k+1)) for every fixed k >= 2. Strong connectivity and
two letters strengthen the original lower-bound conclusion. The argument also
works at k=1, whose quadratic order is already known. No uniform-in-growing-k
lower bound, exact extremal value, or optimal leading constant is claimed.

## Lemma 1: construction and the global all-word promise

Take integers m >= 2 and ell_1,...,ell_k >= 2. Let the disjoint sets of states be

    P = {p_0,...,p_(m-1)},
    C_i = {c_(i,0),...,c_(i,ell_i-1)}  (1 <= i <= k).

Write S = {c_(i,0):1 <= i <= k} and L = lcm(ell_1,...,ell_k). Letter a rotates
P and each C_i by one. Define b by

    p_0.b = S,
    p_1.b = {p_(m-1)},
    p_j.b = {p_(j-1)}                         (2 <= j < m),
    c_(i,ell_i-1).b = empty,
    c_(i,j).b = {p_0}                        (0 <= j < ell_i-1).

The restriction of b to P minus {p_0} is a permutation f of that set. This
includes m=2, when f fixes p_1.

Consider the family F consisting of the empty set, all singleton states, and
all packets S.a^t, t >= 0. It is closed under a. A singleton has b-image empty,
singleton, or S. For a packet, every component under b either disappears or
goes to the SAME p_0; its b-image is therefore empty or {p_0}. Hence F is
closed under b too. Induction on the entire word, starting with any singleton,
gives q.w in F. All its members have size at most k, proving the global
promise, including arbitrarily many successive forks. In fact p_0.b has size
k, so the least admissible global bound is exactly k.

The underlying digraph is strongly connected. From a queue state, powers of
a reach p_0. From a clock state, rotate to position zero and then use b to
reach p_0; ell_i >= 2 makes position zero nonterminal. From p_0, powers of a
reach all of P, while b followed by powers of a reaches any prescribed clock
state (using the appropriate branch). This proves the claimed connectivity.

## Lemma 2: a potential for all words, not only a proposed witness

Letter a is a permutation of Q. Thus Q.a^r = Q for all r >= 0. Also

    Q.b = P union S:

the queue states other than p_0 supply P minus {p_0}, p_0 supplies S, and
nonterminal clock states supply p_0. After every b the current global image
has a unique form T union (cS), where T is a subset of P and c is zero or one.
Set V(T,c) = |T| + c. Immediately after the first b, V=m+1.

Consider any next interval a^t b between consecutive occurrences of b, with
t >= 0. Put U=T.a^t and alpha=1 if p_0 belongs to U and zero otherwise. Put

    epsilon = 1 if c=1 and some clock in S.a^t is nonterminal,
              0 otherwise.

At the next b-boundary the queue part is

    f(U minus {p_0}) union ({p_0} if epsilon=1),

and the clock part is alpha S. The two parts of the displayed queue union
are disjoint; f is injective on P minus {p_0}. Since a permutes P, this gives

    V_new = |T| - alpha + epsilon + alpha = |T| + epsilon,
    V_old - V_new = c - epsilon.

The drop is zero or one. It is one exactly when a packet was present and all
of its clock states are terminal. That condition is

    t = -1 mod ell_i for every i, equivalently L divides t+1.

In particular, every interval responsible for a unit drop has length t+1 >= L.
The intervals between consecutive b occurrences are disjoint in the word.
This identity allows a killed packet to be replaced by a new packet at the
same b: alpha can be one. It does not falsely charge a new packet as another
drop or assume that queue and clock phases are independent.

Any mortal word contains b. Remove its initial a-run, which fixes Q, and
its terminal a-run, whose inverse permutation preserves emptiness. The
remaining word starts and ends with b. Its first b gives potential m+1, and
its last b gives potential zero. There must therefore be exactly m+1 unit
drops (possibly with zero-drop intervals between them), each costing at
least L letters after the first b. Consequently every mortal word satisfies

    |w| >= 1 + (m+1)L.                                      (1)

No coprimality assumption, finite search, or guess about a shortest word was
used in this proof.

## Lemma 3: constructive mortality

Start by applying b, obtaining P union S. At a b-boundary with a packet
present, apply a^(L-1)b. Lemma 2 says that this decreases V by exactly one,
regardless of the queue subset.

If no packet is present and V>0, choose any p_j in the nonempty queue subset.
Apply a^t b with t=(-j mod m) in {0,...,m-1}. This forks a packet and keeps V
unchanged, by the same identity with c=0. Its cost is at most m. Then perform
the packet-killing interval a^(L-1)b.

Each iteration lowers the nonnegative integer V, so after exactly m+1 drops
the subset is empty. The first drop needs no preliminary fork. Thus at most
m forks are used and the total word length is at most

    1 + (m+1)L + m^2.                                      (2)

This proves that the construction is incomplete. In particular, gcd(m,L)=1
is unnecessary; a reset of the packet does not have to retain any previous
queue phase. Equations (1)--(2) bound the threshold, without claiming either
bound is always its exact value.

## Lemma 4: every sufficiently large n, for every fixed k

Use K,A,N_k above; let B=A-1. For an arbitrary n >= N_k define

    M = K floor((n-k)/(AK)),
    ell_i = 1+iM                          (1 <= i <= k),
    m = n-k-BM.

Because AM <= n-k, we have m >= M. Also the floor inequality gives

    M >= (n-k)/A - K >= n/(2A),

where the second inequality is exactly n >= 2k+2AK. In addition
(n-k)/(AK) >= 2, so M >= 2K >= 2. Thus m>=2 and every ell_i>=2. The state
count is exactly m+sum_i ell_i=n, with no padding or loss of connectivity.

For i<j, let d divide both 1+iM and 1+jM. Then gcd(d,M)=1, and d divides
(j-i)M, hence d divides j-i. If d>1, a prime p dividing d has p<=j-i<=k-1,
so p divides K=k! and M, a contradiction. The ell_i are pairwise coprime.
Therefore

    L = product_(i=1)^k (1+iM) >= k! M^k,
    (m+1)L >= k! M^(k+1) >= c_k n^(k+1).

Combining with Lemmas 1--3 proves the stated lower bound for every n>=N_k.

## Upper bound, reproduced only to make the resolution self-contained

The upper-bound order and the tightness question are due to Kiefer and
Ryzhikov, MFCS 2025, Section 9. Here is the elementary upper argument.

List the original states q_1,...,q_n. Suppose a prefix u has already killed
the first i-1 original rows. If q_i.u is empty, do nothing. Otherwise its
image and all its continuations are nonempty subsets of size at most k until
they die: they are images of the same original singleton under longer words.
A killing continuation exists because a global mortal word exists. In a
shortest such continuation, no nonempty subset is repeated, as deleting the
intervening factor would give a shorter one with the same endpoint. Its length
is therefore at most D=sum_(j=1)^min(k,n) binom(n,j).

There are at most n rows to kill; a dead row remains dead under extensions.
This gives a global mortal word of length at most nD. Finally D<=n^k:
encode a nonempty subset by listing its elements in increasing order and
padding to length k by repeating its maximum. The encoded tuple determines
the original subset, so this is an injection into Q^k. Thus M_k(n)<=n^(k+1).

## Proof dependencies, attacks and limitations

The proof uses only elementary finite-set transitions, the subset shortest-
path argument, and the displayed elementary coprimality argument. There is
no dependence on unambiguity, finite ordinary-arithmetic matrix monoids,
an unproved number-theoretic prime distribution, or a computation covering
unbounded parameters. No mathematical gap is currently known to the proposer.

evidence/research-check.py independently constructs relations without importing
the supervisor checkers. It replays all nine frozen certificates, exhausts all
singleton and global subset closures in 18 fixed cases, checks the potential
on every quotient configuration and a-run residue in those cases, and executes
the mortality strategy. Exact output is evidence/research-check-results.json.
The complete finite domains support reproducibility, not the infinite proof.

Novelty and significance remain for a fresh referee. The explicit comparison
and current-source limitations are in evidence/research-literature.md. This
packet asserts a complete proposed proof of the frozen fixed-k question;
it does not assert external peer review, acceptance, or STOC-level quality.
