# Estimated-value register

No estimated or inferred experimental values are used in `4.tex` or `4.pdf`.

The counts in the finite-validation table are generated from actual executions
of `artifact/validate.py`, saved in `artifact/validation_results.json`, and
typeset by `artifact/make_table.py`. They are correctness checks, not measurements
of real repositories or performance estimates.

No p50/p99 latency, memory, treewidth-distribution, or speedup figures have been
invented. The proposed five-to-eight-repository study is a protocol only, and the
paper explicitly says it has not been performed.

Asymptotic expressions, dimensions of the mathematical reductions, loop counts
specified by the validation script, and prospective experimental sample sizes
are not inferred empirical results.

Revision v2 adds 24 actually executed call-diamond updates, recorded in
`artifact/records/sharing.jsonl`. All table counts are now backed by per-record
JSONL data and independently recomputed by `artifact/audit_records.py`.
