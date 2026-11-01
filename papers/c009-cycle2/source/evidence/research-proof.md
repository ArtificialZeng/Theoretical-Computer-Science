# Complete proposed resolution: all 2-subdivided alternating even cycles

Research dossier, not a manuscript or mathematical acceptance. Proposer job: c009-cycle2-research-347a4f87d1ce. Full original scope is `source.md`, interpreted in `problem.md`. The following is an analytic proof proposed for fresh correctness, novelty and value review. Finite checks are supplemental only.

## 1. A rank-one symmetric-part square bound

Let n>=1, let u be any real unit vector, let P=uu^T, let B be any real skew-symmetric n-by-n matrix, and set T=P/2+B. Then

    ||T^2||op >= 1/4.

No nonnegativity, size bound, regularity or smallness of B is required. Write b=Bu, a=<b,b>, and D=(I-P)B(I-P) restricted to u-perp. Skew-symmetry implies b perpendicular to u, D^T=-D and, in the orthogonal decomposition R u plus u-perp,

    T = [ 1/2    -b^T ]
        [ b       D   ].

Put x=u+2b, so ||x||^2=1+4a>0. Multiplying twice by T^T, first

    T^T x = (1/2+2a)u - b - 2Db,

and then

    (T^T)^2 x = u/4 - (1/2+2a)b + Db + 2D^2b.

The first coordinate in the second equality is exactly 1/4, since <b,Db>=0. Furthermore

    <b,Db>=<Db,D^2b>=0,    <b,D^2b>=-||Db||^2.

Consequently, by direct expansion,

    ||(T^T)^2x||^2 - ||x||^2/16
      = 2a^2 + 4a^3 + (3+8a)||Db||^2 + 4||D^2b||^2.        (R)

Every term is nonnegative. For Q=T^2(T^T)^2=(T^2)(T^2)^T, the Rayleigh principle gives

    lambda_1(Q) >= 1/16 + [2a^2+4a^3+(3+8a)||Db||^2+4||D^2b||^2]/(1+4a)
                >= 1/16 + 2a^2/(1+4a).                  (1)

In particular ||T^2||op=sqrt(lambda_1(Q))>=1/4. This proof includes b=0, D=0 and n=1 (empty blocks are zero).

## 2. Exact cycle normalization and the original problem

Let A in [0,1]^(n by n) satisfy A+A^T=J, including A_ii=1/2. Set u=(1,...,1)^T/sqrt(n), B=(A-J/2)/n and T=A/n=P/2+B. For every integer ell>=1, let H_ell be the oriented cycle on 4ell cyclic vertices whose successive clockwise signs are (++--) repeated ell times. Summing the weights of all vertex maps around the cycle is the matrix-product trace:

    t_Hell(A) = tr[(T T T^T T^T)^ell]
              = tr[Q^ell].                              (2)

Indeed a clockwise edge contributes T_ij, and a counterclockwise edge contributes T_ji=(T^T)_ij; the normalization n^(-4ell) is already incorporated in the 4ell factors T. Maps are arbitrary, including coincidences. This gives exactly the weighted density in the source definition, without an asymptotic or injectivity error.

Q is positive semidefinite, so all its eigenvalues are nonnegative. Applying (1), for every n>=1 and every ell>=1,

    t_Hell(A)=sum_j lambda_j(Q)^ell >= lambda_1(Q)^ell >= 16^(-ell).

This is the global tournament Sidorenko lower bound. It implies the complete original LTS question affirmatively for EVERY ell>=1: one may choose any positive epsilon_ell, because the inequality holds even without the spectral-smallness condition. No cycle length or host dimension was fixed.

## 3. Quantitative forcing, with every dimension accounted for

The following strengthening is useful additional evidence of value, rather than necessary for the original resolution. Let beta=||B||op and E=tr(Q^ell)-16^(-ell). Then

    E >= 16^(-ell) beta^(4ell).                           (3)

To prove it, set y=b/2+Db and R=D^2-bb^T. Squaring the block matrix for T gives

    T^2 = [ 1/4-a     -b^T/2-b^TD ]
          [ b/2+Db    D^2-bb^T   ].

