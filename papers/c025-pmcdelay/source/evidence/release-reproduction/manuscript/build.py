#!/usr/bin/env python3
"""Build the manuscript locally using an installed TeX distribution."""
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
for command in (
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
    ["bibtex", "main"],
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
):
    result = subprocess.run(command, cwd=HERE, capture_output=True, text=True, timeout=90)
    if result.returncode:
        print(result.stdout[-10000:])
        print(result.stderr[-2000:])
        raise SystemExit(result.returncode)
print("Built manuscript/main.pdf")
