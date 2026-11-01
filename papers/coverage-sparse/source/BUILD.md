# Build and reproduce

With a standard TeX distribution, run from the extracted source root:

```sh
mkdir -p output/pdf
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex
```

The official local acmart.cls and all declared compilation inputs are included.
Use Python 3.10 or newer for the supplied exact verification scripts. Read their
file headers and corresponding JSON outputs for paths, ranges and limitations.
The proof dossier and manuscript give the analytic arguments. Rebuilt PDF bytes
may differ because timestamps change. The release manifest describes the exact
originally reviewed PDF. Mathematical provenance is not a peer-review claim.

For the first paper, run `python3 manuscript/reproduce.py` from the source root.
This portable entry point reruns all five finite suites without overwriting
their saved evidence. It prints JSON to stdout. Third-party paper fulltexts are
omitted from this ZIP; their original URLs and hashes remain in the dossier.
The internal full-dossier wrapper is not required for portable reproduction.
Finite verification does not prove the infinite-parameter theorems.
