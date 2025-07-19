import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/test", tags=["test"])

POSTCODE_URL = "https://api.postcodes.io/postcodes/"


@router.get("/{postcode}")
async def get_lat_lng(postcode: str):
    try:
        res = httpx.get(POSTCODE_URL + postcode)
        res.raise_for_status()
        data = res.json()

        if data.get("status") == 200 and "result" in data:
            result = data["result"]
            return {
                "latitude": result.get("latitude"),
                "longitude": result.get("longitude"),
            }
    except Exception as err:
        raise HTTPException(status_code=502, detail="bad upstream response") from err
