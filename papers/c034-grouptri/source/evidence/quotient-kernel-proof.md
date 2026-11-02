# Fully charged quotient–kernel lifting argument

Research pass 2, proposer job `c034-grouptri-research-d92d3d43a90d`.
This is mathematical research evidence, not a manuscript or an accepted audit.
The immutable target is `source.md`; no promise or dimension restriction is added.

## Statement and explicit prior dependency

For every fixed integer M>=2 there is a deterministic, uniform classical
algorithm deciding Exact Triangle over every compactly presented finite abelian
group of exponent dividing M and order at most n^c, for every fixed c>0, in
O_(M,c)(n^(3-delta_M) polylog(n+2)) charged word-RAM operations. The positive
constant delta_M is independent of c. All complete instances, preprocessing,
coordinate operations, exceptions, graph construction and recursive calls count.

The external algorithm used is Majdoddin, arXiv:2610.17420v1, Theorem 21.3
and Corollary 21.7(a), with the legitimate H(1/14,0.077) instantiation from
Corollary 9.1(b) and Section 16. For each fixed prime p it supplies deterministic
elementary-group detection in O_(p,C)(b^(3-0.0055) log^6 b) for p^d<=b^C,
with the saving independent of C. We conservatively use epsilon_0=1/1000,
absorbing the logarithms into the slack. Its fixed-p size restriction is
satisfied above a p-dependent constant; below it, brute force suffices.
The algorithm's explicit row construction uses d, not a supplied bound C;
the same procedure works for all fixed C. This dossier relies on this stated
primary theorem; it does not purport to formally verify all of its matrix
dependencies. Its full Theorem 21.3 proof and the Corollary 9.1 instantiation
were inspected in passes 1 and 2.

For prime M set delta_M=epsilon_0. For composite M choose its least prime
divisor p, put q=M/p>=2, and define

    theta=delta_q/12, alpha=theta/6,
    delta_M=epsilon_0*delta_q/144.

These rational positive constants depend only on M. A finite induction on M
will prove the statement. Equivalently, if Omega(M) counts prime factors with
multiplicity, delta_M=(1/1000)*(1/144000)^(Omega(M)-1). For example,
delta_4=1/144000000 and delta_8=1/20736000000000. These conservative exponents
are existence bounds, not practical speed claims. No randomized step is needed.

## Input and signs

Embed a coordinate Z_m (m|M) into Z_M by x -> (M/m)x. This is injective
and preserves zero sums. The resulting group is Z_M^d with d<=c log_2 n;
its order is at most n^(c log_2 M). The embedding and all reading cost
O_(M,c)(n^2 log(n+2)). Never enumerate the label group.

Write the three input labels as A_ik on U--X, B_kj on X--V, and -C_ij
on U--V. Thus the original condition is A_ik+B_kj-C_ij=0 modulo M in
every coordinate. Reducing coordinates modulo p gives a_ik,b_kj,c_ij in
Q=F_p^d. Let W_ij={k:a_ik+b_kj=c_ij}. Parts can have unequal sizes <=n;
all bounds below use their common upper bound n. Empty parts immediately
give NO. If d=0 the original labels are all zero and a nonempty complete
input gives YES. For n<=1, directly read/check its at most one triangle.

## Capped lists and deterministic hitting

For n>=2 set s=2^floor(theta*floor(log_2 n)), an integer in [1,n],
L=floor(n/s), T=L+1, and r=s^2. Then s=Theta(n^theta), L=Theta(n/s),
and T=O(n^(1-theta)). The rational exponents are implemented by integer
logarithms and rational arithmetic on O(log n)-bit integers, without numerical
rounding assumptions. In the capped-listing proof use this T rather than
ceil(n^(1-theta))+1; its proof uses only T=O(n^(1-theta)) and is unchanged.

Apply `capped-listing-proof.md` to Q with cutoff exponent alpha and arbitrary
fixed child order. Obtain exactly min(|W_ij|,T) distinct middle witnesses per
pair. The charged time is

    O_(M,c)(n^(3-epsilon_0*theta/6) polylog(n+2)).               (1)

The masks append three F_p coordinates and all detector calls have side
b>=n^alpha up to constant rounding. Hence their input dimension is bounded
by one fixed constant times log b, even when c is large. The output count
is O(n^3/s). If a list has size <T it is complete and |W_ij|<=L: put every
such triangle into an exception list R_few. All other pairs are called heavy.
For each heavy pair its stored set S_ij has exactly L+1>n/s elements.

Greedily hit the sets S_ij by middle vertices: repeatedly take a vertex in
the most currently unhit sets and remove every set it hits. If m sets
remain, their total incidences exceed mn/s, so some vertex hits >m/s sets
(there are at most n middle vertices). This yields at most O(s log(n+2))
chosen vertices H, including the s=1 boundary. Assign each heavy pair the
first chosen hitter h_ij in its stored set, so h_ij is an actual witness.

