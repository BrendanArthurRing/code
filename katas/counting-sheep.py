# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

'''
Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
'''


def count_sheeps(array):
    return len([i for i in array if i])


# The Best Practice
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
# did not realize that arrays had acount feature, will need to test hwo this works

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


array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

test.assert_equals(count_sheeps(array1), 17,
                   "There are 17 sheeps in total, not %s" % count_sheeps(array1))
