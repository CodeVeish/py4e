c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items(): 
    tmp.append((v,k)) #this turns it back into a tuple
#print(tmp)
#the above code creates a dictionary, then creates an empty list, then runs a for loop within the dictionary appending the values in reverse order intro the list
#tmp = sorted(tmp) this would do the same as below, but sort it from highest to lowest
tmp = sorted(tmp, reverse = True)
print(tmp)