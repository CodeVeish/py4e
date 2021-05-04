#Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can 
# pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon 
# character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
handle = open('mbox-short.txt')
hourc = dict()

for line in handle :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
    timesp = time.split(':')
    hour = timesp[0]
    #print(hour)
    hourc[hour] = hourc.get(hour,0) + 1
#print(hourc)

hourlst = list()
for hour,count in hourc.items() :
    lst = (hour,count)
    hourlst.append(lst)
#print(hourlst)

srthourlst = sorted(hourlst)
for hour,count in srthourlst :
    print (hour,count)
#print(srthourlst)