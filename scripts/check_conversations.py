#!/usr/bin/env python3
"""Verify and reproduce the five existing parallel-conversation packages."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def run(command, cwd, timeout, environment=None):
    try:
        p = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr
    except FileNotFoundError:
        return 127, ('Required executable not found: '+command[0]+'\n').encode()
    except subprocess.TimeoutExpired as e:
        return 124, (e.stdout or b'') + (e.stderr or b'') + b'\nTIMEOUT\n'


def verify(p):
    for key, digest in [('pdf','pdf_sha256'),('source_archive','source_archive_sha256')]:
        assert hashlib.sha256((ROOT / p[key]).read_bytes()).hexdigest() == p[digest]
    source = ROOT / p['source_directory']
    with zipfile.ZipFile(ROOT / p['source_archive']) as archive:
        expected = set()
        for item in archive.infolist():
            if item.is_dir():
                continue
            assert item.filename.startswith(p['archive_prefix'])
            relative = PurePosixPath(item.filename[len(p['archive_prefix']):])
            assert not relative.is_absolute() and '..' not in relative.parts
            expected.add(str(relative))
            assert (source / str(relative)).read_bytes() == archive.read(item)
        actual = {f.relative_to(source).as_posix() for f in source.rglob('*') if f.is_file()}
        assert expected == actual
    return len(expected)


def check(p, args, destination):
    started = time.monotonic()
    count = verify(p)
    steps = []
    with tempfile.TemporaryDirectory(prefix='conversation-check-') as temporary:
        source = Path(temporary) / 'source'
        shutil.copytree(ROOT / p['source_directory'], source)
        python = sys.executable
        dylib = 'libviable.dylib' if sys.platform == 'darwin' else 'libviable.so'
        commands = {
            'stoc1': [('artifact',['rustc','--edition','2021','--crate-type','cdylib','-O','viable.rs','-o',dylib]),('artifact',[python,'-B','verify.py']),('artifact',[python,'-B','verify_blocks.py'])],
            'stoc2': [('.', [python,'-B','research/code/verify.py']),('.', [python,'-B','research/code/check_indexed.py'])],
            'stoc3': [('artifact',['npm','ci','--ignore-scripts']),('artifact',['npm','test'])],
            'stoc4': [('.', [python,'-B','artifact/validate.py']),('.', [python,'-B','artifact/audit_records.py'])],
            'stoc5': [('.', [python,'-B','artifact/build_elina.py']),('.', [python,'-B','artifact/replay_cases.py'])]
        }
        if args.mode in ('all','math'):
            for i,(directory,command) in enumerate(commands[p['id']],1):
                code, output = run(command,source/directory,args.timeout)
                log = destination / f"{p['id']}-math-{i}.log"
                log.write_bytes(output.replace(str(Path(temporary).resolve()).encode(),b'<temporary>'))
                steps.append({'stage':'finite-reproduction','command':[('python3' if x==python else x) for x in command],'cwd':directory,'exit_code':code,'log':log.relative_to(ROOT).as_posix()})
                if code:
                    break
    # A separate fresh copy avoids changing measured/generated table inputs.
    if args.mode in ('all','build'):
        with tempfile.TemporaryDirectory(prefix='conversation-build-') as temporary:
            source = Path(temporary) / 'source'
            shutil.copytree(ROOT / p['source_directory'],source)
            for suffix in ('.aux','.bbl','.blg','.fdb_latexmk','.fls','.out','.toc'):
                for f in source.rglob('*'+suffix):
                    f.unlink()
            index = p['id'].replace('stoc','')
            environment = os.environ.copy()
            environment['TEXINPUTS'] = './/:'
            environment['BSTINPUTS'] = './/:'
            command = ['latexmk','-gg','-pdf','-interaction=nonstopmode','-halt-on-error','-outdir=build',index+'.tex']
            code,output = run(command,source,args.timeout,environment)
            built = source/'build'/(index+'.pdf')
            equal = False
            if code==0 and built.exists():
                texts=[]
                for path in (built,ROOT/p['pdf']):
                    text = subprocess.check_output(['pdftotext',str(path),'-'])
                    texts.append(re.sub(rb'\s+',b' ',text).strip())
                equal=texts[0]==texts[1]
            log=destination/(p['id']+'-build.log')
            log.write_bytes(output.replace(str(Path(temporary).resolve()).encode(),b'<temporary>'))
            steps.append({'stage':'clean-build','exit_code':code,'normalized_pdf_text_matches_release':equal,'log':log.relative_to(ROOT).as_posix()})
    passed=all(x['exit_code']==0 and x.get('normalized_pdf_text_matches_release',True) for x in steps)
    print(p['id']+': '+('PASS' if passed else 'FAIL'),flush=True)
    return {'id':p['id'],'passed':passed,'archive_files_verified':count,'seconds':round(time.monotonic()-started,3),'steps':steps}


def main():
    if sys.version_info<(3,10):
        raise SystemExit('Python 3.10+ required')
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--all',action='store_true')
    group.add_argument('--paper',choices=['stoc'+str(i) for i in range(1,6)])
    parser.add_argument('--mode',choices=['all','verify','math','build'],default='all')
    parser.add_argument('--jobs',type=int,default=2)
    parser.add_argument('--timeout',type=int,default=600)
    args=parser.parse_args()
    papers=[p for p in json.loads((ROOT/'conversation-catalog.json').read_text())['items'] if p['kind']=='existing-conversation-manuscript' and (args.all or p['id']==args.paper)]
    destination=ROOT/'validation/conversations'
    destination.mkdir(parents=True,exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        records=list(executor.map(lambda p:check(p,args,destination),papers))
    passed=all(x['passed'] for x in records)
    (destination/('summary-'+args.mode+'.json')).write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'passed':passed,'scope':'Artifact hashes, finite code checks and PDF compilation only; not a new full mathematical/novelty review','python':sys.version,'papers':records},indent=2)+'\n')
    raise SystemExit(0 if passed else 1)


if __name__=='__main__':
    main()
