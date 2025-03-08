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
        
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    
    def convertToGeojson(self, data):
        features = []
        for station in data['items']:
            if 'lat' in station and 'long' in station:
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [station['long'], station['lat']]
                    },
                    "properties": station
                }
                features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        return geojson



