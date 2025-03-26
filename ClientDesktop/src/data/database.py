from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import settings
from app.data.models import CustomBaseModel

engine = create_engine(
    settings.database_url,
)

session_maker = sessionmaker(engine, expire_on_commit=False)
