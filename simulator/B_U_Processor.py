from memory import register,pc
from B_U_Parser import decode_U_binary
from brgstfncns import sext

def U_processor(dictU):
    if dictU['operation'] == 'lui':
        # Load Upper Immediate: Load imm into the upper 20 bits of the destination register
        register[dictU['dstn_register']] = sext(int(dictU['bin'] + 12*'0')) 
    elif dictU['operation'] == 'auipc':
        # Add Upper Immediate to PC: Add imm to the program counter and store the result in the destination register
        # Assuming 'pc' is the program counter variable available globally or within context
        register[dictU['dstn_register']] = sext(int(dictU['bin'] + 12*'0'))  + pc

    return register

# Example usage
dictU = decode_U_binary('11111111111111111111100100010111') 
newvals = U_processor(dictU)
print(newvals)