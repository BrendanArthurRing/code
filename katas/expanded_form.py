

# This was the top best practice
'''
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    print(' + '.join(result))
'''
'''
Questions:

What are all the -1s on this line:
    for a in range(len(str(n)) - 1, -1, -1):
It must be part of the range function


range(stop)
range(start, stop[, step])

    Rather than being a function, 
    range is actually an immutable sequence type, 
    as documented in Ranges and Sequence Types — list, tuple, range.
# Not sure how the stepping works here for 3x -1s


### Reverse Engineering

So in this case, an int() number goes in - 12345

range(len(str(12345))) >>> range(0, 5)
range(len(str(12345)) - 1) >>> range(0, 4)
range(len(str(12345)) - 1, -1) >>> range(4, -1)
range(len(str(12345)) - 1, -1, -1) >>> range(4, -1, -1)
# The result is range(4, -1, -1) used by the function

for a in range(len(str(n)) - 1, -1, -1): print(a)
>>> 4
>>> 3
>>> 2
>>> 1
>>> 0

So this line counts down as an iterator to zero, and deals with the +1 error.

The result is 
>>> 12345
quo, n = divmod(n, (10 ** 4))
quo, n = divmod(n, (10 ** 3))
quo, n = divmod(n, (10 ** 2))
quo, n = divmod(n, (10 ** 1))
quo, n = divmod(n, (10 ** 0))




What is divmod() ?

# This is from the documentation and I dont get it yet.
divmod(a, b)

    Take two (non complex) numbers as arguments 
    and return a pair of numbers consisting of their quotient and remainder 
    when using integer division. 

    With mixed operand types, the rules for binary arithmetic operators apply. 
    For integers, the result is the same as (a // b, a % b). 

    For floating point numbers the result is (q, a % b), 
    where q is usually math.floor(a / b) but may be 1 less than that. 

    In any case q * b + a % b is very close to a, if a % b is non-zero 
    it has the same sign as b, and 0 <= abs(a % b) < abs(b).
# btw abs() is absolute value

quo, n = divmod(n, (10 ** a))


Testing shows that divmod() returns the product of the divison and the remainder.

divmod(1, 1) >>> (1, 0) - because 1 devided by itself is 1 with no remainder.
divmod(3, 2) >>> (1, 1) - because 2 goes into 3, 1 times with 1 remainder
divmod(4, 2) >>> (2, 0) - because 4 / 2 = 2 with 0 remainder.
divmid(6, 2) >>> (3, 0) - because 6 / 2 = 3 with 0 remainder.

# This now makes sense, but still not sure how n is being set to the rest of the number
# as it is bein defined by itself here.  



# Now confused on what n is euqal to, and how it is being defined by itself.

running a test like this gives the expected NameError
x, y = divmod(y, 10)

So is quo a built in function?

# How is it possible to create quo and n while using n in the original variable assinment?
# because n is the variable given to the function

# But how is n being split?

by re assigning it with divmod()

a = the reverse index
current = 10 ** 2
n = 125
quo, n = divmod(125, 100)
(quo, n) >>> (1, 25) - because 100 goes into 125 1 time with 25 remainder.

'''
'''
def expanded_form(n):
    result = []
    print('result defined >>>', result)
    print()
    print('n =', n)
    print()
    for a in range(len(str(n)) - 1, -1, -1):
        print(range(len(str(n)) - 1, -1, -1))
        print('n =', n)
        print('a =',a)
        print()
        current = 10 ** a
        print('current = 10 **', a, '=', current)
        print()
        # quo is the digit, n is remaining numbers
        quo, n = divmod(n, current)
        print('quo =', quo, '| n =', n)
        print()
        if quo: # This part returns false if the digit is 0, true if not 0.
            result.append(str(quo * current))
            print('result', result)
    print(' + '.join(result))
'''

'''

def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        quo, n = divmod(n, (10 ** a))
        if quo:
            result.append(str(quo * (10 ** a)))
    print(' + '.join(result))
'''






