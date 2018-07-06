def sum_pairs(ints, s):
	f = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			if i != n: # to filter same index sums
				a = ints[i]
				b = ints[n]
				sum = a + b
				if sum == s:
					it = [abs(i-n),i,n,a,b,sum]
					f.append(it)
	f.sort()
	if f == []: return None
	x = f[0][3] # range error
	y = f[0][4]
	z = [x,y]
	return(z)
	

	
l1 = [1, 4, 8, 7, 3, 15]
sum_pairs(l1, 8)
print([1, 7])


l5 = [10, 5, 2, 3, 7, 5]
sum_pairs(l5, 10)
print([3,4])

l3 = [20, -13, 40]
sum_pairs(l3, -7)
print(None)


'''
### TESTS ###
l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

if sum_pairs(l1, 8) == [1, 7]: 
	print('Passed, [1, 7]')
else:
	print('Failed, (l1, 8)')

if sum_pairs(l2, -6) == [0, -6]: 
	print("Passed, [0, -6]")
else:
	print('Failed, (l2, -6)')

if sum_pairs(l3, -7) == None: 
	print("Passed, None")
else:
	print('Failed, (l3, -7)')

if sum_pairs(l4, 2) == [1, 1]: 
	print("Passed, [1, 1]")
else:
	print('Failed, (l4, 2)')

if sum_pairs(l5, 10) == [3, 7]: 
	print("Passed, [3, 7]")
else:
	print('Failed, (l5, 10) != [3, 7]')

if sum_pairs(l6, 8) == [4, 4]: 
	print("Passed, [4, 4]")
else:
	print('Failed, (l6, 8)')

if sum_pairs(l7, 0) == [0, 0]: 
	print("Passed, [0, 0]")
else:
	print('Failed, (l7, 0)')

if sum_pairs(l8, 10) == [13, -3]: 
	print("Passed, [13, -3]")
else:
	print('Failed, (l8, 10) != [13, -3]')
'''





"""
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

test.describe("Testing For Sum of Pairs")
test.expect(sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
test.expect(sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
test.expect(sum_pairs(l3, -7) == None, "No Match: %s should return None for sum = -7" % l3)
test.expect(sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)

"""




### ASSIGNMENT ###

"""
Sum of Pairs

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
"""





'''
def sum_pairs(ints, s):
	x = ints[0]
	y = ints[3]
	if x + y == s:
		print('ints =', ints)
		print('x =', x) 
		print('y =', y)
		for i in ints:
			print('i is', i)
			if i != x or y:
				# this part dosent work like i expect. i thought it would check if i is x and if it is break but if not then try y. 
				print(i, '!=', x, 'or', i, '!=', y, 'removing...')
				ints.remove(i)

	print(ints)
	'''
	



'''
not sure why this is an infinite loop, but it is. 

def sum_pairs(ints, s):
	for i in range(len(ints)):
		n = 1
		while i < len(ints):
			if s != ints[i] + ints[i + n]:
				print('iterating')
				n += 1
			else:
				print('yay')
'''


'''
def sum_pairs(ints, s):
	a=0
	b=1
	if b > (len(ints)- 1):
		print('uh')
	elif ints[a] + ints[b] != s:
		b += 1
	elif ints[a] + ints[b] == s:
		print('found')
	else:
		a += 1
		b = a + 1
'''


'''
i want to rotate the list and check pairs this seems more efficient, lile a padlock

https://stackoverflow.com/questions/9457832/python-list-rotation
'''

'''
i want to add the elements of the two lists after rotated, then make a new list and look for the answer
https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list

'''

'''
def sum_pairs(n, s):
	while True:
		i = 1
		r = n[i:] + n[:i]
		if s in [x + y for x, y in zip(n, r)]:
			return([n[0],r[0]])
		else:
			False
'''

'''
def sum_pairs(n, s):
	print('n',n)
	print('s',s)
	for i in range(0,len(n)+1):
		r = n[i:] + n[:i]
		print('r',r)
		x = [x + y for x, y in zip(n, r)]
		print('x',x)
		if s in x: # this only checks if the number is in the resulting sums array - so if the number is there after one rotation, it could be due to a pair that would be seen much later in the iteration - this needs to be fixed by iterating througn the ints list one at a time
			y = x.index(s)
			print('y',y)
			print('ny',n[y])
			print('ry',r[y])
			return([n[y],r[y]])
'''

