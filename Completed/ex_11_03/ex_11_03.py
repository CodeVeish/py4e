import re

inp = input('Enter file: ')
handle = open(inp)
ls = list()
floatls = []
count = 0
total = 0

for line in handle:
    line = line.rstrip()
    if re.findall('^New Revision: ([0-9.]+)',line):
        words = line.split()
        #print(words)
        ls.append(words[2])

for item in ls :
    count = count + 1
    floatls.append(float(item))
for x in floatls :
    total = total + x
    
count = float(count)
#print(total)
#print(count)
av = total / count
#print(av)
av = int(av)
print(av)
