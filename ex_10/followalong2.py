d = {'d':1, 'c':2, 'b':3, 'a':4}
print(d)
t = sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)
#you can also put () around k,v in the above for loop. It doesn't matter.