# https://www.codewars.com/kata/all-star-code-challenge-number-18/train/python


'''
This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

strCount('Hello', 'o') // => 1
strCount('Hello', 'l') // => 2
strCount('', 'z')      // => 0

Notes:

    The first argument can be an empty string
    The second string argument will always be of length 1

'''


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

# Here is my code


def str_count(strng, letter):
    return strng.count(letter)

# The Best Practice Was


def strCount(string, letter):
    return string.count(letter)


# Tests
Test.assert_equals(str_count('hello', 'l'), 2)
