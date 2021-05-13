import socket

url = input('Enter URL - ')
uparts = url.split('/')
print('parts: ',uparts)
host = uparts[2]
print('host: ',host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = ('GET '+url+' HTTP/1.0\r\n\r\n').encode()
print(cmd)
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
