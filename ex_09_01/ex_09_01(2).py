# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check
# whether a string is in the dictionary.

handle = open('words.txt')
for line in handle :
    print(line)