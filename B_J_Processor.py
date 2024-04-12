from B_J_Parser import decode_J_binary
from memory import register,pc

def process_J_instruction(binary_instruction, pc):

    decoded = decode_J_binary(binary_instruction)
    dstn_val = register[decoded['dstn_register']]
    dstn_val = pc + 4

    print("rd: ", dstn_val)

    pc = pc + decoded['imm']

    print ("pc: ", pc)

#Example usage:
binary_instruction = ''  # Example binary string for a 'jal' instruction
decoded_instruction = decode_J_binary(binary_instruction)
print(decoded_instruction)
process_J_instruction(binary_instruction, pc)