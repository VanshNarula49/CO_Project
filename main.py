from B_R_Parser import decode_R_binary
from B_I_Parser import decode_I_binary
from B_B_Parser import decode_B_binary
from B_U_Parser import decode_U_binary
from B_J_Parser import decode_J_binary
from B_S_Parser import decode_S_binary


def main_parser(binary):
    opcode = binary[::-1][:7]
    print(binary)
    if(opcode == "1100110"):
        return decode_R_binary(binary)
    elif(opcode == "1110011" or opcode == "1100000" or opcode=="1100100"):
        return decode_I_binary(binary)
    elif(opcode == "1100010"):
        return decode_S_binary(binary)
    elif(opcode == "1100011"):
        return decode_B_binary(binary)
    elif(opcode == "1110100"):
        return decode_U_binary(binary)
    elif(opcode == "1111011"):
        return decode_J_binary(binary)
    else:
        return "Invalid Opcode"

f = open("./simulator/output.txt", "w")

with open('./simulator/simin.txt', 'r') as file:
    for line in file:
        output = main_parser(line.strip())
        print(output)
        f.write(str(output)+'\n')

f.close()

