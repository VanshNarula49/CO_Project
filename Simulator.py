import os
from brgstfncns import b_print
from memory import register,memory
from B_R_Parser import decode_R_binary
from B_I_Parser import decode_I_binary
from B_B_Parser import decode_B_binary
from B_U_Parser import decode_U_binary
from B_J_Parser import decode_J_binary
from B_S_Parser import decode_S_binary
from B_B_Processor import process_B_instruction
from B_I_Processor import I_processor
from B_J_Processor import process_J_instruction
from B_R_Processor import R_processor
from B_S_Processor import S_processor
from B_U_Processor import U_processor
from Bonus_Parser import decode_bonus_binary
from Bonus_Processor import process_bonus_instruction
import sys
file_input = sys.argv[1]
file_output = sys.argv[2]


def main_parser(binary):
    opcode = binary[::-1][:7]
    # print(binary)
    if opcode == "1100110":
        decoded = decode_R_binary(binary)
        return R_processor(decoded)
    elif opcode in ["1110011", "1100000", "1100100"]:
        decoded = decode_I_binary(binary)
        return I_processor(decoded)
    elif opcode == "1100010":
        decoded = decode_S_binary(binary)
        return S_processor(decoded)
    elif opcode == "1100011":
        decoded = decode_B_binary(binary)
        return process_B_instruction(decoded)
    elif opcode in ["1110100","1110110"]:
        decoded = decode_U_binary(binary)
        return U_processor(decoded)
    elif opcode == "1111011":
        decoded = decode_J_binary(binary)
        return process_J_instruction(decoded)
    elif opcode in ["0000000 ","1111111"]:
        decoded = decode_bonus_binary(binary)
        return process_bonus_instruction(decoded)
    else:
        return "Invalid Opcode"

def rgstr_print(binary):
    main_parser(binary)
    
    register['zero'] = 0
    strng = b_print(int(os.environ['pc'])*4)+' '
    for key in register.values():
        strng = strng + b_print(key) +' '
    return strng




f = open(file_output, "w")
# print(f)
instrcnnarr = ['']
rgstrarr  = []


with open(file_input, 'r') as file:
    for line in file:
       instrcnnarr.append(line.split('\n')[0]) 
halt = False

while halt==False:
    # print(register)
    os.environ['pc'] = str(int(os.environ['pc'])+1)
    # print('pc',os.environ['pc'])
  
   
    if instrcnnarr[int(os.environ['pc'])] == '00000000000000000000000001100011' or instrcnnarr[int(os.environ['pc'])] == '00000000000000000000000000000000' :
        # os.environ['pc'] = str(int(os.environ['pc'])-1)
        a = rgstr_print(instrcnnarr[int(os.environ['pc'])])
        f.write(a+'\n')
        rgstrarr.append(a)
        halt = True
        break     
    else:
         a = rgstr_print(instrcnnarr[int(os.environ['pc'])])
         f.write(a+'\n')
         rgstrarr.append(a)
         
         
# print(rgstrarr)

for key in memory.keys():   
    f.write(key+':'+b_print(memory[key])+'\n')
file.close()
f.close()

