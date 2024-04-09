from brgstfncns import binary_to_reg_name

def decode_J_binary(binaryi):
    # Check if the binary string represents a 'jal' instruction
    binary = binaryi[::-1]
   
    if binary[:7] == '1101111'[::-1]:
        # Extract the destination register binary code and convert it
        dstn_rgstr_binary = binary[7:12]
        dstn_rgstr = binary_to_reg_name(dstn_rgstr_binary)

        # Extract and reconstruct the immediate value from the binary string
        # Immediate value is split and needs to be reconstructed from different parts of the instruction
        imm_20 = binary[31][::-1] + binary[12:20][::-1] + binary[20][::-1] + binary[21:31][::-1] + '0'
        # Convert the binary immediate value to integer, considering sign extension for negative values
        imm_20_val = int(imm_20, 2)
        if imm_20[0] == '1':  # Check the sign bit for sign extension
            imm_20_val = imm_20_val - (1 << 21)  # Apply sign extension

        return {
            'operation': 'jal',
            'dstn_register': dstn_rgstr,
            'imm': imm_20_val
        }
    else:
        return "Unknown instruction"

# Example usage
# binary_instruction = '11000000000111111111000011101111'  # Example binary string for a 'jal' instruction
# decoded_instruction = decode_J_binary(binary_instruction)
# print(decoded_instruction)