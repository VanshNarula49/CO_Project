def S_parser(instruction):
    S_ops = ['sw']
    
    parts = instruction.split(' ', 1)
    if len(parts) != 2:
        return {'error': "Invalid instruction format"}
    
    operation, params = parts

    if operation not in S_ops:
        return {'error': "Invalid S operation"}
    
    try:
        rtrn_addr, rest = params.split(',', 1)
        imm, src_rgstr1 = rest.split('(', 1)
        src_rgstr1 = src_rgstr1.rstrip(')')
        rtrn_addr = rtrn_addr.strip()
        src_rgstr1 = src_rgstr1.strip()
        imm = imm.strip()
         # Check if imm is an integer
    except ValueError:
        return {'error': "Invalid parameter format for 'sw' instruction"}
    try:
        imm = int(imm) 
    except ValueError:
        return {'error': "Invalid imm"}
    
    if not rtrn_addr or not src_rgstr1 or not imm:
        return {'error': "One or more parameters are empty"}
    
    return {
        'error': None,
        'operation': operation,
        'rtrn_addr': rtrn_addr,
        'src_rgstr1': src_rgstr1,
        'imm': imm
    }

from rgstrfncns import rgstr_func , imm_binary
def S_binary(instruction):
    if instruction['error'] == None:
        return '1100010' + imm_binary(instruction['imm'],12)[0:5] + '010' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['rtrn_addr']) + imm_binary(instruction['imm'],12)[5:12]

    else:
        return {'error': instruction['error']}










# with open('Sinput.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#         print(S_parser(line.strip()))
#         print(S_binary(S_parser(line.strip())))

