import re
fhandle = open('regex_sum_657211.txt')
numlist = list()
for line in fhandle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        numlist.append(int(number))
print(sum(numlist))
