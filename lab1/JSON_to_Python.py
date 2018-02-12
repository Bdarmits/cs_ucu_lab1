'''
this module takes from countries.json the following info:
-for movie map
	country name(list of str)
	coordinates(list of list with digits)
-for two additional layers
	is it landlocked(list of true/false)
	is it independent(list of true/false)
	
'''

def json_to_python():
	'''
	takes nothing
	returns 4 lists
	'''
	countries = []
	coordinates = []
	landlocked = []
	independent = []

	with open('\lab1\countries.json', 'r') as file:
		for line in file:
			if line.startswith('\t\t\t"common":'):
				countries.append(line[13:-2].strip('"'))
			if line.startswith('\t\t"latlng":'):	
				coordinates.append(line[12:-2])
			if line.startswith('\t\t"landlocked":'):
				landlocked.append(line[16:-2])
			if line.startswith('\t\t"independent":'):
				independent.append(line[17:-2])

	file.close()
	#to adapt to locations.list
	countries[235] = "USA"
	countries[80] = "UK"
	return countries, coordinates, landlocked, independent