# Proposed full-scope resolution: randomized divisor-profile hashing

Proposer job: c034-group3sum-research-3974e7a3f8f0.
This is a research proof packet for a fresh referee, not an accepted paper.
The immutable source.md and problem.md control the original scope. No manuscript,
PDF, acceptance report, or venue assessment is created here.

## Statement and explicit dependency

For every fixed integer M>=2 there is a uniform classical randomized algorithm
solving the full original three-list zero-sum problem over every compactly given
finite abelian group of exponent dividing M and order at most n^c. Its worst-case
charged running time is O_(M,c)(n^(2-delta_M) polylog(n)), where

    C=ceil(log_2 M), eta=min(1/18,1/(8C)), gamma=63/1000,
    delta_M=eta*gamma/2 > 0.

The algorithm never returns a false witness; on a positive fixed input it returns
a witness with probability at least 3/4. A negative input always returns NO.
Every random draw, aborted trial, subinstance, and witness scan is charged.
The saving is independent of c. The polylogarithm exponent can depend on M.

The algorithm uses the EXISTING thin-product algorithm of Alman and Vassilevska
Williams, arXiv:2610.06783v1, Corollary 26: for 2<=D<=N^(1/18) and at most
N^2/sqrt(D) prescribed entries of a product of an N-by-D and D-by-N integer
matrix, compute those entries in O(N^2/D^gamma) word operations. We use only
0/1 inputs and test positivity. The exact theorem/interface was checked in the
primary HTML, Section 4.1, and agrees with Lemma 2.2 of the frozen Majdoddin
source. This is a cited algorithmic theorem, not a new assumed oracle. Its full
matrix-algorithm proof is not independently reproved or formalized in this pass.
All its dimension, query, input-size and operation-model hypotheses are checked
below. A polylogarithmic bit simulation is harmless.

## 1. Normalization and easy regimes

Remove duplicate vectors in each list and retain original indices for recovery.
An empty list gives NO. Embed each coordinate Z_m, m|M, into Z_M by x ->(M/m)x.
This is injective and additive. We now work in G=Z_M^r, r=O_c(log n), of order
at most n^(c log_2 M). Thus the normalization preserves the original polynomial
order model and gives only O_(M,c)(polylog n) arithmetic/evaluation overhead.
The zero-dimensional group is handled directly. Write S_i for these ORIGINAL
normalized lists, before any later profile restriction, and |S_i|<=n.

If min_i |S_i|<=sqrt(n), enumerate pairs from that list and any other list and
look up the negative sum in the third sorted list. This costs O_(M,c)(n^1.5
polylog n). Below assume every original list has size >sqrt(n). Also assume
n>=16 and R defined below is >=M. The excluded n are bounded by a constant
depending only on M, and are solved by exhaustive pairs; their entire cost is
absorbed into O_M(n^(2-delta_M)).

## 2. Every divisor profile, with original coset sizes

Let D_M={d>=2:d|M} and L=|D_M|. For each d in D_M put

    H_d=G[d]={x:dx=0}=(M/d)G.

The quotient map is coordinate reduction modulo M/d; for d=M it is trivial.
For x in S_i let c_(i,d)(x)=|S_i intersect (x+H_d)| and let
s_(i,d)(x) be the largest power of two <=c_(i,d)(x). Partition each list by
the full vector of these L dyadic values. There are at most (1+floor(log_2 n))^L
nonempty profiles per list, and at most this quantity cubed subinstances.
Build the coset counts and profiles by sorting in O_(M,c)(n polylog n).
Every original triple lies in exactly one profile subinstance.

Fix one nonempty subinstance (U_1,U_2,U_3). Its profile values s_(i,d) are
constants; put s_d=min_i s_(i,d). Two facts, valid even when profile restrictions
FRAGMENT original cosets, are essential:

(a) The number T_d of triples in U_1 x U_2 x U_3 with sum in H_d is <2s_d n^2.
Choose a list attaining s_d. Each choice of the other two elements determines
one coset modulo H_d for its member, which has fewer than 2s_d elements in its
ORIGINAL list. Intersecting with U_i cannot increase this number.

