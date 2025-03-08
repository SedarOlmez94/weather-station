'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import folium
import json


class FoliumMapMaker:
    """
    A class to create a Folium map with weather station data.

    Attributes:
    ----------
    weather_stations : dict
        A dictionary containing weather station data in GeoJSON format.

    Methods:
    -------
    makeMap():
        Creates a Folium map with markers for each weather station and saves it as an HTML file.
    """
    def __init__(self, weather_stations: dict):
        """
        Constructs all the necessary attributes for the FoliumMapMaker object.

        Parameters:
        ----------
        weather_stations : dict
            A dictionary containing weather station data in GeoJSON format.
        """
        self.weather_stations = weather_stations

    def makeMap(self):
        """
        Creates a Folium map with markers for each weather station and saves it as an HTML file.

        The map is centered at a default location with a specified zoom level. Each weather station
        is represented as a marker on the map. Clicking on a marker displays the weather station's
        data in a popup.

        Returns:
        -------
        folium.Map
            The created Folium map object.
        """
        # Create a map object.
        map = folium.Map(location=[52.3555, -1.1743], zoom_start=6)
        # Iterate through each feature in the geojson dataset.
        for feature in self.weather_stations['features']:
            # Extract the coordinate features and assign to coordinates variable.
            coordinates = feature['geometry']['coordinates']
            # Check if coordinates are nested lists
            if isinstance(coordinates[0], list):
                # Flatten the nested lists and extract the correct lat, long values.
                lon, lat = coordinates[0][0], coordinates[1][0]
            else:
                # If not nested then extract the lat and long values.
                lon, lat = coordinates
            # Get the remaining data for the given coordinates and assign to popup_content variable.
            popup_content = json.dumps(feature['properties'], indent=2)
            # Assign a marker on the coordinates and the feature variables assigned ot that point when clicked.
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup_content, max_width=300)
            ).add_to(map)
        
        # Save the map as an html file.
        map.save('weather_stations.html')
        return map