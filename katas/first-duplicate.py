'''
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

    For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

    There are 2 checked: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

    For a = [2, 2], the output should be firstDuplicate(a) = 2;

    For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer a

    Guaranteed constraints:
    1 ≤ a.length ≤ 105,
    1 ≤ a[i] ≤ a.length.

    [output] integer
        The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.

[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
'''


def generate_random_array(n):
    from random import randint as r
    array = []
    for i in range(1, n):
        array.append(r(1, n))
    return array


def generate_terrible_array(n):
    array = []
    for i in range(1, n):
        array.append(i)
    array[-1] = array[0]
    return array


def firstDuplicate(a):
    from timeit import default_timer as timer
    start = timer()
    checked = []
    for i in a:
        if i not in checked:
            checked.append(i)
            #print(f'Checking {i}')
        else:
            print(f'Found {i}')
            print(f'Running time: {timer() - start}')
            return i
    print('No duplicates found.')
    print(f'Running time: {timer() - start}')
    return -1


firstDuplicate([2, 1, 3, 5, 3, 2])
firstDuplicate([4, 1, 3, 5, 6, 2])
firstDuplicate([2, 2])
firstDuplicate(generate_random_array(10**5))
# firstDuplicate(generate_terrible_array(10**5))

# finding the first duplicate as iterating through.
# if no duplicate return -1
# [execution time limit] 4 seconds (py3)
# 10^5 max
