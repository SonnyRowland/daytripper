import logging

import httpx
from fastapi import HTTPException

from app.config import settings

logger = logging.getLogger(__name__)


class GeolocationService:
    def __init__(self):
        self.postcode_url = settings.postcode_api_url
        self.nominatim_url = settings.nominatim_api_url

    async def get_coords_from_postcode(self, postcode: str):
        try:
            res = httpx.get(f"{self.postcode_url}{postcode}")
            res.raise_for_status()
            data = res.json()

            if data.get("status") == 200 and "result" in data:
                result = data["result"]
                return {
                    "latitude": result.get("latitude"),
                    "longitude": result.get("longitude"),
                }

        except Exception as exc:
            logger.error("Bad upstream response from postcodes.io")
            raise HTTPException(
                status_code=502, detail="bad upstream response"
            ) from exc

    async def get_coords_from_place(self, end: str):
        try:
            res = httpx.get(self.nominatim_url.format(location=end))
            res.raise_for_status()
            data = res.json()

            result = data[0]
            return {
                "latitude": result.get("lat"),
                "longitude": result.get("lon"),
            }
        except Exception as exc:
            logger.error("Bad upstream response from nominatim")
            raise HTTPException(
                status_code=502, detail="bad upstream response"
            ) from exc
