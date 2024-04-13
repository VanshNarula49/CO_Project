def I_parser(instruction):
    I_ops = ['lw', 'addi', 'sltiu', 'jalr']
    x_values = ["s0", "fp", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "sp", "t0", "t1", "t2", "t3", "t4", "t5", "t6", "tp", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "gp", "ra", "zero"]

   
    parts = instruction.split(' ', 1)
    if len(parts) != 2:
        return {'error': "Invalid instruction format"}
    
    instruction_code, params = parts

    if instruction_code not in I_ops:
        return {'error': "Invalid I operation"}
    
    rtrn_addr_rgstr = src_rgstr1 = imm = None
    
    if instruction_code == 'lw':
        try:
            rtrn_addr_rgstr, rest = params.split(',', 1)
            imm, src_rgstr1 = rest.split('(', 1)
            src_rgstr1 = src_rgstr1.rstrip(')')
            rtrn_addr_rgstr = rtrn_addr_rgstr.strip()
            src_rgstr1 = src_rgstr1.strip()
            imm = imm.strip()
            imm = int(imm)  # Check if imm is an integer
        except ValueError:
            return {'error': "Invalid imm"}
    else:
        params_parts = params.split(',')
        if len(params_parts) != 3:
            return {'error': "Invalid number of parameters"}
        
        rtrn_addr_rgstr, src_rgstr1, imm = map(str.strip, params_parts)
        try:
            imm = int(imm)
        except ValueError:
            return {'error': "Invalid imm"}  
    
    if not rtrn_addr_rgstr or not src_rgstr1 or imm == None:
        return {'error': "One or more parameters are empty"}
    if rtrn_addr_rgstr not in x_values or src_rgstr1 not in x_values:
        return {'error': " register not valid"}

    
    return {
        'error': None,
        'operation': instruction_code,
        'rtrn_addr_rgstr': rtrn_addr_rgstr,
        'src_rgstr1': src_rgstr1,
        'imm': imm
    }
from rgstrfncns import rgstr_func , imm_binary

def I_binary(instruction):
    if instruction['error'] == None:
        if instruction['operation'] == 'lw':
            return '1100000' + rgstr_func(instruction['rtrn_addr_rgstr']) + '010' + rgstr_func(instruction['src_rgstr1']) + imm_binary(instruction['imm'],12)
            
        elif instruction['operation'] == 'addi':
            return '1100100' + rgstr_func(instruction['rtrn_addr_rgstr']) + '000' + rgstr_func(instruction['src_rgstr1']) + imm_binary(instruction['imm'],12)
            
        elif instruction['operation'] == 'sltiu':
            return '1100100' + rgstr_func(instruction['rtrn_addr_rgstr']) + '110' + rgstr_func(instruction['src_rgstr1']) + imm_binary(instruction['imm'],12)
            
        elif instruction['operation'] == 'jalr':
            return '1110011' + rgstr_func(instruction['rtrn_addr_rgstr']) + '000' + rgstr_func(instruction['src_rgstr1']) + imm_binary(instruction['imm'],12)
    else :
        return {'error': instruction['error']}

# with open('Iinput.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#         print(I_parser(line.strip()))
#         print(I_binary(I_parser(line.strip())))
