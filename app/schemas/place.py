from pydantic import BaseModel
from typing import Optional

class PlaceResponse(BaseModel):
    id: int
    name: str
    address: str
    postcode: str
    lat: float
    lng: float

    class Config:
        from_attributes = True
