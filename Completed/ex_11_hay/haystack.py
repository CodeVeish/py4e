import re
ls = list()
tot = 0
count = 0
handle = open('regex_sum_1202839.txt')

for line in handle :
    line = line.rstrip()
    vals = re.findall('[0-9]+',line)
    ls = ls + vals
print (ls)

for val in ls :
    tot = tot + int(val)
    count = count + 1 
print(tot)
print(count)