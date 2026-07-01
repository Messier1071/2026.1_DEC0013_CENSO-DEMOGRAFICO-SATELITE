GOOGLE_API_KEY = ""
ROBOFLOW_API_KEY = ""
IMAGE_SIZE = 512
IMG_FILEPATH = "./media/"

DB_FILEPATH = "./database/"
DEBUG = True

def debug_print(message):
    if DEBUG:
        print("[DEBUG]"+str(message))