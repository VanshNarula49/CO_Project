def I_parser(instruction):
    I_ops = ['lw', 'addi', 'sltiu', 'jalr']
    
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
        except ValueError:
            return {'error': "Invalid parameter format for 'lw' instruction"}
    else:
        params_parts = params.split(',')
        if len(params_parts) != 3:
            return {'error': "Invalid number of parameters"}
        
        rtrn_addr_rgstr, src_rgstr1, imm = map(str.strip, params_parts)
    
    if not rtrn_addr_rgstr or not src_rgstr1 or not imm:
        return {'error': "One or more parameters are empty"}
    
    return {
        'error': None,
        'operation': instruction_code,
        'rtrn_addr_rgstr': rtrn_addr_rgstr,
        'src_rgstr1': src_rgstr1,
        'imm': imm
    }

with open('Iinput.txt', 'r') as file:
    for line in file:
        print(line.strip())
        print(I_parser(line.strip()))

