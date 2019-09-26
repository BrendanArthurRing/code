# https://www.codewars.com/kata/5874657211d7d6176a00012f

'''
Aliens from Kepler 27b have immigrated to Earth! They have learned English and go to our stores, eat our food, dress like us, ride Ubers, use Google, etc. However, they speak English a little differently. Can you write a program that converts their Alien English to our English?
Task:

Write a function converting their speech to ours. They tend to speak the letter a like o and o like a u.

>>> convert('hello')
'hellu'
>>> convert('codewars')
'cudewors'

Fundamentals
Strings
'''


# def convert(text):
#     converted = ""
#     for letter in text:
#         letter = letter.replace("o", "u")
#         letter = letter.replace("a", "o")
#         converted += letter
#     print(converted)
#     return converted

def convert(text):
    text = text.replace("o", "u")
    text = text.replace("a", "o")
    return text

# The best practices was


def convert(st):
    return st.replace('o', 'u').replace('a', 'o')


class Test:
    def assert_equals(a, b):
        if a == b:
            print("Passed")
        if a != b:
            print("Failed")


Test.assert_equals(convert('codewars'), 'cudewors')
Test.assert_equals(convert('hello'), 'hellu')