(b) The number of original H_d cosets represented in U_i is <=n/s_(i,d)<=n/s_d.
Each such original coset contains at least s_(i,d) members of S_i, regardless
of how few remain in U_i. These original cosets are disjoint.

No claim that a fragmented U_i-coset itself has size >=s_(i,d) is used.
For d=M, s_M>sqrt(n)/2>=n^(1/4).

## 3. Computable maximum-slope choice

Set h=floor(eta log_2 n), R=2^h and

    alpha=1/2-gamma/4=1937/4000, sigma=floor(R^alpha).

For large enough n, sigma is between R^alpha/2 and R^alpha; also
n^eta/2<=R<=n^eta. These are computable with integer comparisons: eta and alpha
are fixed rationals. No real-number oracle is used.

Let ell be the least nonnegative integer satisfying, for EVERY d in D_M,

    d^ell * sigma >= s_d * R.                              (1)

Choose any e in D_M that violates (1) at ell-1. Such an e exists since ell>=1.
Then

    e^ell < e*s_e*R/sigma.                                 (2)

This is a discrete maximum-slope certificate and uses only O_M(log n) small
integer-power comparisons; all integers have O_M(log n) bits. Choose any prime
p|e. Put q=floor(log_p R), D=p^q, and k=ell-q. We have

    R/M <= R/p < D <= R,    q>=1.

Also ell>=log_M(s_M R/sigma)>=log_M(n)/4, while
q<=eta log_2 n<=log_M(n)/8. Consequently k>=0 (indeed ell>=2q).
Finally ell=O_M(log n), since s_d<=n and d>=2.

## 4. Random homomorphisms and the elementary middle group

Choose ell independent rows u_j uniformly in Z_M^r. Define

    pi(x)=(x mod H_e,
           (<u_j,x> mod M)_(j<=k),
           (<u_j,x> mod (M/p))_(k<j<=ell)),
    K(x) =(x mod H_e, (<u_j,x> mod M)_(j<=ell)).

These are homomorphisms; K determines pi. The quotient component has the
compact residue-vector representation from section 2, even if its order is
large. Every evaluation costs O_(M,c)(log^2 n) charged operations.

For x in ker pi, the quotient and the first k coordinates of K(x) vanish;
each remaining coordinate is a multiple of M/p. Therefore K(ker pi) is
contained in the explicitly represented subgroup

    B={0} x {0}^k x ((M/p)Z_M)^q ~= F_p^q, |B|=D.

Use all of B, even if the actual image is smaller. Split its q coordinates
as B_1 x B_2 of dimensions ceil(q/2) and floor(q/2).

Within ONE original H_e coset, the first k rows have at most e^k joint values.
Each reduced final row has at most e/p values on H_e, since p|e. Thus the
number of pi labels in that coset is at most

    H=e^k(e/p)^q=e^ell/D < M^2*s_e/sigma,                  (3)

using (2) and R/D<=M. By fact (b), each U_i has at most M^2*n/sigma nonempty
pi classes. Cutting each class into blocks of size at most sigma gives at most

    (M^2+1)*n/sigma                                      (4)

blocks, deterministically for EVERY choice of random rows.

## 5. All order layers and an analyzable potential

A fixed vector v of additive order d in Z_M^r has <u,v> uniform on the unique
subgroup of Z_M of order d. Indeed this row map is a homomorphism and its image
is the ideal generated by the coordinates of v, whose order is d; all fibers
have equal size. Reducing modulo M/p changes that image size to d/gcd(d,p).
For v in H_e of nonzero order d, necessarily d|e, so independent rows give

    Pr[K(v)=0]=d^(-ell),
    Pr[pi(v)=0]=gcd(d,p)^q * d^(-ell) <= D*d^(-ell).       (5)

Vectors outside H_e never survive either quotient component. Let N_d be the
number of subinstance triples of EXACT sum-order d. By (a), N_d<=T_d<2s_d n^2.
Let Z0 be the number of true solutions, Zpi the number with pi(sum)=0, and F
the number with nonzero sum and K(sum)=0. From (1) and (5),

    E[F] <= sum_(d|e,d>1) 2s_d n^2 / d^ell
          <= 2L*sigma*n^2/R,
    E[Zpi-Z0] <= D*E[F] <= 2L*sigma*n^2.                 (6)

