# Scope and proof audit

This is a local self-review, not an independent referee or formal proof check.

1. **Original target A:** not proved for arbitrary LR(1). The proved bound is O(ceil(M/w)) mask-query time with normalized commit work r_i charged separately. Bounded-work presentations obtain a worst-case step bound; linear-work presentations obtain an amortized bound. Arbitrary grammar-dependent preprocessing is explicitly distinguished from polynomial preprocessing.
2. **Whole-stack versus suffix:** the general index is a bottom-to-top finite-state annotation of the full stack. Its predicates need not be determined by a fixed top suffix. Only the Dyck artifact uses finite exposure. This restriction is explicitly stated.
3. **Lexer:** DFA lexeme languages do not by themselves implement arbitrary maximal-munch policies as bounded-memory streaming transducers. The upper theorem requires a supplied deterministic boundary-terminating pushdown/lexer presentation. Relational segmentation is allowed in the general input model.
4. **Future tokens:** completion uses V*, not arbitrary byte strings. The saturation product uses zV*, so non-byte-complete vocabularies are correctly covered.
5. **RAM:** g counts machine-word symbol/transition occurrences. w=Theta(log n) requires tables and dynamic data to be addressable; unrestricted preprocessing does not permit arbitrarily large addresses at fixed n.
6. **Original target B:** the one-stream exponent proved by this OMv construction is 1/2, not 1. Matrix dimension m gives total streamed bytes Theta(m^2). The exponent 1 is proved only with independently initialized streams of length Theta(m). No polynomial-in-g factor is hidden in the forbidden online time.
7. **Liveness in reduction:** actual commits follow universal blocks. Query byte '?' is only probed and is never committed. Thus zero products do not kill the stream. The right-linear grammar is allowed to be ambiguous while its language is regular; this refutes a language-determinism-only interpretation of the proposed combined-complexity dichotomy.
8. **Typed target C:** PSPACE-completeness is proved for externally typed, goal-directed long normal proof-term serialization. Hardness extends to general prefixes; the unrestricted upper bound is not asserted. General recursion fills typed holes when divergence is permitted but cannot repair a completed bad application.
9. **Finite evidence:** the Rust/Python artifact validates only the explicitly enumerated instances. It is not a general parser/compiler nor a proof of the infinite claims. Counts are actual, not estimates. No serving or model evaluation has been performed.
10. **Novelty:** not certified. Standard pushdown regularity, stack annotations, and classical inhabitation results are acknowledged. A new STOC-level contribution is not established merely by producing this manuscript.

## Remaining research obligations

- Either prove the arbitrary-LR(1) worst-case commit bound or identify a larger useful structural class with an effective recognition/compilation theorem.
- Resolve novelty against incremental pushdown stack annotations and fine-grained online NFA/regular-language simulation, not only LLM papers.
- Run a production compiler and serving-system evaluation if the empirical claims are expanded.
- Obtain external human mathematical review before submission.
