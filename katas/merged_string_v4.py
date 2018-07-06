# https://www.codewars.com/kata/merged-string-checker





def is_merge(s, part1, part2):
	parts = (part1, part2)
	x = []
	for i in s:
		print(i)
		for n in part1:
			if n is i:
				print('a:', n)
				
		for j in part2:
			if j is i:
				print('b:', j)
	return True
		

is_merge('codewars', 'code', 'wars')
is_merge('codewars', 'cde', 'owars')
is_merge('codewars', 'cod', 'wars')
is_merge('codewars', 'cwdr', 'oeas')
is_merge('codewars', 'code', 'wasr')



'''
for i in x:
	print(i)
	for n in range(len(a)):
		if a[n] is i:
			print('a:', a[n])
	for j in range(len(b)):
		if b[j] is i:
			print('b:', b[j])
	print('ok')
'''


'''
for i in x:
	print(i)
	for n in a:
		if n is i:
			print('a:', n)
	for j in b:
		if j is i:
			print('b:', j)
print('ok')


s = 'codewars'
part1 = 'cde'
part2 = 'owars'
parts = (part1, part2)
x = []

for c in s:
	for part in parts:
		for i in part:
			if i is c:
				print('==',c)
				x.append(c)
x = ''.join(x)
if s == x:
	print('ok', x)
else:
	print('crap')





def is_merge(s, part1, part2):
	parts = (part1, part2)
	x = []
	for c in s:
		for part in parts:
			for i in part:
				if i is c:
					print('==',c)
					x.append(c)
	x = ''.join(x)
	print('x is', x)
	print('s is', s)
	if s != x:
		print('this is false___')
		return False
	else:
		print('this is true')
		return True
'''