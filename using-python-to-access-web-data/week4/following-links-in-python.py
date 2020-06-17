import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')[position - 1]
    url = tag.get('href', None)
    name = re.findall('http://py4e-data.dr-chuck.net/known_by_([a-zA-Z]+).html', url)[0]
    print('Retrieving:', url)
print('Name at count', count, 'position', position, 'is', name)