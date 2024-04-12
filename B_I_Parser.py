from brgstfncns import binary_to_reg_name
def decode_I_binary(binaryi):
    binary_instruction = binaryi[::-1]
    # Ensure the binary instruction is of the correct length for I-type instructions
    if len(binary_instruction) != 32:
        return {'error': "Invalid binary instruction length"}

    opcode = binary_instruction[0:7]
    rtrn_addr_rgstr_binary = binary_instruction[7:12]
    func3 = binary_instruction[12:15]
    src_rgstr1_binary = binary_instruction[15:20]
    imm_binary = binary_instruction[20:]

    # Convert binary to integer, considering it as a signed value
    imm = int(imm_binary[::-1], 2)
    if imm & (1 << 11):  # Check if the 12th bit is set (negative number)
        imm -= (1 << 12)  # Apply two's complement to get the negative value

    # Use binary_to_reg_name to get register names
    rtrn_addr_rgstr = binary_to_reg_name(rtrn_addr_rgstr_binary)
    src_rgstr1 = binary_to_reg_name(src_rgstr1_binary)

    # Determine the operation based on opcode and func3
    operation = "Unknown"
    if opcode == '1100000' and func3 == '010':
        operation = 'lw'
        
    elif opcode == '1100100':
        if func3 == '000':
            operation = 'addi'
        elif func3 == '110':
            operation = 'sltiu'
    elif opcode == '1110011' and func3 == '000':
        operation = 'jalr'

    return {
        'error': None,
        'operation': operation,
        'rtrn_addr_rgstr': rtrn_addr_rgstr,
        'src_rgstr1': src_rgstr1,
        'imm': imm
    }

# Example usage

binary_instruction = "00000010000001110000000011100111"  # Example binary instruction for 'lw'
decoded = decode_I_binary(binary_instruction)
print(decoded)