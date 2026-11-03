# Fresh mathematical referee assessment

Job: `c015-imagebound-referee-c91c0d194005`. Date: 2026-11-01.
Frozen snapshot: `cb1b52760e44f40d39212ae4e2487e31dff8bbdea70ba237a86a02d321ed9f7e`.

**Verdict: accept the exact frozen resolution-paper claim.** The proposed
construction proves the full fixed-k assertion in immutable `source.md`, with
the constants and every-sufficiently-large-n quantifiers in `claim.json`.
The substantive contribution is a compressed nondeterministic delay together
with a global progress invariant, giving the missing linear factor at every
fixed image-bound level. No change to the candidate was needed in this review.

This is an actual local review by a fresh model context, not external peer
review, a proof assistant certificate, or a judgment of STOC acceptance.

## Scope, isolation and integrity

I used the skill/referee/release-contract instructions, project and parent
governance, publication-policy.json, and the authorized frozen packet. The
parent instructions additionally required reading outer-root-note.md; I treated
its assertions as supervisor claims to attack, not a prior verdict. I did not
read checkpoint.md, state.json, earlier job transcripts, or previous audits.
Historical decisions embedded in the authorized problem.md were not used as
evidence of correctness. No agent or background worker was spawned.

All 24 snapshot file hashes and the canonical snapshot digest were freshly
recomputed and matched. The original source hash remains
`7cf4a0de6b28019b0fa2f5e92ea04bee150c74cb9db945e382c75d8379326aa7`.
The decisive mathematical input is evidence/research-proof.md. The original
primary source was checked in its frozen local text and current publisher
text, particularly Sections 2, 7 and 9. The source's short tightness question
does not spell out all asymptotic quantifiers; the user's fixed-k reading was
explicitly frozen and the candidate covers that reading in full.

In particular, the conclusion is for every integer k>=2 and every n>=N_k,
with constants allowed to depend on k. It is not an isolated k=2 statement,
an n^k CRT lower bound, or a joint lower bound for growing k. Binary alphabet
and strong connectivity strengthen the lower bound; neither replaces an
original hypothesis. No ambiguity restriction is imposed or claimed.

## Reconstruction and adversarial checks of the proof

Let P have m>=2 states, and let disjoint cycles C_i have lengths ell_i>=2.
Letter a rotates every component; S consists of one position-zero state in
each clock. Letter b sends p_0 to S, permutes P minus p_0 cyclically, kills
the last position of every clock, and sends every other clock position to
p_0. These are exactly the frozen transitions.

**Global image bound.** Starting from a singleton, the only possible images
are empty, a singleton, or a rotated packet S.a^t. Letter a preserves this
family. Under b, a packet becomes either empty or the single port p_0,
because all surviving clock components have the same endpoint. A singleton
under b becomes empty, singleton, or S. Induction is on an arbitrary whole
word, so repeated forks never accumulate two packets in a single row. This
proves |q.w|<=k globally. Equality occurs at p_0.b for every k. It does not
follow merely from inspecting letter degrees.

**All-word mortality lower bound.** Since a is a permutation, an initial or
terminal a-run can be deleted from a mortal word. A mortal word must contain
b. Initially Q.b=P union S, because each clock has a nonterminal state and
the queue's restricted b-action is onto P minus p_0.

At every b-boundary the global image has the unique form T union cS, with
T subset P and c in {0,1}. Define V=|T|+c. It starts at m+1. For an arbitrary
next interval a^t b, let alpha indicate whether the rotated queue subset
contains p_0, and epsilon indicate whether an old packet survives b. The
new queue has |T|-alpha+epsilon elements: injectivity on P minus p_0 avoids
merges there, and any surviving packet returns to the separate port p_0.
The new packet indicator is alpha. Thus V_new=|T|+epsilon, and the drop is
c-epsilon. It is exactly one iff a packet was present and every component
was terminal, or equivalently t+1 is divisible by
L=lcm(ell_1,...,ell_k). Otherwise the drop is zero.

This calculation includes simultaneous killing and reforking at the same b,
empty queue subsets, consecutive b's (t=0), repeated clock lengths, and
noncoprime lengths. Each unit decrease costs at least L letters in a
disjoint interval between b's. Reaching empty requires exactly m+1 such
decreases, so every mortal word has length at least 1+(m+1)L. This argument
applies to every word and does not assume an optimal witness's shape beyond
the justified deletion of initial/terminal permutations.

