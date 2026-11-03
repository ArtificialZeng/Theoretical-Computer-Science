# Reproducing c049 research records

The original problem remains unresolved. This is a research dossier, not a manuscript.
From the repository root, with Python 3.10+ and a C++17 compiler available:

```sh
python3 -B notes/c049-dualpreserve/source/reproduce.py
```

The driver builds both C++ programs and runs eight declared finite checkers on
disposable copies. It makes no new search or general mathematical verification.
One expired operational research-deadline assertion is removed only in a
hash-bound temporary copy; all mathematical assertions and finite ranges remain.
The original script, all proofs and original result files are preserved in source.zip.
The archive and its exact expanded source are checked by scripts/verify_artifacts.py.
