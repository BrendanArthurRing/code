
def correct(string):
	numbers = ['0', '1', '5']
	letters = ['O', 'I', 'S']
	for character in string:
		if character in numbers:
			index = numbers.index(character)
			string = string.replace(character, letters[index])
	print(string)

correct("L0ND0N")
correct("DUBL1N")
correct('51NGAP0RE')
correct("BUDAPE5T")
correct("PAR15")

"""
Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
"""


"""
Test.assert_equals(correct("L0ND0N"),"LONDON");
Test.assert_equals(correct("DUBL1N"),"DUBLIN");
Test.assert_equals(correct("51NGAP0RE"),"SINGAPORE");
Test.assert_equals(correct("BUDAPE5T"),"BUDAPEST");
Test.assert_equals(correct("PAR15"),"PARIS");
"""
