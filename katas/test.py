class Test:
	def assert_equals(this, that):
		if this == that:
			print('Test Passed!')
		else:
			print('Test Failed!', this, 'does not equal', that, '.')