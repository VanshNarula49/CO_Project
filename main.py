from I_parser import I_parser
from R_parser import R_parser
from S_parser import S_parser
from B_parser import B_parser
from Uparser import U_parser
from J_parser import J_parser
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
        return B_parser(inputstr)
    elif operation in I_ops:
        return I_parser(inputstr)
    elif operation in J_ops:
        return J_parser(inputstr)
    elif operation in R_ops:
        return R_parser(inputstr)
    elif operation in S_ops:
        return S_parser(inputstr)
    elif operation in U_ops:
        return U_parser(inputstr)
    else:
        return {'error': "Unknown operation"}

with open('main.txt', 'r') as file:
    for line in file:
        print(line.strip())
        print(main_parser(line.strip()))
