import os
from memory import register,memory
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


def rgstr_print(binary):
    main_parser(binary)
    strng = ''
    for key in register.values():
        strng = strng + str(bin(key)[2:].zfill(32)) +' '
    return strng




f = open("output.txt", "w")
print(f)
instrcnnarr = ['']
rgstrarr  = []


with open('simin.txt', 'r') as file:
    for line in file:
       instrcnnarr.append(line.split('\n')[0]) 
halt = False

while halt==False:
    oldpc = int(os.environ['pc'])
    if instrcnnarr[int(os.environ['pc'])] == '00000000000000000000000001100011':
        halt = True
        break
    else:
        a = rgstr_print(instrcnnarr[int(os.environ['pc'])])
        f.write(a+'\n')
        rgstrarr.append(a)
        if int(os.environ['pc']) == oldpc:
            os.environ['pc'] = str(int(os.environ['pc'])+1)
print(rgstrarr)

for key in memory.keys():   
    f.write(key+': '+str(bin(memory[key]))+'\n')

f.close()

