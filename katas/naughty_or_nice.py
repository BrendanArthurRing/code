# https://www.codewars.com/kata/585eaef9851516fcae00004d/train/python
# Naughty or Nice?
'''
In this kata, you will write a function that receives an array of string and returns a string that is either 'naughty' or 'nice'. Strings that start with the letters b, f, or k are naughty. Strings that start with the letters g, s, or n are nice. Other strings are neither naughty nor nice.
If there is an equal amount of bad and good actions, return 'naughty'
'''

def naughty_or_nice(actions):
    
    naughty_letters = ['b', 'f', 'k']
    nice_letters = ['g', 's', 'n']
    naughty_actions = []
    nice_actions = []
    
    for i in actions:
    	if i[0] in nice_letters:
    		nice_actions.append(i[0])
    	elif i[0] in naughty_letters:
    		naughty_actions.append(i[0])

    if len(nice_actions) > len(naughty_actions):
    	return 'nice'
    elif len(naughty_actions) >= len(nice_actions):
    	return 'naughty'






# Define Test Class
class Test:
	def assert_equals(testing, expected, description=None):
		if testing == expected:
			print("Passed")
			return True
		elif testing != expected:
			print("Failed")
			return False




# Begin Testing Block

w = naughty_or_nice
bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
Test.assert_equals(w(bad_actions), 'naughty')
Test.assert_equals(w(good_actions), 'nice')
Test.assert_equals(w(actions), 'naughty')