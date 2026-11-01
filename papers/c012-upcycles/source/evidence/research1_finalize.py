"""Summarize actual saved solver records and bind the evidence to frozen source."""
import hashlib
import json
from pathlib import Path
import re
from datetime import datetime, timezone


def main():
    start=datetime.fromisoformat('2026-11-01T04:32:47+00:00')
    now=datetime.now(timezone.utc)
    records=[]
    for directory in ['research1-sat','research1-relaxation','research1-euler']:
        for path in sorted((Path('evidence')/directory).glob('*.result.json')):
            r=json.loads(path.read_text())
            r['record_path']=str(path)
            log=Path(r['log']).read_text()
            m=re.search(r'total process time since initialization:\s*([0-9.]+)',log)
            r['solver_logged_cpu_seconds']=float(m.group(1)) if m else None
            records.append(r)
    usage=dict(
        job_id='c012-upcycles-research-cfe911474960',role='research',research_pass=1,
        budget_seconds=1500,first_observed_clock_utc=start.isoformat(),completed_at_utc=now.isoformat(),
        elapsed_since_first_observed_clock_seconds=(now-start).total_seconds(),
        timing_limit='First observed tool clock is not exact session start; completion is well below the 25-minute ceiling.',
        research_passes_consumed=1,research_passes_remaining_under_default_ceiling=2,
        sat_solver_runs=len(records),
        solver_status_counts={s:sum(r['status']==s for r in records) for s in ['SAT','UNSAT','unknown']},
        measured_solver_wall_seconds=sum(r['elapsed_seconds'] for r in records),
        solver_logged_cpu_seconds=sum(r['solver_logged_cpu_seconds'] or 0 for r in records),
        solver_logged_cpu_limit='Sum of rounded CaDiCaL log values; individual child CPU also recorded where collected.',
        token_usage='not exposed to this worker; no invented count',
        subagents_or_background_workers_started=0,dependency_changes=[],
        certificate_checks='17 unique original UNSAT CNFs; first target additionally checked once before aggregate run. One tiny genuine certificate accepted and three invalid certificates rejected as controls. No independent referee context or external peer review.',
        mathematical_attempts=[
            dict(route='Global-position exact XOR CNFs for eight n8 masks',label='proved-obstruction',
                 scope='Finite encodings and symmetry-complete binary n8 d2/d3 exclusion only',
                 evidence='evidence/research1-proof-checks.json'),
            dict(route='Balanced tiling relaxation',label='proved-obstruction',
                 scope='All four surviving n8d3 frame classes fail balanced tiling; all four n8d2 classes have verified balanced tilings',
                 evidence='evidence/research1-relaxation-proof-checks.json'),
            dict(route='Private-subset Fourier constraints',label='observed-failure',
                 scope='Normalized local codes remain, so these necessary constraints alone do not give an obstruction. Initial and reproduced runs retained.',
                 evidence='evidence/research1-private-fourier-reproduced.json'),
            dict(route='Exact tile cover plus literal Euler balance',label='unknown',
                 scope='n12d3 cycle cover found; connectedness not searched. Models alone are multiple cycles, not upcycles.',
                 evidence='evidence/research1-euler/n12d3_period4.family-verification.json')],
        intentional_negative_controls='Three pinned CNF corruptions, one Euler pin corruption; checker rejects three invalid/incomplete certificate controls.',
        operational_failures=[
            'Initial rg inventory named nonexistent tools/ directory and exited 2; requested files read and solver binaries found subsequently.',
            'Checker utility inventory found no standalone drat/lrat checker executable; implemented a separate inspectable RUP-only LRAT checker.',
            'First problem.md append patch used an absent anchor and failed without changing that file; retried with its actual final line. No mathematical attempt affected.'],
        solver_records=records,prior_usage_preserved='evidence/triage-usage.json')
    Path('evidence/research1-usage.json').write_text(json.dumps(usage,indent=2)+'\n')
    expected='773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac'
    source_hash=hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
    assert source_hash==expected
    checks=[]
    for r in records:
        for key in ['cnf','encoding','log','proof']:
            assert Path(r[key]).is_file()
        if r['status']=='UNSAT':
            path=Path(r['record_path'].replace('.result.json','.proof-check.json'))
            v=json.loads(path.read_text())
            assert v['checked_empty_clause']
            assert v['cnf_sha256']==hashlib.sha256(Path(r['cnf']).read_bytes()).hexdigest()
            assert v['proof_sha256']==hashlib.sha256(Path(r['proof']).read_bytes()).hexdigest()
            checks.append(str(path))
        elif r['status']=='SAT':
            assert Path(r['model_verification']).is_file()
    files=[p for p in Path('evidence').rglob('research1*') if p.is_file() and '__pycache__' not in str(p)]
    for directory in ['research1-sat','research1-relaxation','research1-euler','research1-checker-controls']:
        files.extend(p for p in (Path('evidence')/directory).rglob('*') if p.is_file())
    files.extend([Path('problem.md'),Path('checkpoint.md'),Path('source.md')])
    manifest={str(p):dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
              for p in sorted(set(files)) if p.name!='research1-integrity.json'}
    integrity=dict(job_id='c012-upcycles-research-cfe911474960',source_sha256=source_hash,
                   source_unchanged=True,solver_results=len(records),
                   unsat_certificates_independently_checked=len(checks),certificate_checks=checks,
                   manuscript_or_pdf_created=False,claim_created=False,files=manifest)
    assert not Path('claim.json').exists()
    Path('evidence/research1-integrity.json').write_text(json.dumps(integrity,indent=2)+'\n')
    print(json.dumps({k:usage[k] for k in ['sat_solver_runs','solver_status_counts',
          'measured_solver_wall_seconds','solver_logged_cpu_seconds','elapsed_since_first_observed_clock_seconds']}))
    print(json.dumps(dict(source_unchanged=True,checked_unsat_certificates=len(checks),manifest_files=len(manifest))))


if __name__=='__main__':
    main()
