'''
this module for finding countries without independence
'''
from JSON_to_Python import *
def find_ind():
    countries, coordinates, landlocked, independent = json_to_python()
    coords = []
    for i in range(len(independent)):
        if independent[i] == 'false':
            coords.append(coordinates[i])
    return coords