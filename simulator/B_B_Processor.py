from B_B_Parser import decode_B_binary
from memory import register,pc  # Assuming this function exists

def process_B_instruction(binary_instruction):
    # Decode the binary instruction
    decoded = decode_B_binary(binary_instruction)
    
    # Retrieve the source register values
    src_val1 = register(decoded['src_rgstr1'])
    src_val2 = register(decoded['src_rgstr2'])
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
    elif decoded['operation'] == 'bltu' and src_val1 < src_val2:  # Unsigned comparison
        should_branch = True
    elif decoded['operation'] == 'bgeu' and src_val1 >= src_val2:  # Unsigned comparison
        should_branch = True
    
    # If the condition is met, modify the program counter
    if should_branch:
          # Assuming PC is a global variable representing the program counter
        pc = pc + imm  # Adjust PC based on the immediate value

# Example usage
binary_instruction = '00001100111101101100010001100011'  # Example binary instruction
process_B_instruction(binary_instruction)