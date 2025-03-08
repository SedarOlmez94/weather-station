'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import folium
import json


class FoliumMapMaker:
    def __init__(self, weather_stations: dict):
        self.weather_stations = weather_stations

    def makeMap(self):
        map = folium.Map(location=[52.3555, -1.1743], zoom_start=6)
        for feature in self.weather_stations['features']:
            coordinates = feature['geometry']['coordinates']
            # Check if coordinates are nested lists
            if isinstance(coordinates[0], list):
                # Flatten the nested lists and extract the correct lat, lon values
                lon, lat = coordinates[0][0], coordinates[1][0]
            else:
                lon, lat = coordinates
            popup_content = json.dumps(feature['properties'], indent=2)
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup_content, max_width=300)
            ).add_to(map)
        
        map.save('weather_stations.html')
        return map