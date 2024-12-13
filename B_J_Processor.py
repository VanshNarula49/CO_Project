from B_J_Parser import decode_J_binary
from memory import register
import os

def process_J_instruction(decoded):
    
    register[decoded["dstn_register"]] = (int(os.environ['pc']) )*4#DATA SHEET SAYS +4 BUT PC ALREADY IS DIVIDED BY 4
    # print(register)
    imm = int(decoded['imm']/4)


    os.environ['pc'] = str(int(os.environ['pc']) + imm-1)
    

#Example usage:
# binary_instruction = '11111110111111111111000011101111'  # Example binary string for a 'jal' instruction
# decoded_instruction = decode_J_binary(binary_instruction)
# print(decoded_instruction)
# process_J_instruction(decoded_instruction)
# print(os.environ['pc'])
