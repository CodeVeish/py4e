import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x) #this is looking for an '@' with non-blank characters on each side
print(y)

z = re.findall('^From (\S+@\S+)', x) #this restricts it further to only lines starting with from
print(z)