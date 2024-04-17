from brgstfncns import binary_to_reg_name

def decode_bonus_binary(binaryi):

    bin_instr = binaryi[::-1]
    op_code = bin_instr[0:7]

    error = None
    
    if (binaryi == "00000000000000000000000000000000"):
        operation = "hlt"
        rd = None
        rs1 = None
        rs2 = None
        
    elif (binaryi == "11111111111111111111111111111111"):
        operation = "rst"
        rd = None
        rs1 = None
        rs2 = None
        
    elif (op_code == "0000000"):
        operation = "mul"
        rd = binary_to_reg_name(bin_instr[7:12])
        rs1 = binary_to_reg_name(bin_instr[15:20])
        rs2 = binary_to_reg_name(bin_instr[20:25])
    elif (op_code == "1111111"):
        operation = "rvrs"
        rd = binary_to_reg_name(bin_instr[7:12])
        rs1 = binary_to_reg_name(bin_instr[15:20])
        rs2 = None
    else:
        error = "Invalid"
        operation = None
        rd = None
        rs1 = None
        rs2 = None
    return {
        'error': error,
        'operation': operation,
        'rd': rd,
        'rs1': rs1,
        'rs2': rs2
    }

# i1 = "00000001001010011000101000000000" #mul s4,s2,s3
# i2 = "11111111111111111111111111111111" #rst
# i3 = "00000000000000000000000000000000" #hlt
# i4 = "00000000000010010000100111111111" #rvrs s3,s2
# i5 = "00000000000010000000010000000010" #invalid op

# print(decode_bonus_binary(i1))
# print(decode_bonus_binary(i2))
# print(decode_bonus_binary(i3))
# print(decode_bonus_binary(i4))
# print(decode_bonus_binary(i5))