Here both expectations are over the same rows; independence BETWEEN the two
random variables is unnecessary. If desired, the nonnegative proof potential
is (Zpi-Z0)/(sigma*n^2)+F*R/(sigma*n^2), whose expectation is <=4L.
It need not be evaluated by enumerating triples: the operational stopping
rules below are computable and protect the total time on every random path.
Markov and a union bound show that with probability at least 5/6, simultaneously

    Zpi-Z0 <=24L*sigma*n^2,
    F <=24L*sigma*n^2/R.                                (7)

Because lists are sets, Z0<=n^2. Thus on this event Zpi<=n^2+24L*sigma*n^2.
Mixed prime powers are already included in (5)-(6); no CRT-factor enumeration,
recursive call, or uncharged carry-target computation is required.

## 6. Fully charged block/probe construction and witness recovery

For each block b of lists 2 and 3, choose representative z_b. List probes
Q=(x_1;b_2,b_3) whose labels sum to zero under pi, by enumerating (x_1,b_2)
and looking up the required block-label list in list 3. The elementary ceiling
bound for numbers of blocks per class gives

    |P| <= n*C_2 + 2n^2/sigma + Zpi/sigma^2,             (8)

where C_2 is the number of nonempty pi classes in U_2. This follows by expanding
ceil(a/sigma)ceil(b/sigma)<=(1+a/sigma)(1+b/sigma) on nonempty classes and
summing. Together with (3)-(7), on the good event

    |P| <= A*n^2/sigma,  A=M^2+3+24L.                   (9)

Abort this subinstance trial and return NO if listing would exceed
ceil(A*n^2/sigma) probes. This is detected BEFORE doing more work. By (4), the
outer enumeration costs O_M(n^2/sigma) plus the capped output. Sort/deduplicate
query positions in polylogarithmic time per position; retain their probe lists.

Here is the support product explicitly, also checked against Majdoddin Lemmas
19.6-19.7. Put b0=M^2+1, g0=M(A+b0+3), g'=ceil(g0*n/sigma), and
N=g'*p^ceil(q/2). Left vertices are (b_2,mu_1), right vertices (b_3,mu_2),
padded to N on both sides; the middle is B. Define the 0/1 matrices by membership:

    X[(b_2,mu_1),lambda]=1 iff some x_2 in b_2 satisfies
       K(x_2)-K(z_b2)+(mu_1,0)=lambda,
    Y[lambda,(b_3,mu_2)]=1 iff some x_3 in b_3 satisfies
       -(K(x_3)-K(z_b3))-(0,mu_2)=lambda.

All these differences lie in B. Probe Q is queried at the unique pair with
(mu_1,mu_2)=K(x_1)+K(z_b2)+K(z_b3), which is in B by its pi-label condition.
The product entry is positive exactly when some pair in the two blocks has
K(x_1+x_2+x_3)=0: equate the two expressions for lambda. Thus every true witness
is in a positively answered probe. Each triple with pi(sum)=0 belongs to exactly
one probe, so at most F positive probes contain no true witness.

Scan a positive probe by enumerating x_2 in b_2 and looking up -x_1-x_2 in
sorted b_3, with original vector arithmetic. A successful scan returns original
indices. A scan costs O_(M,c)(sigma polylog n). Stop and return NO on this trial
if the number of failed scans would exceed ceil(24L*sigma*n^2/R); allow one
additional successful scan. On event (7) neither cap prevents finding a witness
if one exists. A returned witness is always verified against the original lists.

## 7. Legal matrix call and worst-case running time

Since sigma<=sqrt(R), D>=R/M and g0>=sqrt(M),

    N>=g0*n*sqrt(D)/sigma>=n.

