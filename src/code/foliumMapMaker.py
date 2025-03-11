"""
Author: Sedar Olmez
Email: olmez49@gmail.com
Description: This script defines the FoliumMapMaker class, which provides methods to create a Folium map with weather station data.
"""


# folium_map_maker.py object.
import folium


class FoliumMapMaker:
    """
    A class to create a Folium map with weather station data.

    Attributes:
        weather_stations (dict): A dictionary containing weather station data in GeoJSON format.
    """

    def __init__(self, weather_stations: dict):
        """
        Constructs all the necessary attributes for the FoliumMapMaker object.

        Parameters:
            weather_stations (dict): A dictionary containing weather station data in GeoJSON format.
        """
        self.weather_stations = weather_stations

    def makeMap(self):
        """
        Creates a Folium map with markers, adding JavaScript to fetch hourly data when clicked.

        The map is centered at a default location with a specified zoom level. Each weather station
        is represented as a marker on the map. Clicking on a marker displays the weather station's
        data in a popup, and a button to fetch hourly readings.

        Returns:
            folium.Map: The created Folium map object.
        """

        map = folium.Map(location=[52.3555, -1.1743], zoom_start=6)

        for feature in self.weather_stations["features"]:
            # Ensure coordinates are extracted
            coordinates = feature["geometry"]["coordinates"]

            # If coordinates are nested, extract the first valid pair
            if isinstance(coordinates[0], list):
                # Nested case
                lon, lat = coordinates[0]
            else:
                # Normal case
                lon, lat = coordinates

            # Ensure values are float before passing to Folium
            lon, lat = float(lon), float(lat)

            station_id = feature["properties"].get("stationReference", "N/A")
            station_name = feature["properties"].get("label", "Unknown Station")

            # Create a popup with a button to fetch readings in javascript
            popup_html = f"""
            <b>{station_name} (ID: {station_id})</b><br>
            <button onclick="fetchReadings('{station_id}')">Show Readings</button>
            <div id="graph-{station_id}"></div>
            """

            folium.Marker(
                location=[lat, lon], popup=folium.Popup(popup_html, max_width=450)
            ).add_to(map)

        # Add JavaScript to fetch data on click
        script = """
        <script>
        function fetchReadings(station_id) {
            fetch(`/get_readings/${station_id}`)
            .then(response => response.json())
            .then(data => {
                let graphDiv = document.getElementById('graph-' + station_id);
                if (data.length === 0) {
                    graphDiv.innerHTML = "<p>No data available</p>";
                } else {
                    let times = data.map(d => d.dateTime);
                    let values = data.map(d => d.value);
                    let graphHTML = `<img src="/plot_graph/${station_id}" width="400"/>`;
                    graphDiv.innerHTML = graphHTML;
                }
            })
            .catch(error => console.error("Error fetching data:", error));
        }
        </script>
        """
        map.get_root().html.add_child(folium.Element(script))

        map.save("weather_stations.html")
        return map
