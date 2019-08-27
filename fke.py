#!/usr/bin/python3

from xml.dom import minidom
import base64
import json
import html
import sys

if len(sys.argv) < 2:
    print(f'Usage: ./{sys.argv[0]} <inputfile>')
    print(f'Example: ./{sys.argv[0]} tokens.xml')
    sys.exit(2)

xml = minidom.parse(sys.argv[1])

items = xml.getElementsByTagName('string')

for elem in items:
    name = elem.attributes['name'].value
    if name != 'tokenOrder':
        jsonToken = json.loads(html.unescape(elem.firstChild.data))
        secret = bytes((x + 256) & 255 for x in jsonToken['secret'])
        code = base64.b32encode(secret)
        key = code.decode()
        print(f'Name: {name}\nKey: {key}\n\n')
