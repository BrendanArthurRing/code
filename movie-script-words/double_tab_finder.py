# (\t{4}[a-zA-z].{10,40}\n)
# (^\t{4}.*\n)
# ((?<!\t)\t{4}(?!\t)[a-zA-Z .,'-?!()0-9]*)

import re

pattern = re.compile("((?<!\t)\t{4}(?!\t)[a-zA-Z0-9 .,'-?!()@#$%^&*+=]*)")

lines = []

for i, line in enumerate(open('input.txt')):
    for match in re.finditer(pattern, line):
        
        # Save the line in lower case
        line = match.group().lower()
        
        # Take out the four tab indent on dialogue lines
        line = line.replace("\t\t\t\t", "")
        
        # Remove punctiation
        punctuation = ["?", "!", ",", ".", "-"]
        for i in punctuation:
            line = line.replace(i, " ")

        # Build Lines List
        lines.append(line)

# Build words list
dialogue = ' '.join(lines)

# Builds words list
words = dialogue.split(" ")

#Clean Words List
filler = ["the", "you", "i", "a", "to", "and", "it", "is", "of", "your", "in", "that", "this", "what", "my", "me", "was", "not", "on", "he", "get", "got", "at", "as", "see", "be", "up", "so", "out", "they", "have", "well", "no", "about", "with", "if", "here", "his", "will", "can", "all", "there", "are", "do", "but", "who", "it's", "just", "you're", "for", "i'm", "we", "don't", "know", "him", "her", "that's", "look", "want", "say", "he's", "come", "can't", "want", "she", "from", "i'll", "when", "any", "our", "did", "didn't", "what's", "has", "these", ]

for f in filler:
    words[:] = [word for word in words if word != f]   

# Write words to file
with open('words.txt', 'w') as outfile:
    for word in words:
        outfile.write(word + " ")

from collections import Counter

#opens the file. the with statement here will automatically close it afterwards.
with open("words.txt") as input_file:
    #build a counter from each word in the file
    count = Counter(word for line in input_file
                         for word in line.split())

print(count.most_common(50))
