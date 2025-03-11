"""
Author: Sedar Olmez
Email: olmez49@gmail.com
Description: This script defines the WeatherApiAccess class, which provides methods to access weather data from the API. 
It includes methods to fetch weather station locations and hourly readings for a specific weather station within the last 24 hours.
"""

import requests
from datetime import datetime, timedelta


# weatherApiAccess.py object.
class WeatherApiAccess:
    """
    A class to access weather data from the specified API.

    Attributes:
        url (str): The base URL of the weather API.
    """

    def __init__(self, url: str):
        self.url = url

    def getWeatherStations(self):
        """
        Fetch station locations (without readings).

        This method sends a GET request to the specified URL to fetch the weather station locations.
        It returns the JSON response if the request is successful, otherwise it prints an error message.

        Returns:
            dict: A dictionary containing the weather station locations if the request is successful.
            None: If the request fails.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching stations: {response.status_code}")
            return None

    def fetchStationReadings(self, station_id: str):
        """
        Fetch hourly readings only for the selected station.

        This method sends a GET request to fetch the hourly readings for a specific weather station
        within the last 24 hours. It returns a list of readings if the request is successful, otherwise
        it prints an error message.

        Args:
            station_id (str): The ID of the weather station.

        Returns:
            list: A list of hourly readings if the request is successful.
            None: If the request fails.
        """
        # Here we get the start and end date for the last 24 hours from the current date.
        start_date = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
        end_date = datetime.utcnow().strftime("%Y-%m-%d")

        api_url = f"https://environment.data.gov.uk/flood-monitoring/data/readings?stationReference={station_id}&startdate={start_date}&enddate={end_date}"
        print(f"Fetching hourly data from: {api_url}")

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data.get("items", [])  # Only return the readings list
        else:
            print(
                f"Error fetching hourly data for {station_id}: {response.status_code}"
            )
            return []
