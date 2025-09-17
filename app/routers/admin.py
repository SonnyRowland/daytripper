import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.place import Place
from app.schemas.place import PlaceCreate

router = APIRouter(prefix="/admin", tags=["admin"])
logger = logging.getLogger(__name__)


@router.post("/")
async def post_place(place: PlaceCreate, db: Session = Depends(get_db)):
    try:
        max_id = db.query(func.max(Place.id)).scalar() or 0
        next_id = max_id + 1

        place_data = place.model_dump()
        place_data["id"] = next_id
        db_place = Place(**place_data)
        db.add(db_place)
        db.commit()
        db.refresh(db_place)
        return {"message": "Database entry created successfully"}

    except Exception as ex:
        db.rollback()
        print(ex)
        raise HTTPException(
            status_code=500, detail="Failed to create database entry"
        ) from ex
