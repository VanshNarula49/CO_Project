from brgstfncns import binary_to_reg_name
def decode_S_binary(binary_instruction):
    # Ensure the binary instruction is of the correct length for S-type instructions
    if len(binary_instruction) != 32:
        return {'error': "Invalid binary instruction length"}

    # Extract parts of the binary instruction
    imm_11_5 = binary_instruction[0:7]
    rtrn_addr_binary = binary_instruction[7:12][::-1]
    src_rgstr1_binary = binary_instruction[12:17][::-1]
    imm_4_0 = binary_instruction[20:25][::-1]
    imm_binary = imm_11_5 + imm_4_0

    # Convert binary to integer, considering it as a signed value
    imm = int(imm_binary, 2)
    if imm & (1 << 11):  # Check if the 12th bit is set (negative number)
        imm -= (1 << 12)  # Apply two's complement to get the negative value

    # Use binary_to_reg_name to get register names
    rtrn_addr = binary_to_reg_name(rtrn_addr_binary)
    src_rgstr1 = binary_to_reg_name(src_rgstr1_binary)

    return {
        "operation":"sw",
        'imm': imm,
        'rtrn_addr': rtrn_addr,
        'src_rgstr1': src_rgstr1
    }

# Example usage
# binary_instruction = "00000010000100010010000000100011" # Example binary instruction for 'sw'
# decoded = decode_S_binary(binary_instruction)
# print(decoded)