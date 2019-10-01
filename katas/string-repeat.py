# https://www.codewars.com/kata/string-repeat/train/python

'''
Write a function called repeatString which repeats the given String src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

Fundamentals
'''


def repeat_str(repeat, string):
    return string * repeat


# this one is simple - yay I got the best practice
def repeat_str(repeat, string):
    return repeat * string


# Test Block
class Test:
    def assert_equals(a, b):
        if a == b:
            print("Passed")
        if a != b:
            print("Failed")

    def describe(text):
        print(text)

    def it(text):
        print(text)


Test.describe("Example Tests")
Test.assert_equals(repeat_str(4, 'a'), 'aaaa')
Test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
Test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
