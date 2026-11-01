from pathlib import Path
import json,hashlib,zipfile
root=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
artifact=[p for p in (root/'artifact').iterdir() if p.suffix in ['.py','.json','.gz','.tex'] and p.name not in ['MANIFEST.json']]
artifact+=list((root/'artifact/logs').glob('*.log'))
artifact+=[root/p for p in json.loads((root/'artifact/vendor_files.json').read_text())]
# Exclude full-build logs from the initial exploratory library build; ship actual scalar/check logs.
artifact=[p for p in artifact if p.name not in ['elina-configure.log','elina-build.log','elina-build-retry.log']]
manifest={str(p.relative_to(root)):sha(p) for p in sorted(set(artifact))}
(root/'artifact/MANIFEST.json').write_text(json.dumps({'sha256':manifest,'scope':'artifact sources, actual fixtures/results/logs and pinned kernel subset; manifest itself excluded'},indent=2)+'\n')
files=[root/p for p in ['5.tex','5.bbl','authors.tex','references.bib','acmart.cls','alphaurl.bst','ACM-Reference-Format.bst','LICENSE','Makefile.octafine','README.octafine.md','estimated_values.md','submission_readiness.md','response_to_reviewers.md','figures/framework.tex','figures/incremental.tex','research/reference_audit.tsv','research/proof_audit.md','research/2026_literature_check.md','research/2026_source_hashes.json','revision/format_verification.json','revision/package_revision.py','artifact/MANIFEST.json']]
files+=artifact;files+=list((root/'research/sources').glob('*.crossref.json'))
files=sorted(set(files))
(root/'source_manifest.json').write_text(json.dumps({str(p.relative_to(root)):sha(p) for p in files},indent=2)+'\n');files.append(root/'source_manifest.json')
with zipfile.ZipFile(root/'5_source.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in files:z.write(p,str(p.relative_to(root)))
 assert z.testzip() is None
with zipfile.ZipFile(root/'5_source.zip') as z:z.extractall(root/'build/review-package-check')
print('Packaged',len(files),'files;', (root/'5_source.zip').stat().st_size,'bytes')
