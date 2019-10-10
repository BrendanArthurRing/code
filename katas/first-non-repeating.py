from collections import Counter as c


def first_non_repeating_character(s):
    x = c(s).most_common()
    for i in x:
        if 1 in i:
            return i[0]
    return '_'


s = 'ababdbabac'
first_non_repeating_character(s)
