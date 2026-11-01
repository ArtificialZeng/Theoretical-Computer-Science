"""ctypes binding for the finite-exposure Rust reference implementation."""
import ctypes as C
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
LIB = HERE / ('libviable.dylib' if sys.platform == 'darwin' else 'libviable.so')
lib = C.CDLL(str(LIB))
lib.viable_new.restype = C.c_void_p
lib.viable_free.argtypes = [C.c_void_p]
lib.viable_commit.argtypes = [C.c_void_p, C.c_char_p, C.c_size_t]
lib.viable_commit.restype = C.c_bool
lib.viable_mask.argtypes = [C.c_void_p, C.POINTER(C.c_uint64), C.c_size_t]
lib.viable_mask.restype = C.c_size_t
lib.viable_vocab_size.restype = C.c_size_t
lib.viable_mask_table_words.restype = C.c_size_t
lib.viable_token.argtypes = [C.c_size_t, C.POINTER(C.c_uint8), C.c_size_t]
lib.viable_token.restype = C.c_size_t

class Decoder:
    def __init__(self):
        self.ptr = lib.viable_new()
        self.size = lib.viable_vocab_size()
        self.output = (C.c_uint64 * ((self.size+63)//64))()
    def close(self):
        if self.ptr: lib.viable_free(self.ptr); self.ptr = None
    def __enter__(self): return self
    def __exit__(self, *args): self.close()
    def commit(self, text): return lib.viable_commit(self.ptr, text, len(text))
    def mask(self):
        copied = lib.viable_mask(self.ptr, self.output, len(self.output))
        assert copied == len(self.output)
        return sum(int(w) << (64*i) for i,w in enumerate(self.output)), copied

def vocabulary():
    result = []
    for i in range(lib.viable_vocab_size()):
        buf = (C.c_uint8 * 4)()
        length = lib.viable_token(i, buf, 4)
        result.append(bytes(buf[:length]))
    return result
