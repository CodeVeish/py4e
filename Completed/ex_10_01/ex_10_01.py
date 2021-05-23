#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
inp = input('Enter File: ')
handle = open(inp)
dic = dict()
for line in handle :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
    emails = words[1]
    dic[emails] = dic.get(emails,0) + 1
#print(dic)

lst = list()
for em,vl in dic.items() :
    revl = (vl,em)
    lst.append(revl)

srtlst = sorted(lst,reverse=True)
#print(srtlst[:1])

for vl,em in srtlst[:1] : 
    print (em,vl)