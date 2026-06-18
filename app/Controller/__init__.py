"""
1. receber coordenadas
2. Converter p formato do google (ponto central, tamanho imagem e zoom)
2.1
center_lat = (lat1 + lat2) / 2
center_lon = (lon1 + lon2) / 2

2.2
import math

height_m = abs(lat2-lat1) * 111320

width_m = abs(lon2-lon1) * 111320 * math.cos(math.radians(center_lat))


2.3
mpp = width_m / 512

zoom = math.log2(
    156543.03392 * math.cos(math.radians(center_lat)) / mpp
)
zoom = round(zoom)

2.4.
params = {
    "center": f"{center_lat},{center_lon}",
    "zoom": zoom,
    "size": "512x512",
    "maptype": "satellite",
    "key": API_KEY
}


"""