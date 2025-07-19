from app.config import settings
import httpx

class PostcodeService:
    def __init__(self):
        self.base_url = settings.postcode_api_url

    async def get_coords_from_postcode(self, postcode: str):
        try:
            res = httpx.get(f"{self.base_url}{postcode}")
            res.raise_for_status()
            data = res.json()

            if(data.get("status") == 200 and "result" in data):
                result = data["result"]
                return {"latitude": result.get("latitude"), "longitude": result.get("longitude")}
            
        except:
            raise httpx.RequestError(status_code=502, detail="bad upstream response")