**Existence and upper construction bound.** At a b-boundary with a packet,
apply a^(L-1)b to decrease V by one. Without a packet, a nonempty queue can
be rotated to place an active state at p_0 and followed by b. This creates
a packet at cost at most m without changing V. The next length-L interval
decreases V. Starting at m+1, exactly m+1 drops terminate in empty. The first
drop needs no fork and at most m further forks are needed. Hence the
threshold is at most 1+(m+1)L+m^2. No condition on gcd(m,L) is needed.
The lower and upper construction bounds do not purport to give the exact
threshold at all parameters.

**State count and fixed-parameter quantifiers.** For a given k>=2 set
K=k!, A=1+k(k+1)/2, N_k=2k+2AK. For every n>=N_k choose
M=K floor((n-k)/(AK)), ell_i=1+iM and
m=n-k-(A-1)M. Then m>=M>=n/(2A)>=2 and the number of states is exactly n.
There is no padding step that could damage the claimed strong connectivity.
If a common divisor d of ell_i and ell_j exceeded one, it would be coprime
to M and divide j-i. A prime divisor of d would then be at most k-1 and
would divide K and M, a contradiction. Thus the clock lengths are pairwise
coprime. Consequently L is their product and is at least K M^k. This gives
(m+1)L >= K[n/(2A)]^(k+1) = c_k n^(k+1), exactly the stated constant.
The floor estimate follows from n>=2k+2AK and is valid at the boundary.

**Strong connectivity.** A queue state rotates to p_0. Any clock state can
rotate to its nonterminal zero position and use b to reach p_0. From p_0,
a reaches every queue state, and b followed by a suitable a-power reaches
each individual clock state along the appropriate branch. Nondeterministic
reachability needs only that branch, not equality of the full image to the
target. Thus the underlying digraph is strongly connected.

**Matching general upper bound.** In any admissible incomplete automaton,
kill the images of the n original singleton rows successively. Along any
continuation of an original row, every nonempty image has size at most k.
A shortest killing suffix cannot repeat a nonempty subset, since deletion
of the loop gives the same final empty image. Its length is at most
D=sum_(j=1)^min(k,n) binom(n,j). At most n suffixes suffice and already dead
rows stay dead. The increasing-list encoding padded by copies of its maximum
injects each nonempty subset of size <=k into Q^k, so D<=n^k. Therefore
M_k(n)<=n^(k+1). The possible off-by-one issue is resolved by counting the
nonempty subsets before the final empty state. No unambiguity or matrix
finiteness assumption is used. Combining the two bounds proves the exact
frozen full hierarchy.

I found no missing quantifier, unproved auxiliary lemma, circular dependence,
or essential change of scope. The infinite proof is elementary and independent
of the finite experiments.

## Independent exact computation

I wrote audit/referee-verify.py with integer bitmask transitions, without
importing any discovery or research checker. It independently regenerated
the automata from the displayed definition and exhausted both the global
subset graph and the union of all singleton subset closures. All nine frozen
serialized transition tables, all edges and distances in their global BFS
tables, and their entire row closures matched. The nine remaining frozen
boundary examples also matched the research result tables in full.

The 18 independently reproduced shortest lengths, in frozen order, are
48,91,181,63,123,243,78,155,301; then
7,21,21,7,21,80,37,45,843. The row maximum was exactly k in each case.
Every global BFS ran to exhaustion; these are complete reachable domains,
not searches up to a length cutoff. The verifier reconstructed shortest words
and replayed the supplied constructive words.

Four controls chosen before the verification run were (m;ell_i)=(2;2,3),
(4;2,2), (3;3,6), and (4;2). Their complete BFS thresholds were 19,13,27,13.
Across the 22 cases, 19,392 checks covered every queue subset, both packet
indicators and every phase residue modulo lcm(m,L). Every potential identity
matched. The independently controlled mortality strategy chose the highest
active queue index instead of the research checker's lowest, and terminated
within the stated bound. Graph reachability verified strong connectivity.
There were also 836 exact-integer arithmetic samples for k=2,...,20 near
the threshold and at larger fixed n values. These samples corroborate the
arithmetic proof and do not replace its universal argument.

The script and compact reproducibility results are audit/referee-verify.py
and audit/referee-verification.json. No frozen evidence was modified.

## Current primary-source comparison and value

