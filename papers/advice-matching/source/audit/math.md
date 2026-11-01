# Fresh mathematical referee report

Job: `advice-matching-referee-aa04e7abc7cb`.
Frozen snapshot: `9e5ce19e70bcedf07302fd469630c6922133d2418685a0789184566a1578f92c`.

**Verdict: accept the exact frozen resolution-paper scope.** In the fixed oblivious graph/order/advice model, the maximum robustness for requested consistency c is min{3/4,3/2-c} on both-sides maximum-degree-two graphs and min{7/8,7/4-c} on their 2-regular subclass. The original frontier question is resolved under the precise reading frozen in problem.md. Neither frontier, algorithm, advice domain, nor adversary scope is weakened in this review.

The report identifies three non-decisive arithmetic/wording slips below and gives their explicit corrections. The unchanged theorem follows from the frozen invariant and component counts. These corrections add no lemma, hypothesis, algorithmic capability, or new mathematical scope. Frozen evidence has not been edited. There is no outstanding substantive proof gap.

## Inputs and integrity

Read source.md, problem.md, requirements.md, claim.json, audit/snapshot.json and the listed proof, code, finite certificates, known obstruction, and literature comparison files. The required skill, referee instructions and release contract were read. No owner checkpoint, state, earlier verdict, confidence statement or transcript was consulted. Only the decisive frozen proof was treated as the candidate; a researcher's statement that no gaps were known was not evidence.

All snapshot hashes and the canonical mapping digest matched before review; see audit/referee-integrity.json. The immutable source hash is `3ec230456a31ba9b004000be9e79c74a77636a28a31e9b4eec31918f5ab305ed`. This fresh context is an additional AI review pass, not human peer review or statistically independent evidence.

The precise advice domain is essential: a partial injective table may contain absent edges. Good advice means every maximum realized matching, including partial maxima. The algorithms inspect only the table and revealed incident edges. The graph, order and table are fixed independently of the private random coins. Achievability for adaptive adversaries, fractional or weighted actions, and online-degree-only restrictions is not asserted.

## Reconstruction of the component argument

After an offline vertex's second revealed incident edge, it has no future neighbor. Thus the priority given to an available exhausted neighbor is implementable from the revealed prefix and the degree promise. No component decomposition or future edge information is supplied to the algorithm.

At a fresh degree-two root both neighbors are available, and matching exactly one gives complementary occupied/free endpoint bits. Rule E assigns these by an independent fair coin. A degree-one initial online leaf instead creates a deterministic occupied endpoint. At a degree-two extension the old endpoint's bit is transported unchanged to the new endpoint: if the old vertex is free it is preferred and the new one remains free; if occupied the new vertex is matched. The extension always succeeds. At a merge both old endpoints have their final appearances, so failure is exactly the event that both bits are occupied. A terminal online leaf fails exactly when its single old endpoint is occupied. Choices between free exhausted vertices have no future effect.

The map from each remaining boundary to its original root port is fixed by graph and order, not by outcomes. Merges consume ports without copying them. This justifies using independence of distinct root coins unconditionally. Independence after conditioning on success histories is neither needed nor claimed.

For a nontrivial final path, let m,q be its online/offline sizes and ell its number of online endpoints. Let a,b,z,s,t count roots, extensions, merges, initial leaves and terminal leaves. Direct counting gives

    q=m+1-ell=2a+b+s,
    m=a+b+z+s+t,  s+t=ell,  z=a+s-1.

For a>=1, the contracted root/initial-leaf port graph is a path. Its s initial-leaf ports each meet a root port, and its other a-1 merge edges meet distinct roots. An initial-leaf-to-initial-leaf merge or an initial-leaf-to-terminal-leaf segment would complete a separate final path; therefore neither can occur in a component also containing a root. Terminal leaves in that component consume root bits. The expected failures are (a-1)/4+(s+t)/2, so

    E|E(path)|=m-(a-1)/4-ell/2.

For a=0 the first arrival is a leaf, all surviving boundary bits are occupied, and the failures number z+t=ell-1. This gives m-ell+1=min(m,q), including a single edge and the two-online-leaf component. Isolated vertices contribute zero.

