# Optimal Deterministic Incremental--Decremental Submodular Maximization

**working_paper** · 6 total pages.

[PDF](c025-incdec_working_paper.pdf) · [Unified index](../../README.md)

Finds one ordering whose every prefix approximately maximizes h(S)+g(E\S) among sets of the same size, for arbitrary nonnegative monotone submodular h and g. An oriented greedy algorithm is deterministically 2-competitive using O(|E|²) value queries, including unequal endpoint totals and negative marginal gains. Together with the prior lower bound, this settles the optimal uniform deterministic constant.

Classification basis: fresh_internal_stoc_assessment

Mathematical scope: proved

From the repository root:

```sh
python3 scripts/reproduce.py --paper c025-incdec
python3 scripts/build_pdfs.py --paper c025-incdec
```

The original archive and expanded source are linked in the unified index. Checks run on disposable copies. Finite checks are not a full proof, formal verification, new novelty review or external peer review. Original author lists and archived files remain unchanged.
