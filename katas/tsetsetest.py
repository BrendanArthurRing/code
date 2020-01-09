def r_pop(a):
    from random import randint
    r = randint(0, len(a) - 1)
    return r, a.pop(r)


def increasing(a):
    if len(a) <= 1:
        return None
    if len(a) >= 2:
        for i, j in zip(a, a[1:]):
            if i >= j:
                return False
    return True


def almostIncreasingSequence(a):
    if increasing(a):
        return True
    for i in range(len(a * 10)):
        x = r_pop(a)
        if increasing(a) is None:
            return True
        if increasing(a) is True:
            return True
        a.insert(x[0], x[1])
    return False


# s = [1, 3, 2, 1]
# s = [1, 3, 2]
#s = [1, 1]
# almostIncreasingSequence(s)


x = (1, 2, 3)
x.
