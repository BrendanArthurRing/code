

def mult_d(n):
    result = 1
    digits = tuple([int(i) for i in str(n)])
    for number in digits:
        result *= number
    return result

def mult_s(n):
    steps = 0
    if '0' in str(n):
        return steps + 1
    while len(str(n)) > 1:
        n = mult_d(n)
        steps += 1
    return steps

def find_per(n):
    return [mult_s(n), n]

print(find_per(68889))

# Generate Number Test Set
'''
test_range = range(277777788888899, 999999999999999)
test_set = []
for i in test_range:
    ns = str(i)
    if not '0' in ns:
        if not '1' in ns:
            if not '5' in ns:
                print(f'Appending {i}')
                test_set.append(i)
'''
'''
import csv

with open('numbers.csv', mode='w', newline='') as csv_file:
    number_writer = csv.writer(csv_file, delimiter=',')
    number_writer.writerow(['Steps', 'Number'])

    for i in range(277777788888899, 999999999999999):
        ns = str(i)
        if not '0' in ns:
            if not '1' in ns:
                if not '5' in ns:
                    data =  find_per(i)
                    print(data)
                    number_writer.writerow(data)


# 277777788888899
'''