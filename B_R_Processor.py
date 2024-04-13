from memory import register
from brgstfncns import sext
from B_R_Parser import decode_R_binary

def R_processor(dictR):
    if dictR['operation'] == 'add':
        v1 = sext(register[dictR['src_rgstr1']]) #sext?
        v2 = sext(register[dictR['src_rgstr2']]) #sext?
        v3 = v1 + v2
        register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'sub' and dictR['src_rgstr1'] == "zero":
        v2 = register[dictR['src_rgstr2']]
        v3 = 0 - v2
        register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'sub':
        v1 = register[dictR['src_rgstr1']]
        v2 = register[dictR['src_rgstr2']]
        v3 = v1 - v2
        register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'slt':
        v1 = sext(register[dictR['src_rgstr1']]) #sext?
        v2 = sext(register[dictR['src_rgstr2']]) #sext?
        if v1 < v2:
            v3 = 1
            register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'sltu':
         v1 = register[dictR['src_rgstr1']] #sext?
         v2 = register[dictR['src_rgstr2']] #sext?
         v1 = int(format(v1,'032b'),2)
         v2 = int(format(v2,'032b'),2)
         if v1 < v2:
            v3 = 1
            register[dictR['dstn_rgstr']] = v3
    #     #?
    elif dictR['operation'] == 'xor':
        v1 = register[dictR['src_rgstr1']]
        v2 = register[dictR['src_rgstr2']]
        v3 = v1^v2
        register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'sll':
         v1 = register[dictR['src_rgstr1']]
         v2 = register[dictR['src_rgstr2']]
         v3 = v1<<(int(format(v2,'032b')[::-1][0:5][::-1],2))
         register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'srl':
         v1 = register[dictR['src_rgstr1']]
         v2 = register[dictR['src_rgstr2']]
         v3 = v1>>(int(format(v2,'032b')[::-1][0:5][::-1],2))
         register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'or':
        v1 = register[dictR['src_rgstr1']]
        v2 = register[dictR['src_rgstr2']]
        v3 = v1|v2
        register[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'and':
        v1 = register[dictR['src_rgstr1']]
        v2 = register[dictR['src_rgstr2']]
        v3 = v1&v2
        register[dictR['dstn_rgstr']] = v3

    return register

# Example usage
dict = decode_R_binary('00000000000010010000010010110011') ## add s1,s2,zero
newvals = R_processor(dict)
print (newvals)
print(register['s1'])