def unique_in_order(iterable):
	if type(iterable) is str:
		print('string')
		iterable = list(iterable)
		print(iterable)
		print('len', len(iterable))
		unique = []; x = 0; y = 1
		for i in range(len(iterable) - 1):
			if iterable[x] != iterable[y]:
				unique.append(iterable[x])
				print(unique)
				print('x', x, 'y', y)
				#if y <= len(iterable) - 1:
				print('unique incriment')
				x += 1
				y += 1 
				print('x', x, 'y', y)
			elif iterable[x] == iterable[y]:
				print('not unique incriment')
				x += 1
				y += 1
				print('x', x, 'y', y)
	elif type(iterable) is list:
		print('list')
	
	
	
	
	
	
	





unique_in_order('AAAABBBCCDAABBB')
#unique_in_order('ABBCcAD')
#unique_in_order([1, 2, 2, 3, 3])
	
#test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
#test.assert_equals(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
#test.assert_equals(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])


'''First Try
def unique_in_order(iterable):
	if type(iterable) == str:
		print('string')
	elif type(iterable) == list:
		print('list')
	#x = [i for i in list(iterable)]
	x = type(iterable)
	print x
'''

'''2nd Try
def unique_in_order(iterable):
	x = set(iterable)
	print(x)
'''

'''
def unique_in_order(iterable):
	x = list(iterable)
	n = 0
	for i in x:
		if i == x[n + 1]:
			# Googled: python delete list element
			del x[n + 1]
		
	print(x)
'''


'''
def unique_in_order(iterable):
	x = list(iterable)
	n = 0
	for i in x:
		del x[n+1] if i == x[n + 1] #syntax error
		
	print(x)
'''


'''
def unique_in_order(iterable):
	x = list(iterable)
	n = 0
	for i in x:
		if x[n + 1] == i:
			# Googled: python delete list element
			del x[n + 1] # not working as expected
			# Googled: python find similar elements
			# this works for A and B but stops at C
		else:
			pass
		
	print(x)
'''


'''
def unique_in_order(iterable):
	#Googled: python regex delete repeated characters
	import re
	print(type(iterable))
	#x = re.sub(r'([a-z])\1+', r'\1', iterable)
	iterable = re.sub(r'([a-z])\1+', r'\1', iterable)
	print(iterable)

# for some reason the variable is not being read by the regex when this is used in a function - but it works fine out side of thenfunction- what the fuck

'''


'''
def unique_in_order(iterable):
	if type(iterable) is str:
		print('string')
		iterable = list(iterable)
		print(iterable)
		print('len', len(iterable))
		unique = []; x = 0; y = 1
		for i in range(len(iterable) - 1):
			if iterable[x] != iterable[y]:
				unique.append(iterable[x])
				print(unique)
				print('x', x, 'y', y)
				#if y <= len(iterable) - 1:
				print('unique incriment')
				x += 1
				y += 1 
				print('x', x, 'y', y)
			elif iterable[x] == iterable[y]:
				print('not unique incriment')
				x += 1
				y += 1
				print('x', x, 'y', y)
	elif type(iterable) is list:
		print('list')
'''

