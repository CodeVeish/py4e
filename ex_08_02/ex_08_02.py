han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    words = line.split()
    if words[0] != 'From' :
        continue
    print(words[2])