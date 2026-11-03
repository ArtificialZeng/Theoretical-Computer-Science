# Clean build and finite reproduction

Run from the extracted source root. The listed mathematical checkers use only the Python standard library; their finite checks supplement the written proof. Run on a copy: scripts regenerate their diagnostic JSON outputs.

Declared Python helper modules under intake/ are also included. Other optional diagnostic entry points may require their stated extra dependencies; the commands explicitly listed below use the standard library.

The manuscript build requires a working LaTeX distribution and latexmk. The official class and bibliography style are included.

```sh
cd manuscript
TEXINPUTS=.//: BSTINPUTS=.//: latexmk -gg -pdf -jobname=main -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex
cd ..
python3 research/check_outlier_charges_pass2.py
python3 audit/referee-8513177dc0bb-check.py
```

The rebuilt PDF is output/pdf/main.pdf. Primary-literature full texts are not redistributed; citations and bounded verification reports retain source URLs. Raw browsing caches are also omitted. Their original hashes remain in the internal evidence snapshot and delivery manifest. Use the standalone checkers listed above; internal snapshot checks may additionally require those caches.
