import {equal,subtype} from './core.mjs';
import {minimizeSplitter} from './splitter.mjs';
export function runMuSub(g,h,s,t){
 const now=()=>process.hrtime.bigint(),elapsed=start=>Number(now()-start)/1e6;
 const wallStart=now();let start=now(),eq=equal(g,h,s,t),equalityMs=elapsed(start);
 if(eq.ok)return {ok:true,pairs:0,equalityMs,minimizationMs:0,searchMs:0,totalMs:equalityMs};
 start=now();let a=minimizeSplitter(g,s),b=minimizeSplitter(h,t),minimizationMs=elapsed(start);
 start=now();let result=subtype(a.g,b.g,a.root,b.root),searchMs=elapsed(start);
 return {...result,equalityMs,minimizationMs,searchMs,totalMs:elapsed(wallStart),
 quotient:[a.size,b.size],refinementStats:[a.stats,b.stats]};
}
