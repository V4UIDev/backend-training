import xml.etree.ElementTree as ET
import json

# Using XML as a way to transfer data

data = '''<person>
    <name>Jared</name>
    <phone type="intl">
        +44 1111 111111
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))

# Using JSON as a way to transfer data
print(" ")

datajson = '''
    [
        {"id" : "007",
        "x" : "2",
        "name" : "Bond"
        },
        {"id" : "147",
        "x" : "6",
        "name" : "Ramsay"
        } 
        ]
'''

info = json.loads(datajson)
print('User count: ', len(info))
for item in info:
    print('Name: ', item['name'])
    print('ID: ', item['id'])
    print('Attribute: ', item['x'])



