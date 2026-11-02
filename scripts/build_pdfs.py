#!/usr/bin/env python3
"""Clean-build the primary PDFs of the unified catalog on disposable copies."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode=True
from reproduce import ROOT,select


def pdf_text(path):
    output=subprocess.check_output(['pdftotext',str(path),'-'])
    return re.sub(rb'\s+',b' ',output).strip()


def build(p,timeout,destination):
    if p.get('legacy_check_adapter'):
        from check_conversations import check as original_check
        return original_check(p,argparse.Namespace(mode='build',timeout=timeout),destination)
    started=time.monotonic()
    with tempfile.TemporaryDirectory(prefix='tcs-build-') as temporary:
        source=Path(temporary)/'source'
        shutil.copytree(ROOT/p['source_directory'],source)
        for suffix in ['.aux','.bbl','.blg','.fdb_latexmk','.fls','.out','.toc']:
            for path in source.rglob('*'+suffix):
                path.unlink()
        directory=source/p.get('build_directory','manuscript')
        output=source/'.sync-clean-build'
        environment=os.environ.copy()
        environment['TEXINPUTS']='.//:'
        environment['BSTINPUTS']='.//:'
        tex=p.get('tex_entry','main.tex')
        command=['latexmk','-gg','-pdf','-interaction=nonstopmode','-halt-on-error','-outdir='+str(output),tex]
        try:
            result=subprocess.run(command,cwd=directory,env=environment,capture_output=True,timeout=timeout)
            log_bytes,code=result.stdout+result.stderr,result.returncode
        except subprocess.TimeoutExpired as e:
            log_bytes,code=(e.stdout or b'')+(e.stderr or b'')+b'\nTIMEOUT\n',124
        built=output/(Path(tex).stem+'.pdf')
        equal=code==0 and built.is_file() and pdf_text(built)==pdf_text(ROOT/p['pdf'])
        log=destination/(p['id']+'.log')
        log.write_bytes(log_bytes.replace(str(Path(temporary)).encode(),b'<temporary>'))
        record={'id':p['id'],'passed':bool(equal),'exit_code':code,'normalized_pdf_text_matches_release':bool(equal),
                'seconds':round(time.monotonic()-started,3),'log':log.relative_to(ROOT).as_posix()}
    print(p['id']+': '+('PASS' if equal else 'FAIL'),flush=True)
    return record


def main():
    args,papers=select(argparse.ArgumentParser(description=__doc__))
    for name in ['latexmk','pdftotext']:
        if not shutil.which(name):
            raise SystemExit('Required tool missing: '+name)
    destination=ROOT/'validation/unified-builds'
    destination.mkdir(parents=True,exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        records=list(executor.map(lambda p:build(p,args.timeout,destination),papers))
    passed=all(p['passed'] for p in records)
    summary_name='summary.json' if args.all else 'summary-'+args.paper+'.json'
    (destination/summary_name).write_text(json.dumps({'at_utc':datetime.now(timezone.utc).isoformat(),
        'passed':passed,'scope':'Clean builds and normalized PDF text comparison for the primary indexed versions; no new manuscript editing or mathematical acceptance.',
        'papers':records},indent=2)+'\n')
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