'''
def sum_pairs(n, s):
	print('n',n, 's',s)
	for i in range(len(n)):
		r = n[i:] + n[:i]
		print('r',r)
		x = [x + y for x, y in zip(n, r)]
		print('x',x)
		if s == n[i] + r[i]:
			y = x.index(s)
			print('y',y)
			print('ny',n[y])
			print('ry',r[y])
			return([n[y],r[y]])
# I didnt understand the assignment - actually the entire pair is counted as how early it is in the search process so if n[0]+n[5]=x and n[2]+n[3]=x then the second pair is "better"
'''

'''
s = 4
t = [1,0,2,2,0,3]

t[0]+t[5] == s
t[2]+t[3] == s # Correct

5 - 0 == 5
3 - 2 == 1 

1 < 5

# test earlyness of firs indicie
# and the span of the pair
'''

'''
getting too far ahead pf myself here
def sum_pairs(ints, s):
	r = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			
			if ints[i] + ints[n] == s:
				#r.append([i, n])
				if r == []:
					r.append([i,n])
				elif n < r[0][1]:
					r = [i,n]
					print(r)

l1 = [1, 4, 8, 7, 3, 15]
sum_pairs(l1, 8)

need to go strp by step'''

'''
this code finally shows the building blocks of what im working with.  ot prints and appends the basics of what inworked out on paper of how the problem should be solved mechanically and gives the final options to narrow down based on earlyness, the next step is to design some logic to determine earlyness, but first i need to get my head around what that really is 
def sum_pairs(ints, s):
	r = []
	f = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			if i != n:
				sum = ints[i] + ints[n]
				print('appending [',i,',',n,',',sum,']')
				r.append([i, n, sum])
				if sum == s:
					it = [i,n,sum]
					f.append(it)
					print('found',it)
	print(ints)
	print(f)
'''




'''
#got this with adding the abs to the front as a ranking system, using sort also conveniently did the rest of the work to find the earliest of the same pairs of indicies. 
def sum_pairs(ints, s):
	r = []
	f = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			if i != n:
				sum = ints[i] + ints[n]
				print('appending [',i,',',n,',',sum,']')
				r.append([i, n, sum])
				if sum == s:
					it = [abs(i-n),i,n,sum]
					f.append(it)
					print('found',it)
	print(ints)
	print(f)
	f.sort()
	print(f)
	print([f[0][1],f[0][2]])
	
	
# if abs(i-n) is ==:
#	print(the one with the lowest i)
'''




'''
#this one works , again need to keep in mind exactly what to output. got confused here as i thought the output was the indicies not the numbers being added. 

def sum_pairs(ints, s):
	r = []
	f = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			if i != n: # to filter same index sums
				a = ints[i]
				b = ints[n]
				sum = a + b
				print(a,'(',i,')','+',b,'(',n,')','=',sum)
				r.append([i, n, sum])
				if sum == s:
					it = [abs(i-n),i,n,sum]
					f.append(it)
					print('found',it)
	print(ints)
	print(f)
	f.sort()
	print(f)
	print([f[0][1],f[0][2]])
	x = f[0][1]
	y = f[0][2]
	z = [ints[x],ints[y]]
	print(z)
	'''
	
	
	
'''
	#this one works and is simplified, all the debug is removed and a b are included in the aappended array
	def sum_pairs(ints, s):
	f = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			if i != n: # to filter same index sums
				a = ints[i]
				b = ints[n]
				sum = a + b
				if sum == s:
					it = [abs(i-n),i,n,a,b,sum]
					f.append(it)
	f.sort()
	x = f[0][3]
	y = f[0][4]
	z = [x,y]
	print(z)
'''


'''
this works, but throws a range error when no pairs are found - need to accoint for none

def sum_pairs(ints, s):
	f = []
	for i in range(len(ints)):
		for n in range(1, len(ints)):
			if i != n: # to filter same index sums
				a = ints[i]
				b = ints[n]
				sum = a + b
				if sum == s:
					it = [abs(i-n),i,n,a,b,sum]
					f.append(it)
	f.sort()
	x = f[0][3] # range error
	y = f[0][4]
	z = [x,y]
	return(z)
'''
