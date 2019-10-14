# https://www.testdome.com/questions/24226

def group_by_owners(files):
	return None
	
files = {
	'Input.txt': 'Randy',
	'Code.py': 'Stan',
	'Output.txt': 'Randy'
}
print(group_by_owners(files))

for i in files: 
	print(f'key {files[i]} value {i}')

# 

# https://stackoverflow.com/questions/10036731/transpose-values-and-key-in-python-dictionary-when-values-are-not-unique

# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping

'''
You can also do it with a defaultdict:

year_person = {2000: 'Linda', 2001: 'Ron', 2002: 'Bruce', 2003: 'Linda', 2004: 'Bruce', 2005: 'Gary', 2006: 'Linda'}

from collections import defaultdict
d = defaultdict(list)
for k, v in year_person.items():
    d[v].append(k)

print dict(d)
>>> {'Bruce': [2002, 2004], 'Linda': [2000, 2003, 2006], 'Ron': [2001], 'Gary': [2005]}
'''

def group_by_owners(files):
	return None
	from collections import defaultdict
	d = defaultdict(list)
	for k, v in files.items():
		d[v].append(k)
	print(dict(d))

def group_by_owners(files):
	from collections import defaultdict
	d = defaultdict(list)
	for k, v in files.items():
		d[v].append(k)
	return dict(d)
