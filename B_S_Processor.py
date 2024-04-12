from memory import register, memory
from brgstfncns import sext,hexconv
from B_S_Parser import decode_S_binary

def S_processor(dictS):
    if dictS['operation'] == 'sw':
        effective_address = register[dictS['src_rgstr1']] + sext(dictS['imm'], bits=12)
        memory[hexconv(effective_address)]=register[dictS['rtrn_addr']]


# Example usage
dict = decode_S_binary('00000011001010011010000000100011') 
newmem = S_processor(dict)
print(newmem)