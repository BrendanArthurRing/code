# Delete all lines with all caps characters

# OR

# Keep only lines that have two tabs

# https://stackoverflow.com/questions/42027013/extracting-dialogs-from-movie-scripts-using-regex/42028043#42028043

# https://stackoverflow.com/questions/49860162/uncover-a-dialogue-of-a-movie-script-to-count-the-words-spoken-by-characters




import re
pattern = re.compile("(?:([A-Z]+ *[A-Z]+)\n).*?(?=$|([A-Z]+ *[A-Z]+)\n)")

for i, line in enumerate(open('input.txt')):
    for match in re.match(pattern, line):
        print('Found on line %s: %s' % (i+1, match.group()))