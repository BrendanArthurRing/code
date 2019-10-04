# https://www.codewars.com/kata/correct-the-mistakes-of-the-character-recognition-software/train/python

'''
Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

    S is misinterpreted as 5
    O is misinterpreted as 0
    I is misinterpreted as 1

The test cases contain numbers only by mistake.
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


def correct(string):
    mistakes = {
        '5': 'S',
        '0': 'O',
        '1': 'I'
    }
    return ''.join(mistakes[i] if i in mistakes else i for i in string)


# Here is the best practice!

def correct(string):
    # Translate takes one argument dict - make trans creates a mapping dict in unicode out of the string for each character
    return string.translate(str.maketrans("501", "SOI"))


string.translate(str.maketrans)

Test.assert_equals(correct("L0ND0N"), "LONDON")
Test.assert_equals(correct("DUBL1N"), "DUBLIN")
Test.assert_equals(correct("51NGAP0RE"), "SINGAPORE")
Test.assert_equals(correct("BUDAPE5T"), "BUDAPEST")
Test.assert_equals(correct("PAR15"), "PARIS")
