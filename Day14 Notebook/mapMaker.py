import folium
#folium.Map(location=[48.130518, 11.5364172], zoom_start=12)

m = folium.Map(location=[48.218871184761596, 11.624819877497147], zoom_start=15)

tooltip = "Click Here For More Info"

marker = folium.Marker(
    location=[48.218871184761596, 11.624819877497147],
    popup="<stong>Allianz Arena</stong>",
    tooltip=tooltip)
marker.add_to(m)

m

tooltip = "Click Here For More Info"

marker = folium.Marker(
    location=[48.218871184761596, 11.624819877497147],
    icon=folium.Icon(icon="cloud"),
    popup="<stong>Allianz Arena</stong>",
    tooltip=tooltip)
marker.add_to(m)

m.save("map7.html")