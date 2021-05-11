import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#print('URL: ',url)
#print('html: ',html)
print('parsed html: ',soup)
#Retrieve all of the anchor tags
tags = soup('a')
print('tags: ',tags)
for tag in tags:
    print(tag.get('href',None))