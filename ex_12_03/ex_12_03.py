import urllib.request, urllib.parse, urllib.error

txt = urllib.request.urlopen('http://data.pr4e.org/intro.txt')
fhand = open('intro.txt','wb') #wb 'w' means write. 'b' mearns if it exists.
size = 0

while True:
    info = txt.read(3000)
    if len(info) < 1 or len(info) > 3000:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')

fhand.close()