#expanded_form(2)
#expanded_form(12)
#expanded_form(42)
#expanded_form(70304)
#expanded_form(4982342)
#expanded_form(9000000)



def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    print(' + '.join(result))

expanded_form(125)
expanded_form(2)
expanded_form(12)
expanded_form(42)
expanded_form(70304)
expanded_form(4982342)
expanded_form(9000000)

# So now I get how it works, but the range part still dosent make sense, 
# tried editing the 2nd -1 and it has no effect - but the third -1 breaks the code.
# It does nothing
# The first - 1 I think does the count down iteration, as it is skipping if I change to - 2

'''
https://docs.python.org/3/library/stdtypes.html#range
 
 class range(start, stop[, step])
 range(len(str(n)) - 1, -1, -1)
Start at len(str(n)) - 1 | stop at -1 | step by -1

'''







'''
# This was my best effort
def expanded_form(num):
	n = str(num); d = len(n); n = list(n); e = []
	for i in range(d):
		x = int(n[i]) * (10 ** (d - 1))
		if x != 0: e.extend((x, '+'))
		d -= 1
	e.pop(); e = ' '.join(str(i) for i in e)
	return(e)
'''

# I will take a different approach and just make the list - then pop out all the 0s and trailing +

'''

def expanded_form(num):
	n = str(num); d = len(n); n = list(n); e = []
	for i in range(d):
		x = int(n[i]) * (10 ** (d - 1))
		# if the only num
		
		# if the first few numbers 
		if x != 0  and d > 1:
			e.extend((x, '+'))
		#if last num
		elif x != 0:
			e.append(x)
			
		d -= 1
	e = ' '.join(str(i) for i in e)
	print(e)
'''



'''
def expanded_form(num):
	n = str(num)
	print('n', n)
	
	d = len(n)
	print('d', d)
	
	n = list(n)
	print('n',n)
	
	e = []
	print('e',e)
	
	print('range',range(d))

	for i in range(d):
		x = int(n[i]) * (10 ** (d - 1))
		print('x',x)
		print('d',d)
		if x > 0 and i < d or d > 1:
			e.extend((x, '+'))
			print('plus e',e)
		elif x != 0:
			e.append(x)
			print('end e',e)
		d -= 1
		print('d decrease',d)
	e = ' '.join(str(i) for i in e)
	print(e)
'''


'''


def expanded_form(num):
	n = str(num); d = len(n); n = list(n); e = []
	for i in range(d):
		x = int(n[i]) * (10 ** (d - 1))
		if x > 0 and i < d:
		    e.extend((x, '+'))
		elif x != 0:
			e.append(x)
		d -= 1
	e = ' '.join(str(i) for i in e)
	print(e)


'''



'''
def expanded_form(num):
	n = str(num) # Convert Number to String
	d = len(n) # Get Number of Digits
	n = list(n) # Convert number to list from string.
	e = []
	for i in range(d):
		x = int(n[i]) * (10 ** (d - 1))
		if x > 0 and i < d:
		    e.extend((x, '+'))
		elif x != 0:
			e.append(x)
		d -= 1
	e = ' '.join(str(i) for i in e)
	return(e)

'''






'''

def expanded_form(number):
	string = str(number) # Convert Number to String
	digits = len(string) # Get Number of Digits
	#print('There are', digits, 'digits in the number', number, '.')
	num_list = list(string) # Convert number to list from string.
	#print('This is the number in list form:', num_list)
	i = 0
	expanded = []
	for i in range(len(num_list)):
		place = 10 ** (digits - 1)
		x = int(num_list[i]) * place
		if x > 0:
			expanded.append(x)
		digits -= 1
	#print(expanded)
	result = []
	for i in expanded:
		if expanded.index(i) < (len(expanded) - 1):
			result.extend((i, '+'))
		else:
			result.append(i)
	#print(result)
	result = ' '.join(str(i) for i in result)
	return(result)

'''






'''
def expanded_form(number):
	string = str(number)
	length = len(string)
	print(length)
	num_list = list(string)
	print(num_list)
	x = int(num_list[0]+'0')
	y = num_list[1]
'''
