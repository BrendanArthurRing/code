
# Define Split Variables
y = []
z = []

# Find Decreasing Pair


def decr_pair(a):
    for i, j in zip(a, a[1:]):
        if i > j:
            return (i, j)

# Confirm Increasing


def incr_check(a):
    for i, j in zip(a, a[1:]):
        if i >= j:
            return False
    return True

# Check for decreasing pair and split


def decr_split(a):
    if decr_pair(a):
        print(decr_pair(a))
        p = decr_pair(a)
        # Split
        y = tuple(a.remove(p[0]))
        z = tuple(a.remove(p[1]))
    else:
        return True

# Check if splits are increasing


def check_splits(a, b):
    if incr_check(a) or incr_check(b):
        return True
    return False


x = [3, 6, 5, 8, 10, 20, 15]
x = [1, 1]
x = [1, 1, 1, 2, 3]

decr_split(x)
check_splits(y, z)
