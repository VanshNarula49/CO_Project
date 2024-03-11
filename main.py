from I_parser import I_parser , I_binary
from R_parser import R_parser , R_binary
from S_parser import S_parser , S_binary
from B_parser import B_parser , B_binary
from U_parser import U_parser, U_binary
from J_parser import J_parser, J_binary
def main_parser(inputstr):
    
    B_ops = ['beq', 'bne', 'bge', 'bgeu', 'blt', 'bltu']
    I_ops = ['lw', 'addi', 'sltiu', 'jalr']
    J_ops = ['jal']
    R_ops = ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
    S_ops = ['sw']
    U_ops = ['auipc', 'lui']
    
   
    parts = inputstr.split(' ', 1)
    if len(parts) < 2:
        return {'error': "Invalid inputstr format"}
    
    operation = parts[0]
    
   
    if operation in B_ops:
        return B_binary(B_parser(inputstr)) 
    elif operation in I_ops:
        return I_binary(I_parser(inputstr))
    elif operation in J_ops:
        return J_binary(J_parser(inputstr))
    elif operation in R_ops:
        return R_binary(R_parser(inputstr))
    elif operation in S_ops:
        return S_binary(S_parser(inputstr))
    elif operation in U_ops:
        return U_binary(U_parser(inputstr))
    else:
        return {'error': "Unknown operation"}

f = open("output.txt", "w")


with open('main.txt', 'r') as file:
    
    for line in file:
        print(main_parser(line.strip())[::-1])
        f.write(main_parser(line.strip())[::-1]+'\n')
f.close()

 

