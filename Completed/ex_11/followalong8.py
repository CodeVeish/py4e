import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x) #'\' tells us that regex should not consider the '$' code
print(y)
