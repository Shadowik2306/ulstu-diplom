from app.data.database import async_session_maker
from app.data.models import MusicModel
from app.data.schemas.MusicSchema import MusicCreateSchema, MusicSchema


class MusicRepository:
    @classmethod
    async def create(cls, music_create_schema: MusicCreateSchema):
        async with async_session_maker() as session:
            music = MusicModel(**music_create_schema.model_dump())

            session.add(music)
            await session.commit()
            await session.flush()

            return MusicSchema.model_validate(music, from_attributes=True)

