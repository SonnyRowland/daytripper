from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.place import PlaceResponse
from app.services.place_service import PlaceService
from app.services.postcode_service import PostcodeService

router = APIRouter(prefix="/places", tags=["places"])


@router.get("/{place_id}", response_model=PlaceResponse)
def get_place(place_id: int, db: Session = Depends(get_db)):
    """Returns single place from id."""
    place_service = PlaceService(db)
    place = place_service.get_place_by_id(place_id)
    if not place:
        raise HTTPException(status_code=404, detail="place not found")
    return place


@router.get("/postcode/{postcode}", response_model=list[PlaceResponse])
def get_places_by_postcode(postcode: str, db: Session = Depends(get_db)):
    """Returns all places with postcodes like given string."""
    place_service = PlaceService(db)
    return place_service.get_places_by_postcode(postcode)


@router.get("/name/{name}", response_model=list[PlaceResponse])
def get_places_by_name(name: str, db: Session = Depends(get_db)):
    """Returns all places with name like given string."""
    place_service = PlaceService(db)
    return place_service.get_places_by_name(name)


@router.get("/walk/postcode/{postcode}/{length}", response_model=list[PlaceResponse])
async def get_walk_from_postcode(
    postcode: str, length: int, db: Session = Depends(get_db)
):
    """Returns a walk from postcode given of length given."""
    place_service = PlaceService(db)
    postcode_service = PostcodeService()
    coords = await postcode_service.get_coords_from_postcode(postcode)
    nearest = place_service.get_nearest_by_coords(
        coords["latitude"], coords["longitude"]
    )
    return place_service.get_walk(nearest.id, length)
