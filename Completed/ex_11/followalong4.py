import re

x = 'From: Using the : character'
y = re.findall('F.+:', x) #this is the greedy expression and takes as much as possible
print('y: ',y)

z = re.findall('F.+?:',x) # this is the non-greedy and will stop at the first occurence
print('z: ',z)
