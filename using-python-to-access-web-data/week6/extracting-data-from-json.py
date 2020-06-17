import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location:')
print('Retrieving:', url)
json_string = urllib.request.urlopen(url).read()
print('Retrieved', len(json_string), 'characters')
json_object = json.loads(json_string)
total, count = 0, 0
for item in json_object['comments']:
    total = total + int(item['count'])
    count = count + 1
print('Count:', count)
print('Sum:', total)