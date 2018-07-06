def abbreviate(s):
	# Split string by spaces or hyphens. 
	# Modify the words as follows
	# take the first character
	# count the number of removed characters
	# inbetween
	# have the last letter on the end
	# ignore words < 4
	sentance = []
	word = ''
	for i in s:
		if i.isalpha():
			word = word + i
		else:
			sentance.append(word)
			sentance.append(i)
	pass


from testing import *
# Sample Tests
Test.assert_equals(abbreviate("internationalization"), "i18n")
Test.assert_equals(abbreviate("accessibility"), "a11y")
Test.assert_equals(abbreviate("Accessibility"), "A11y")
Test.assert_equals(abbreviate("elephant-ride"), "e6t-r2e")



# Instructions
'''
The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

    A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
    The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

Example

abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"

'''

# Kata Link:
# https://www.codewars.com/kata/word-a10n-abbreviation/train/python
	
# Research Links:
'''
https://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters

Splitting strings with multiple delimiters.

import re
# Split with ; and ,
re.split('; |, ',str)

>>> a='Beautiful, is; better*than\nugly'
>>> import re
>>> re.split('; |, |\*|\n',a)
['Beautiful', 'is', 'better', 'than', 'ugly']


https://www.programiz.com/python-programming/methods/string
looking into string functions to see if there is something builtin to help
string.isalpha() - could be useful to split the string but keep the position of spaces - and .!? etc

for i in s:
		if i.isalpha():
			word = word + i
		else:
			sentance.append(word)
			sentance.append(i)


'''
