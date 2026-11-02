# Research pass 1 progress — 2026-11-01 23:10 UTC

Job c025-pmcdelay-research-338d67d18097. Source remains immutable; entry source hash verified. State already records research_passes=1, revisions=0; worker has not edited scheduling state.

New mathematical checks: the witnessed separator helper has a valid clique-sum minimality argument and fiber at most n. The two invariants E(j)<=Q(n)j and T<=Q(n)K close with Q(n)=Q(n-1)+(n+10)p(n), provided source closure and named polynomial primitives are used. Total time is a separate invariant; using a prefix +1 estimate instead would introduce a spurious multiplicative recurrence. Final buffering must use T as well as E when fewer than j solutions exist.

A newly identified source wording issue requires explicit treatment: Definition 12 of 2610.19850v3 says X\{a} is an (a,b)-separator, but Definition 20 chooses both endpoints in X. Use the explicit graph-search formula A=C_b(G-(X\{b})), reject u in N[A], S=N(C_u(G-N(A))), and check the resulting PMC. The preimages constructed in source Theorems 9/10 have Omega subset X subset Omega union C_a, with u in C_a and b in T. A transfer proof is being written to show these arcs survive this endpoint-safe interpretation; no literal inconsistency is silently assumed away.

Primary checks: actual local MCS-M pseudocode p291, Theorem 4.4 p294 and O(nm) discussion p297 verified. Source Lemma 1 states O(n^3) separator delay. Live arXiv histories still list 2610.19850v3 and 2610.24856v1. Bounded current searches found no full all-graph polynomial-delay result. Capelli–Strozecki STACS 2023 / Computational Complexity 2026 explicitly cover the known buffering conversion; it must not be claimed new. IPEC 2025 Proposition 29 already contains the separator extension analogue.

No proof acceptance, candidate, manuscript, PDF or new finite output test has been created at this progress checkpoint. Next: finish source-arc transfer and write the complete all-input timing/buffering proof; then adversarially check phase boundaries and the exact source dependency.
