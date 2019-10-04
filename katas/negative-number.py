# https://www.codewars.com/kata/return-negative/train/python

'''
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0

Notes:

    The number can be negative already, in which case no change is required.
    Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
'''


def make_negative(number):
    return abs(number) * -1


# The best practice was
def make_negative(number):
    return -abs(number)

# Test Block


class Test:
    def assert_equals(a, b, hint=None):
        if a == b:
            print("Passed \n \n")
        if a != b:
            print(f"Failed\n{a} should equal {b}\n\n")
        if hint:
            print(hint)

    def describe(text):
        print(text)

    def expect_error(text, test_function):
        print(text)
        if test_function == ZeroDivisionError:
            print("Passed")
        print("Failed")

    def it(text):
        print(text)


Test.assert_equals(make_negative(42), -42)
Test.assert_equals(make_negative(0), 0)
