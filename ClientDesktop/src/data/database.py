from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.config import settings
from src.data.models import CustomBaseModel

engine = create_engine(
    settings.database_url,
)

session_maker = sessionmaker(engine, expire_on_commit=False)
