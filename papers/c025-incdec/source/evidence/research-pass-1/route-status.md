# Changed constructive route and current gap

`code/net_greedy.py` tests the following polynomial-query algorithmic route.
Maintain S subset T, initially empty and E. For every e in T minus S, compare
L(e)=f(S+e)-f(S) and R(e)=f(T-e)-f(T). Take a maximum over all these choices;
on L append e to the prefix, on R prepend e to the suffix. These are actual
objective gains, unlike the source's comparison of h/g gains separately.
Both side priorities in ties were tested, with the smallest item within a side.
There are O(n^2) value queries and polynomial arithmetic operations.

Two elementary properties are proved, with no claim of novelty:

1. L(e)+R(e)>=0 by submodularity of f for S subset T-e. Thus every chosen
   gain is nonnegative. Every left boundary has value at least g(E), and every
   right boundary has value at least h(E).
2. The sequence of selected gains is nonincreasing. A left move decreases all
   other left gains by submodularity, leaves right gains fixed, and removes an
   option; a right move has the symmetric property. Neither operation increases
   the maximum remaining gain.

At equal totals this recovers the already known easy factor 2 from the global
bound f(U)<=h(E)+g(E). At unequal totals it does not by itself compare a smaller
endpoint's prefixes with OPT_k. No general ratio theorem has been proved here.

It passes 510 exact runs on the 255-instance suite, worst observed ratio 7/4.
The broader bounded LP search `code/net_greedy_lp.py` uses separate values of
h,g on every subset, all elementary monotonicity and submodularity constraints,
h(empty)=g(empty)=0 and h(E)+g(E)=1. It fixes chronological item order 0..n-1
by relabeling symmetry and enumerates all L/R side words and same-size
comparison subsets at every nonendpoint prefix. Chosen-gain inequalities allow
every tie-admissible trace. The objective is f(O)-2f(prefix). At n=3,4,5,6,
respectively 32,176,832,3648 LPs returned no positive objective above numerical
tolerance 1e-7. All 4688 calls returned solver success, without time-limit hits.
No duals or interval-certified bounds were checked, so this is FLOATING
SCREENING, not exact class exhaustion or a theorem. The 120-second experiment
completed in 25.14 seconds. Summary: net-greedy-lp-summary.json.

A separately bounded 90-second n=7 numerical screen made 2435 additional
successful LP calls and stopped during the 21st of 128 side words; it found no
positive objective, but is explicitly INCOMPLETE. The partial final word is
included in the word counter; it is not claimed fully checked. This timeout
is an operational limit, not mathematical evidence of nonexistence. See
net-greedy-lp-n7-summary.json. No n=8 general-function LP was run.

To move from solver evidence toward proof, `code/trace_dual.py` reconstructed
and checked a rational dual identity coefficient by coefficient for the one
n=6 trace RLLRRL, prefix {1,2}, comparator {0,5}. Its normalized objective
f({0,5})-2f({1,2}) has certified upper bound -1/3 when h(E)+g(E)=1.
`code/compact_dual.py` then synthesized an alternative 17-constraint aggregate
certificate proving the weaker desired upper bound 0, with exact nonnegative
rational weights and no nonzero normalization RHS. See trace-dual.json and
compact-dual.json. Both are statements about just this trace/comparator, not
all traces or arbitrary n. The compact certificate uses some choices made
after the target prefix; a useful general proof may require such future
constraints rather than only greedy prefix recurrence. This is a clue, not
a proved necessity or a general invariant.

Preserved operational failures: the default python3 interpreter did not have
SciPy; the existing `python` interpreter did. No package was installed. The
first trace-dual verifier asserted that the normalization multiplier was zero;
it was actually -1/3. The coefficient identity itself checked. The assertion
was corrected to the mathematically sufficient nonpositive condition, and the
successful exact certificate records the actual negative multiplier. Neither
event is a mathematical failed approach or evidence about the original claim.

The primary-source refresh on 2026-11-01 UTC checked the current Acta Informatica
publisher page and searched exact title plus incremental-decremental/submodular
competitive-ratio terms. No full resolution was identified in those checked
primary results. This is not exhaustive priority certification. The official
ESA 2026 incremental paper remains a different problem; its 1.373 theorem
explicitly sacrifices efficiency, per the downloaded primary introduction and
intake/ESA2026-scope-update.json. No polynomial 1.373 bound is asserted.

Current minimal unresolved kernel: prove or refute that the specified actual-
gain bidirectional greedy order satisfies 2f(S_k)>=f(O) for every k and every
|O|=k, for all normalized monotone submodular pairs h,g with arbitrary unequal
totals. This sufficient assertion is not claimed equivalent to the original
sharp-ratio question. Its failure would reject this method only. A proof,
combined with the verified structural lower bound 2, would settle both constants
in the original scope; no such proof exists yet.
