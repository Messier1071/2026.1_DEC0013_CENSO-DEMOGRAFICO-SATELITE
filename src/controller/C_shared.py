GOOGLE_API_KEY = ""
ROBOFLOW_API_KEY = ""
IMAGE_SIZE = 512
IMG_FILEPATH = "./media/"

DB_FILEPATH = "./database/"
DEBUG = True

def debug_print(message):
    if DEBUG:
        print("[DEBUG]"+str(message))

def get_center(lat_tl,lon_tl,lat_br,lon_br) -> tuple[int,int]:
    center_lat = (lat_tl + lat_br) / 2
    center_lon = (lon_tl + lon_br) / 2
    return center_lat,center_lon