from pathlib import Path
from pydantic_settings import BaseSettings

import keyring

BD_PATH = Path(__file__).parent.parent / "database.sqlite"

system_name = "Tinkle"
user_name = "User"

class Settings(BaseSettings):

    @property
    def database_url(self):
        return f"sqlite:///{BD_PATH}"

    @property
    def server_url(self):
        return "http://127.0.0.1:8000"

    @property
    def jwt_secret_key(self) -> str | None:
        return keyring.get_password(system_name, user_name)

    @classmethod
    def set_jwt(cls, jwt_secret_key: str | None) -> None:
        keyring.set_password(system_name, user_name, jwt_secret_key)

    @classmethod
    def remove_jwt(cls) -> None:
        if keyring.get_password(system_name, user_name):
            keyring.delete_password(system_name, user_name)


settings = Settings()
