#I could not figure this one out...
import socket

#url = input('Enter URL - ')
url='http://data.pr4e.org/intro.txt'
uparts = url.split('/')
#print('parts: ',uparts)
host = uparts[2]
#print('host: ',host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = ('GET '+url+' HTTP/1.0\r\n\r\n').encode()
#print('cmd:',cmd)
mysock.send(cmd)

while True:
    data = mysock.recv(3000)
    if len(data) < 1:
        break
    if len(data) >3001:
        break
    else:
        print(data.decode())



    #x = data.decode()
    #x = x.strip()
    #print(data.decode(),end='')
    #print(x[:300])
#print(type(data))
#print(type(x))
mysock.close()