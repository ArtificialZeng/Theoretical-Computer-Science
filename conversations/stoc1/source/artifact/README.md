# VIABLE finite validation artifact

This artifact specializes the stack index to two-bracket Dyck completion and implements generic NFA block tables. It is not a general LR compiler, a pushdown-saturation implementation, or a model-serving benchmark.

Requirements: stable Rust (`rustc`) and Python 3.10 or later; no Python packages.

On macOS, from this directory:

```sh
rustc --edition 2021 --crate-type cdylib -O viable.rs -o libviable.dylib
python3 verify.py
python3 verify_blocks.py
```

On Linux use `-o libviable.so`. Run from the repository root to build the paper:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build 1.tex
cp build/1.pdf 1.pdf
```

The verifier regenerates `results.json` and `validation_table.tex`. Counts in the paper come only from these outputs. The NFA witness construction is independently simulated against direct Boolean matrix multiplication. Dyck masks are compared against a direct whole-candidate stack oracle. Neither test is a proof of a general theorem. There is no CUDA, model inference, throughput measurement, production baseline comparison, or vLLM/llama.cpp integration.

The C ABI is intended for the included binding. Callers must provide valid non-null live decoder handles, valid input buffers, and sufficient output capacity; handles must not be concurrently mutated or used after freeing. The reference library does not harden these foreign-function preconditions.

## Revision 2 checks and table payloads

`verify_blocks.py` exhausts all 256 two-state/two-symbol NFA transition systems, four initial active sets, both block sizes, and all prefixes through depth five, comparing with an independent set oracle. It also checks all active sets of a fixed eight-state classifier for block sizes 1, 2, 3, 4, and 8. `block_results.json` records every comparison count and the exact allocated array payload of the block tables. Logical payloads exclude Python allocator/container overhead.

The script really compiles the Dyck mask rows for maximum token lengths 1 through 5. Their table payloads are measured by serialization length and reported separately from general-PDA compilation. The Rust core has 31 valid classes plus one unused zero row: 192 allocated u64 words, 1536 bytes of row payload. This is not process RSS. Universal liveness checks test prefixes of two consecutive identical complete blocks, including empty prefixes, for each matrix/vector case.
