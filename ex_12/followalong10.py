from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ct = ssl.create_default_context()
ct.check_hostname = False
ct.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context = ct).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    #look at the parts of a tag
    print('Tag:',tag)
    print('URL:',tag.get('href',None))
    print('Contents:',tag.contents[0])
    print('Attrs:', tag.attrs)
    