import re

#Pythonic method
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = x.split()
email = words[1]
pieces = email.split('@')
print('Python: ',pieces[1])

#regex method
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)
print('Regex: ',y)

z = re.findall('^From .*@([^ ]*)',line)
print('Regex:', z)