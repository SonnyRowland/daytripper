import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.place import PlaceResponse
from app.services.place_service import PlaceService
from app.services.postcode_service import PostcodeService

router = APIRouter(prefix="/places", tags=["places"])
logger = logging.getLogger(__name__)


@router.get("/{place_id}", response_model=PlaceResponse)
def get_place(place_id: int, db: Session = Depends(get_db)):
    """Returns single place from id."""
    try:
        if place_id <= 0:
            raise HTTPException(
                status_code=400, detail="Place id must be a positive integer"
            )
        place_service = PlaceService(db)
        place = place_service.get_place_by_id(place_id)
        return place

    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error("Database error getting %s: %s", place_id, str(e))
        raise HTTPException(status_code=500, detail="A database error occurred") from e
    except Exception as e:
        logger.error("An unexpected error occurred: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred"
        ) from e


@router.get("/postcode/{postcode}", response_model=list[PlaceResponse])
def get_places_by_postcode(postcode: str, db: Session = Depends(get_db)):
    """Returns all places with postcodes like given string."""
    try:
        place_service = PlaceService(db)
        return place_service.get_places_by_postcode(postcode)

    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(
            "Database error getting places from postcode %s: %s", postcode, str(e)
        )
        raise HTTPException(status_code=500, detail="A database error occurred") from e
    except Exception as e:
        logger.error("An unexpected error occurred: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred"
        ) from e


@router.get("/name/{name}", response_model=list[PlaceResponse])
def get_places_by_name(name: str, db: Session = Depends(get_db)):
    """Returns all places with name like given string."""
    try:
        place_service = PlaceService(db)
        return place_service.get_places_by_name(name)
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error("Database error getting places from name %s: %s", name, str(e))
        raise HTTPException(status_code=500, detail="A database error occurred") from e
    except Exception as e:
        logger.error("An unexpected error occurred: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred"
        ) from e


@router.get("/walk/postcode/{postcode}/{length}", response_model=list[PlaceResponse])
async def get_walk_from_postcode(
    postcode: str, length: int, db: Session = Depends(get_db)
):
    """Returns a walk from postcode given of length given."""
    try:
        place_service = PlaceService(db)
        postcode_service = PostcodeService()
        coords = await postcode_service.get_coords_from_postcode(postcode)
        nearest = place_service.get_nearest_by_coords(
            coords["latitude"], coords["longitude"]
        )
        return place_service.get_walk(nearest.id, length)
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(
            "Database error occurred getting walk of length %s from postcode %s: %s",
            length,
            postcode,
            str(e),
        )
        raise HTTPException(status_code=500, detail="A database error occurred") from e
    except Exception as e:
        logger.error("An unexpected error occurred: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred"
        ) from e


@router.get("/walk/postcode/{start}/{end}/{length}", response_model=list[PlaceResponse])
async def walk_between_postcodes(
    start: str, end: str, length: int, db: Session = Depends(get_db)
):
    """Returns a walk from postcode given of length given."""
    try:
        place_service = PlaceService(db)
        postcode_service = PostcodeService()
        start_coords = await postcode_service.get_coords_from_postcode(start)
        start_place = place_service.get_nearest_by_coords(
            start_coords["latitude"], start_coords["longitude"]
        )
        end_coords = await postcode_service.get_coords_from_postcode(end)
        end_place = place_service.get_nearest_by_coords(
            end_coords["latitude"], end_coords["longitude"]
        )
        return place_service.walk_between(start_place.id, end_place.id, length)
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(
            "Database error occurred getting walk of length %s from postcode %s to postcode %s: %s",
            length,
            start,
            end,
            str(e),
        )
        raise HTTPException(status_code=500, detail="A database error occurred") from e
    except Exception as e:
        logger.error("An unexpected error occurred: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred"
        ) from e


@router.get(
    "/crawl/{start_lat}/{start_lng}/{end}/{length}",
    response_model=list[PlaceResponse],
)
async def crawl_between_coords(
    start_lat: float,
    start_lng: float,
    end: str,
    length: int,
    db: Session = Depends(get_db),
):
    try:
        place_service = PlaceService(db)
        postcode_service = PostcodeService()
        end_coords = await postcode_service.get_coords_from_place(end)
        start_place = place_service.get_nearest_by_coords(start_lat, start_lng)
        end_place = place_service.get_nearest_by_coords(
            end_coords["latitude"], end_coords["longitude"]
        )
        return place_service.walk_between(start_place.id, end_place.id, length)
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(
            "Database error occurred getting crawl of length %s from %s, %s to %s: %s",
            length,
            start_lat,
            start_lng,
            end,
            str(e),
        )
        raise HTTPException(status_code=500, detail="A database error occurred") from e
    except Exception as e:
        logger.error("An unexpected error occured: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred"
        ) from e
