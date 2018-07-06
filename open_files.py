# Simple Module for Opening Files

class OpenFile:

	def txt(file_path):
		"""Open .txt file and read. can be saved to variable."""
		with open(file_path, 'r') as txt_file:
			return txt_file.read()

	def txt_list(file_path):
		"""Open .txt file and read all lines to a list. """
		with open(file_path, 'r') as txt_file:
			return txt_file.read().split('\n')