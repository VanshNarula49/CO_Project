def R_parser(instruction):
    x_values = ["s0", "fp", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "sp", "t0", "t1", "t2", "t3", "t4", "t5", "t6", "tp", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "gp", "ra", "zero"]

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
    
    if dstn_rgstr not in x_values or src_rgstr1 not in x_values or src_rgstr2 not in x_values:
        return {'error': "One or more registers are not valid"}
    
    return {
        'error': None,
        'operation': operation,
        'dstn_rgstr': dstn_rgstr,
        'src_rgstr1': src_rgstr1,
        'src_rgstr2': src_rgstr2
    }


from rgstrfncns import rgstr_func
def R_binary(instruction):
    if instruction['error'] == None:
        if instruction['operation'] == 'add':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '000' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'sub':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '000' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000010'
        elif instruction['operation'] == 'sll':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '100' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'slt':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '010' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'sltu':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '110' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'xor':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '001' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'srl':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '101' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'or':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '011' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
        elif instruction['operation'] == 'and':
            
            return '1100110' + rgstr_func(instruction['dstn_rgstr']) + '111' + rgstr_func(instruction['src_rgstr1']) + rgstr_func(instruction['src_rgstr2']) + '0000000'
    else:
        return {'error': instruction['error']}
# with open('Rinput.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#         print(R_parser(line.strip()))
#         print(R_binary(R_parser(line.strip())))

