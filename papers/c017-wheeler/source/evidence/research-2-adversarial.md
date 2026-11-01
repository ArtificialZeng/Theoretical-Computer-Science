# Research pass 2: attacks, exact shortcut failures and coverage

Job `c017-wheeler-research-98a17f8eb2fd`; research evidence, 2026-11-01.
All prior failed routes, pass counters and usage records are retained. These
attacks concern the realizability consequence; they do not weaken or replace
the immutable original membership question.

## Exact counterexample to skipping normalized residual merging

Unary alphabet {a}; two states p (initial) and q; transitions p --a/epsilon--> q,
q --a/epsilon--> p; both final with empty terminal output. The partial function
is actually total and identically epsilon. Its original state colors alternate
at every length, so every convex monochromatic component in unary colex is a
singleton. That coloring has infinitely many components. Nevertheless a single
state with an a/epsilon loop and empty terminal computes the function and is
Wheeler. A procedure testing convex finiteness of the GIVEN machine's state
coloring would therefore be wrong.

The normalized continuation functions here are equal, so the correct procedure
merges p,q before adding the new initial singleton. Its representative language
is {epsilon,a}, and it accepts. The exact automatic prototype also tests the
unmerged coloring and detects its representative language as infinite by a
useful directed cycle, without a depth cap.

## Exact counterexample to dropping the initial LCP

Unary one-state machine p --a/0--> p, initial and final, with terminal 0.
It computes f(a^n)=0^(n+1). Its residual LCP lambda_p is 0. Normalizing gives
an a/0 loop with terminal epsilon. Using that normalized state as an initial
state with no initial output would compute 0^n, already wrong at epsilon.
The correct construction has a new initial state with terminal 0, an initial
a/00 edge to the normalized class, then the a/0 loop with empty terminal.
It computes exactly f, is Wheeler, and respects the source's absent initial
output convention. The prototype serializes this full quotient.

## Adverse original-source and boundary controls

The source's unary floor-length function f(a^n)=a^floor(n/2), with alternating
empty/a edge outputs and both terminal words empty, has DISTINCT normalized
continuations. Their colors alternate forever, even after canonical merging.
Every component is a singleton, Rep is infinite, and the procedure rejects.
This is not a new source counterexample; it is a regression control.

For the unary even-length domain with empty output, one of the same parity
states is nonfinal. The two normalized continuations have different domains,
so they must not merge. Exact representative finiteness again rejects.

Binary identity and all-erasing functions have finite components and pass the
membership test. Binary complementation and binary length coding have finite
components and FAIL the membership test: input-color finiteness alone is not
a realizability criterion. The existing membership theorem is essential to
this route. The length-coding test has nonempty initial LCP too.

Other named controls cover the empty input alphabet, an epsilon-only domain,
partial terminal domains and actual convex splitting. The latter uses the
constant-empty function on binary words of length at most two. Its three
canonical states split into five convex components; merely retaining canonical
state labels would not provide total reaching-language separation.

## Automatic constructions challenged independently

The prototype constructs a ternary synchronous automaton for an intervening
different-color word, projects that word, and takes the correct relative
complement to form the maximal-component relation. It separately constructs
shortlex-smaller equivalent pairs and projects again. In particular it does
not enumerate words until a guessed stable number of components appears.

Projection explicitly tests an empty free word whose existential witness is
longer. A raw column projection without all-padding suffix closure would miss
this witness. Padding invariance is also checked by adding three all-padding
columns to relation calls. The written proof handles arbitrary suffix length.

Twenty held-out acyclic finite-domain models were chosen with a new fixed seed
after the statement was fixed. For these models the domain is completely
enumerated because every transition increases the state index; maximum path
length is at most the original state count minus one. Directly sort the whole
domain, group adjacent equal colors, and select a shortest reversed word from
each group. This completely independent finite procedure agrees with EVERY
automatic relation pair and the ENTIRE automatically computed representative
language. For the infinite controls finite replays only supplement the exact
automata conclusions and the all-size proof.

Actual report: 13 named controls; 20 held-out complete finite domains;
1,475 direct function comparisons, 1,318 nonempty H-identity comparisons,
8,171 automatic relation comparisons, and 1,315 component-successor checks.
All passed on the recorded final run. Infinite-control literal input tests
stop at length 7; the representative-language finiteness answers do not.
These checks are implementation evidence, not a fresh referee or formal proof.

## Remaining review targets and operational record

No counterexample to the strengthened statement was found, and the researcher
identifies no gap in its written proof. A fresh reviewer should attack the
exact residual-equality refinement (including partial continuation domains),
the new initial state with nonempty LCP and cycles, projection when all free
tracks end before a witness, right invariance of maximal components, and the
necessity of the output-property transfer from an arbitrary realization.

There was no failed mathematical experiment in this pass. Two documentation patches were rejected (a stale textual context and an
unsupported delete/add pair for one path); the intended text was then applied
correctly. Neither rejection changed mathematical data. A direct institutional-source lookup returned
a cache miss; no unavailable text was treated as evidence. The old pass-1
manually reversed certificate-direction failure remains in its original
adversarial record. No counter or audit was reset, no scheduling state edited,
and no manuscript/PDF or external action was produced.
