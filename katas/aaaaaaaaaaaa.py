from operator import itemgetter


class Test:
    def assert_equals(a, b, text=None):
        if text:
            print(text)
        if a == b:
            print('Passed')
        else:
            print(f'Failed: {a} should be {b}.')


def almostIncreasingSequence(a):

    for i, j in zip(a, a[1:]):
        if i >= j:
            a.remove(i)

    print(no_duplicates)

    x = [i for i in enumerate(a)]
    print(x)
    y = sorted(x, key=itemgetter(1))
    print(y)
    if x == y:
        return True
    else:
        return False


s = [1, 2, 993, 4, 5]
almostIncreasingSequence(s)


print('TRUE TESTS')
Test.assert_equals(almostIncreasingSequence([1, 1]), True, text='1')  # True
Test.assert_equals(almostIncreasingSequence([1, 3, 2]), True, text='2')  # True
Test.assert_equals(almostIncreasingSequence(
    [1, 3, 2, 1]), True, text='3')  # True
Test.assert_equals(almostIncreasingSequence(
    [0, -2, 5, 6]), True, text='4')  # True
Test.assert_equals(almostIncreasingSequence(
    [1, 2, 5, 3, 5]), True, text='5')  # True
Test.assert_equals(almostIncreasingSequence(
    [10, 1, 2, 3, 4, 5]), True, text='6')  # True
Test.assert_equals(almostIncreasingSequence(
    [1, 2, 3, 4, 99, 5, 6]), True, text='7')  # True
Test.assert_equals(almostIncreasingSequence(
    [123, -17, -5, 1, 2, 3, 12, 43, 45]), True, text='8')  # True
print('FALSE TESTS')
Test.assert_equals(almostIncreasingSequence(
    [1, 2, 1, 2]), False, text='9')  # False
Test.assert_equals(almostIncreasingSequence(
    [1, 1, 1, 2, 3]), False, text='10')  # False
Test.assert_equals(almostIncreasingSequence(
    [1, 2, 5, 5, 5]), False, text='11')  # False
Test.assert_equals(almostIncreasingSequence(
    [1, 4, 10, 4, 2]), False, text='12')  # False
Test.assert_equals(almostIncreasingSequence(
    [1, 1, 2, 3, 4, 4]), False, text='13')  # False
Test.assert_equals(almostIncreasingSequence(
    [1, 2, 3, 4, 3, 6]), False, text='14')  # False
Test.assert_equals(almostIncreasingSequence(
    [1, 2, 3, 4, 5, 3, 5, 6]), False, text='15')  # False
Test.assert_equals(almostIncreasingSequence(
    [40, 50, 60, 10, 20, 30]), False, text='16')  # False
Test.assert_equals(almostIncreasingSequence(
    [3, 6, 5, 8, 10, 20, 15]), False, text='17')  # False
Test.assert_equals(almostIncreasingSequence(
    [10, 1, 2, 3, 4, 5, 6, 1]), False, text='18')  # False