For completeness, deterministic implementation uses incidence lists and a
max heap of vertex degrees with deterministic tie breaking. When a set is
first hit, delete its incidences, decrement the corresponding degrees, and
record its pivot. Each incidence is deleted once. Heap initialization,
degree updates, set deletion and pivot recording take
O((n^3/s+n^2+n) log(n+2)) operations. This is not cubic preprocessing.

## Frequency tables and the exact decomposition

For every h in H and k in X, sort the values b_hj-b_kj indexed by j in V,
retaining the list of indices for each distinct value. Define F_hk to contain
exactly the values occurring more than n/r times; it has fewer than r
elements (at most r is sufficient). Give these distinct values a canonical
lexicographic order, with t_hk,l its l-th element when defined, 1<=l<=r.
Coordinates, comparisons and sorts cost polylog(n+2) each. All tables cost
O(|H| n^2 polylog(n+2)) time and storage.

For each (h,i,k), look up v=a_ik-a_ih. If v is not in F_hk, its table list
has at most n/r indices j. Scan exactly this list and retain (i,k,j) in
R_low only when (i,j) is heavy and h_ij=h. The latter condition is deliberate:
it prevents copies from different pivots. With that condition and the matched
value, a_ik+b_kj=a_ih+b_hj=c_ij automatically, since h is the pair's witness.
An explicit coordinate check can also be made at the same charged cost.
The scan cost and number retained are bounded by

    O(|H| n^2 + |H| n^3/r) polylog(n+2)
      = O(s n^2+n^3/s) polylog(n+2).                          (2)

For every (h,l) with h in H and 1<=l<=r form a masked tripartite graph
P_hl on the ORIGINAL vertex sets. Its present edges are precisely

    U_i V_j: (i,j) is heavy and h_ij=h;
    U_i X_k: t_hk,l is defined and a_ik-a_ih=t_hk,l;
    X_k V_j: t_hk,l is defined and b_hj-b_kj=t_hk,l.

There are at most |H|r=O(s^3 log(n+2)) such graphs. Empty graphs can either
be skipped by scanning their edges or be encoded and queried; both are charged.

Every triangle in a piece is a quotient-zero triangle. Conversely, consider
a quotient-zero triangle (i,k,j). If its pair is light it lies in R_few.
Otherwise use its unique assigned h=h_ij and v=a_ik-a_ih=b_hj-b_kj.
If v is low frequency it lies in R_low. Otherwise it occurs in exactly one
slot l of F_hk and lies in exactly P_hl. No triangle occurs in two cases
or two pieces. Thus the following is an equality of disjoint triangle sets:

    {quotient-zero triangles}=R_few disjoint-union R_low
                                 disjoint-union union_h,l Triangles(P_hl).

This construction uses equality and group subtraction only. Its validity over
Q does not require Q to have an order compatible with addition. Lexicographic
order is only a deterministic representation for dictionary/sort operations.
This is a reconstruction of CVX23 Theorem 5.1's combinatorial decomposition,
with capped lists replacing its cubic fresh-input witness sorting.

## Edgewise potentials and genuine kernel instances

Fix a piece P_hl. Set alpha_i=a_ih, beta_j=b_hj, and tau_k=t_hk,l when
defined, otherwise tau_k=0. On every PRESENT edge respectively one has

    a_ik=alpha_i+tau_k,
    b_kj=beta_j-tau_k,
    c_ij=alpha_i+beta_j.                                     (3)

The last identity follows from the assigned actual witness h. If tau_k was
undefined, both edge kinds incident to X_k are absent, so its arbitrary value
causes no present-edge assertion. These are edgewise identities, stronger
than the assertion that all triangles in the piece are quotient-zero.

Lift alpha_i,beta_j,tau_k into Z_M^d by their coordinate representatives
0,...,p-1, denoting the lifts u_i,v_j,z_k. No homomorphic section is used.
On present edges compute in Z_M^d

    A'_ik=A_ik-u_i-z_k,
    B'_kj=B_kj-v_j+z_k,
    C'_ij=C_ij-u_i-v_j.

By (3), every coordinate of these residues is divisible by p. On any present
triangle, exact cancellation gives

    A'_ik+B'_kj-C'_ij=A_ik+B_kj-C_ij in Z_M^d.                (4)

The map from p Z_M to Z_q sending a residue p x to x mod q is a well-defined
isomorphism of additive groups. Consequently the transformed triangle is
zero in Z_q^d exactly when the original triangle is zero in Z_M^d.

To query the inductive COMPLETE-input algorithm, append three Z_q coordinates
and encode the three plus-sum edge labels as A'/p, B'/p, -C'/p. A present
edge has zero markers. An absent edge has arbitrary zero original coordinates
and marker 1 only in its own edge-kind coordinate. A triangle has exactly one
edge of each kind, so zero in the three marker coordinates is equivalent to
all three edges being present, for every q>=2, including q=2. Thus there are
no sentinel cancellations or spurious triangles. The completed group is
Z_q^(d+3), still of exponent q. Each materialized query has at most n vertices
per part and q^(d+3)<=n^C for a fixed C depending on M,c (n>=2).

