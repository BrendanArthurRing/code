import datetime

def make_readable(secs):
	mins, secs = divmod(secs, 60)
	hours, mins = divmod(mins, 60)
	print('%02d:%02d:%02d' % (hours, mins, secs))

# https://bbs.archlinux.org/viewtopic.php?id=77634

# So, what is divmod?
# https://www.programiz.com/python-programming/methods/built-in/divmod
	
make_readable(60)
make_readable(86399)
make_readable(359999)
