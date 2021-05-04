#this is the regular expression and python version of code
import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^X-\S+:', line) : #start at the beginning, look for 'X-' that matches any non-whitespace character one or more time. 
        print(line)                 #this makes it so anything with a ' ' space between X and colon is skipped


#    if re.search('^X.*:', line) :
#        print(line)


#    if re.search('^From:', line) :
#        print(line)

#    if re.search('From:', line) :
#        print(line)