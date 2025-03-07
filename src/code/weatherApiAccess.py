'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import requests
import json


class WeatherApiAccess:
    def __init__(self, url: str):
        self.url = url


    def getWeatherStations(self):
        url = 'https://api.weather.gov/stations'
        response = requests.get(url)
        return response.json()
