a = [1, 2, 3, 4, 5]
b = [10, 0, 10, 0, 10]

new_list = [max(i, n) for i, n in zip(a, b)]


def fmax(a, b):
    return [max(i, n) for i, n in zip(a, b)]

# needs to be less than 36 char


def fmax(a, b): print(max(zip(a, b)))


fmax(a, b)


def fmax(a, b): return max(a, b)


####################################
max()


print(max([(int(5, x) for x in range(8)])[1])
