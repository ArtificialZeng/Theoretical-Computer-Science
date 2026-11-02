# Proposed full resolution by endpoint-oriented objective greedy

Researcher proof dossier, job `c025-incdec-research-76b5f4e5209a`, pass 3.
This is a proposed theorem for fresh review, not an acceptance or venue assessment.
The immutable original `source.md` and precise reading `problem.md` are unchanged.

## Theorem

For every finite E and every pair of normalized nonnegative monotone submodular
functions h,g on 2^E, a deterministic algorithm using O(n^2) exact value queries
and polynomial additional arithmetic/comparisons returns one permutation pi
such that, simultaneously for every k=0,...,n and every O with |O|=k,

    h(O)+g(E\O) <= 2 [h(S_k)+g(E\S_k)].

The optimal uniform deterministic constants in both the unrestricted and the
polynomial-oracle readings of the original question are therefore exactly 2.
The lower bound is the existing source Proposition 11 at curvature 1, reproduced
below; the proposed new contribution is the sharp algorithmic upper bound on
the entire arbitrary unequal-total class.

## Algorithm

Fix a total ordering of E to resolve all ties. Put H=h(E), G=g(E).
If H>=G, define F(S)=h(S)+g(E\S). Starting at P_0=empty, for i=1,...,n,
choose e_i outside P_{i-1} maximizing F(P_{i-1}+e)-F(P_{i-1}), and put
P_i=P_{i-1}+e_i. Continue even if the maximum gain is negative. Return
(e_1,...,e_n).

If H<G, perform exactly the same construction with h and g interchanged,
so F'(S)=g(S)+h(E\S)=F(E\S), and return the REVERSE of that greedy order.
This endpoint comparison is part of the algorithm. A fixed direction without
the comparison is not the claimed algorithm. For E empty return the empty order.

At each step there are at most n candidate sets, each evaluated using one h and
one g query. Caching the current objective gives O(n^2) queries, comparisons
and additions/subtractions in the exact-value unit-cost oracle model specified
in problem.md. No unknown OPT value is queried or computed. Negative gains,
zero totals and all deterministic ties are allowed.

## Universal upper-bound proof

It suffices first to analyze H>=G. Complementation preserves submodularity:
applying g's submodular inequality to E\A and E\B gives the required inequality
for S -> g(E\S). Thus F is submodular, though it need not be monotone.
F(empty)=G and F(E)=H. Also, by monotonicity of h and g,

    F(O) <= H+G                                             (1)

for every O. For any O,P, monotonicity of h and nonnegativity of g imply

    F(O)-F(O union P)
      = h(O)-h(O union P)
        +g(E\O)-g(E\(O union P)) <= G.                     (2)

Write a_i=F(P_i)-F(P_{i-1}) for the greedy gains. They are nonincreasing:
for every still available e, submodularity gives
F(e | P_i)<=F(e | P_{i-1})<=a_i. Taking the maximum over e outside P_i gives
a_{i+1}<=a_i. No positivity assumption is used in this argument.

Fix 1<=k<n, put P=P_k and d=a_{k+1}, and take any |O|=k.
If d>=0, repeated diminishing returns, followed by the greedy maximality at P,
gives

    F(O union P)-F(P)
      <= sum_{e in O\P} F(e | P)
      <= |O\P| d <= k d.

Combining this with (2) and the nonincreasing gains yields

    F(O) <= F(P)+G+k d
         <= F(P)+G+sum_{i=1}^k a_i
          = 2 F(P).                                      (3)

This includes d=0 and does not assume disjoint O,P.
If d<0, all remaining greedy gains are at most d, so

    H=F(E)=F(P)+sum_{i=k+1}^n a_i <= F(P).

Equation (1), H>=G and this last inequality give

    F(O)<=H+G<=2H<=2F(P).                                (4)

The k=0,n cases compare the unique feasible set with itself. This proves the
claim for all k simultaneously on the SAME greedy order when H>=G.

