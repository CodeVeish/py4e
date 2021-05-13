# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ') #http://py4e-data.dr-chuck.net/known_by_Fikret.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


index = 0
ls = []
#tmpurl = [None]

if index == 0:
    lshold = [url]

tags = soup('a')
for tag in tags:
    urls = tag.get('href', None)
    #print('url',url)
    ls.append(urls)

tarurl = ls [2]

lshold.append(tarurl)

#print('ls: ', ls)
print(type(ls))
print(type(url))
print('tarurl:', tarurl)
print('URLs:', lshold)




#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')



# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#    urls = tag.get('href', None)
    #print(url)
#    ls.append(urls)

#tarurl = ls [3]

#print(ls)
#print(type(ls))
#print(type(url))

#print(tarurl)

