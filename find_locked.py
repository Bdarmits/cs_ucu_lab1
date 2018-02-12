'''
this module for finding countries without entrance to the water
'''
from JSON_to_Python import *
def find_lock():
    countries, coordinates, landlocked, independent = json_to_python()
    coords = []
    for i in range(len(landlocked)):
        if landlocked[i] == 'true':
            coords.append(coordinates[i])
    return coords