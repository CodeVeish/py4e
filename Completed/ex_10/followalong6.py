fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words :
        dic[word] = dic.get(word,0) + 1 
#print(dic)

revlist = list()
for (wd,vl) in dic.items() :
    revl = (vl,wd)
    revlist.append(revl)
#print(revlist)

x = sorted(revlist,reverse=True)
#print(x[:5])

for vl,wd in x[:5] :
    print(wd,vl)
