from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import db_settings

engine = create_async_engine(
    db_settings.database_url,
    # echo=True
)


async_session_maker = async_sessionmaker(engine, expire_on_commit=False)