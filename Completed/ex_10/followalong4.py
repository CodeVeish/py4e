#open romeo.txt, extract the words and insert them in the dictionary while counting each occurence as the value
handle = open('romeo.txt')
count = dict()
for line in handle :
    words = line.split()
    for word in words :
        count[word] = count.get(word,0)+1

#print(count)

#take the count dictionary and extract the values in reverse and put them into a tuple. Then sort the tup  from high to low
lst = list()
for word,value in count.items() :
    rev = (value,word)
    lst.append(rev)
#print(lst)
#print('Break')
lst = sorted(lst,reverse=True)
#print(lst)

# Take only the top ten values
for value,word in lst[:10] :
    print(value,word)
