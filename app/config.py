import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.database_url = os.getenv("database_url", "postgresql://localhost:5432/tripper_db")
        self.postcode_api_url = os.getenv("POSTCODE_API_URL", "https://api.postcodes.io/postcodes/")

settings = Settings()
