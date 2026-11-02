# AON working paper source package

Classification: working_paper, as assessed in the included audit/stoc-assessment.json.
From manuscript/, run make clean and then make all with TeX Live, latexmk, pdflatex and bibtex installed.
The PDF target is manuscript/build/aonflow-working_paper.pdf.
For finite diagnostic checks run python evidence/research-2-check.py from the package root.
The checker overwrites only the extracted copy of evidence/research-2-check-results.json. It does not implement the complete algorithm or certify the theorem.
The complete local research dossier and third-party source PDFs are not included; this package does not claim to reproduce full-dossier integrity checks.
The manuscript states its complete proof and primary dependencies. No external submission is authorized.
