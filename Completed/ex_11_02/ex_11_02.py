import re
handle = open('mbox.txt')

for line in handle :
    line = line.rstrip()
    if re.findall('^New Revision: ([0-9.]+)',line):
        print(line)