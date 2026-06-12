import os
import math
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
OUTPUT_DIR = "tiles"
IMAGE_SIZE = "1024x1024"
ZOOM = 18  # adjust depending on detail level
if not API_KEY:
    print("Please set GOOGLE_MAPS_API_KEY")
    exit()


cities = [
    {
        "name": "ARA",
        "min_lat": -28.9768650,
        "max_lat": -28.9234312,
        "min_lon": -49.5297051,
        "max_lon": -49.4420395
    },
    {
        "name": "GRA",
        "min_lat": -29.3916343,
        "max_lat": -29.3662286,
        "min_lon": -50.8924234,
        "max_lon": -50.8652098
    },
    {
        "name": "CRI",
        "min_lat": -28.7029451,
        "max_lat": -28.6735156,
        "min_lon": -49.3813604,
        "max_lon": -49.3600906
    },
    {
        "name": "BLU",
        "min_lat": -26.9230051,
        "max_lat": -26.8897759,
        "min_lon": -49.1096872,
        "max_lon": -49.0535495
    },
    {
        "name": "MAN",
        "min_lat": -3.1365062,
        "max_lat": -3.1220843,
        "min_lon": -60.0272819,
        "max_lon": -60.0096007
    },
    {
        "name": "XIQ",
        "min_lat": -10.8338609,
        "max_lat": -10.8180440,
        "min_lon": -42.7314260,
        "max_lon": -42.7157684
    },
    {
        "name": "RIO",
        "min_lat": -9.9845296,
        "max_lat": -9.9520263,
        "min_lon": -67.8397350,
        "max_lon": -67.8005350
    },
    {
        "name": "MAR",
        "min_lat": -14.0237858,
        "max_lat": -14.0101409,
        "min_lon": -49.1849514,
        "max_lon": -49.1673497
    },
    {
        "name": "XAN",
        "min_lat": -26.8944701,
        "max_lat": -26.8594887,
        "min_lon": -52.4222857,
        "max_lon": -52.3810694
    }

]


# Approx conversions
METERS_PER_DEGREE_LAT = 111320  # constant
TILE_SIZE_METERS = 500

def meters_to_lat(meters):
    return meters / METERS_PER_DEGREE_LAT

def meters_to_lon(meters, lat):
    return meters / (METERS_PER_DEGREE_LAT * math.cos(math.radians(lat)))

def get_satellite_image(lat, lon, filename):
    url = "https://maps.googleapis.com/maps/api/staticmap"
    params = {
        "center": f"{lat},{lon}",
        "zoom": ZOOM,
        "size": IMAGE_SIZE,
        "maptype": "satellite",
        "scale": 2,
        "key": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed: {lat}, {lon}")

def generate_tiles(min_lat, max_lat, min_lon, max_lon):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    lat_step = meters_to_lat(TILE_SIZE_METERS)

    lat = min_lat
    tile_id = 0

    while lat < max_lat:
        lon_step = meters_to_lon(TILE_SIZE_METERS, lat)
        lon = min_lon

        while lon < max_lon:
            filename = os.path.join(OUTPUT_DIR, f"tile_{tile_id}.png")
            print(f"Downloading tile {tile_id} at {lat}, {lon}")
            get_satellite_image(lat, lon, filename)

            lon += lon_step
            tile_id += 1

        lat += lat_step

# Example: bounding box for a city (replace with your own)\

# generate_tiles(
#     min_lat=-28.97686,
#     max_lat=-28.92343,
#     min_lon=-49.52970,
#     max_lon=-49.44203
# )
for city in cities:
    # OUTPUT_DIR = "tiles"
    name = city["name"]
    min_lat = city["min_lat"]
    max_lat = city["max_lat"]
    min_lon = city["min_lon"]
    max_lon = city["max_lon"]
    print(f"Processing city {name}")
    OUTPUT_DIR = f"tiles/{name}"
    print(f"Saving tiles to {OUTPUT_DIR}")
    generate_tiles(min_lat, max_lat, min_lon, max_lon)
    print(f"{name} done")