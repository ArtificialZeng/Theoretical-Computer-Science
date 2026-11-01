#!/usr/bin/env python3
"""Build the pinned, unmodified ELINA scalar kernel on macOS or Linux."""
import os,pathlib,platform,subprocess,sys,json
base=pathlib.Path(__file__).resolve().parent;vendor=base/'vendor/ELINA'
cc=os.environ.get('CC','clang' if platform.system()=='Darwin' else 'cc')
cmd=[cc,('-dynamiclib' if platform.system()=='Darwin' else '-shared'),'-fPIC','-O3','-std=c99','-Wno-incompatible-function-pointer-types']
for d in ['elina_oct','elina_auxiliary','elina_linearize','partitions_api']:cmd+=['-I'+str(vendor/d)]
for d in ['/opt/homebrew/include','/usr/local/include']:
 if pathlib.Path(d).exists():cmd+=['-I'+d]
suffix='.dylib' if platform.system()=='Darwin' else '.so'
cmd+=[str(vendor/'elina_oct/opt_oct_closure_dense_scalar.c'),'-lm','-o',str(base/('elina_scalar'+suffix))]
print(json.dumps({'command':cmd,'platform':platform.platform()}),flush=True);subprocess.run(cmd,check=True)
