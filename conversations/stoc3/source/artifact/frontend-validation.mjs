import fs from 'node:fs';import {parseTS,parseScala} from './frontends.mjs';import {subtype} from './core.mjs';
let a=parseTS('interface A { next: A; payload: never } interface B { next: B; payload: unknown }');let b=parseScala('type A = { val next: A; val payload: Nothing }; type B = { val next: B; val payload: Any }');
if(a.roots.length!==2||b.roots.length!==2)throw Error('parse');for(let x of [a,b]){let [A,B]=x.roots;if(!subtype(x.g,x.g,A.id,B.id).ok||subtype(x.g,x.g,B.id,A.id).ok)throw Error('subtype');}
fs.writeFileSync(new URL('frontend-validation.json',import.meta.url),JSON.stringify({typescript:true,scalaSubset:true,queries:4},null,2));
