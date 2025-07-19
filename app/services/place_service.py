from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.place import Place
from app.services.postcode_service import PostcodeService
from geopy.distance import distance

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

    def get_places_in_radius(self, place_id: int, radius: float) -> List[Place]:
        place = self.db.get(Place, place_id)
        if not place:
            return []
        
        coords = (place.lat, place.lng)

        north_point = distance(kilometers=radius).destination(coords, bearing=0)
        east_point = distance(kilometers=radius).destination(coords, bearing=90)
        south_point = distance(kilometers=radius).destination(coords, bearing=180)
        west_point = distance(kilometers=radius).destination(coords, bearing=270)

        north_lat = north_point.latitude
        east_lng = east_point.longitude
        south_lat = south_point.latitude
        west_lng = west_point.longitude

        return self.db.query(Place).filter(Place.lat.between(south_lat, north_lat), Place.lng.between(west_lng, east_lng)).all()
    
    def get_places_in_radius_coords(self, lat: float, lng: float, radius=float) -> List[Place]:
        coords = (lat, lng)
        north_point = distance(kilometers=radius).destination(coords, bearing=0)
        east_point = distance(kilometers=radius).destination(coords, bearing=90)
        south_point = distance(kilometers=radius).destination(coords, bearing=180)
        west_point = distance(kilometers=radius).destination(coords, bearing=270)

        north_lat = north_point.latitude
        east_lng = east_point.longitude
        south_lat = south_point.latitude
        west_lng = west_point.longitude

        return self.db.query(Place).filter(Place.lat.between(south_lat, north_lat), Place.lng.between(west_lng, east_lng)).all()

    def get_nearest_by_id(self, place_id: int) -> Place:
        place = self.db.get(Place, place_id)
        if not place:
            return []
        
        coords = (place.lat, place.lng)

        nearby_places = []
        radius = 0.5
        while not nearby_places:
            nearby_places = self.get_places_in_radius(place_id, radius)
            nearby_places.remove(place)
            radius += 0.5

        dists = []
        for neighbour in nearby_places:
            dists.append(distance(coords, (neighbour.lat, neighbour.lng)).km)

        return nearby_places[dists.index(min(dists))]
        
    def get_nearest_by_coords(self, lat: float, lng: float) -> Place:
        nearby_places = []
        radius = 0.5
        while not nearby_places:
            nearby_places = self.get_places_in_radius_coords(lat, lng, radius)
            radius += 0.5
        
        dists = []
        for neighbour in nearby_places:
            dists.append(distance((lat, lng), (neighbour.lat, neighbour.lng)).km)
        
        return nearby_places[dists.index(min(dists))]

    def get_walk(self, place_id: int, length: int, walk = []) -> List[Place]:
        place = self.db.get(Place, place_id)
        if not place:
            return []
        
        if len(walk) == length:
            return walk
        
        place_coords = (place.lat, place.lng)
        
        walk.append(place)

        appended = False

        radius = 0.5
        dists = []

        while not appended:
            nearby_places = self.get_places_in_radius(place_id, radius)
            nearby_places.remove(place)
            for neighbour in nearby_places:
                dists.append(distance(place_coords, (neighbour.lat, neighbour.lng)).km)
            for i in range(len(nearby_places)):
                closest_in_nearby = nearby_places[dists.index(min(dists))]
                if(closest_in_nearby in walk):
                    nearby_places.remove(closest_in_nearby)
                    dists.remove(min(dists))
                else:
                    return self.get_walk(closest_in_nearby.id, length, walk)
            radius += 0.5


    async def get_nearest_by_postcode(self, postcode: str) -> Place:
        postcode_service = PostcodeService()
        [lat, lng] = await postcode_service.get_coords_from_postcode(postcode)

        return{lat, lng}
