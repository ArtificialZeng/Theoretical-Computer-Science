"""Deterministic writing checks; no claim of mathematical certification."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

snapshot = json.loads((ROOT / 'audit/snapshot.json').read_text())
unchanged = all(sha(ROOT / name) == digest for name, digest in snapshot['files'].items())
official = Path('/Users/mac/Documents/ChatGPT/STOC理论计算机/templates/acm-official/distribution/acmart/acmart.cls')
pdf = ROOT / 'manuscript/bounded-exponent-3sum-working_paper.pdf'
info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
text = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
log = (ROOT / 'manuscript/build/main.log').read_text()
biblog = (ROOT / 'manuscript/build/main.blg').read_text()
bbl = (ROOT / 'manuscript/build/main.bbl').read_text()
source = (ROOT / 'manuscript/main.tex').read_text()
assessment = json.loads((ROOT / 'audit/stoc-assessment.json').read_text())
checks = {
    'all_frozen_mathematical_inputs_unchanged': unchanged,
    'source_sha256': sha(ROOT / 'source.md'),
    'official_acmart_byte_identical': sha(official) == sha(ROOT / 'manuscript/acmart.cls'),
    'pdf_exists': pdf.is_file(),
    'pdf_pages': pages,
    'within_12_total_pages': pages <= 12,
    'letter_size': bool(re.search(r'^Page size:\s+612 x 792 pts', info, re.M)),
    'unencrypted': bool(re.search(r'^Encrypted:\s+no', info, re.M)),
    'no_undefined_or_overfull': not bool(re.search(r'undefined|Overfull|Fatal error|LaTeX Error|Class acmart Error', log)),
    'no_bibtex_warnings': 'Warning--' not in biblog,
    'reference_count': bbl.count('\\bibitem'),
    'primary_reference_links': bbl.count('https://arxiv.org/abs/') == 3,
    'sole_supplied_author_in_source': source.count('\\author{') == 1 and '\\author{Zijian Zeng}' in source,
    'supplied_affiliation_email_in_pdf': 'UCSI University' in text and '1002266693@ucsiuniversity.edu.my' in text,
    'body_material_ai_disclosure': '\\paragraph{Research methodology.}' in source,
    'end_ai_methodology': '\\section*{AI methodology statement}' in source,
    'no_internal_job_or_snapshot_in_pdf': 'c034-group3sum' not in text and snapshot['digest'] not in text,
    'readiness_label': assessment['verdict'],
    'assessment_binds_accepted_snapshot': assessment['snapshot_digest'] == snapshot['digest'],
    'pdf_sha256': sha(pdf),
    'final_warning': 'Unused global option [natbib=false] forwarded by acmart to amsart; recognized by acmart, no missing citations or layout defect.',
}
required = [
    'all_frozen_mathematical_inputs_unchanged', 'official_acmart_byte_identical',
    'pdf_exists', 'within_12_total_pages', 'letter_size', 'unencrypted',
    'no_undefined_or_overfull', 'no_bibtex_warnings', 'primary_reference_links',
    'sole_supplied_author_in_source', 'supplied_affiliation_email_in_pdf',
    'body_material_ai_disclosure', 'end_ai_methodology',
    'no_internal_job_or_snapshot_in_pdf', 'assessment_binds_accepted_snapshot',
]
checks['ok'] = all(checks[k] for k in required) and checks['readiness_label'] == 'working_paper'
(ROOT / 'evidence/write-final-checks.json').write_text(json.dumps(checks, indent=2) + '\n')
print(json.dumps(checks, indent=2))
raise SystemExit(0 if checks['ok'] else 1)
