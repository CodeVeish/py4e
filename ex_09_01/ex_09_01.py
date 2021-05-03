# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check
# whether a string is in the dictionary.

count = 0
dictionary = dict()

handle = open('words.txt')
for line in handle :
    words = line.split()
    for word in words :
        count = count + 1
        dictionary[word] = count
            
#print(dictionary)
usercheck = input('What word would you like to find? ')
if usercheck in dictionary :
    print(usercheck,dictionary[usercheck])
else :
    print('Value Not Found')