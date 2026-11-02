# TreeFlow v2 executable evidence

This archive is embedded in the revised `4.pdf` as `treeflow-artifact-v2.zip`.
Use a PDF reader's attachment panel or `pdfdetach -saveall 4.pdf` to extract it.
The adjacent `4_source.zip` is the complete LaTeX/source delivery; this archive
is the stand-alone executable evidence. No public repository URL is claimed.

Requirements: CPython 3.9 or later; Python standard library only. Runtime and
actual interpreter version used for the supplied execution are in `runtime.json`.

After extracting this archive to a directory, run from that directory:

```sh
python3 validate.py
python3 audit_records.py
```

`validate.py` executes every test and regenerates the JSONL records and
`validation_results.json`. `audit_records.py` reconstructs graph states and
circuits from those recorded inputs, independently recomputes expected answers,
checks every record ID, and writes `record_audit.json`. It does not import
`treeflow.py`. Its closure oracle uses graph search rather than Warshall.

`treeflow.py` is the maintained semantic reference. It uses Warshall closure,
not asymptotically fast matrix multiplication. The validation concerns finite
correctness and sharing; it is not a repository performance experiment.

## Table-to-evidence mapping

| Paper quantity | Records / calculation |
|---|---|
| 4,164 matrix-vector cases | distinct `(k,matrix_bits,vector)` in `lower_row.jsonl` |
| 12,420 answers for each of three gadgets | each row in `lower_row.jsonl` stores control, fact, and explicit-stack answers |
| 12,420 selector checks | `selector.jsonl`, including updated integer row counts |
| 108 graph edits | `bag_edit.jsonl`; initial graphs/decompositions in `bag_init.jsonl` |
| 24,696 bag/BFS comparisons | `bag_answer.jsonl`, including source and target facts |
| 300 circuit edits | `circuit_edit.jsonl`; initial 40-gate DAGs in `circuit_init.jsonl` |
| 9,600 circuit comparisons | `circuit_answer.jsonl`, 32 internal gates per edit |
| 3 recursive states | `recursion.jsonl`, including every fixed-point round |
| 24 sharing edits | `sharing.jsonl`, r=1..8 diamonds, three edits each |

Every record has a unique, sequential `kind:index` identifier. The fixed random
seed is 20261031. The logs contain complete initial relations and edit payloads,
so aggregate counts can be traced to actual executions. `MANIFEST.json` records
SHA-256 digests of every source, report, and raw-record file in this archive.

The manuscript proof and executable reference were revised with OpenAI Codex.
The attached checks were actually run. They do not certify novelty or replace
an independent human proof audit.
