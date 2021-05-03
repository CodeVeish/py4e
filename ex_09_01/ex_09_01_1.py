# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check
# whether a string is in the dictionary.

dic = dict()
handle = open('words.txt')
for line in handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        dic[word] = dic.get(word,0) +1

print(dic)
usercheck = input('What word would you like to find? ')
if usercheck in dic :
    print(usercheck,dic[usercheck])
else :
    print('Value Not Found')




            