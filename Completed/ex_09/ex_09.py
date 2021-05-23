fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

dic = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        # idiom: retrieve, create, update, counter
        dic[word] = dic.get(word,0) + 1
        #print(word,'new',dic[word])

#print(dic)

#now we want to find the most common word
largest = -1
theword = None
for k,v in dic.items() :
    #print(k,v)
    if v > largest :
        largest = v
        theword = k #remember the word associated with the largest number


print('The Word: ',theword, 'Occurences: ', largest)