def test(s):
	from random import randint
	r = randint(0, len(s) - 1)
	print(f'Making random number {r}')
	
	if len(s) > 2:
		# brute force
		random_tried = set()
		if r not in random_tried:
			
		# del s[x]
		print(f'Brute force needed, len is {len(s)} > 2')
		pass
	
	if len(s) == 2:
		# check if strictly increasing
		print('Len is 2, checking if increasing')
		print(f'Comparing {s[0]} < {s[1]}')
		if s[0] < s[1]:
			print('Increasing, True')
		else:
			print('Not increasing, False')
	
	if len(s) <= 1:
		print(f'Len is {len(s)} <= 1. False')
		# return False
	
	print(f'{s}\n\n')
	



test([1,3,2,1])
test([1,2,4,3]) # True
test([1,1]) # False
test([1,2])  # 
