//! Finite-exposure specialization of VIABLE for two-bracket Dyck prefixes.
//! Build: rustc --crate-type cdylib -O viable.rs -o libviable.dylib
use std::sync::OnceLock;

const ALPHABET: &[u8] = b"()[]";
struct Tables { vocab: Vec<Vec<u8>>, rows: Vec<Vec<u64>> }
static TABLES: OnceLock<Tables> = OnceLock::new();

fn extend(stack: &mut Vec<u8>, text: &[u8]) -> bool {
    for &c in text {
        match c {
            b'(' => stack.push(0), b'[' => stack.push(1),
            b')' => if stack.pop() != Some(0) { return false; },
            b']' => if stack.pop() != Some(1) { return false; },
            _ => return false,
        }
    }
    true
}
fn words(prefix: &mut Vec<u8>, remaining: usize, out: &mut Vec<Vec<u8>>) {
    if remaining == 0 { out.push(prefix.clone()); return; }
    for &c in ALPHABET { prefix.push(c); words(prefix, remaining-1, out); prefix.pop(); }
}
fn tables() -> &'static Tables {
    TABLES.get_or_init(|| {
        let mut vocab = Vec::new();
        for length in 1..=4 { words(&mut Vec::new(), length, &mut vocab); }
        let mut rows = vec![vec![0; (vocab.len()+63)/64]; 32];
        for h in 1..32usize {
            let depth = (usize::BITS-1-h.leading_zeros()) as usize;
            let stack: Vec<u8> = (0..depth).rev().map(|j| ((h>>j)&1) as u8).collect();
            for (i, token) in vocab.iter().enumerate() {
                if extend(&mut stack.clone(), token) { rows[h][i/64] |= 1u64<<(i%64); }
            }
        }
        Tables { vocab, rows }
    })
}
struct Node { parent: usize, symbol: u8, h: usize }
pub struct Decoder { nodes: Vec<Node>, root: usize, dead: bool }

#[no_mangle]
pub extern "C" fn viable_new() -> *mut Decoder {
    let _ = tables();
    Box::into_raw(Box::new(Decoder { nodes: vec![Node {parent:0,symbol:0,h:1}], root:0,dead:false }))
}
#[no_mangle]
pub unsafe extern "C" fn viable_free(p: *mut Decoder) {
    if !p.is_null() { drop(Box::from_raw(p)); }
}
#[no_mangle]
pub unsafe extern "C" fn viable_commit(p: *mut Decoder, data: *const u8, len: usize) -> bool {
    let d = &mut *p;
    if d.dead { return false; }
    for &c in std::slice::from_raw_parts(data,len) {
        match c {
            b'(' | b'[' => {
                let symbol = if c==b'(' {0} else {1};
                let old = d.nodes[d.root].h;
                let h = if old>=16 {16|(((old<<1)|symbol as usize)&15)} else {(old<<1)|symbol as usize};
                d.nodes.push(Node {parent:d.root,symbol,h}); d.root=d.nodes.len()-1;
            },
            b')' | b']' => {
                let expected=if c==b')' {0} else {1};
                if d.root==0 || d.nodes[d.root].symbol!=expected {d.dead=true;return false;}
                d.root=d.nodes[d.root].parent;
            },
            _ => {d.dead=true;return false;}
        }
    }
    true
}
#[no_mangle]
pub unsafe extern "C" fn viable_mask(p: *const Decoder, out: *mut u64, capacity: usize) -> usize {
    let d=&*p; let t=tables(); let row=&t.rows[d.nodes[d.root].h];
    if capacity<row.len() {return 0;}
    for (i,&word) in row.iter().enumerate() {*out.add(i)=if d.dead {0} else {word};}
    row.len()
}
#[no_mangle]
pub extern "C" fn viable_vocab_size() -> usize { tables().vocab.len() }
#[no_mangle]
pub extern "C" fn viable_mask_table_words() -> usize {
    tables().rows.iter().map(|row| row.len()).sum()
}
#[no_mangle]
pub unsafe extern "C" fn viable_token(i: usize, out: *mut u8, capacity: usize) -> usize {
    let t=tables(); if i>=t.vocab.len() {return 0;}
    let token=&t.vocab[i]; if capacity<token.len() {return 0;}
    std::ptr::copy_nonoverlapping(token.as_ptr(),out,token.len()); token.len()
}