The compression of Q to u-perp is yy^T+R^2. Set K=-R=-D^2+bb^T, so K>=-D^2>=0. If D is nonzero, the top eigenvalue ||D||op^2 of -D^2 has multiplicity at least two: a real skew matrix is an orthogonal sum of 2-by-2 rotation blocks and zero blocks. By the min-max principle, the second eigenvalue of K is at least ||D||op^2; the second eigenvalue of K^2=R^2 is therefore at least ||D||op^4. Adding yy^T and passing from a compression to Q cannot decrease the corresponding ordered eigenvalue. Thus

    lambda_2(Q) >= ||D||op^4.                            (4)

An equivalent direct min-max check avoids any concern about squaring a Loewner inequality: on the at-least-two-dimensional top eigenspace F of -D^2, one has <Kz,z> >= ||D||op^2||z||^2, hence ||Kz||>=||D||op^2||z|| by Cauchy-Schwarz. Thus <Qz,z> = <(yy^T+K^2)z,z> >= ||D||op^4||z||^2 for z in F, which directly proves (4). No assertion K^2>=D^4 in Loewner order is needed.

This argument is used when D is nonzero, which entails dim(u-perp)>=2. If D=0 and n>=2, (4) is just positivity; if n=1, B=0 and (3) is immediate. Hence no nonexistent second eigenvalue is used in dimension one.

By (1), convexity of s^ell on s>=0 (or its binomial expansion), and (4),

    E >= ell*16^(-(ell-1))*2a^2/(1+4a),
    E >= ||D||op^(4ell).                                (5)

The second bound follows from tr(Q^ell)>=lambda_1(Q)^ell+lambda_2(Q)^ell and lambda_1(Q)>=1/16; the first follows by discarding every other eigenvalue.

For a weighted tournament, every entry of B has absolute value <=1/(2n). Thus beta<=||B||HS<=1/2 and a=||Bu||^2<=1/4. Also beta<=||D||op+sqrt(a), since B is the sum of the extended compression D and the off-diagonal skew block [0,-b^T;b,0], whose norm is sqrt(a).

If ||D||op>=beta/2, (5) yields E>=beta^(4ell)/16^ell. Otherwise sqrt(a)>beta/2, and 2/(1+4a)>=1 gives

    E >= ell*16^(-(ell-1))*a^2
       >= ell*16^(-ell)*beta^4
       >= 16^(-ell)*beta^(4ell),

using ell>=1 and beta<=1. This proves (3). In particular equality in the density lower bound holds precisely when B=0 (A=J/2). If cut(A-J/2) means the maximum absolute unnormalized rectangle sum, then cut(A-J/2)/n^2<=beta by Cauchy-Schwarz, hence beta<=2 E^(1/(4ell)) is a dimension-free forcing modulus.

## 4. Sharpness of the exponent

For n=3 let

    K = [ 0  1 -1 ]
        [-1  0  1 ]
        [ 1 -1  0 ],        A=J/2+rK,    0<r<=1/2.

This is a weighted tournament. With B=rK/3 and u=(1,1,1)^T/sqrt(3), Bu=0, PB=BP=0 and beta=r/sqrt(3). Thus Q=P/16+B^4 and

    t_Hell(A)=16^(-ell)+2 beta^(4ell).

(The nonzero eigenvalues of B are +/- i r/sqrt(3).) For a fixed ell and any positive constant c, no bound E>=c beta^p holding for all weighted tournaments can have p<4ell, since E/beta^p=2 beta^(4ell-p) tends to zero with r. The exponent in (3), not its constant, is optimal in this formulation.

## Dependencies and gap list

The proof uses only real-skew orthogonal block form, direct algebra, the finite-dimensional spectral theorem, Rayleigh/min-max comparison, PSD compression interlacing, and an elementary power inequality. No external theorem about tournament Sidorenko densities or operator powers is used. Mathematical gaps known to proposer: none. This is a request for fresh scrutiny, not a referee verdict. Current priority, nonroutine value and nearest-prior comparison must be separately assessed; proof length alone establishes neither novelty nor insignificance. A loopless finite-tournament corollary, if desired, follows by setting diagonal entries to 1/2 and bounding colliding maps by O_ell(1/n), but is not needed for the original weighted statement and is not a separate claim here.
