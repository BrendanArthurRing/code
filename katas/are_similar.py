# Results in a time out.
'''
def areSimilar(a, b):

    # Check a and b are equal
    if a == b:
        return True

    # Check if swapping is possible
    swapping_possible = False
    x, y = sorted(a), sorted(b)
    if x == y:
        swapping_possible = True

    # Try swapping if possible
    if swapping_possible:
        for i in range(len(a) - 1):
            a[i], a[i + 1] = a[i + 1], a[i]
            # Check if Equal
            if a == b:
                return True
            # Put it back the way it was
            a[i + 1], a[i] = a[i], a[i + 1]
    
    # Try swapping spaced by one if possible
    for i in range(len(a) - 2):
            a[i], a[i + 2] = a[i + 2], a[i]
            # Check if Equal
            if a == b:
                return True
            # Put it back the way it was
            a[i + 2], a[i] = a[i], a[i + 2]

    # Not similar
    return False
'''

from collections import Counter as C
a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
print(sum(A != B for A, B in zip(a, b)))
print([A != B for A, B in zip(a, b)])


#areSimilar(a, b)

a = [2, 3, 1]
b = [1, 3, 2]
print(sum(A != B for A, B in zip(a, b)))
#areSimilar(a, b)

a = [1, 2, 2]
b = [2, 2, 1]
print(sum(A != B for A, B in zip(a, b)))
#areSimilar(a, b)


# Best Answers to this one


def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3

# returns a list of false for when the items match and true for when they are not matching
# sum, totals the number of instances where there is not a match
# if the total number of non matches is less than three then it must be similar
# Counter returns a dict with the counts of each number instance in the array
# This checks for the possibility of swapping


a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
print(C(a))
print(C(b))
