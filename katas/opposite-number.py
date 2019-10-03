# https://www.codewars.com/kata/opposite-number/train/python

'''
Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
'''


def opposite(number):
    return number * -1


# The best practice
def opposite(number):
    return -number

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


Test.assert_equals(opposite(1), -1)
