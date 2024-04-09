def binary_to_reg_name(binary_input):
    # Reverse the binary input since rgstr_func reverses the output of rgstr_func2
    reversed_binary_input = binary_input[::-1]
    
    # Mapping of binary representations to register names
    binary_to_name = {
        "01000": "s0/fp", "01001": "s1", "10010": "s2", "10011": "s3",
        "10100": "s4", "10101": "s5", "10110": "s6", "10111": "s7",
        "11000": "s8", "11001": "s9", "11010": "s10", "11011": "s11",
        "00010": "sp", "00101": "t0", "00110": "t1", "00111": "t2",
        "11100": "t3", "11101": "t4", "11110": "t5", "11111": "t6",
        "00100": "tp", "01010": "a0", "01011": "a1", "01100": "a2",
        "01101": "a3", "01110": "a4", "01111": "a5", "10000": "a6",
        "10001": "a7", "00011": "gp", "00001": "ra", "00000": "zero"
    }
    
    # Lookup the register name using the reversed binary input
    return binary_to_name.get(reversed_binary_input, "Unknown Register")

# Should return "a4"