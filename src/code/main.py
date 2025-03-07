'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import weatherApiAccess

if __name__ == '__main__':
    weather_obj = weatherApiAccess.WeatherApiAccess('https://environment.data.gov.uk/flood-monitoring/id/stations')
    weather_stations = weather_obj.getWeatherStations()
    if weather_stations:
        print(weather_stations)
    else:
        print('Error in fetching data')