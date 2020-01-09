def random_pop(array):
    # Removes random element from array.
    from random import randint
    r = randint(0, len(array) - 1)
    #print(f'Array: {array}')
    array.pop(r)
    #print(f'Array: {array}')
    return array


def strictly_increasing(array):
    # Checks if the array is strictily increasing.
    if len(array) >= 2:
        for i, j in zip(array, array[1:]):
            if i >= j:
                #print(f'False: {i} >= {j}')
                return False
        #print(f'True: Increasing {array}')
        return True
    #print('False: Only one int.')
    return False


def alsmost_increasing_sequence(array):
    x = []
    for i in range(len(array * 2)):
        if not strictly_increasing(x):
            x = array
            random_pop(x)
    print('False')


s = [1, 3, 2, 1]
alsmost_increasing_sequence(s)


'''
check_increase([1, 2, 3, 4, 5])  # True
check_increase([1, 2, 3, 5, 6, 7])  # True
check_increase([1, 2])  # True
check_increase([2, 2])  # False
check_increase([1])  # False
check_increase([1, 2, 9, 5, 6, 7])  # False


def test(s):
    from random import randint
    r = randint(0, len(s) - 1)
    print(f'Making random number {r}')

    if len(s) > 2:
        # brute force
        random_tried = set()
        if r not in random_tried:

            # del s[x]
            print(f'Brute force needed, len is {len(s)} > 2')
        pass

    if len(s) == 2:
        # check if strictly increasing
        print('Len is 2, checking if increasing')
        print(f'Comparing {s[0]} < {s[1]}')
        if s[0] < s[1]:
            print('Increasing, True')
        else:
            print('Not increasing, False')

    if len(s) <= 1:
        print(f'Len is {len(s)} <= 1. False')
        # return False

    print(f'{s}\n\n')


test([1, 3, 2, 1])
test([1, 2, 4, 3])  # True
test([1, 1])  # False
test([1, 2])  #
'''
