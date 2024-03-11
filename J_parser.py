def J_parser(instruction):
    J_ops = ['jal']  
    x_values = ["s0", "fp", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "sp", "t0", "t1", "t2", "t3", "t4", "t5", "t6", "tp", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "gp", "ra", "zero"]
    
    parts = instruction.split(' ', 1)
    if len(parts) != 2:
        return {'error': "Invalid instruction format"}
    
    instruction_code, params = parts

    if instruction_code not in J_ops:
        return {'error': "Invalid J operation"}
    
    params = params.replace(' ', '')  
    params_parts = params.split(',')
    
    if len(params_parts) != 2:
        return {'error': "Invalid number of parameters"}
    
    dstn_register, imm = params_parts
    
    if not dstn_register or not imm:
        return {'error': "One or more parameters are empty"}
    
    if dstn_register not in x_values:
        return {'error': "Register not valid"}
    
    try:
        imm = int(imm)  
    except ValueError:
        return {'error': "Invalid imm"}

    return {
        'error': None,
        'operation': instruction_code,
        'dstn_register': dstn_register,
        'imm': imm
    }
from rgstrfncns import rgstr_func , imm_binary
def J_binary(instruction):
    if instruction['error'] == None:
        return '1111011' + rgstr_func(instruction['dstn_register'])  + imm_binary(instruction['imm'],20)[12:20] +imm_binary(instruction['imm'],20)[10]+imm_binary(instruction['imm'],20)[1:11]+imm_binary(instruction['imm'],20)[19]

    else:
        return {'error': instruction['error']}


# with open('Jinput.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#         print(J_parser(line.strip()))
#         print(J_binary(J_parser(line.strip())))
