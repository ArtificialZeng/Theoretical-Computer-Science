#!/usr/bin/env python3
"""Clean portability rerun of unchanged finite cases; not a new research pass."""
from pathlib import Path
import ast,hashlib,json,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent
SCRIPTS=['research-67929c1f9552-flow-test.py', 'research-67929c1f9552-return-test.py', 'research-c6b2b0ea3f71-core-test.py', 'research-2396269cbd5d-energy-test.py', 'research-2396269cbd5d-sharing-test.py', 'research-2396269cbd5d-independent-check.py', 'research-960416a85f25-selector-test.py', 'research-960416a85f25-certificate-test.py']
PREFIX="research-960416a85f25"
SELECTOR_SHA="d588ed92931171afb4ea689f633acaaf50f6882cf7a50a7108b5caabd2e60c38"
GUARD="assert now < datetime.datetime(2026,11,3,21,30,tzinfo=datetime.timezone.utc)"
def adapt_operational_deadline(code):
    path=code/(PREFIX+"-selector-test.py");source=path.read_text()
    assert hashlib.sha256(path.read_bytes()).hexdigest()==SELECTOR_SHA
    tree=ast.parse(source)
    matches=[node for node in ast.walk(tree) if isinstance(node,ast.Assert) and ast.get_source_segment(source,node)==GUARD]
    assert len(matches)==1 and source.count(GUARD)==1
    original_assertions=[ast.dump(node,include_attributes=False) for node in ast.walk(tree) if isinstance(node,ast.Assert) and node is not matches[0]]
    portable=source.replace(GUARD,"pass  # Portable replay: expired operational deadline only.")
    remaining_assertions=[ast.dump(node,include_attributes=False) for node in ast.walk(ast.parse(portable)) if isinstance(node,ast.Assert)]
    assert remaining_assertions==original_assertions
    path.write_text(portable)
    return {"original_source_sha256":SELECTOR_SHA,"temporary_source_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"removed_operational_assertions":1,"mathematical_assertions_retained":len(remaining_assertions)}
def main():
    compiler=next((shutil.which(x) for x in ["c++","clang++","g++"] if shutil.which(x)),None)
    if not compiler:raise SystemExit("A C++17 compiler is required")
    rows=[]
    with tempfile.TemporaryDirectory(prefix="c049-records-v2-") as temporary:
        code=Path(temporary)/"code";shutil.copytree(ROOT/"code",code)
        adaptation=adapt_operational_deadline(code)
        for stem in [PREFIX+"-allfault",PREFIX+"-verify"]:
            run=subprocess.run([compiler,"-std=c++17","-O2",str(code/(stem+".cpp")),"-o",str(code/stem)],capture_output=True,text=True,timeout=120)
            if run.returncode:print(run.stderr[-2000:]);return run.returncode
        for name in SCRIPTS:
            run=subprocess.run([sys.executable,"-B",name],cwd=code,capture_output=True,text=True,timeout=180)
            rows.append({"script":name,"exit_code":run.returncode})
            print(name+": "+("PASS" if run.returncode==0 else "FAIL"),flush=True)
            if run.returncode:print(run.stdout[-1500:]);print(run.stderr[-1500:]);break
    passed=len(rows)==len(SCRIPTS) and all(x["exit_code"]==0 for x in rows)
    print(json.dumps({"passed":passed,"original_status":"unresolved","declared_finite_checks_only":True,"cpp_clean_builds":2,"operational_deadline_adapter":adaptation,"checks":rows},indent=2))
    return 0 if passed else 1
if __name__=="__main__":raise SystemExit(main())
