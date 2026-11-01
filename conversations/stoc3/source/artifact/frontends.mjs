import ts from 'typescript';
import {Graph,reach,minimize} from './core.mjs';
// Accept only closed, monomorphic, file-top-level declarations. Reject unsupported dependencies.
export function parseTS(text,file='input.d.ts'){
 let sf=ts.createSourceFile(file,text,ts.ScriptTarget.Latest,true),decl=new Map(),badNames=new Set(),total=0;
 for(let st of sf.statements)if(ts.isInterfaceDeclaration(st)||ts.isTypeAliasDeclaration(st)){
  total++;let name=st.name.text;if(decl.has(name))badNames.add(name);decl.set(name,st);
 }
 let g=new Graph(),ids=new Map(),status=new Map(),atoms=new Map();
 const atom=k=>{if(!atoms.has(k))atoms.set(k,g.add('atom',{},k));return atoms.get(k);};
 function buildName(name){if(!decl.has(name)||badNames.has(name))throw Error('nonlocal/merged reference');if(status.get(name)==='bad')throw Error('bad dependency');if(ids.has(name))return ids.get(name);
  let d=decl.get(name);if(d.typeParameters?.length||d.heritageClauses?.length)throw Error('generic/heritage');let id=g.add('pending');ids.set(name,id);status.set(name,'building');
  try{let built=ts.isInterfaceDeclaration(d)?record(d.members):build(d.type);g.nodes[id]=g.nodes[built];if(g.nodes[id].kind==='pending')throw Error('unguarded alias');status.set(name,'ok');return id;}catch(e){status.set(name,'bad');throw e;}
 }
 function record(members){let edges={};for(let m of members){if(!ts.isPropertySignature(m)||m.questionToken||!m.type||!m.name||(!ts.isIdentifier(m.name)&&!ts.isStringLiteral(m.name)&&!ts.isNumericLiteral(m.name)))throw Error('unsupported member');let k=m.name.text;if(k in edges)throw Error('duplicate field');edges[k]=build(m.type);}return g.record(edges);}
 function build(x){
  if(ts.isParenthesizedTypeNode(x))return build(x.type);
  if(x.kind===ts.SyntaxKind.UnknownKeyword)return g.top;
  if(x.kind===ts.SyntaxKind.NeverKeyword)return g.bot;
  if([ts.SyntaxKind.StringKeyword,ts.SyntaxKind.NumberKeyword,ts.SyntaxKind.BooleanKeyword,ts.SyntaxKind.VoidKeyword,ts.SyntaxKind.UndefinedKeyword,ts.SyntaxKind.SymbolKeyword,ts.SyntaxKind.BigIntKeyword].includes(x.kind))return atom(ts.tokenToString(x.kind));
  if(ts.isTypeLiteralNode(x))return record(x.members);
  if(ts.isTypeReferenceNode(x)&&ts.isIdentifier(x.typeName)&&!x.typeArguments?.length)return buildName(x.typeName.text);
  if(ts.isFunctionTypeNode(x)&&!x.typeParameters?.length&&x.parameters.length===1){let p=x.parameters[0];if(!p.type||p.questionToken||p.dotDotDotToken)throw Error('optional parameter');return g.add('fun',{dom:build(p.type),cod:build(x.type)});}
  throw Error('unsupported type');
 }
 let roots=[];for(let name of decl.keys()){try{let id=buildName(name);let nodes=reach(g,id);if(nodes.some(x=>g.nodes[x].kind==='pending'))throw Error('unresolved');roots.push({name,id});}catch{}}
 // Recheck transitive references to failed declarations after all builds.
 roots=roots.filter(r=>!reach(g,r.id).some(i=>g.nodes[i].kind==='pending'));
 return {g,roots,total};
}
// Small explicit Scala-like type-equation frontend: type A = { val next: A; val f: (Any) => Nothing }
export function parseScala(text){
 const toks=text.match(/=>|[A-Za-z_]\w*|[{}():;=]/g)||[];let p=0,g=new Graph(),ids=new Map(),defs=[];
 const need=x=>{if(toks[p++]!==x)throw Error(`expected ${x}`);};
 for(let j=0;j<toks.length;j++)if(toks[j]==='type'&&toks[j+2]==='=')ids.set(toks[j+1],g.add('pending'));
 function typ(){let t=toks[p++];if(t==='Any')return g.top;if(t==='Nothing')return g.bot;if(t==='Int'||t==='String'||t==='Boolean')return g.add('atom',{},t);
  if(t==='{'){let e={};while(toks[p]!=='}'){need('val');let k=toks[p++];need(':');e[k]=typ();if(toks[p]===';')p++;}need('}');return g.record(e);}
  if(t==='('){let a=typ();need(')');need('=>');return g.add('fun',{dom:a,cod:typ()});}
  if(ids.has(t))return ids.get(t);throw Error('unsupported Scala subset');
 }
 while(p<toks.length){need('type');let name=toks[p++];need('=');let v=typ();g.nodes[ids.get(name)]=g.nodes[v];defs.push({name,id:ids.get(name)});if(toks[p]===';')p++;}
 if(g.nodes.some(v=>v.kind==='pending'))throw Error('unguarded alias');return {g,roots:defs,total:defs.length};
}
export function graphStats(g,root){
 let ids=reach(g,root),color=new Map(),back=0,edges=0;
 function visit(x){color.set(x,1);for(let y of Object.values(g.nodes[x].edges)){edges++;if(color.get(y)===1)back++;else if(!color.has(y))visit(y);}color.set(x,2);}visit(root);
 let q=minimize(g,root);return {nodes:ids.length,edges,back,states:q.size};
}
