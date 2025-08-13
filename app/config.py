import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.database_url = os.getenv(
            "DATABASE_URL",
            "postgresql://daytripper_user:postgres@postgres:5432/daytripper_db",
        )
        self.postcode_api_url = os.getenv(
            "POSTCODE_API_URL", "https://api.postcodes.io/postcodes/"
        )
        self.nominatim_api_url = os.getenv(
            "NOMINATIVE_API_URL",
            "https://nominatim.openstreetmap.org/search?q={location},london&format=json",
        )


settings = Settings()
