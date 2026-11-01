"""Exact NFA stack-annotation block tables; no saturation compiler is implied."""
from array import array

class BlockIndex:
    def __init__(self, transitions, labels, state_count, block_bits, mask_bits):
        assert 1 <= block_bits <= min(state_count,64)
        self.s=state_count; self.b=block_bits; self.M=mask_bits
        self.d=(state_count+63)//64; self.B=(mask_bits+63)//64
        self.groups=[(start,min(block_bits,state_count-start)) for start in range(0,state_count,block_bits)]
        self.transitions={c:self._tabulate(rows,self.d) for c,rows in transitions.items()}
        self.outputs={q:self._tabulate(rows,self.B) for q,rows in labels.items()}
        self.payload_words=sum(len(a) for tables in [self.transitions,self.outputs] for groups in tables.values() for a in groups)
    def _tabulate(self,rows,words):
        result=[]
        for start,width in self.groups:
            table=array('Q',[0])*((1<<width)*words)
            for pattern in range(1,1<<width):
                bit=pattern & -pattern; index=bit.bit_length()-1
                previous=pattern ^ bit
                for j in range(words):
                    table[pattern*words+j]=table[previous*words+j] | ((rows[start+index]>>(64*j))&((1<<64)-1))
            result.append(table)
        return result
    def _apply(self,annotation,tables,words):
        result=[0]*words
        for (start,width),table in zip(self.groups,tables):
            pattern=(annotation>>start)&((1<<width)-1)
            for j in range(words):result[j] |= table[pattern*words+j]
        return sum(v<<(64*j) for j,v in enumerate(result))
    def push(self,annotation,symbol):return self._apply(annotation,self.transitions[symbol],self.d)
    def mask(self,annotation,control):return self._apply(annotation,self.outputs[control],self.B)

