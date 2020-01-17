def rangeBitCount(a, b):
    return ''.join([f'{i:b}' for i in range(a, b + 1)]).count('1')
