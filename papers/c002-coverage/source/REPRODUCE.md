# Clean build and finite reproduction

Run from the extracted source root. The two mathematical checkers use only the Python standard library; their finite checks supplement the written proof. Run on a copy: scripts regenerate their diagnostic JSON outputs.

The manuscript build requires a working LaTeX distribution and latexmk. The official class and bibliography style are included.

```sh
cd manuscript
TEXINPUTS="vendor//:" BSTINPUTS="vendor//:" latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex
cd ..
python3 evidence/research_rounding_check.py
python3 audit/referee_verify.py
```

The rebuilt PDF is output/pdf/main.pdf. Primary-literature full texts are not redistributed; citations and bounded verification reports retain source URLs.
