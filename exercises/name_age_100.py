# Year at 100
# This Python script asks your name and age, 
# then calculates what there year will be when you turn 100.

def ask_name():
	name = input('''Hello, 
What is your name?
>>> ''')
	print()
	return name

ask_name()





'''
print()
name = input()
print()
print('Hello', name)
print()
#age = int(input('''#How old are you?
#>>> '''))
'''
print()
years_to_100 = 100 - age

import datetime
now = datetime.datetime.now()
current_year = now.year
year_at_100 = current_year + years_to_100
print()
print('In the year', year_at_100, 'you will be 100 years old.')
'''