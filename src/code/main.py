'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import weatherApiAccess
import json
import foliumMapMaker

if __name__ == '__main__':
    weather_obj = weatherApiAccess.WeatherApiAccess('https://environment.data.gov.uk/flood-monitoring/id/stations')
    weather_stations = weather_obj.getWeatherStations()

    if weather_stations:
        geojson_data = weather_obj.convertToGeojson(weather_stations)
        map_obj = foliumMapMaker.FoliumMapMaker(geojson_data)
        map_obj.makeMap()
        print('Created map with weather station data.')
    else:
        print('Error in fetching data')