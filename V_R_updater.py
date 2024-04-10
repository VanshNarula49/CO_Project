from reg_value import reg_value
from reg_value import values
from B_R_Parser import decode_R_binary

def updater_R(dictR):
    if dictR['operation'] == 'add':
        v1 = values[dictR['src_rgstr1']] #sext?
        v2 = values[dictR['src_rgstr2']] #sext?
        v3 = v1 + v2
        values[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'sub' and dictR['src_rgstr1'] == "zero":
        v2 = values[dictR['src_rgstr2']]
        v3 = 0 - v2
        values[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'sub':
        v1 = values[dictR['src_rgstr1']]
        v2 = values[dictR['src_rgstr2']]
        v3 = v1 - v2
        values[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'slt':
        v1 = values[dictR['src_rgstr1']] #sext?
        v2 = values[dictR['src_rgstr2']] #sext?
        if v1 < v2:
            v3 = 1
            values[dictR['dstn_rgstr']] = v3
    # elif dictR['operation'] == 'sltu':
    #     #?
    elif dictR['operation'] == 'xor':
        v1 = values[dictR['src_rgstr1']]
        v2 = values[dictR['src_rgstr2']]
        v3 = v1^v2
        values[dictR['dstn_rgstr']] = v3
    # elif dictR['operation'] == 'sll':
        #?
    # elif dictR['operation'] == 'srl':
        #?
    elif dictR['operation'] == 'or':
        v1 = values[dictR['src_rgstr1']]
        v2 = values[dictR['src_rgstr2']]
        v3 = v1|v2
        values[dictR['dstn_rgstr']] = v3
    elif dictR['operation'] == 'and':
        v1 = values[dictR['src_rgstr1']]
        v2 = values[dictR['src_rgstr2']]
        v3 = v1&v2
        values[dictR['dstn_rgstr']] = v3

    return values

# Example usage
dict = decode_R_binary('00000000000010010000010010110011') ## add s1,s2,zero
newvals = updater_R(dict)
print (newvals)