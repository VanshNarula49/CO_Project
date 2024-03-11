def R_parser(instruction):
    R_ops = ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
    
    parts = instruction.split(' ', 1)
    if len(parts) != 2:
        return {'error': "Invalid instruction format"}
    
    operation, params = parts

    if operation not in R_ops:
        return {'error': "Invalid R operation"}
    
    params_parts = params.split(',')
    if len(params_parts) != 3:
        return {'error': "Invalid number of parameters"}
    
    dstn_rgstr, src_rgstr1, src_rgstr2 = map(str.strip, params_parts)
    
    if not dstn_rgstr or not src_rgstr1 or not src_rgstr2:
        return {'error': "One or more parameters are empty"}
    
    return {
        'error': None,
        'operation': operation,
        'dstn_rgstr': dstn_rgstr,
        'src_rgstr1': src_rgstr1,
        'src_rgstr2': src_rgstr2
    }

with open('Rinput.txt', 'r') as file:
    for line in file:
        print(line.strip())
        print(R_parser(line.strip()))