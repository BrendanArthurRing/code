def check_palindrome(input_string):

    for i, j in zip(input_string, reversed(input_string)):
        if i is not j:
            print('bad')
            return False
    print('good')
    return True


s = 'aabaa'
check_palindrome(s)

s = 'aabdaa'
check_palindrome(s)
