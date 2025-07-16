from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.place import Place

class PlaceService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_place_by_id(self, place_id: int) -> Optional[Place]:  
        return self.db.get(Place, place_id)
    
    def get_places_by_postcode(self, postcode: str) -> List[Place]:  
        return self.db.query(Place).filter(
            Place.postcode.like(f"{postcode.upper()}%")
        ).all()

    def get_places_by_name(self, name: str) -> List[Place]:
        return self.db.query(Place).filter(Place.name.like(f"%{name.capitalize()}%")).all()
