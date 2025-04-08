from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseSettings):
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ulstu_diploma"

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"


REDIS_HOST: str = "redis"

class AuthJWT(BaseSettings):
    private_key_path: Path = BASE_DIR / "certs" / "private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "public.pem"
    algorithm: str = "RS256"
    access_token_expires_minutes: int = 30


class SubscriptionConstraint(BaseSettings):
    max_samples_count: int = 20
    max_preset_count: int = 3
    max_requests_count: int = 10


subscription_settings = SubscriptionConstraint()
db_settings = DBSettings()
jwt_settings = AuthJWT()