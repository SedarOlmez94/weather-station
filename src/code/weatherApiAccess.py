'''
Author: Sedar Olmez
Email: olmez49@gmail.com
Description...
'''

import requests
from datetime import datetime, timedelta

class WeatherApiAccess:
    def __init__(self, url: str):
        self.url = url

    def getWeatherStations(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error fetching stations: {response.status_code}")
            return None

    def getHourlyData(self, station_id: str):
        start_date = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
        end_date = datetime.utcnow().strftime("%Y-%m-%d")
        
        # Corrected API endpoint
        hourly_url = f"https://environment.data.gov.uk/flood-monitoring/data/readings?stationReference={station_id}&startdate={start_date}&enddate={end_date}"
        print(f"Fetching hourly data from: {hourly_url}")

        response = requests.get(hourly_url)
        if response.status_code == 200:
            data = response.json()
            if "items" in data and data["items"]:
                print(f"Retrieved {len(data['items'])} readings for station {station_id}")
            else:
                print(f"No readings found for station {station_id}")
            return data
        else:
            print(f"Error fetching hourly data for {station_id}: {response.status_code}")
            return None

    def convertToGeojson(self, data):
        features = []
        for station in data['items']:
            if 'lat' in station and 'long' in station:
                station_id = station['stationReference']
                hourly_data = self.getHourlyData(station_id)
                
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [station['long'], station['lat']]
                    },
                    "properties": {
                        **station,
                        "hourly_data": hourly_data if hourly_data else {"items": []}  # Ensure valid format
                    }
                }
                features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        return geojson
