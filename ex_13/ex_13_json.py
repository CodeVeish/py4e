import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving:', url)
urlreq = urllib.request.urlopen(url, context = ctx)

data = urlreq.read()
data = data.decode()

#print(data)

#print(data)

info = json.loads(data)
#print(type(info))
#print('count',len(info))

#print(info)

count = 0
total = 0

for item in info['comments']:
    count = count + 1
    numb = item['count']
    total = total + numb

print (total)
#print (count)

#data = '''

#]'''

#for item in info:
#    print('Name', item['name'])
#    print('Id', item['id'])
#    print('Attribute', item['x'])