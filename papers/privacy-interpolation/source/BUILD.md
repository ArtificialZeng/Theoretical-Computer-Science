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

Run `python3 manuscript/reproduce.py` from the extracted source root for the
portable finite verification suite. It uses the Python standard library,
prints a JSON object, and leaves the frozen evidence unchanged. Read
manuscript/REPRODUCIBILITY.md for the exact finite scope. The general theorems
are proved in the manuscript; finite checks do not establish them by themselves.
