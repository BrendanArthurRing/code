# https://www.codewars.com/kata/simple-fraction-to-mixed-number-converter/train/python

'''
Task

Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).
Value ranges

    -10 000 000 < x < 10 000 000
    -10 000 000 < y < 10 000 000

Examples

    Input: 42/9, expected result: 4 2/3.
    Input: 6/3, expedted result: 2.
    Input: 4/6, expected result: 2/3.
    Input: 0/18891, expected result: 0.
    Input: -10/7, expected result: -1 3/7.
    Inputs 0/0 or 3/0 must raise a zero division error.

Note

Make sure not to modify the input of your function in-place, it is a bad practice.


'''


from fractions import gcd
from fractions import Fraction
from re import match
from fractions import Fraction as frac


def mixed_fraction(string):
    # Use RegEx to extract the fractions parts
    expression = r'(-?\d*)(/)(-?\d*)'
    matched = match(expression, string)
    num = int(matched.group(1))
    den = int(matched.group(3))
    whole_num = 0
    simple_fract = 0

    print(f"Original: {string}")
    print(f'Matched: {num}/{den}')

    # Check for zero division
    try:
        num / den
    except ZeroDivisionError:
        print('Denominator cannot be 0.')
        raise ZeroDivisionError

    # Zero Numerator
    if num == 0:
        print('Zero Numerator')
        return '0'

    # Double Negative
    if num < 0 and den < 0:
        print('Double Negative')
        whole_num = num // den
        num = abs(num) % abs(den)
        den = abs(den)
        print(f'Mixed Fraction: {whole_num} {num}/{den}')
        simple_fract = frac(f'{num}/{den}')
        print(f'Simple Mixed Fraction: {whole_num} {simple_fract}')

    # Negative Numerator | Num < Den
    elif num < 0 and den > 0 and abs(num) < abs(den):
        print('Negative Numberator | Num < Den')
        whole_num = (num // den) + 1
        if whole_num == 0:
            simple_fract = frac(f'{num}/{den}')
            print(f'Simple Fraction: {simple_fract}')
            num = simple_fract.numerator
            den = simple_fract.denominator
        else:
            num = (num % den) - 1
        print(f'Negative Numerator: {whole_num} {num}/{den}')

    # Negative Numerator | Num > Den
    elif num < 0 and den > 0 and abs(num) > abs(den):
        print('Negative Numerator | Num > Den')
        simple_fract = frac(f'{num}/{den}')
        print(f'Simple Fraction: {simple_fract}')
        num = simple_fract.numerator
        den = simple_fract.denominator
        if den == 1:
            whole_num = num
        else:
            whole_num = (num // den) + 1
        num = abs(num) % abs(den)

    # Negative Denominator | Num < Den
    elif num > 0 and den < 0 and abs(num) < abs(den):
        print('Negative Denominator | Num < Den')
        whole_num = (num // den) + 1
        if whole_num == 0:
            den = abs(den)
            num = num * -1
            simple_fract = frac(f'{num}/{den}')
            print(f'Simple Fraction: {simple_fract}')
            num = simple_fract.numerator
            den = simple_fract.denominator
        else:
            num = num % den
            den = abs(den)
        print(f'Negative Denominator: {whole_num} {num}/{den}')

    # Negative Denominator | Num > Den
    elif num > 0 and den < 0 and abs(num) > abs(den):
        print('Negative Denominator | Num > Den')
        if abs(num) % abs(den) == 0:
            return f'{int(num / den)}'
        else:
            whole_num = (num // den) + 1
            num = abs(num) % abs(den)
            den = abs(den)
        print(f'Negative Denominator: {whole_num} {num}/{den}')

    # Negative Denominator | Num = Den
    elif num > 0 and den < 0 and abs(num) == abs(den):
        return '-1'

    # Normal Fraction
    elif num > 0 and den > 0:
        whole_num = num // den
        num = num % den
        print(f'Normal Fraction: {whole_num} {num}/{den}')

    # Simplify Fraction if numerator is not 0
    simple_fract = frac(f'{num}/{den}')

    print(f"Result: {whole_num} and {simple_fract}")

    # Return results
    if whole_num and num:
        result = f'{whole_num} {simple_fract}'
        print(result)
        return result
    if whole_num and not num:
        result = f'{whole_num}'
        print(result)
        return result
    if not whole_num and num:
        result = f'{simple_fract}'
        print(result)
        return result
    if not whole_num and not num:
        result = '0'
        print(result)
        return result


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

# Print('Zero Division Tests')
# Test.assert_equals(mixed_fraction('0/18891'), '0')
# Test.expect_error("Must raise ZeroDivisionError", lambda: mixed_fraction(0, 0))
# Test.expect_error("Must raise ZeroDivisionError", lambda: mixed_fraction(3, 0))


def mixed_fraction(s):
    f = Fraction(*map(int, s.split('/')))
    if f.denominator == 1:
        return str(f.numerator)
    n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
    f = abs(f - n) if n else f - n
    return "{} {}".format(n, f) if n else str(f)


print('--- Zero Numerator Tests ---')
Test.assert_equals(mixed_fraction('0/-8192867'), '0')
print('-----------------------------------------\n\n')


# # Regular Fractions
# print('--- Regular Fraction Tests ---\n')
# Test.assert_equals(mixed_fraction('42/9'), '4 2/3')
# Test.assert_equals(mixed_fraction('6/3'), '2')
# Test.assert_equals(mixed_fraction('4/6'), '2/3')
# print('-----------------------------------------\n\n')

# print('--- Double Negative Tests ---\n')
# Test.assert_equals(mixed_fraction('-22/-7'), '3 1/7')
# print('-----------------------------------------\n\n')

print('--- Negative Numerator | Num < Den | Tests ---\n')
Test.assert_equals(mixed_fraction('-1639839/5749154'), '-1639839/5749154')

print('--- Negative Numerator | Num > Den | Tests ---\n')
Test.assert_equals(mixed_fraction('-10/7'), '-1 3/7')
Test.assert_equals(mixed_fraction('-9056102/8938892'), '-1 58605/4469446')
Test.assert_equals(mixed_fraction('-2487956/1243978'), '-2')
print('-----------------------------------------\n\n')

print('--- Negative Denominator | Num < Den | Tests ---\n')
Test.assert_equals(mixed_fraction('1820963/-6645345'), '-1820963/6645345')
print('-----------------------------------------\n\n')

print('--- Negative Denominator | Num > Den | Tests ---\n')
Test.assert_equals(mixed_fraction('8877176/-210033'), '-42 55790/210033')
Test.assert_equals(mixed_fraction('12145792/-6072896'), '-2')
print('-----------------------------------------\n\n')

print('--- Negative Denominator | Num = Den | Tests ---\n')
Test.assert_equals(mixed_fraction('9628608/-9628608'), '-1')
print('-----------------------------------------\n\n')


'''

   if numer and denom < 0:
        string = f'{numer * -1}/{denom * -1}'
        numer = numer * -1
        denom = denom * -1
    p_frac = frac(string)
    p_numer = p_frac.numerator
    p_denom = p_frac.denominator

    w_num = p_numer // p_denom

    # Check if fraction needs reducing
    if numer != p_numer and denom != p_denom:
        numer = p_numer % p_denom
        denom = p_denom
    print('')
    print('')
    print(f'Original: {string}')
    print(f'Whole Number: {w_num}')
    print(f'Numerator: {numer}')
    print(f'Denominator: {denom}')

    if w_num and numer:
        result = f'{w_num} {numer}/{denom}'
        print(result)
        return result
    if w_num and not numer:
        result = f'{w_num}'
        print(result)
        return result
    if not w_num and numer:
        result = f'{numer}/{denom}'
        print(result)
        return result
    if not w_num and not numer:
        result = '0'
        print(result)
        return result


'''


# Wow

'''
In retrospect I got totally schooled here, took me about 10 hours of work to get my code that passed all the tests.  Wrote 122 lines of code.  The best pracitce is ... 7 lines of code ... the pain! But actually am finding that it does not pass the tests - so am wondering how this got to be a best practice?
'''


def mixed_fraction(s):
    f = Fraction(*map(int, s.split('/')))
    if f.denominator == 1:
        return str(f.numerator)
    n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
    f = abs(f - n) if n else f - n
    return "{} {}".format(n, f) if n else str(f)


def mixed_fraction(s):
    # Uses split to get the values, and maps to int becuse int() is a func
    # The star packs the values into the Fraction tuple
    f = Fraction(*map(int, s.split('/')))
    # Returns the numerator if denominator is 1
    if f.denominator == 1:
        return str(f.numerator)
    # Crazy math logic distilled into one line
    n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
    f = abs(f - n) if n else f - n
    return "{} {}".format(n, f) if n else str(f)
    # The ZeroDivisionError is built-in to the Fraction module


'''
The best practice 2nd place is from the guy who made this kata
'''


def mixed_fraction(s):
    x, y = map(int, s.split('/'))
    signx = x/abs(x) if x else 1
    signy = y/abs(y) if y else 1
    sign = signx * signy
    x, y = map(abs, (x, y))
    a, b = divmod(x, y)
    g = gcd(b, y)
    b, c = b/g, y/g
    result = (str(a) * bool(a) + ' ' * bool(a) *
              bool(b) + (str(b) + '/' + str(c)) * bool(b))
    if not result:
        return '0'
    if sign < 0:
        result = '-' + result
    return result
