def rgstr_func2(x):
    if x == "s0" or x == "fp":
        return "01000"
    elif x == "s1":
        return "01001"
    elif x == "s2":
        return "10010"
    elif x == "s3":
        return "10011"
    elif x == "s4":
        return "10100"
    elif x == "s5":
        return "10101"
    elif x == "s6":
        return "10110"
    elif x == "s7":
        return "10111"
    elif x == "s8":
        return "11000"
    elif x == "s9":
        return "11001"
    elif x == "s10":
        return "11010"
    elif x == "s11":
        return "11011"
    elif x == "sp":
        return "00010"
    elif x == "t0":
        return "00101"
    elif x == "t1":
        return "00110"
    elif x == "t2":
        return "00111"
    elif x == "t3":
        return "11100"
    elif x == "t4":
        return "11101"
    elif x == "t5":
        return "11110"
    elif x == "t6":
        return "11111"
    elif x == "tp":
        return "00100"
    elif x == "a0":
        return "01010"
    elif x == "a1":
        return "01011"
    elif x == "a2":
        return "01100"
    elif x == "a3":
        return "01101"
    elif x == "a4":
        return "01110"
    elif x == "a5":
        return "01111"
    elif x == "a6":
        return "10000"
    elif x == "a7":
        return "10001"
    elif x == "gp":
        return "00011"
    elif x == "ra":
        return "00001"
    elif x == "zero":
        return "00000"

def rgstr_func(x):
    return rgstr_func2(x)[::-1]

def imm_binary(inpnum, n):
    number = int(inpnum)

    if number >= 0:
        binary = bin(number)[2:].zfill(n)
    else:
        binary = bin((1 << n) + number)[2:]

    return binary[::-1]

