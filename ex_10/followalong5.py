#Another method
c = {'a':10, 'b':1, 'c':22}
print(c)
s = sorted([(v,k) for k,v in c.items()])
print(s)