The fresh searches and exact primary pages inspected are recorded in
audit/referee-sources.json. The current arXiv record for the posing paper
still shows v2 (2025-07-23). Its Section 7 uses the global endpoint promise,
and Section 9 supplies the n^(k+1) bound and open tightness question. This
identifies a precise published problem, rather than an invented extremal
objective. [Kiefer and Ryzhikov, MFCS 2025](https://doi.org/10.4230/LIPIcs.MFCS.2025.62).

The closest concrete construction I verified is the binary deterministic
queue and physical tail in Section 4 of Ryzhikov's mortality paper. The queue
b-action agrees with the candidate's queue action up to indexing; that
mechanism is prior work. The tail in that paper has linearly many physical
states and produces quadratic mortality order. Its unrestricted NFA
exponential bounds do not impose the global fixed-k promise.
[Ryzhikov, RP 2024, current v4](https://arxiv.org/html/2405.19622v4).

The older appended-tail lemma gives an n*h increase using h additional
deterministic states under the permutation-order condition. That sequential
delay mechanism is also prior work. Applying it alone with h=L would consume
L states and does not yield this exponent hierarchy in the final state count.
The exact lemma checked was Section 2, Lemma 2.1 in the earlier single-author
preprint; the joint journal version's first page confirms bibliographic scope,
but I did not inspect its full proof or assert its lemma numbering.
[Ananichev, arXiv:1701.07954v1](https://arxiv.org/pdf/1701.07954),
[Ananichev and Vorel, JALC 2019 first page](https://jalc.de/issues/2019/issue_24_2-4/abs-153.pdf).

The candidate replaces that physical delay by a k-state packet rotating in
sum_i ell_i states with period of order n^k. Merely adjoining independent
CRT cycles gives only n^k. Reusing the same packet for m+1 disjoint costly
events requires preventing early resets, queue collisions, or reforks from
reducing the global workload. The packet closure and exact port-separated
potential establish precisely this additional property. No inspected prior
theorem already supplies it as a hypothesis-free corollary. This is a
substantive construction and proof innovation relative to the checked work,
despite its concise elementary presentation.

Two current adjacent matrix results do not settle this question. STACS 2026,
Theorem 29 concerns finite ordinary rational matrix semigroups. The September
2026 preprint's Theorem 1.2 requires joint spectral radius <=1 and a cycle
hub. In the candidate, the ordinary matrix B of b satisfies
e_(p_0) B^(2r)=k^r e_(p_0), so its powers are unbounded and its spectral
radius is at least sqrt(k)>1. Its strongly connected graph contains disjoint
a-cycles, so there is no cycle hub. These direct checks exclude those
hypotheses; Boolean support finiteness cannot replace ordinary finiteness.
[Kiefer and Ryzhikov, STACS 2026, Theorem 29](https://doi.org/10.4230/LIPIcs.STACS.2026.60),
[Chandelkar and Chadha, arXiv:2609.30817v2, Theorem 1.2](https://arxiv.org/html/2609.30817v2).

The author's current list and the public small-NFA project were also checked
for direct follow-ups. The latter explicitly limits its results to small
binary enumeration and leaves general tightness unanswered; its computations
are not used here. [Author's research list](https://sites.google.com/site/ryzandrew/research),
[small image-bounded NFA exploration](https://github.com/umaia1234/agentic-conjectures/blob/main/problems/nfa-mortal-words/README.md).
No equivalent full hierarchy result was found in this bounded screen. This
is an explicit search limitation, not proof of absolute priority. The raw
GitHub URL initially failed; the rendered primary README was then accessible.
No access failure was treated as mathematical evidence.

The theoretical value passes the publication policy: the result determines
the optimal polynomial exponent at every fixed level k>=2 of a published
hierarchy and retains both binary alphabet and strong connectivity. It does
not claim novelty for CRT, the deterministic queue, the k=1 order, or the
known upper bound. It is not a restricted substitute for the original
question and is not routine reuse of a theorem already containing the
asserted construction. Venue suitability and optimal constants remain
outside the claim, not gaps in the accepted resolution.

## Decision and handoff

Original scope resolved: yes. Correctness: passes. Substantive mathematical
innovation and significance relative to the verified prior results: pass.
Remaining mathematical or scope gaps: none identified. The exact candidate
may proceed to the normal structural check-math gate and, only after that
passes, a separately assigned writing phase. This review creates no
manuscript, PDF, external submission, or workflow success flag.

The actual `release_gate.py check-math PROJECT_DIR` command subsequently
passed with exit code 0 and `ok=true`, bound to this snapshot and referee job.
The receipt is audit/referee-gate.json. It checks integrity and provenance,
not the truth of the foregoing mathematical assessment.
