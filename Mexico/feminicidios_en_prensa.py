#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from pykml import parser
from os import path

# Trying to extract all the descriptions from Mexico on how they describe feminicides.

with open('feminicidios.kml') as f:
    root = parser.parse(f).getroot()

    print(dir(root))
    for data in root.Document.Folder.Placemark.ExtendedData:
        print(data.values)
        print(data.text)
        print(data.tag)
        print(data.items)

# xmldoc = minidom.parse('feminicidios.kml')
# itemlist = xmldoc.getElementsByTagName('Data')

# for data in itemlist:
#     if (data.attributes['name'].value == 'DESCRIPTION'):
#         print (data.attributes['name'].data)
#         # print(data.attributes['name'].value)
#         # print(dir(data.attributes['name']))