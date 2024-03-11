
def B_parser(instruction):
    B_ops = ['beq', 'bne', 'bge', 'bgeu', 'blt', 'bltu']
    
    
    parts = instruction.split(' ', 1)
    if len(parts) < 2:
        return {'error': "Invalid instruction format"}
    
    instruction_code, rest = parts[0], parts[1].replace(' ', '')
    params = rest.split(',')
    
    if len(params) != 3:
        return {'error': "Invalid number of parameters"}
    
    if instruction_code not in B_ops:
        return {'error': "Invalid B operation"}
    
    src_rgtstr1, src_rgstr2, imm = params

    if not src_rgtstr1 or not src_rgstr2 or not imm:
        return {'error': "One or more parametersare empty"}
    
    try:
        imm = int(imm)  # Check if imm is an integer
    except ValueError:
        return {'error': "Invalid imm"}
    
    return {
        'error': None,
        'operation': instruction_code,
        'src_rgstr1': src_rgtstr1,
        'src_rgstr2': src_rgstr2,
        'imm': imm
    }



from rgstrfncns import rgstr_func, imm_binary

def B_binary(instruction):
    B_ops = ['beq', 'bne', 'bge', 'bgeu', 'blt', 'bltu']

    if instruction['error'] is None:
        if instruction['operation'] == 'beq':
             return '1100011' + imm_binary(instruction['imm'], 12)[10]+imm_binary(instruction['imm'], 12)[1:5] +"000"+ rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + imm_binary(instruction['imm'], 12)[5:11]+imm_binary(instruction['imm'], 12)[11]
        elif instruction['operation'] == 'bne':
             return '1100011' + imm_binary(instruction['imm'], 12)[10]+imm_binary(instruction['imm'], 12)[1:5] +"100"+ rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + imm_binary(instruction['imm'], 12)[5:11]+imm_binary(instruction['imm'], 12)[11]
        elif instruction['operation'] == 'bge':
             return '1100011' + imm_binary(instruction['imm'], 12)[10]+imm_binary(instruction['imm'], 12)[1:5] +"101"+ rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + imm_binary(instruction['imm'], 12)[5:11]+imm_binary(instruction['imm'], 12)[11]
        elif instruction['operation'] == 'bgeu':
             return '1100011' + imm_binary(instruction['imm'], 12)[10]+imm_binary(instruction['imm'], 12)[1:5] +"111"+ rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + imm_binary(instruction['imm'], 12)[5:11]+imm_binary(instruction['imm'], 12)[11]
        elif instruction['operation'] == 'blt':
              return '1100011' + imm_binary(instruction['imm'], 12)[10]+imm_binary(instruction['imm'], 12)[1:5] +"001"+ rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + imm_binary(instruction['imm'], 12)[5:11]+imm_binary(instruction['imm'], 12)[11]
        elif instruction['operation'] == 'bltu':
             return '1100011' + imm_binary(instruction['imm'], 12)[10]+imm_binary(instruction['imm'], 12)[1:5] +"011"+ rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + imm_binary(instruction['imm'], 12)[5:11]+imm_binary(instruction['imm'], 12)[11]
        else:
            return {'error': "Invalid B operation"}
    else:
        return {'error': instruction['error']}








# with open('Binput.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#         print(B_parser(line.strip()))
#         print(B_binary(B_parser(line.strip())))

