import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

numlist = list()
# Retrieve all span tags
tags = soup('span')
for tag in tags:
    numlist.append(int(tag.contents[0]))
print('Count', len(numlist))
print('Sum', sum(numlist))