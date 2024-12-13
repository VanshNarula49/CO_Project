from Bonus_Parser import decode_bonus_binary
from memory import register  # Assuming this function exists

def process_bonus_instruction(dict_bonus):

    def decimal_to_twos_complement_binary(decimal_num):
        if decimal_num < 0:
            decimal_num = 2**32 + decimal_num  # Convert negative number to 32-bit equivalent

        binary_num = bin(decimal_num)[2:]  # Convert decimal to binary, remove '0b' prefix
        binary_num = binary_num.zfill(32)  # Ensure binary number is 32 bits long
        return binary_num
    def twos_complement_to_decimal(binary_str):
        # Check if the number is negative
        if binary_str[0] == '1':
            # Find the 2's complement
            inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
            decimal = -int(inverted, 2) - 1
        else:
            decimal = int(binary_str, 2)
        return decimal

    if (dict_bonus['operation'] == 'mul'):
        v1 = register[dict_bonus['rs1']]
        v2 = register[dict_bonus['rs2']]
        v3 = v1 * v2

        v3 &= 0xFFFFFFFF
        binary_string = format(v3, '032b')
        v3 = twos_complement_to_decimal(binary_string)

        register[dict_bonus['rd']] = v3

    elif (dict_bonus['operation'] == 'rst'):
        for key in register.keys():
            if key == 'sp':
                register[key] = 256
            else:
                register[key] = 0

    elif (dict_bonus['operation'] == 'rvrs'):
        
        v1 = register[dict_bonus['rs1']]
        v1 = decimal_to_twos_complement_binary(v1)
        v2 = v1[::-1]
        v2 = twos_complement_to_decimal(v2)
        register[dict_bonus['rd']] = v2

    else:
        print ("Invalid op")
        
# Example usage
# print(register)
# dict = decode_bonus_binary('00000001001010011000101000000000') 
# process_bonus_instruction(dict)
# print(register)