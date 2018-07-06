# https://www.codewars.com/kata/merged-string-checker



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
	if s == x:
		return True
	else:
		return False
		

is_merge('codewars', 'code', 'wars')
is_merge('codewars', 'cde', 'owars')
is_merge('codewars', 'cod', 'wars')





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

'''