For a cycle, m=q=2a+b and z=a. With a=1 the closing merge sees complementary ports and cannot fail. With a>=2 every root-port merge joins distinct roots; otherwise a self-join would already close a separate final cycle. Each merge therefore fails with probability 1/4. In the two-root case the port graph has parallel edges, but each consumes different ports; linearity needs no independence between merge failures. Hence the expected size is m for a=1 and m-a/4 otherwise. Simple bipartite four-cycles are included.

The path inequalities, with the correct counts, are:

* ell=0: m=2a+b-1, OPT=m and deficit (a-1)/4 <= m/8, since 2(a-1)<=m.
* ell=2: OPT=q=m-1=2a+b+s and deficit relative to OPT is (a-1)/4 <= q/8.
* ell=1: OPT=m=2a+b+s. For a>=1, m>=2a>=a+1, so deficit (a+1)/4 <= m/4. The a=0 case is optimal.

Cycles have deficit a/4<=m/8. Summing over components gives the 3/4 guarantee on D and 7/8 on C even with arbitrary interleaving. Coins for different roots can be generated independently online. No limit, rounding, compactness or asymptotic additive term is involved.

## Perfect-advice optimality of rule T

Let A be any maximum realized matching and M the output. If |M|<|A|, their symmetric difference contains an M-augmenting path from an M-unmatched online vertex v0 to an M-unmatched offline vertex uk, with A edges vi-ui and M edges vi-ui-1 for i>=1.

Because T always matches when it can, u0 was already occupied when v0 arrived, so its M partner v1 arrived earlier. Inductively, if vi arrived before vi-1, the vertex ui-1 was fresh when vi selected it: its two graph neighbors are exactly vi and the later vi-1. Choosing that fresh endpoint implies that no free exhausted alternative existed. If vi's actual advised neighbor ui had been free, T would therefore have taken it, whether it was fresh or exhausted. It must instead already have been occupied by vi+1. This produces strictly decreasing arrival times along the path. At the final vk, the advised endpoint uk is free even at termination, giving a contradiction. The single-edge augmenting path is excluded directly by greediness.

This proof uses only the offline degree-two promise for this lemma and is valid for partial maximum advice. It does not assume uniqueness, perfection, or a special oracle-selected optimum. The online degree bound is used elsewhere in the component analysis, so no larger-class theorem is silently accepted.

## Arbitrary-advice guarantees and interpolation

For any wrong or absent-edge advice, T still produces a maximal matching, hence at least OPT/2 on D. On a cycle, each of the a roots produces exactly one occupied port regardless of the advised choice. Extensions preserve ports, and each failed merge consumes two occupied ports that cannot be reused. Thus failures <= floor(a/2), and

    |T(cycle)| >= m-floor(a/2) >= m-a/2 >= 3m/4.

This count is deterministic and allows all correlations induced by the entire advice table. It proves endpoints (1,1/2) on D and (1,3/4) on C. On C, wrong advice cannot invalidate the endpoint by directing different roots in coordinated ways.

Let beta be 3/4 or 7/8 respectively. E gives (beta,beta), while T gives (1,2beta-1). For c>=beta, selecting T once with probability (c-beta)/(1-beta) and E otherwise gives c-consistency and robustness 2beta-c for every fixed input and table. The denominator is nonzero for both beta values. For c<=beta use E. This standard convex interpolation establishes exactly the claimed lower envelopes, including all endpoints.

## Universal matching upper bounds

For the two Z-path completions the first online neighborhood and complete advice table agree. Coupling any algorithm's private random tape gives the same initial action. The sums of best possible continuation sizes are at most 3, including abstention. Empty common advice implies r<=3/4; a common matching table optimal in one world implies c+r<=3/2. The n=2 gadget meets both degree bounds and the global part-size condition.

For the two frozen eight-cycles, both early neighborhoods and the full table again agree. If both early vertices match, their two free offline vertices occupy the same late neighborhood in exactly one completion and different late neighborhoods in the other, giving a sum <=7. With one or zero early matches the sums are <=6 or <=4. These bounds permit arbitrary correlations and later strategies and include abstention. Both completions are connected simple 2-regular bipartite graphs with OPT=4. Empty common advice yields r<=7/8. The table (0,2,3,1) in online order is a perfect matching in G1 and an allowed injective table in G0, so the same inequality yields c+r<=7/4.

