from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import db_settings

engine = create_engine(
    db_settings.database_url,
)

session_maker = sessionmaker(engine, expire_on_commit=False)