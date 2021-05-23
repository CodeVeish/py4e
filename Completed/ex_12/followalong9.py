#Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl #the SSL library allows this program to access web sites that strictly enforce HTTPS.

# Ignore SSL certificate errors
ctx =  ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('URL: ',url)
html = urllib.request.urlopen(url,context=ctx).read() #the read method returns html source code as bytes object instead of returning an HTTP response object
#print('HTML: ',html)
links = re.findall(b'href="(http[s]?://.*?)"',html) #the findall reg exp method will give us a list of all of the strings that match our regular expression, returning only the link between the double quotes
print('links: ',links)
for link in links: 
    print(link.decode())
    