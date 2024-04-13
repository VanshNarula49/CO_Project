from B_J_Parser import decode_J_binary
from memory import register
import os

def process_J_instruction(decoded):

    register[decoded["dstn_register"]] = int(os.environ['pc']) + 4
    print(register)

    os.environ['pc'] = str(int(os.environ['pc']) + decoded['imm'])


#Example usage:
binary_instruction = '11000000000111111111000011101111'  # Example binary string for a 'jal' instruction
decoded_instruction = decode_J_binary(binary_instruction)
process_J_instruction(decoded_instruction)
