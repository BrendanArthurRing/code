def decr_pair(a):
    c1, c2 = 0, 1
    for i, j in zip(a, a[1:]):
        if i > j:
            return ((c1, i), (c2, j))
        c1 += 1
        c2 += 1


def decr_split(a, y, z):
    if decr_pair(a):
        p = decr_pair(a)
        del y[p[0][0]]
        del z[p[1][0]]
    else:
        return True


def incr_check(a):
    print(f'checking {a}')
    for i, j in zip(a, a[1:]):
        if i > j:
            return False
        elif i < j:
            pass
        elif i == j:
            return False
    return True


def almostIncreasingSequence(x):
    if len(x) <= 2:
        return True
    y, z = x[:], x[:]
    decr_split(x, y, z)
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

# This does not work - need to try test cases for all > pairs
# Dont assume the first one disqualifies.
# Also have to account for where the pair is found
# Just removing the element causes issues because of duplicates
# Fixed by resolving the remove issue with duplicates

'''
