def arrayPacking(a):
    bits = [f'{i:08b}' for i in a]
    M = ''.join(bits[::-1])
    return int(M, 2)
