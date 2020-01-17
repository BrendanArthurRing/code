def rangeBitCount(a, b):
    return ''.join([f'{i:b}' for i in range(a, b + 1)]).count('1')

# The top voted solution


def rangeBitCount(a, b):
    return sum(bin(x).count('1') for x in range(a, b+1))
