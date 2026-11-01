import fs from 'node:fs';import {Graph,minimize,subtype,ovGraphs} from './core.mjs';import {minimizeSplitter} from './splitter.mjs';
let seed=20271031,tests=0;const rng=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n;};
for(let trial=0;trial<3000;trial++){
 const g=new Graph();let count=2+rng(25);for(let i=2;i<count;i++)g.add(['rec','fun','atom'][rng(3)],{},String(rng(3)));
 for(let i=2;i<count;i++){let v=g.nodes[i];if(v.kind==='fun')v.edges={dom:rng(count),cod:rng(count)};if(v.kind==='rec')for(let k of ['a','b','c'])if(rng(2))v.edges[k]=rng(count);}
 let root=rng(count),a=minimize(g,root),b=minimizeSplitter(g,root);
 if(a.size!==b.size||!subtype(a.g,b.g,a.root,b.root).ok||!subtype(b.g,a.g,b.root,a.root).ok)throw Error('splitter vs Moore mismatch');
 // Every same-output successor class must be coherent within each final block.
 let signatures=new Map();for(let [u,c] of b.classes){let v=g.nodes[u],s=JSON.stringify([v.kind,v.atom,Object.entries(v.edges).sort().map(([k,t])=>[k,b.classes.get(t)])]);if(signatures.has(c)&&signatures.get(c)!==s)throw Error('unstable partition');signatures.set(c,s);}
 tests++;
}
fs.writeFileSync(new URL('splitter-validation.json',import.meta.url),JSON.stringify({seed:20271031,randomGraphs:tests,passed:true},null,2));console.log('Splitter validated on',tests,'random graphs');
