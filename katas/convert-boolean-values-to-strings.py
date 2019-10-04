# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no/train/python

'''
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
'''


def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# This is the best practice


def bool_to_word(bool):
    return "Yes" if bool else "No"


class Test:
    """TEST BLOCK"""
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


Test.assert_equals(bool_to_word(True), 'Yes')
Test.assert_equals(bool_to_word(False), 'No')
