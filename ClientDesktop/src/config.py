from pathlib import Path
from pydantic_settings import BaseSettings

BD_PATH = Path(__file__).parent.parent / "database.sqlite"


class Settings(BaseSettings):
    @property
    def database_url(self):
        return f"sqlite:///{BD_PATH}"

    @property
    def server_url(self):
        return "http://127.0.0.1:8000"


settings = Settings()
