#working sample XML programs

import xml.etree.ElementTree as ET

xml1 = '''
<person>
    <name>shital</name>
    <phone type='intl'>+1 551 689 1536</phone>
    <email hide='yes'/>
</person>'''

lst1 = ET.fromstring(xml1)

print('Name: ' ,lst1.find('name').text)
print('Phone: ', lst1.find('phone').text)
print('Email attribute: ', lst1.find('email').get('hide'))

# read through multiple elements
xml2 = '''
<stuff>
    <people>
        <person user="1">
            <name>Shital</name>
            <phone type='intl'>+1 551 689 1536</phone>
            </person>
        <person user="2">
            <name>Kapil</name>
            <phone type='intl'>+1 347 495 3683</phone>
        </person>
    </people>
</stuff>'''  # stuff is a root node

data1 = ET.fromstring(xml2)
lst2 = data1.findall('people/person')

for item in lst2:
    print('Person',item.get("user"))
    print('Name: ', item.find('name').text)
    print('phone:', item.find('phone').text)

#using google API to track the locations
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = False
# If you have a Google Places API key, enter it here
#api_key = 'A.............................o9dvNitJQV2Y'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/xml?'
else:
     service_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'

#ignore ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Please enter location: ')
    if(len(address)<1): break

    parms = dict()
    parms['address'] = address
    if(api_key is not False):
        parms['key'] = api_key
    url = service_url + urllib.parse.urlencode(parms)
    print('retrieving ', url)
    data2 = urllib.request.urlopen(url, context = ctx).read()

    print('Retrieved ', len(data2), 'characters.')
    #print(data2)
    data3 = data2.decode()
    print(data3)
    tree = ET.fromstring(data3)
    results = tree.findall('result')
    print(results)
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    addr_type = results[0].findall('address_component')
    #print(addr_type)
    for addr_type1 in addr_type:
        addr_type2 = addr_type1.find('type').text
        if(addr_type2 == 'country'):
            country_code = addr_type1.find('short_name').text
            print(country_code)
            if(country_code is not None):
                print('country code is: ', country_code)

    print('lattitude: ', lat)
    print('longitude:', lng)
    print('location:', location)