For H<G, the swapped instance has endpoint totals H'=G>=G'=H, so its greedy
prefix Q_j satisfies 2F'(Q_j)>=max_{|A|=j} F'(A) for every j. A prefix S_k of
the returned reverse order is E\Q_{n-k}. Thus F(S_k)=F'(Q_{n-k}), while
max_{|O|=k} F(O)=max_{|A|=n-k}F'(A) under A=E\O. The identical factor-2
inequality follows. All original functions, cardinalities and unequal totals
are included; no subclass restriction is introduced.

For the unnormalized nonnegative monotone variant, subtract h(empty),g(empty)
inside the algorithm and apply the established normalization transfer in
problem.md: the original objective is F'+B with B>=0. Then
2(F'(S)+B)>=OPT'+B. This needs only two further value queries. Normalized
instances suffice for the matching lower bound.

## Matching structural lower bound, reproduced from the source

For n>=2 let E={a,b_1,...,b_{n-1}}. Let q(S)=n-1 if a belongs to S and
q(S)=|S| otherwise, and let h=g=q. This is a coverage function: a covers all
n-1 unit features, and b_i covers feature i. Hence both functions satisfy
every original hypothesis, including normalization.

For cardinality 1 and n-1 the optimum is 2(n-1), attained respectively by
{a} and E\{a}. In any permutation, if a is not first, the prefix of size 1
is a singleton b_i and has F value 1+(n-1)=n. If a is first, the prefix of
size n-1 contains a and its complement is one b_i, again with F value n.
Consequently EVERY permutation has competitive ratio at least 2(n-1)/n.
For every r<2 choose n with 2(n-1)/n>r. No deterministic algorithm, even with
unlimited access/computation, can have uniform ratio r. Combined with (3)-(4)
and reversal this proves C_struct=C_poly=2; an infimum-attainment assumption
is unnecessary. This lower bound is PRIOR WORK, not a claimed contribution.

## Scope, dependencies, and gaps

Dependencies: elementary diminishing returns for submodular functions,
complement submodularity, h/g monotonicity and nonnegativity, and the explicitly
reproduced source lower bound. No finite experiment is used to prove the theorem.
Known mathematical gaps in the argument as written: none identified by the
proposer. A fresh referee must check the proof, oracle reading, novelty and
substantive value independently. No referee verdict is asserted here.

The previous bidirectional residual kernel is false (prefix-kernel-screen.json).
It is abandoned as an unnecessary sufficient route; no claim about the
bidirectional algorithm's factor 2 is made. This new algorithm has no right
moves inside its chosen orientation, which removes the deleted-comparator
term responsible for that kernel. Equation (2) charges the ENTIRE remaining
g-loss once to G. Its interaction with the initial value F(empty)=G cancels
that budget in (3). Endpoint orientation handles the decreasing tail in (4).
This is the proposed conceptual delta from separately comparing h/g marginals.
The sharp full-scope improvement, rather than a special-case corollary or a
method counterexample, is the proposed substantive contribution. Its broad
STOC importance and technical depth remain for an actual fresh assessment.
No manuscript or PDF is created in this research phase.

## Explicit nonnegative-summand identities for audit

For the d>=0 branch, put m=|O\P| and U=O union P. The proof can also be
checked by summing the following five nonnegative quantities:

    A = G+F(U)-F(O),
    B = F(P)+sum_{e in O\P}F(e|P)-F(U),
    C = sum_{e in O\P}(d-F(e|P)),
    D = (k-m)d,
    E = F(P)-G-kd = sum_{i=1}^k(a_i-d).

Their sum is EXACTLY 2F(P)-F(O). A is nonnegative by (2), B by repeated
submodularity, C by greedy maximality at P, D by d>=0 and m<=k, and E by
the nonincreasing gain sequence. For the d<0 branch the exact identity is

    2F(P)-F(O) = [H+G-F(O)] + [H-G] + 2[F(P)-H].

Each bracket is nonnegative by (1), orientation and the decreasing tail,
respectively. These identities expose all sign conditions and cancellation;
code/verify_pass3.py checks their coefficient algebra separately without a
numerical solver. The displayed arbitrary-n derivation, not finite checking,
is the universal argument.
