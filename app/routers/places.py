from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.place import PlaceResponse
from app.services.place_service import PlaceService

router = APIRouter(prefix="/places", tags=["places"])


@router.get("/{place_id}", response_model=PlaceResponse)
def get_place(place_id: int, db: Session = Depends(get_db)):
    place_service = PlaceService(db)
    place = place_service.get_place_by_id(place_id)
    if not place:
        raise HTTPException(status_code=404, detail="place not found")
    return place


@router.get("/postcode/{postcode}", response_model=list[PlaceResponse])
def get_places_by_postcode(postcode: str, db: Session = Depends(get_db)):
    place_service = PlaceService(db)
    return place_service.get_places_by_postcode(postcode)


@router.get("/name/{name}", response_model=list[PlaceResponse])
def get_places_by_name(name: str, db: Session = Depends(get_db)):
    place_service = PlaceService(db)
    return place_service.get_places_by_name(name)


@router.get("/radius/{place_id}/{radius}", response_model=list[PlaceResponse])
def get_places_in_radius(place_id: int, radius: float, db: Session = Depends(get_db)):
    place_service = PlaceService(db)
    return place_service.get_places_in_radius(place_id, radius)


@router.get("/nearest/{place_id}", response_model=PlaceResponse)
def get_nearest_place(place_id: int, db: Session = Depends(get_db)):
    place_service = PlaceService(db)
    return place_service.get_nearest_place(place_id)


@router.get("/walk/{place_id}/{length}", response_model=list[PlaceResponse])
def get_walk(place_id: int, length: int, db: Session = Depends(get_db)):
    place_service = PlaceService(db)
    return place_service.get_walk(place_id, length)
