from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseSettings):
    @property
    def database_url(self):
        return f"sqlite:///database.db"


db_settings = DBSettings()
