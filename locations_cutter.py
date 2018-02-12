from JSON_to_Python import *
'''
cuts places where movies were filmed by an entered year
'''

def cut_place(year):
	'''
	takes year of movie
	returns list of countries where movie was filmed
	'''
	needed_countries = []
	with open('\lab1\locations.list', 'r') as list:
		for line in list:
			if str(year) in line:
				splited_line = line.strip().split(',')
				needed_countries.append(splited_line)
	return needed_countries					

def list_cleaner(list_to_clean):
	'''
	takes a list with countries but with other info
	returns list with only needed countries
	'''
	countries, coordinates, landlocked, independent = json_to_python()
	almost_cleaned = []
	cleaned = []
	for i in list_to_clean:
		almost_cleaned.append(i[-1].split('\t'))
	for i in almost_cleaned:
		for j in i:
			if countries.count(j.strip()) != 0:
				cleaned.append(j)
			
	return cleaned
	
def remove_doubles(list_to_remove):
	'''
	takes a list with countries, some of them might be mentioned few times
	returns list with only one mention 
	'''
	final_list = []
	for i in list_to_remove:
		if i in final_list:
			continue
		else:
			final_list.append(i)
	#print(final_list)
	return final_list