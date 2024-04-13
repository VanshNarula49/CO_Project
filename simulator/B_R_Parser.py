from brgstfncns import binary_to_reg_name
def decode_R_binary(binaryi):
    binary_instruction = binaryi[::-1]
    # Ensure the binary instruction is of the correct length for R-type instructions
    if len(binary_instruction) != 32:
        return {'error': "Invalid binary instruction length"}

    opcode = binary_instruction[0:7]
    dstn_rgstr_binary = binary_instruction[7:12]
    func3 = binary_instruction[12:15]
    src_rgstr1_binary = binary_instruction[15:20]
    src_rgstr2_binary = binary_instruction[20:25]
    func7 = binary_instruction[25:]

    # Use binary_to_reg_name to get register names
    dstn_rgstr = binary_to_reg_name(dstn_rgstr_binary)
    src_rgstr1 = binary_to_reg_name(src_rgstr1_binary)
    src_rgstr2 = binary_to_reg_name(src_rgstr2_binary)

    # Determine the operation based on opcode, func3, and func7
    operation = "Unknown"
    if opcode == '1100110':
        if func3 == '000':
            if func7 == '0000000':
                operation = 'add'
            elif func7 == '0000010':
                operation = 'sub'
        elif func3 == '100' and func7 == '0000000':
            operation = 'sll'
        elif func3 == '010' and func7 == '0000000':
            operation = 'slt'
        elif func3 == '110' and func7 == '0000000':
            operation = 'sltu'
        elif func3 == '001' and func7 == '0000000':
            operation = 'xor'
        elif func3 == '101':
            if func7 == '0000000':
                operation = 'srl'
            elif func7 == '0100000':  # Assuming this is for 'sra', not present in the given operations but added for completeness
                operation = 'sra'
        elif func3 == '011' and func7 == '0000000':
            operation = 'or'
        elif func3 == '111' and func7 == '0000000':
            operation = 'and'

    return {
        'error': None,
        'operation': operation,
        'dstn_rgstr': dstn_rgstr,
        'src_rgstr1': src_rgstr1,
        'src_rgstr2': src_rgstr2
    }

# Example usage
# binary_instruction = "00000001001110010000010010110011" # Example binary instruction for 'add'
# decoded = decode_R_binary(binary_instruction)
# print(decoded)