Therefore D<=R<=n^eta<=N^(1/18). Also D^(1+gamma)<=N since
eta<=1/18 and gamma<=1/2. The query cap is at most (A+1)n^2/sigma, whereas

    N^2/sqrt(D)>=g0^2*n^2*sqrt(D)/sigma^2
                >=(g0^2/sqrt(M))*n^2/sigma
                >=(A+1)*n^2/sigma.

Thus EXACTLY ONE existing thin-product call suffices per nonaborted profile
subinstance; both the rectangular shape and the prescribed-entry bound hold.
Furthermore p^ceil(q/2)<=sqrt(pD), g'<= (g0+1)n/sigma, and D is within a fixed
factor of R. The call costs

    O_M(N^2/D^gamma)
       =O_M(n^2 R^(1-gamma)/sigma^2)
       =O_M(n^2 R^(-gamma/2)).                          (10)

Writing the dense 0/1 matrices costs O(ND), at most O(N^2/D^gamma) by
D^(1+gamma)<=N. Setting their nonzero entries costs O(n*p^ceil(q/2) polylog n),
which is within (10) as well. Probe listing, storing and sorting cost
O_M(n^2/sigma polylog n), within (10) because gamma<=1/2 implies
1/2-gamma/4>=gamma/2. Capped failed scans and one successful scan cost

    O_(M,c)((sigma^2*n^2/R+sigma) polylog n)
      =O_(M,c)(n^2 R^(-gamma/2) polylog n).              (11)

Row generation/evaluation, class sorting, label arithmetic, and recovery use
O_(M,c)(n polylog n) additional time, dominated by this bound. Every trial has
these caps even for adverse random rows. Multiply (10)-(11) by at most
(1+floor(log_2 n))^(3L) subinstances. Since R>=n^eta/2, the total is the stated
O_(M,c)(n^(2-eta*gamma/2) polylog n). There is no exponent dependence on c.

## 8. Random-bit cap and fixed-input correctness

Uniform Z_M coefficients can be generated using b=ceil(log_2 M) fair bits and
rejecting b-bit integers >=M. Each accepted coefficient takes at most two
attempts in expectation. For each subinstance cap the total number of attempts
at 24*r*ell, returning NO on that trial if exceeded. Coupling to the unlimited
iid uniform-row experiment, Markov bounds this additional failure probability
by 1/12. Its time is O_M(r*ell), regardless of outcomes. Together with the two
1/12 tails in (7), failure probability is at most 1/4.

If the input has a witness, fix one before drawing randomness. Its deterministic
profile subinstance is processed unless an earlier verified witness was found.
On that fixed subinstance the two listing/scanning caps and the generation cap
all succeed with probability at least 3/4, and its witness is found. No union
bound over all subinstances is needed for existential detection. For a negative
input, every return is NO since YES requires a directly verified zero-sum triple.
This proves a bounded-time one-sided-error full-scope algorithm. Optional
independent repetitions reduce error, at a constant cost.

## Scope, prior work, value and limits

Majdoddin's Theorem 19.17 already handles all exponent-dividing-p^2 groups;
its Open Problem 19.26 explicitly leaves general bounded exponent and suggests
layer induction. We do not claim that suggestion, elementary groups, or Z4 x F2
as new. The proposed new step is simultaneous ORIGINAL-coset divisor profiles
and the maximum-slope certificate (1)-(2), allowing a single elementary-middle
support call for arbitrary mixed-prime/higher-power exponents. This controls
fragmentation, all order layers, aggregate profile costs, computable caps and
witness recovery. It avoids any assumption of an integer-like convolution hash
on torsion groups. It sacrifices determinism and some exponent size; randomness
is expressly allowed by the immutable original question.

A successful fresh verification would settle the full source question and
supply the general group primitive anticipated in source Remark 20.6. No separate
coordinatewise theorem is claimed in this packet. Source originality and STOC
significance require fresh critical assessment; no assessment is invented here.
Known gaps in the proposed argument after this pass's self-check: none identified.
This is a proposer statement, not independent acceptance. Finite exact checks
are regression evidence for the algebra and interfaces, not proof of asymptotics
or novelty. See evidence/research-pass1-literature.md and divisor-hash-tests.json.
