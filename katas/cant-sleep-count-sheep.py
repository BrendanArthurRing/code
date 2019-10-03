# https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep/train/python

'''
If you can't sleep, just count sheep!!
Task:

Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
'''


def count_sheep(n):
    sheep_count = ''
    for i in range(1, n + 1):
        sheep_count += f'{i} sheep...'
    return sheep_count


# The best practice was
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))


# Test Block


class Test:
    def assert_equals(a, b):
        if a == b:
            print("Passed \n \n")
        if a != b:
            print(f"Failed\n{a} should equal {b}\n\n")

    def describe(text):
        print(text)

    def expect_error(text, test_function):
        print(text)
        if test_function == ZeroDivisionError:
            print("Passed")
        print("Failed")

    def it(text):
        print(text)


Test.assert_equals(count_sheep(1), "1 sheep...")
Test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
Test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
