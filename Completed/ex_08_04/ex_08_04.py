romeo = open('Romeo.txt')
wordlist = list()
for line in romeo :
    words = line.split()
    #wordlist.append(words)  
    # print(words)
    for word in words :
        if word in wordlist :
            continue
        worldlist = wordlist.append(word)
wordlist.sort()

print(wordlist)
