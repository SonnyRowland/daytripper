import logging

import httpx
from fastapi import HTTPException

from app.config import settings

logger = logging.getLogger(__name__)


class PostcodeService:
    def __init__(self):
        self.base_url = settings.postcode_api_url

    async def get_coords_from_postcode(self, postcode: str):
        try:
            res = httpx.get(f"{self.base_url}{postcode}")
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
