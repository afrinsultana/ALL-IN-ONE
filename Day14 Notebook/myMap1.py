import folium

#map = folium.Map(location=[23.755,90.370])
map = folium.Map(location=[23.729814, 90.381222],zoom_start=16)
#map.add_child(folium.Marker(location=[23.755,90.370],popup="Hi Dhaka"))
map.add_child(folium.Marker(location=[23.755,92.370],icon=folium.Icon(color='green')))
#map.add_child(folium.Marker(location=[23.755,92.370],popup="Hi Dhaka",icon=folium.Icon(color='red')))
folium.Marker([23.755,90.370], popup = f'Name:Nazmul').add_to(map)

map.save("map6.html")

center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location=center, zoom_start=8)
#display map
map_kenya
