import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    def __init__(self):
        self.database_url = os.getenv(
            "database_url", "postgresql://localhost:5432/daytripper_db"
        )


settings = Settings()
