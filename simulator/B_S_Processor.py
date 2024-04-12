from memory import register, memory
from brgstfncns import sext
from B_S_Parser import decode_S_binary

def S_processor(dictS):
    if dictS['operation'] == 'sw':
        effective_address = register[dictS['src_rgstr1']] + sext(dictS['imm'], bits=12)
        print(effective_address)
        memory.insert(effective_address,register[dictS['rtrn_addr']])

    return memory

# Example usage
dict = decode_S_binary('00000010000100010010000000100011') 
newmem = S_processor(dict)
print(newmem)