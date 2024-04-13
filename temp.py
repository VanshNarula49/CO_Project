# instcn = '11111111000111111111000011101111'
# binary = '11111111000111111111000011101111'
# imm = instcn[::-1][12:][::-1]
# # immin[0] 20th bit
# # immin[1:11] 10-1 bit
# #immin[11] 11 bit
# # immin[12:20] 19-12 bit
# print(imm)
# cnstrcbin = imm[0] + imm[12:19] + imm[11] + imm[1:11] + '0'
# imm_20 = binary[31][::-1] + binary[12:20][::-1] + binary[20][::-1] + binary[21:31][::-1] 
# imm_20 = imm_20[0:19]
# print(cnstrcbin)
# print(imm_20)
# print(int(imm_2,2))



# # Example usage
# print_32bit_twos_complement(10)  # Positive number
# print_32bit_twos_complement(-10)  # Negative number
from memory import register
for keys in register.keys():
    print(keys)