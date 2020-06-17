import urllib.request, urllib.parse, urllib.error
import json

api_endpoint = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    address = input('Enter location:')
    parms = dict()
    parms['key'] = api_key
    parms['address'] = address
    url = api_endpoint + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    json_string = urllib.request.urlopen(url).read()
    print('Retrieved', len(json_string), 'characters')
    json_obj = json.loads(json_string)
    if json_obj['status'] != 'OK':
        continue
    else:
        print('Place id', json_obj['results'][0]['place_id'])
        break