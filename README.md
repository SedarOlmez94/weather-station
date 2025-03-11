# Weather Station Visualization

This repository contains code for visualizing weather station data using a Folium map. The project fetches weather station data from the UK government's Environment Agency Real Time flood-monitoring API service and displays it on an interactive map. When a weather station marker is clicked, it shows a line graph of the past 24 hours of readings for that specific weather station.

## Features

- Fetches weather station locations and hourly readings from the Environment Agency Real Time flood-monitoring API.
- Displays weather stations on an interactive Folium map.
- Shows a line graph of the past 24 hours of readings when a weather station marker is clicked.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/weather-station.git
    cd weather-station
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server:

    ```sh
    python src/code/main.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to view the interactive map.

## Project Structure

- [weatherApiAccess.py](http://_vscodecontentref_/1): Contains the `WeatherApiAccess` class for fetching weather station data and hourly readings from the API.
- [foliumMapMaker.py](http://_vscodecontentref_/2): Contains the `FoliumMapMaker` class for creating the Folium map with weather station markers and popups.
- [main.py](http://_vscodecontentref_/3): The main script that initializes the Flask server, fetches weather station data, and creates the Folium map.
- [requirements.txt](http://_vscodecontentref_/4): Lists the required Python packages for the project.

## API Endpoints

- `/get_readings/<station_id>`: Fetches hourly readings for a specific weather station.
- `/plot_graph/<station_id>`: Returns a line graph of the past 24 hours of readings for a specific weather station.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/5) file for details.

## Author

Sedar Olmez
Email: olmez49@gmail.com
