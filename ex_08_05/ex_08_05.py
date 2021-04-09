grab = open('mbox-short.txt')
count = 0
for line in grab :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    #print(line)
    count = count + 1
    emails = words[1]
    print(emails)
count = str(count)
print('There were '+ count + ' lines in the file with From as the last word')