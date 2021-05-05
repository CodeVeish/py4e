import re
handle = open('mbox.txt')
inp = input('Enter RegEx: ')
count = 0


for line in handle :
    line = line.rstrip()
    if re.search(inp,line):
        count = count + 1

print(count)