All pieces retain the same n; the induction never applies its group-order
promise to a tiny side with the original large dimension. Along an induction
branch only three coordinates per layer are added, and its depth is bounded
by the prime-factor count of the fixed M. All coordinates and sizes are
explicit; no succinct-graph oracle is assumed.

## Decision algorithm and complete cost induction

Check each triangle in R_few and R_low in the ORIGINAL group. If any is zero,
return YES. Otherwise construct each P_hl, materialize its complete encoded
kernel instance as above, and run the inductive algorithm at exponent q.
Return YES if any call does; if none does return NO. No all-edges kernel
algorithm is needed. Completeness follows because every original-zero triangle
is quotient-zero and belongs to exactly one exception/piece. Soundness follows
from checking exceptions directly and from (3)--(4) plus the three markers.

For primes the algorithm is the actual elementary backend. For composite M,
all operations have the following envelope, with constants/polylogs depending
only on fixed M,c and the already established algorithms:

    capped listing:        n^(3-epsilon_0*theta/6) polylog n;
    lists/hitting/R_few:   (n^3/s+n^2) polylog n;
    tables/R_low:          (s n^2+n^3/s) polylog n;
    materialized graphs:  s^3 n^2 polylog n;
    ALL kernel calls:     s^3 n^(3-delta_q) polylog n.

The materialized-graph line charges every edge of every piece, all potentials,
modular subtraction, division on present edges, all absence markers and padding.
It is intentionally larger than the compact representation charge in CVX23.
The input/setup/control/output charges are included; storing or streaming
exceptions and streaming one piece at a time is sufficient. Memory and address
sizes are polynomial in n; word sizes remain Theta(log n). The capped routine's
subinstance word size differs by only the fixed factor 1/alpha. Coordinatewise
operations cost O_(M,c)(log(n+2)); no unit-cost long integers are required.

As s=Theta(n^theta), the respective exponent savings are

    epsilon_0*theta/6, theta, at least 1-theta,
    1-3theta, delta_q-3theta=3delta_q/4.

Here 0<delta_q<=epsilon_0<=1, theta=delta_q/12, and the smallest displayed
saving is epsilon_0*delta_q/72. Taking half of it, namely delta_M defined
above, absorbs every fixed polylogarithm if desired. In particular the claimed
bound, even without its allowed polylog factor after adjusting constants,
holds with a strictly positive saving independent of c. Rounding s,L,T and
the octree cutoff changes only fixed multiplicative constants. Finite small-n
ranges in the prime backend and cutoff proof use direct enumeration, with
constants depending only on the fixed parameters. Induction terminates at
a prime; it never requires a masked trivial-group call. Original trivial
groups and empty inputs were handled explicitly.

This proves the claimed algorithm given the stated, inspected prior elementary
backend. No unproved new matrix primitive, preprocessing universe, sparsity
promise, all-edges kernel oracle, favorable input distribution or randomized
success condition is inserted. The argument resolves the mathematical scope
of source.md as a proposed proof; fresh correctness, novelty and value review
is still required before any publication gate can pass.

## Prior-work and significance boundary

The capped-listing principle and CVX23 decomposition are prior tools, not claimed
new results. The proposed substantive delta is their use to compute polynomially
few quotient pieces with explicit gauge potentials, eliminate nonhomomorphic
lift carries edgewise, and close a fully charged induction through every fixed
exponent. The nearest source only handles elementary groups and two restricted
p^2 cases, explicitly leaving all Z_4^d and the all-M question open. A fresh
referee must decide whether this extension principle is substantive rather
than a routine consequence already present in prior work. No STOC significance
or submission-readiness judgment is made by this proof dossier.

Primary references: [Majdoddin](https://arxiv.org/abs/2610.17420), Theorem 21.3,
Corollaries 9.1 and 21.7, Propositions 21.9--21.10, Open Problem 21.12;
[Chan--Vassilevska Williams--Xu](https://arxiv.org/abs/2303.14572), Theorem 5.1;
[Sheffield--Vassilevska Williams--Xi](https://arxiv.org/abs/2608.19092), established
generic detection/listing relationships. Live records reopened 2026-11-02
display v1 only. Bounded exact-phrase searches located no full equivalent
closure theorem; that is not an exhaustive priority certificate.

## Gap and verification record

Known unresolved internal proof obligations: none identified by the proposer
after the above derivation and exact semantic checks. This is the proposer's
gap list, not a fresh referee finding. Reliance on the explicitly cited prior
elementary backend remains; no new unproved backend is assumed. Current novelty,
whether the extension has substantive independent value, and correctness of
the full argument await the required fresh review. No mathematical acceptance,
innovation acceptance, venue assessment, or publication authorization is claimed.

`test_quotient_kernel.py` and `quotient-kernel-tests.json` check the exact
disjoint decomposition, all present-edge potentials, every encoded triangle
against original zero sums, repeated lifting with inherited markers, and the
rational exponent ledger. Their bounded domains and brute-force backends are
explicit in the JSON. They supplement rather than establish the infinite proof.
