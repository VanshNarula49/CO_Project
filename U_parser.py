def U_parser(instruction):
    U_ops = ['auipc','lui']
    
    parts = instruction.split(' ', 1)
    if len(parts) != 2:
        return {'error': "Invalid instruction format"}
    
    instruction_code, params = parts

    if instruction_code not in U_ops:
        return {'error': "Invalid U operation"}
    
    params = params.replace(' ', '')  
    params_parts = params.split(',')
    
    if len(params_parts) != 2:
        return {'error': "Invalid number of parameters"}
    
    dstn_register, imm = params_parts
    
    if not dstn_register or not imm:
        return {'error': "One or more parameters are empty"}
    
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
def U_binary(instruction):
    if instruction['error'] == None:
        if instruction['operation'] == 'lui':
            return '1110110' + rgstr_func(instruction['dstn_register']) + imm_binary(instruction['imm'],32)[12:32]
        elif instruction['operation'] == 'auipc':
            return '1110100' + rgstr_func(instruction['dstn_register']) + imm_binary(instruction['imm'],32)[12:32]

    else:
        return {'error': instruction['error']}

# with open('Uinput.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#         print(U_parser(line.strip()))
#         print(U_binary(U_parser(line.strip())))

