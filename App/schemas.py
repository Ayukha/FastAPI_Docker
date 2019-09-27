from pydantic import BaseModel

class Information(BaseModel):
    key: str
    place_name: str
    city: str
    latitude: str
    longitude: str
    accuracy: str