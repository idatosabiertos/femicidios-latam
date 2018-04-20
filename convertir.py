import csv
import json


def get_map_file(filename):
    with open(filename, 'r') as f:
        map_file = json.loads(f.read(), object_pairs_hook=OrderedDict)
    return map_file


def get_data_file(filename):
    return csv.DictReader(filename 'r')


def convert(map, data):
    # save hecho file
    for k in map['hecho']:
        hecho[k] = data[map['hecho'][k]]

    # save victima file
    for k in map['victima']:
        hecho[k] = data[map['victima'][k]]


def main():
    map = get_map_file('map_argentina.json')
    data = get_data_file('Feminicidios_Ministerio_Justicia_2012_2016.csv')

    convert(map, data)
