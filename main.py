from JSON_to_Python import *
from locations_cutter import *
from find_independance import *
from find_locked import *
import folium

if __name__ == '__main__':
	needed_countries = []
	final_list = []
	cords = []
	year = int(input("Enter a year of movie:"))
	print("Wait a sec!")
	#cutting countries from a locations.list
	final_list = cut_place(year)
	needed_countries = list_cleaner(final_list)
	final_list = remove_doubles(needed_countries)
	countries, coordinates, landlocked, independent = json_to_python()
	#creating map, adding coordinates to it
	map = folium.Map(location = [49.85, 24.0166666667], zoom_start = 1)
	fg = folium.FeatureGroup(name = "Movies Originals")
	for i in final_list:
		i = i.strip()
		index = countries.index(i)
		cords.append(coordinates[index])
	for i in cords:
		i = i.strip('[')
		i = i.strip(']')
		help = i.find(',')
		fg.add_child(folium.Marker(location = [float(i[0:help]), float(i[help+1:])], popup = "Hi", icon = folium.Icon()))
	map.add_child(fg)
	#adding other layers
	#1st layer: not independent lands
	fa = folium.FeatureGroup(name="independence")
	cords = find_ind()
	for i in cords:
		i = i.strip('[')
		i = i.strip(']')
		help = i.find(',')
		fa.add_child(folium.Marker(location=[float(i[0:help]), float(i[help + 1:])], popup="Hi", icon=folium.Icon()))
		map.add_child(fa)
	#2nd layer counties without entrance to the water
	fb = folium.FeatureGroup(name="landlocked")
	cords = find_lock()
	for i in cords:
		i = i.strip('[')
		i = i.strip(']')
		help = i.find(',')
		fb.add_child(folium.Marker(location=[float(i[0:help]), float(i[help + 1:])], popup="Hi", icon=folium.Icon()))
		map.add_child(fb)
	folium.LayerControl().add_to(map)
	map.save('Movies_map.html')