'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import weatherApiAccess
import json

if __name__ == '__main__':
    weather_obj = weatherApiAccess.WeatherApiAccess('https://environment.data.gov.uk/flood-monitoring/id/stations')
    weather_stations = weather_obj.getWeatherStations()
    if weather_stations:
        geojson_data = weather_obj.convertToGeojson(weather_stations)
        with open('weather_stations.geojson', 'w') as f:
            json.dump(geojson_data, f)
        print('GeoJSON data has been written to weather_stations.geojson')
    else:
        print('Error in fetching data')