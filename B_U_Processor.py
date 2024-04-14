from memory import register
from B_U_Parser import decode_U_binary
from brgstfncns import sext
import os

def U_processor(dictU):
    if dictU['operation'] == 'lui':
        # Load Upper Immediate: Load imm into the upper 20 bits of the destination register
        register[dictU['dstn_register']] = dictU['imm']#sext(int(dictU['bin'] + 12*'0')) 
        print(dictU['dstn_register'],'updated with ',dictU['imm'])
    elif dictU['operation'] == 'auipc':
        # Add Upper Immediate to PC: Add imm to the program counter and store the result in the destination register
        # Assuming 'pc' is the program counter variable available globally or within context
        register[dictU['dstn_register']] = dictU['imm']+4*int(os.environ['pc'])-4#sext(int(dictU['bin'] + 12*'0'))  + pc

    return register

# # Example usage
# dictU = decode_U_binary('00000000000000010000010000110111') 
# print(dictU)
# newvals = U_processor(dictU)
# print(newvals)