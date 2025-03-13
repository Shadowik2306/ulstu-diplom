import functools

from sqlalchemy import select, event

from app.data.database import async_session_maker
from app.data.models import MusicModel
from app.data.schemas.MusicSchema import MusicCreateSchema, MusicSchema
from app.utils.music_generaion import delete_sample_file


class MusicRepository:
    @classmethod
    async def create(cls, music_create_schema: MusicCreateSchema):
        async with async_session_maker() as session:
            music = MusicModel(**music_create_schema.model_dump())

            session.add(music)
            await session.commit()
            await session.flush()

            return MusicSchema.model_validate(music, from_attributes=True)

    @classmethod
    async def remove(cls, music_id: int):
        async with async_session_maker() as session:
            queue = select(MusicModel).where(MusicModel.id == music_id)
            res = await session.execute(queue)

            music = res.scalar()
            await session.delete(music)
            await session.commit()

            return MusicSchema.model_validate(music, from_attributes=True)

    @classmethod
    async def delete_useless(cls):
        async with async_session_maker() as session:
            query = select(MusicModel)
            res = await session.execute(query)

            for music in res.scalars():
                if not music.used_by:
                    await delete_sample_file(music.music_url)
                    await session.delete(music)

            await session.commit()


def check_music():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            res = await func(*args, **kwargs)
            await MusicRepository.delete_useless()
            return res
        return wrapped
    return wrapper
