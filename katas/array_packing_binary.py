def arrayPacking(a):
    bits = [f'{i:08b}' for i in a]
    M = ''.join(bits[::-1])
    return int(M, 2)

# The top voted is


def arrayPacking(a):
    return sum([a[i] << i*8 for i in range(len(a))])

# I have no idea what << does or, why multiplying
# the iteration through the range of len(a) by 8 works
