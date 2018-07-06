def camel_case(string):
	x = ''.join([i.capitalize() for i in string.split()])
	print(x)





camel_case("Basic tests")
camel_case("test case")
camel_case("camel case method")
camel_case("say hello ")
camel_case(" camel case word")
camel_case("")


# https://stackoverflow.com/questions/12410242/python-capitalize-first-letter-only/32232764

# My Submission
def camel_case(string):
	return ''.join([i.capitalize() for i in string.split()])


# Best Practice 
def camel_case(string):
    return string.title().replace(" ", "")

# Title is a built in function that capitalizes the words, replace takes out all the spaces.