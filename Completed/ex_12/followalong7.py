import urllib.request, urllib.parse, urllib.error

img = fhand = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg','wb') #The wb argument opens a binary file for writing only. It will continue to write as long as my computer has memory available.
fhand.write(img)
fhand.close()

#the file will write whereever the terminal library is pointing
