"""Version and package the executable source and complete raw evidence."""
import hashlib,json
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
here=Path(__file__).resolve().parent
names=['treeflow.py','trace_support.py','validate.py','audit_records.py','pack_artifact.py',
       'make_table.py','README.md','runtime.json','validation_results.json','record_audit.json']
files=[here/n for n in names]+sorted((here/'records').glob('*.jsonl'))
manifest={'revision':'treeflow-v2','sha256':{str(p.relative_to(here)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(here/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
with ZipFile(here/'treeflow-artifact-v2.zip','w',ZIP_DEFLATED) as archive:
    for p in files+[here/'MANIFEST.json']:
        archive.write(p,str(p.relative_to(here)))
print('Packed treeflow-artifact-v2.zip:',(here/'treeflow-artifact-v2.zip').stat().st_size,'bytes')
