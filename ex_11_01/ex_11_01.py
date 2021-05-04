handle = open('mbox.txt')

for line in handle :
    line = line.rstrip()
    for word in line :
        word = line.split()
    print(word)