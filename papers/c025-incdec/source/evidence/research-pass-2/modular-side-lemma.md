# Restricted analytic progress, not an original-scope resolution

Job c025-incdec-research-5525eccf7fba, assigned pass 2. This is a researcher
proof record, not an independently accepted claim. The original arbitrary-pair
question remains unresolved and no publication candidate is proposed.

Let h be normalized monotone submodular, and let g(A)=sum_{e in A} c_e,
c_e>=0. Write G=g(E), H=h(E), f(A)=h(A)+G-c(A). Run the actual-gain
bidirectional greedy algorithm from route-status.md. At a state (L,T), write
R=E\T, U=T\L and let d be the maximum remaining actual left/right gain
(or d=0 if U is empty). All previous selected gains are at least d, and
nonnegative, by the already recorded submodularity argument.

**Restricted residual lemma.** For every comparator O,

    f(O) <= f(L) + G + |O intersect U| d.

Proof: Put D=O intersect R and A=O intersect U. When e in D was deleted
on the right, let (L_i,T_i) be the state immediately before that deletion.
The chosen right gain is c_e-h(e | T_i-e), and is at least the available
left gain h(e | L_i)-c_e for the same element. Hence

    h(e | L_i) <= 2c_e-h(e | T_i-e) <= 2c_e.

Since L_i is a subset of the present L, diminishing marginal gains imply
h(e | L)<=2c_e. For e in A, the present left gain is at most d, so
h(e | L)<=c_e+d. Monotonicity and submodularity of h give

    h(O) <= h(O union L)
         <= h(L) + sum_{e in O\L} h(e | L).

It follows that

    f(O) <= h(L)+G-c(O intersect L)+c(D)+|A|d
          = f(L)+c(L\O)+c(D)+|A|d
         <= f(L)+G+|A|d.

The last inequality uses disjointness of L\O and D, and nonnegative modular
weights. This proves the residual lemma for all n, all comparators, and all
states of the specified algorithm. It requires neither equal totals nor a
restriction on later choices.

If |O|=|L|=k, let a_1,...,a_k be the gains of the left choices producing L.
Then |A|d<=k d<=sum_j a_j=f(L)-G. Thus f(O)<=2f(L).
Every prefix produced as a left boundary has the desired factor 2.
Every prefix produced as a right boundary T has f(T)>=H. Consequently,
**if in addition H>=G, the complete output order is 2-competitive**, since
f(O)<=H+G<=2H<=2f(T) at each right boundary. By reversal the symmetric
statement holds when h is modular and G>=H. Endpoint cases are automatic.
The proof includes arbitrary deterministic tie breaking among maximum gains.
There are O(n^2) value queries and arithmetic/comparison operations.

This does NOT prove the order 2-competitive for every modular g: the case
G>H does not have the right-boundary argument just used. More importantly,
it does not handle arbitrary nonmodular h and g. Neither omission is silently
removed from the immutable original question. No novelty or STOC significance
claim is made for this restricted lemma.

# Exact unresolved kernel for this route

For general h,g, prove or refute the coupled residual inequality

    f(O) <= f(L)+g(E)+|O| d

at left boundary states with |O|=|L|. Here d is the actual maximum available
gain (0 if finished). This is sufficient, by the nonincreasing-gain argument
above and reversal, to establish the full ratio-2 guarantee. It is not claimed
equivalent to the original question or necessary for the algorithm's success.
The modular proof actually yields |O intersect U| in place of |O|, but the
weaker displayed general template is the one numerically screened this pass.

A direct replacement of modular costs by g's chronological marginals is
unjustified: redundant coverage features can be charged to both deleted
comparator elements and selected non-comparator elements. A general proof
must control that overlap using the actual h/g comparisons. Bounds on the h
term alone and a comparator-loss bound by g(E) are false; see obstructions.md.
