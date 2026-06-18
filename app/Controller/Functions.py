import math
import os
import C_shared
from dotenv import load_dotenv

def debug_print(message):
    if C_shared.DEBUG:
        print(message)



def setup_api_keys():
    load_dotenv()
    C_shared.GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
    C_shared.ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
    if C_shared.GOOGLE_API_KEY == "":
        raise ValueError("Missing GOOGLE_MAPS_API_KEY in .env or system environment values")
    else:
        debug_print("GOOGLE API key loaded successfully")
    if C_shared.ROBOFLOW_API_KEY == "":
        raise ValueError("Missing ROBOFLOW_API_KEY in .env or system environment values")
    else:
        debug_print("roboflow key loaded successfully")





