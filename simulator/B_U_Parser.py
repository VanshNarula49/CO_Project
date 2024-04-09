from brgstfncns import binary_to_reg_name

def decode_U_binary(binaryi):
    # Determine the operation based on the opcode
    binary = binaryi[::-1]
    opcode = binary[:7]
    print(opcode)
    if opcode == '0110111'[::-1]:
        operation = 'lui'
    elif opcode == '0010111'[::-1]:
        operation = 'auipc'
    else:
        return "Unknown operation"

    # Extract the destination register binary code and convert it
    dstn_rgstr_binary = binary[7:12]
    dstn_rgstr = binary_to_reg_name(dstn_rgstr_binary)

    # Extract the immediate value from the binary string
    imm_binary = binary[12:33][::1]   # Append zeros to the right to form a 32-bit value
    imm_val = int(imm_binary, 2)
    if imm_binary[19] == '1':  # Check the sign bit for sign extension
        imm_val = imm_val - (1 << 20)  # Apply sign extension

    return {
        'operation': operation,
        'dstn_register': dstn_rgstr,
        'imm': imm_val
    }

# Example usage
binary_instruction_lui = '00000000000000010000010000010111'
decoded_instruction_lui = decode_U_binary(binary_instruction_lui)
print(decoded_instruction_lui)
# 