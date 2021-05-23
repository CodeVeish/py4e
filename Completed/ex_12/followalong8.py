import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg','wb')
size = 0
while True:
    info = img.read(100000) #This sets the limit on the amount of characters held by my memory at a time. Once this threshold is reached, the program writes the 100000 characters into the cover3.jpg file and dumps the memory. It then starts again from where it left off until the whole file is copied.
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()

#this program is slightly different than fa7. It protects my computer's memory by periodically writing what's held in the memory to file and dumping the memory.