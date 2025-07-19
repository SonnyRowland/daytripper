from pydantic import BaseModel


class PlaceResponse(BaseModel):
    id: int
    name: str
    address: str
    postcode: str
    lat: float
    lng: float

    class Config:
        from_attributes = True
