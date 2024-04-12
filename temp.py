def hexconv(a):
    a = a + 65536
    b = (hex(a)[2:].zfill(8))
    return '0x'+b
print(hexconv(44))