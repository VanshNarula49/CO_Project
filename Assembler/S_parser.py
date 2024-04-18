def S_parser(instruction):
    S_ops = ['sw']
    x_values = ["s0", "fp", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "sp", "t0", "t1", "t2", "t3", "t4", "t5", "t6", "tp", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "gp", "ra", "zero"]
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
    
    if not rtrn_addr or not src_rgstr1 or imm == None:
        return {'error': "One or more parameters are empty"}
    
    if rtrn_addr not in x_values or src_rgstr1 not in x_values:
        return {'error': "Return address or source register not valid"}
    
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

