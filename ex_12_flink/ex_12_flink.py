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

url = input('Enter URL - ') #http://py4e-data.dr-chuck.net/known_by_Fikret.html or  http://py4e-data.dr-chuck.net/known_by_Amaney.html
urllist=[url]

count = input('Enter Count - ') # how many times you want to click through links
count = int(count) #3 or 7

position = input('Enter Position -') # what url to select on page
position = int(position) #3 or 18
position = position - 1

while count > 0:
    #restart of cycle, opening link
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    #select urls
    ls = list() # this creates a blank list for each iteration

    tags = soup('a')
    for tag in tags:
        urls = tag.get('href',None)
        ls.append(urls)
        
    url = ls[position]
    urllist.append(url)
    print('Retrieving: ', url)

    count = count - 1

print(urllist)
#last is Anayah or Emon






















#index = 1
#ls = []
#tmpurl = [None]
#lshold = [url]

#tags = soup('a')
#for tag in tags:
#    urls = tag.get('href', None)
#    #print('url',url)
#    ls.append(urls)

#tarurl = ls [2]

#lshold.append(tarurl)

#print('ls: ', ls)
#print(type(ls))
#print(type(url))
#print('tarurl:', tarurl)
#print('URLs:', lshold)
#print(index)


#if index < 5:


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
