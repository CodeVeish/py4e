import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
data = data.decode()
#print(data)

tree = ET.fromstring(data)
ls = tree.findall('comments/comment')

#print('Comment Count:', len(ls))

total = 0

for item in ls:
    cnt = item.find('count').text
    cnt = int(cnt)
    total = total + cnt
    #print('Commented', cnt , 'times.' )
print(total)



#print('name', item.find())

#print('type:', type(data))
#print('Retrieved', len(data), 'characters')