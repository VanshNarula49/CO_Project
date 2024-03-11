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
    
    return {
        'error': None,
        'operation': instruction_code,
        'src_rgstr1': src_rgtstr1,
        'src_rgstr2': src_rgstr2,
        'imm': imm
    }

with open('Binput.txt', 'r') as file:
    for line in file:
        print(line.strip())
        print(B_parser(line.strip()))

