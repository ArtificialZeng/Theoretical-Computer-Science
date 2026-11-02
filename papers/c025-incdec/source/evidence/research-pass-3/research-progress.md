# Final-pass route change and exact diagnostic

Job c025-incdec-research-76b5f4e5209a. The pass started with the assigned
bidirectional residual kernel, f(O)<=f(L)+G+|O|d for |O|=|L|. A new
prefix-only LP representation avoided fixing irrelevant future moves and
explicitly bounded d above every current gain. After 522 numerical LP calls
at n=7,8, it found an exact rational counterexample; arbitrary n=9 was in the
configured loop but never reached. The scan stopped upon obtaining that exact
witness, before its 70-second limit. It was not exhaustive.

Let E={0,...,7}. Use weighted coverage functions with entries (item mask; weight).

    h: (3;2/29),(6;2/29),(8;2/29),(9;10/29),
       (18;2/29),(34;2/29),(66;2/29),(130;2/29).
    g: (3;5/29).

The maximal-gain bidirectional prefix is L(0), R(1), L(2), with gains
12/29,5/29,2/29. At this state L={0,2}, T=E\{1}, O={1,3}, k=2,
H=24/29, G=5/29, f(L)=19/29, f(O)=1, and the current maximum gain is
d=2/29. Hence

    f(O)-f(L)-G-kd = 1/29 >0.

Every original function hypothesis, every maximal choice, and the compact
coverage description are checked exactly by code/verify_pass3.py using the
preserved full tables. A maximal-gain completion of this prefix still has
all factor-2 prefixes (see exact-verification.json). In particular f(O)-2f(L)
is -9/29 at the displayed state. This is ONLY a counterexample to a sufficient
intermediate kernel; the old bidirectional algorithm and original question
are not disproved by it. Earlier numerical nonfindings and certificates
remain valid at their stated, limited scopes.

The route then changed explicitly to one-sided actual-objective greedy,
with its direction chosen once by comparing the endpoint totals. No right
deletions occur in its forward orientation. The union-comparison loss can
therefore be bounded ONCE by G, without a double-counted overlap budget.
That G cancels the initial F(empty)=G in the greedy average bound. If greedy
marginals have turned negative, the larger endpoint H handles every remaining
prefix. The resulting all-n proof, algorithm, oracle cost, reversal, normalization
and existing matching structural lower bound are in oriented-greedy-proof.md.

This is a proposed complete full-scope result for fresh review. No mathematical
acceptance, novelty certification or STOC readiness judgment is asserted by this
research job, and no manuscript or PDF is created. The new proposed upper bound
has passed exact tests on 261 finite instances, including the preserved source
families and all previous witnesses. A separate full-table numerical LP attack
made 492 successful calls at n=3..8 and found no violation. Those computations
are diagnostics only; the universal claim depends on the written proof.
