#!/usr/bin/env python3
"""Clean-build the working paper using only bundled source inputs and TeX Live."""
from pathlib import Path
import hashlib, json, os, shutil, subprocess, tempfile

root = Path(__file__).resolve().parent
inputs = ["main.tex", "references.bib", "acmart.cls", "alphaurl.bst"]
# Pin public document timestamps for repeatable local builds; never print environments.
build_env = os.environ.copy()
build_env.update({"SOURCE_DATE_EPOCH": "1793491200", "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
logs = []
with tempfile.TemporaryDirectory(prefix=".clean-build-", dir=root) as stage_name:
    stage = Path(stage_name)
    for name in inputs:
        shutil.copyfile(root / name, stage / name)
    commands = [
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-recorder", "main.tex"],
        ["bibtex", "main"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-recorder", "main.tex"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-recorder", "main.tex"],
    ]
    for command in commands:
        run = subprocess.run(command, cwd=stage, env=build_env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=60)
        logs.append("COMMAND: " + " ".join(command) + "\n" + run.stdout)
        if run.returncode:
            (root / "build-console.log").write_text("\n".join(logs), encoding="utf-8")
            raise SystemExit("Clean build failed; inspect build-console.log")
    for name in ["main.bbl", "main.log", "main.blg", "main.fls"]:
        shutil.copyfile(stage / name, root / name)
    pdf = root / "optimal-incdec-working_paper.pdf"
    shutil.copyfile(stage / "main.pdf", pdf)
(root / "build-console.log").write_text("\n".join(logs), encoding="utf-8")
final_log = (root / "main.log").read_text(encoding="utf-8")
errors = [line for line in final_log.splitlines()
          if any(s in line for s in ["undefined", "Overfull", "Underfull", "LaTeX Error", "Class acmart Error"])]
if errors:
    raise SystemExit("Unresolved build diagnostics: " + repr(errors))
print(json.dumps({"ok": True, "pdf": pdf.name,
                  "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
                  "clean_build_commands": commands, "unresolved_diagnostics": errors}))
