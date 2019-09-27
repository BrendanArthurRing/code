# https://www.codewars.com/kata/square-every-digit/train/python

'''
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
Fundamentals
Mathematics
Algorithms
Numbers
'''


def square_digits(num):
    result = [int(i)**2 for i in str(num)]
    return int(''.join(map(str, result)))


# https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/

# Test Block


class Test:
    def assert_equals(a, b):
        if a == b:
            print("Passed")
        if a != b:
            print("Failed")


Test.assert_equals(square_digits(9119), 811181)
