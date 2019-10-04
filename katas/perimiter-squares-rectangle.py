# https://www.codewars.com/kata/559a28007caad2ac4e000083

'''
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

alternative text

# Hint: See Fibonacci sequence

# Ref: http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
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


def perimeter(n):
	arr = [1, 1]
	for i in range(n - 1):
		arr.append(arr[i] + arr[i + 1])
	x = 4 * sum(arr)
	return x


# Tests
Test.assert_equals(perimeter(5), 80)
Test.assert_equals(perimeter(7), 216)
Test.assert_equals(perimeter(20), 114624)
Test.assert_equals(perimeter(30), 14098308)
Test.assert_equals(perimeter(100), 6002082144827584333104
