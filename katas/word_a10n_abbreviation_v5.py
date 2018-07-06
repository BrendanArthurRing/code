def abbreviate(s):
	word = ''
	sentence = []
	output = []
	for character in s:
		# Check if the character is a letter.
		if character.isalpha():
			# If it's a letter, build a word.
			word = word + character
		else: # When the character is not a letter,
			# add the word to a sentence. 
			sentence.append(word)
			# Then add the character  
			sentence.append(character)
			# and get ready for a new word. 
			word = ''
	# If there was only one word given,
	sentence.append(word) # make a single word sentence.
	# Loop through the sentence 
	for word in sentence:
		# using the length of each word,
		l = len(word) # to check for words 
		if l > 3: # longer than 4 letters.
			# Then use abbreviation the word, 
			a10n = word[0] + str(l - 2) + word[l - 1]
			# and add it to the output. 
			output.append(a10n)
		else: # Add shorter words and characters 
			output.append(word) # to the output,
	# and finally join it all together. 
	output = ''.join(output)
	return output # Then return the output.

from test import *
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
