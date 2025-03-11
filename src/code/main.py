"""
Author: Sedar Olmez
Email: olmez49@gmail.com
Description: This script creates a Flask server that fetches weather station data from an API and displays it on a map.
The server also provides API endpoints to fetch hourly readings for a specific station and to plot graphs of the readings.
"""

from flask import Flask, jsonify, send_file
import weatherApiAccess
from foliumMapMaker import FoliumMapMaker
from io import BytesIO
import matplotlib

matplotlib.use("Agg")  # Required to save plots as images
import matplotlib.pyplot as plt

# Initialise Flask server
app = Flask(__name__)

# Fetch all weather station data from the API.
weather_obj = weatherApiAccess.WeatherApiAccess(
    "https://environment.data.gov.uk/flood-monitoring/id/stations"
)
weather_stations = weather_obj.getWeatherStations()

# Create a map with weather station data if they exist.
if weather_stations:
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [s["long"], s["lat"]]},
                "properties": {
                    "stationReference": s["stationReference"],
                    "label": s.get("label", "Unknown"),
                },
            }
            for s in weather_stations["items"]
            if "lat" in s and "long" in s
        ],
    }
    map_obj = FoliumMapMaker(geojson_data)
    map_obj.makeMap()
    print("Created map with weather station data.")
else:
    print("Error fetching station locations")


@app.route("/")
def home():
    """Render the homepage with the map."""
    return send_file("weather_stations.html")


# Added API endpoints to fetch readings and plot graphs
@app.route("/get_readings/<station_id>")
def get_readings(station_id):
    """Fetch hourly data for a specific station."""
    readings = weather_obj.fetchStationReadings(station_id)
    return jsonify(readings)


# Added API endpoint to plot graphs
@app.route("/plot_graph/<station_id>")
def plot_graph(station_id):
    """Generate and return a line graph for station readings."""
    readings = weather_obj.fetchStationReadings(station_id)
    if not readings:
        return "No data available", 404

    # Extract times and values
    times = [r["dateTime"] for r in readings]
    values = [r["value"] for r in readings]

    # Create a graph
    plt.figure(figsize=(10, 5))
    plt.plot(times, values, marker="o")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title(f"Last 24 Hours for Station: {station_id}")

    # Rotate x-axis for readability.
    plt.xticks(rotation=45, ha="right")

    # Adjust labels for readability.
    step = max(1, len(times) // 10)  # Adjust 10 to a different value if necessary
    plt.xticks(times[::step], rotation=45, ha="right")

    # Format x-axis labels (optional)
    # You can format the time as you need. Here, we use "%H:%M" for hour and minute.
    # For instance:
    # times = [pd.to_datetime(t).strftime('%H:%M') for t in times]

    plt.tight_layout()  # Adjust layout to prevent overlap

    img_io = BytesIO()
    plt.savefig(img_io, format="png")
    img_io.seek(0)
    plt.close()

    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
