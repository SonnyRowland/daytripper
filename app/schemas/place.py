"""Pydantic schema for API request and response serialisation"""

from pydantic import BaseModel


class PlaceCreate(BaseModel):
    """Schema for creating a new place"""

    name: str
    address: str
    postcode: str
    lat: float
    lng: float

    class Config:  # pylint: disable=c0115
        from_attributes = True


class PlaceResponse(BaseModel):
    """Response schema for place data returned by the API"""

    id: int
    name: str
    address: str
    postcode: str
    lat: float
    lng: float

    class Config:  # pylint: disable=c0115
        from_attributes = True
