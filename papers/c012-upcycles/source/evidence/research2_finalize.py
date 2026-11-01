"""Save actual usage and integrity without modifying any earlier pass records."""
from collections import Counter
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path

JOB='c012-upcycles-research-456cb4499028'
FIRST=datetime.fromisoformat('2026-11-01T04:50:16+00:00')
EXPECTED='773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path,value):
    Path(path).write_text(json.dumps(value,indent=2)+'\n')


def main():
    assert sha('source.md')==EXPECTED
    summaries=[]
    records=[]
    for path in sorted(Path('evidence/research2-connectivity').glob('*.result.json')):
        data=json.loads(path.read_text())
        summaries.append(dict(path=str(path),label=data['label'],outcome=data['outcome'],
                              rounds=len(data['rounds']),solver_wall_seconds=data['solver_wall_seconds']))
        for r in data['rounds']:
            records.append(dict(label=data['label'],**r))
    assert len(records)==10
    assert Counter(r['status'] for r in records)=={'SAT':8,'UNSAT':2}
    target=json.loads(Path('evidence/research2-connectivity/n12d3_period4.result.json').read_text())
    assert target['outcome']=='connected-witness' and target['original_question_resolved']
    assert len(target['rounds'])<=20 and target['solver_wall_seconds']<=180
    assert [r['component_count'] for r in target['rounds']]==[22,32,1]
    proofchecks=[r['proof_check'] for r in records if 'proof_check' in r]
    for path in proofchecks:
        c=json.loads(Path(path).read_text())
        assert c['checked_empty_clause'] and sha(c['cnf'])==c['cnf_sha256']
        assert sha(c['proof'])==c['proof_sha256']
    witness=json.loads(Path('evidence/research2-witness/witness.json').read_text())
    from_digits=''.join('*'+format(int(c),'03b') for c in witness['pane_representation'])
    assert witness['word']==from_digits==Path('evidence/research2-witness/word.txt').read_text().strip()
    assert hashlib.sha256(from_digits.encode()).hexdigest()==witness['word_sha256']
    inv=json.loads(Path('evidence/research2-witness/inverse-coverage.json').read_text())
    assert inv['coverage_counts']==[1]*4096
    assert Counter(inv['unique_start_by_lexicographic_total_word'])=={i:8 for i in range(512)}
    old=json.loads(Path('evidence/research1-integrity.json').read_text())
    preserved=[]
    for path,data in old['files'].items():
        if path in ['problem.md','checkpoint.md']:
            continue
        assert Path(path).is_file(),path
        assert sha(path)==data['sha256'],path
        preserved.append(path)
    assert sha('evidence/research2-checkpoint-before.md')==old['files']['checkpoint.md']['sha256']
    claim=json.loads(Path('claim.json').read_text())
    assert claim['kind']=='resolution-paper' and claim['original_status']=='proved'
    assert claim['proposer_job_id']==JOB and 'candidate_kind' not in claim and 'scope' not in claim
    assert {'source.md','problem.md'}<=set(claim['evidence_files'])
    assert all(Path(p).is_file() for p in claim['evidence_files'])
    now=datetime.now(timezone.utc)
    usage=dict(job_id=JOB,role='research',research_pass=2,budget_seconds=1500,
               first_observed_clock_utc=FIRST.isoformat(),completed_utc=now.isoformat(),
               elapsed_since_first_observed_clock_seconds=(now-FIRST).total_seconds(),
               timing_limit='First observed tool clock is not an exact session-start measurement; job completed well below its ceiling.',
               research_passes_consumed=2,research_passes_remaining_under_default_ceiling=1,
               previous_usage_preserved='evidence/research1-usage.json',
               solver_runs=len(records),solver_status_counts=dict(Counter(r['status'] for r in records)),
               measured_solver_wall_seconds=sum(r['elapsed_seconds'] for r in records),
               measured_solver_child_cpu_seconds=sum(r['child_cpu_seconds'] for r in records),
               target_solver_wall_seconds=target['solver_wall_seconds'],
               target_refinement_rounds=2,target_solver_calls=3,
               timeout_count=sum(r['wall_timeout'] for r in records),
               independent_CNF_proof_checks=proofchecks,
               standalone_verification='evidence/research2-witness/standalone-verification.json',
               subagents_or_background_workers_started=0,dependency_changes=[],
               token_usage='not exposed to this worker; no invented token count',
               operational_failures=['One combined apply_patch was rejected because deleting and adding checkpoint.md targeted the same file twice. No changes from that rejected patch; retried with separate updates. No mathematical attempt or counter was affected.'],
               mathematical_attempts=[
                   dict(route='guarded connectivity refinement',status='exact-positive-witness',
                        scope='binary n12d3 single upcycle; positive existential full-scope resolution proposed',
                        evidence='evidence/research2-proof.md'),
                   dict(route='known n8d2 negative benchmark',status='proved-obstruction',
                        scope='fixed binary n8d2 period-four frame only',
                        evidence='evidence/research2-connectivity/negative_n8d2_period4.r02.proof-check.json')],
               summary_records=summaries,solver_records=records,
               fresh_referee_performed=False,manuscript_or_pdf_created=False)
    save('evidence/research2-usage.json',usage)
    # Only new evidence and expected state changes; do not rehash credentials or
    # unrelated files, and do not overwrite the earlier integrity inventory.
    paths=[Path('source.md'),Path('problem.md'),Path('checkpoint.md'),Path('claim.json')]
    paths+=sorted(Path('evidence').glob('research2*'))
    all_files=[]
    for path in paths:
        all_files.extend([path] if path.is_file() else sorted(p for p in path.rglob('*') if p.is_file()))
    files={str(p):dict(bytes=p.stat().st_size,sha256=sha(p)) for p in all_files
           if str(p)!='evidence/research2-integrity.json'}
    integrity=dict(job_id=JOB,source_sha256=sha('source.md'),source_unchanged=True,
                   prior_pass_files_preserved_count=len(preserved),prior_pass_files_verified=preserved,
                   previous_checkpoint_preserved=True,claim_evidence_files_exist=True,
                   exact_word_encodings_agree=True,coverage_array_all_ones=True,
                   every_cyclic_start_covers_eight_words=True,
                   manuscript_or_pdf_created=False,review_or_acceptance_claimed=False,files=files)
    save('evidence/research2-integrity.json',integrity)
    print(json.dumps(dict(job_id=JOB,source_unchanged=True,prior_files_preserved=len(preserved),
                          solver_runs=len(records),solver_wall_seconds=usage['measured_solver_wall_seconds'],
                          elapsed_seconds=usage['elapsed_since_first_observed_clock_seconds'],
                          evidence_files=len(files),claim_kind=claim['kind'])))


if __name__=='__main__':
    main()