These are fixed pairs, not adversaries reacting to realized random actions. Known n does not distinguish the worlds. The upper bounds and lower bounds coincide for every c in [0,1], with no additive loss. OPT=0 is vacuous and already handled by the algorithms. Arbitrary labels and absent cross-component advice edges are covered.

## Explicit non-decisive corrections in the submitted exposition

1. The corollary's assertion m>=2a for an offline-ended path is false, for example a single online root with m=1,a=1. The correct already-derived identity is m=2a+b-1. The needed inequality 2(a-1)<=m follows immediately and proves the same 7/8 bound.
2. For an online-ended path the corollary prints m-1=2a+b+s-1. The correct identity is m-1=2a+b+s. The desired bound is consequently still valid.
3. In the cycle gadget the sentence saying the last two advised pairs are absent in G0 is inaccurate. Only the pair (y1,3) is absent; (y2,1) is present in both worlds. G0 advice remains an admissible wrong table, and the upper bound uses only that fact. No step requires two absent pairs.

These are explicitly disclosed, not silently corrected frozen inputs. The proof of the exact candidate is complete above using the original identities and the literal gadget. Manuscript exposition should use these correct counts and edge-membership statements. No substantive claim change, new freeze or weaker replacement theorem is proposed by this referee.

## Independent finite verification

Created audit/referee_check.py without importing or executing the researcher's implementation. It uses direct online simulations, enumeration of root coin strings, independent matching enumeration and recursive optimum continuations. It writes only audit/referee-checks.json. The frozen research scripts, which would overwrite their certificates if run as main, were inspected but not run that way.

The fresh checker passed:

* All 7,343 labelled n=4 graphs satisfying both degree bounds, all 24 online orders: 176,232 graph/order inputs, including isolates and disconnected components.
* Every maximum realized advice matching on those inputs: 375,960 advice cases.
* All 209 injective partial advice tables on each regular graph/order input: 451,440 cases, including absent advised edges. Minimum observed T ratio is 3/4.
* Every connected component type, every induced online order through seven online vertices: 23,650 orders. Both exact expectation formulas and claimed component bounds match direct simulations.
* All three Z-gadget prefixes, all nine cycle-gadget prefixes, both cycle degree/optimum/connectivity conditions, and the exact missing-advice-edge assertion.

Minimum observed E ratio on labelled n=4 inputs is 3/4. The computations are exact finite supporting evidence, not a proof of the unbounded theorem or statistical independence. The analytic arguments above provide the quantified result.

## Literature, contribution and final decision

The actual primary-source comparison and bounded search limits are recorded in audit/referee-literature.md. In particular, Fàbrega–Muñoz already have the cycle baseline, the gadget and the orientation argument; Feng et al. identify the same relevant priority algorithm. Choo et al. and Jin–Ma already have the Z obstruction and linear bound. None of those is accepted as a new contribution. The 2026 multistage paper was inspected directly: its singleton theorem permits fractional matching actions, so it does not subsume the integral structural frontier. Likewise, the 2025 one-side degree theorem and fractional-advice literature cannot be transferred by changing model labels.

The remaining result passes the contribution gate as a compact exact structural classification. The exhausted-neighbor rule's compatibility with every maximum matching table requires a separate argument; a prediction-oblivious guarantee alone does not imply it. Its arbitrary-advice cycle endpoint, coupled with the common-table use of the old gadget, determines an exact advice frontier. The path analysis supplies a sequential algorithm for the original class, rather than reusing a batched algorithm. A credible use is distinguishing the effect of path endpoints from regular cycle structure on the cost of fully trusting matching advice: perfect consistency costs robustness down to 1/2 in D but only to 3/4 in C. This is not supplied by the old advice-free cycle theorem, the known obstruction alone, or interpolation alone.

The contribution is elementary and modest. Acceptance is for this one coherent characterization with explicit prior credit; it is not certification of priority, a new orientation method, a new 7/8 baseline, or a venue acceptance prediction. No equivalent advice-frontier statement was found in the bounded primary inspection. The original generated question is not described as a recognized open problem.

**Accept the unchanged frozen scope as resolution-paper / original_status=proved.** There are no unresolved substantive mathematical gaps. Proceed only to the authorized local WRITE phase under requirements.md, carrying the three explicit exposition corrections and preserving all frozen research files. No manuscript, PDF, external submission, or other external write was performed in this referee job. The structural check is recorded separately and is not mathematical evidence.
