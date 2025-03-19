from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import db_settings
from app.data.models import MusicModel
from app.utils.music_generaion import delete_sample_file

engine = create_async_engine(
    db_settings.database_url,
    # echo=True
)


async_session_maker = async_sessionmaker(engine, expire_on_commit=False)