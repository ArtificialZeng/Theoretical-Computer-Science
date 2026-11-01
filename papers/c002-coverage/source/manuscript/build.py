#!/usr/bin/env python3
"""Clean, foreground-only local build of the accepted manuscript."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"
DESTINATION = ROOT / "output/pdf/sparse-coverage-discrepancy.pdf"
env = dict(os.environ)
env["TEXINPUTS"] = "./vendor:" + env.get("TEXINPUTS", "")
env["BSTINPUTS"] = "./vendor:" + env.get("BSTINPUTS", "")
commands = [
    ["latexmk", "-C", "main.tex"],
    ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
]
with (ROOT / "evidence/write-build.log").open("w") as log:
    for command in commands:
        print("COMMAND: " + " ".join(command), file=log, flush=True)
        subprocess.run(command, cwd=MANUSCRIPT, env=env, stdout=log,
                       stderr=subprocess.STDOUT, check=True)
DESTINATION.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(MANUSCRIPT / "main.pdf", DESTINATION)
record = {
    "job_id": "c002-coverage-write-64c05c6e47b4",
    "commands": commands,
    "cwd": "manuscript",
    "TEXINPUTS": "./vendor:",
    "BSTINPUTS": "./vendor:",
    "pdf": str(DESTINATION.relative_to(ROOT)),
    "pdf_sha256": hashlib.sha256(DESTINATION.read_bytes()).hexdigest(),
    "bytes": DESTINATION.stat().st_size,
}
(ROOT / "evidence/write-build.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
