import folium

map = folium.Map(location=[23.755,90.370],zoom_start=6)
#map.add_child(folium.Marker(location=[23.755,90.370],popup="Hi Dhaka"))
map.add_child(folium.Marker(location=[23.755,92.370],icon=folium.Icon(color='red')))
map.save("map3.html")

