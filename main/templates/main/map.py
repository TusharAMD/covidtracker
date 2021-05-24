import folium




m=folium.Map(location=[19.11804,72.9122007], zoom_start=12)

#def createMap(x,y,popup):
tooltip='Vaccinated'
folium.Marker(
    [19.11804,72.9122007], 
    popup='<strong>Safe</strong>',
    tooltip=tooltip
    ).add_to(m)

tooltip='Vulnerable'
folium.Marker(
    #('72.9122007', '19.11804')
    [19.11804,72.9122007], 
    popup='<strong>Safe</strong>',
    tooltip=tooltip
    ).add_to(m)
    
m.save('map.html')

#createMap