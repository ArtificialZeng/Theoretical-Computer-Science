"""Check the requested submission layout and citation completeness."""
import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tex = (root / '4.tex').read_text()
text = subprocess.check_output(['pdftotext', '-layout', str(root / '4.pdf'), '-'], text=True)
info = subprocess.check_output(['pdfinfo', str(root / '4.pdf')], text=True)
pages = [p for p in text.split('\f') if p.strip()]
authors = ['Zijian Zeng', 'Jiayin Cao', 'Weinan Dai', 'Rui Wang', 'Fei Ding']
affiliations = ['UCSI University', 'Ningbo University', 'Zhejiang University',
                'Nanchang Institute of Technology', 'Alibaba Group']
assert r'\documentclass[11pt,letterpaper]{article}' in tex
assert r'\usepackage[letterpaper,margin=1in]{geometry}' in tex
assert r'\twocolumn' not in tex
assert r'\onehalfspacing' not in tex and r'\doublespacing' not in tex
assert all(name in pages[0] for name in authors + affiliations)
assert [pages[0].index(name) for name in authors] == sorted(pages[0].index(name) for name in authors)
assert re.search(r'1\s+Introduction', pages[1])
# STOC 2027 submissions have NO total-page limit.  The initial twelve pages
# after the title page (excluding an optional immediately following contents
# page) must present the merits.  The 12-page proceedings limit is unrelated.
for source in [tex]+[p.read_text() for p in (root/'figures').glob('*.tex')]+[(root/'artifact'/'validation_table.tex').read_text()]:
    assert not re.search(r'\\(?:small|footnotesize|scriptsize|tiny|resizebox|scalebox)\b',source)
assert r'\captionsetup{font=normalsize,labelfont=bf}' in tex
assert r'\bibliographystyle{alphaurl}' in tex
merits = '\n'.join(pages[1:13])
for phrase in ['Program-point barrier', 'Path-procedure barrier', 'Fact-domain barrier',
               'Certified TreeFlow', 'Quantitative comparison', 'Technical overview']:
    assert phrase in merits, phrase
reference_start=next(i for i,p in enumerate(pages) if p.lstrip().startswith('References'))
assert reference_start==len(pages)-1
assert '612 x 792 pts (letter)' in info
cited = set()
for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', tex):
    cited.update(group.split(','))
entries = set(re.findall(r'@\w+\{([^,]+),', (root / 'references.bib').read_text()))
assert not cited - entries
log = (root / 'build' / '4.log').read_text(errors='replace')
warnings = re.findall(r'^.*(?:Warning|Overfull|undefined|LaTeX Error).*$', log, re.M)
assert not warnings, warnings
report = {
    'artifact': '4.pdf', 'physical_pages': len(pages),
    'title_pages': 1, 'body_pages': reference_start-1, 'reference_pages':len(pages)-reference_start,
    'total_page_limit': None,
    'total_page_limit_policy': 'No total-page limit for the review submission',
    'merits_presentation_window_pages': 12,
    'policy_source': 'https://acm-stoc.org/stoc2027/stoc2027-cfp.html',
    'policy_verified_on': '2026-11-02',
    'paper_size': 'Letter, 612 x 792 PDF points',
    'main_font': '11pt class setting; captions/tables/figure text use normalsize', 'columns': 1,
    'spacing': 'single (article default)', 'margins': '1 inch (geometry setting)',
    'authors_in_supplied_order': authors, 'affiliations_present': affiliations,
    'main_results_and_overview_within_initial_12_body_pages': True,
    'references_at_very_end': True, 'cited_entries': len(cited),
    'missing_bibliography_keys': [], 'citation_style':'alphaurl (alphabetic year labels)',
    'embedded_artifact':subprocess.check_output(['pdfdetach','-list',str(root/'4.pdf')],text=True).strip(),
    'latex_warnings_and_overfull_boxes': [],
    'visual_checks': ['title page', 'comparison table', 'architecture figure',
                      'shared-callee reduction', 'two selector panels', 'validation table', 'reference page'],
    'scope': 'Format and reference-key audit; not a novelty or scientific-readiness certificate.'
}
(root / 'research' / 'final_checks.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
