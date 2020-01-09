# This does not work - need to try test cases for all > pairs
# Dont assume the first one disqualifies.
# Also have to account for where the pair is found
# Just removing the element causes issues because of duplicates


def find_first_decreasing_pair(a):
    for i, j in zip(a, a[1:]):
        if i > j:
            print(f'Decreasing Pair {i, j}')
            return (i, j)


decreasing_pairs = []


def find_decreasing_pairs(a):
    for i, j in zip(a, a[1:]):
        if i > j:
            print(f'Decreasing Pair {i, j}')
            decreasing_pairs.append((i, j))


def split_at_decreasing_pairs(a, *):
    pass


def decr_split(a, y, z):
    if decr_pair(a):
        p = decr_pair(a)
        y.remove(p[0])
        z.remove(p[1])
    else:
        return True


def incr_check(a):
    print(f'checking {a}')
    for i, j in zip(a, a[1:]):
        if i > j:
            print(f'{i} > {j}, not increasing')
            return False
        elif i < j:
            print(f'{i} < {j}, ok so far')
        elif i == j:
            print(f'{i} = {j}, not increasing')
            return False
    print('made it through the check')
    return True


def almostIncreasingSequence(x):
    print(f'Testing {x}')
    if len(x) <= 2:
        return True
    y, z = x[:], x[:]
    decr_split(x, y, z)
    print(f'checking {y} vs {z}')
    incr_check(y)
    incr_check(z)
    if not incr_check(y) and not incr_check(z):
        return False
    if incr_check(y) or incr_check(z):
        return True


# Test Block
x = [1, 3, 2, 1]

incr_check(x)

'''
if almostIncreasingSequence(x) == False:
    print('Passed')
def check_splits(a, b):
    if incr_check(a) or incr_check(b):
        return True
    return False

'''
