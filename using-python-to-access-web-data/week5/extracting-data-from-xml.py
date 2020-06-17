import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
xml_string = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xml_string), 'characters')
xml_tree = ET.fromstring(xml_string)
comment = xml_tree.findall('comments/comment')
print('Count:', len(comment))
total = 0
for tag in comment:
    total = total + int(tag.find('count').text)
print('Sum:', total)