from pydantic import BaseModel

class LocationCreate(BaseModel):
    slug: str
    lat: float
    lon: float