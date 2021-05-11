import urllib.request, urllib.parse, urllib.error

img = fhand = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg','wb')
fhand.write(img)
fhand.close()

#the file will write whereever the terminal library is pointing
