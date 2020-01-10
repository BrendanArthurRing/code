from collections import Counter as C


def palindromeRearranging(string):
    return sum(value % 2 != 0 for value in C(string).values()) < 2
    '''
    # If there's only one odd count.
    odd_count = sum(value % 2 != 0 for value in C(string).values())
    print(odd_count)

    #palindrome = sum(i != j for i, j in zip(string, reversed(string))) == 0
    '''


print(palindromeRearranging('aabb'), True)
print(palindromeRearranging('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc'), False)
print(palindromeRearranging('abbcabb'), True)


# The top voted solution was
def palindromeRearranging(inputString):
    '''
    print(set(inputString))
    print(inputString.count('a') % 2)
    print([inputString.count(i) % 2 for i in set(inputString)])
    print([inputString.count(i) % 2 for i in inputString])
    x = [inputString.count(i) % 2 for i in inputString]
    print(set(x))
    '''
    return sum([inputString.count(i) % 2 for i in set(inputString)]) <= 1


print(palindromeRearranging('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc'), False)
print(palindromeRearranging('aaaaaaaaaaaaaaaaabaaaaaaaaaaaaac'), False)


# This code counts the occurances of the letters
# The set is called on the list of odds vs evens during the list comprehension
# This somehow sets just the value of i at the moment and but preserves counts from
# the previous iteration - due to the function of list comprehensions.
