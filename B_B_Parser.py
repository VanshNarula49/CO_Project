from brgstfncns import binary_to_reg_name
def decode_B_binary(binaryi):
    binary_instruction = binaryi[::-1]
    # Define the operation codes for reverse lookup
    op_codes = {
        '000': 'beq',
        '001': 'bne',
        '100': 'blt',
        '101': 'bge',
        '110': 'bltu',
        '111': 'bgeu'
    }
    
    # Extract parts of the binary instruction
    opcode = binary_instruction[:7]
    imm_11 = binary_instruction[7][::-1]
    imm_1_4 = binary_instruction[8:12][::-1]
    funct3 = binary_instruction[12:15][::-1]
    src_rgstr1 = binary_instruction[15:20]
    src_rgstr2 = binary_instruction[20:25]
    imm_5_10 = binary_instruction[25:31][::-1]
    imm_12 = binary_instruction[31][::-1]
    
    # Reconstruct the immediate value
    imm_bits = imm_12 + imm_11 + imm_5_10 + imm_1_4 + '0'
    imm = int(imm_bits, 2)
    # Adjust for sign extension if imm[12] (the sign bit) is '1'
    if imm_12 == '1':
        imm -= 2**12
    
    # Lookup the operation
    operation = op_codes[funct3]
    
    # Convert register numbers back to names (assuming a mapping function exists)
    # For simplicity, this example uses a direct conversion assuming a function `reg_name` exists
    src_rgstr1_name = binary_to_reg_name(src_rgstr1)  # Implement this function based on your register naming scheme
    src_rgstr2_name = binary_to_reg_name(src_rgstr2)  # Implement this function based on your register naming scheme
    
    return {
        'operation': operation,
        'src_rgstr1': src_rgstr1_name,
        'src_rgstr2': src_rgstr2_name,
        'imm': imm,
        
    }



# Example usage
# binary_instruction = "00001101001001001110010001100011"#'00001100111101101100010001100011'  # Example binary instruction
# decoded = decode_B_binary(binary_instruction)
# print(decoded)