from memory import register,memory
from brgstfncns import sext,unsingedint
from B_I_Parser import decode_I_binary
import os
def I_processor(dictI):
    
    if dictI['operation'] == 'lw':
        effective_address = register[dictI['src_rgstr1']] + sext(dictI['imm'], bits=12)
        register[dictI['rtrn_addr_rgstr']] = memory[effective_address]
    elif dictI['operation'] == 'addi':
        register[dictI['rtrn_addr_rgstr']] = register[dictI['src_rgstr1']] + sext(dictI['imm'], bits=12)
    elif dictI['operation'] == 'sltiu':
        register[dictI['rtrn_addr_rgstr']] = unsingedint(register[dictI['src_rgstr1']] < unsingedint(dictI['imm'], bits=12))
    elif dictI['operation'] == 'jalr':
        register[dictI['rtrn_addr_rgstr']] = int(os.environ['pc']) + 4  # Assuming 'pc' is the program counter register
        os.environ['pc'] = str(int(register[dictI['src_rgstr1']] + sext(dictI['imm'], bits=12) & ~1))  # Direct jump with alignment
        
dictI = decode_I_binary('00000010000001110000000011100111')  # Example binary instruction for 'lw'
I_processor(dictI)
print(register)