def convertFracts(lst):
    pass


# Sample Tests
'''
a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
test.assert_equals(convertFracts(a), b)
'''



# Instructions
'''
Common denominators

You will have a list of rationals in the form

 { {numer_1, denom_1} , ... {numer_n, denom_n} }

or

 [ [numer_1, denom_1] , ... [numer_n, denom_n] ]

or

 [ (numer_1, denom_1) , ... (numer_n, denom_n) ]

where all numbers are positive ints.

You have to produce a result in the form

 (N_1, D) ... (N_n, D)

or

 [ [N_1, D] ... [N_n, D] ]

or

 [ (N_1', D) , ... (N_n, D) ]

or

{{N_1, D} ... {N_n, D}}

depending on the language (See Example tests)

in which D is as small as possible and

 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

Note for Bash

input is a string, e.g "2,4,2,6,2,8"

output is then "6 12 4 12 3 12"
'''



# Link
# https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python