from B_B_Parser import decode_B_binary
from memory import register  # Assuming this function exists
from brgstfncns import unsingedint
import os

def process_B_instruction(decoded):
    # Decode the binary instruction


    # Retrieve the source register values
    src_val1 = register[decoded['src_rgstr1']]
    src_val2 = register[decoded['src_rgstr2']]
    usrc_val1 = unsingedint(src_val1)
    usrc_val2 = unsingedint(src_val2)
    imm = decoded['imm']

    
    # Initialize a variable to indicate whether to branch
    should_branch = False
    
    # Determine the operation and evaluate the condition
    if decoded['operation'] == 'beq' and src_val1 == src_val2:
        should_branch = True
    elif decoded['operation'] == 'bne' and src_val1 != src_val2:
        should_branch = True
    elif decoded['operation'] == 'blt' and src_val1 < src_val2:
        should_branch = True
    elif decoded['operation'] == 'bge' and src_val1 >= src_val2:
        should_branch = True
    elif decoded['operation'] == 'bltu' and usrc_val1 < usrc_val2:  # Unsigned comparison
        should_branch = True
    elif decoded['operation'] == 'bgeu' and usrc_val1 >= src_val2:  # Unsigned comparison
        should_branch = True
    
    # If the condition is met, modify the program counter
    if should_branch:
          # Assuming PC is a global variable representing the program counter
       os.environ['pc'] = str(int(os.environ['pc'])+int(imm/4)-1)
        

# # Example usage
# binary_instruction = '00001100111101101100010001100011' 
# tDict = {'operation': 'bltu', 'src_rgstr1': 'asss1', 'src_rgstr2': 's2', 'imm': 200} # Example binary instruction
# process_B_instruction(tDict,register)