def J_parser(instruction):
    J_ops = ['jal']  
    
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
    
    return {
        'error': None,
        'operation': instruction_code,
        'dstn_register': dstn_register,
        'imm': imm
    }

with open('Jinput.txt', 'r') as file:
    for line in file:
        print(line.strip())
        print(J_parser(line.strip()))
