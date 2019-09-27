# https://www.codewars.com/kata/disarium-number-special-numbers-series-number-3/train/python

'''
Definition

Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.
Task

Given a number, Find if it is Disarium or not .
Warm-up (Highly recommended)
Playing With Numbers Series
Notes

    Number passed is always Positive .
    Return the result as String

Input >> Output Examples

disariumNumber(89) ==> return "Disarium !!"

Explanation:

    Since , 81 + 92 = 89 , thus output is "Disarium !!"

disariumNumber(564) ==> return "Not !!"

Explanation:

Since , 51 + 62 + 43 = 105 != 546 , thus output is "Not !!"
Playing with Numbers Series
Playing With Lists/Arrays Series
For More Enjoyable Katas
ALL translations are welcomed
Enjoy Learning !!
Zizou
Fundamentals
Numbers
Mathematics
Algorithms
Basic Language Features
Conditional Statements
Control Flow
'''

# Code


def disarium_number(number):
    numbers = [int(i) for i in str(number)]
    print(f"Numbers: {numbers}")
    results = []
    power = 1
    for i in numbers:
        results.append(pow(i, power))
        power += 1
    print(f"Results: {results}")
    result = sum(results)
    print(f"Number: {number}, Result: {result}")
    import csv
    with open("numbers.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(results)
    if number == result:
        return "Disarium !!"
    else:
        return "Not !!"

# There is a problem using the index function, because if there are duplicated numbers the index function will return the lowest indext number meaning a number later in the list will be powered by a lower index position.

# Not sure what a disarium number is from the explaination, will need to do some research. Disarium number is not in wikipedia.
# https://www.w3resource.com/java-exercises/numbers/java-number-exercise-11.php

# I will try to use zip - making a tuple of index and number - actuall zip didnt help me here
# https://codewithmosh.com/courses/417695/lectures/6781700

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


Test.describe("Sample Tests")
Test.it("Basic Test")
# Test.assert_equals(disarium_number(89), "Disarium !!")
# Test.assert_equals(disarium_number(518), "Disarium !!")
# Test.assert_equals(disarium_number(1024), "Not !!")
# These Dont Work - fixed by not using index() as power
# Test.assert_equals(disarium_number(1676), "Disarium !!")
# Test.assert_equals(disarium_number(2427), "Disarium !!")
# This does not work
Test.assert_equals(disarium_number(24226467987), "Disarium !!")
