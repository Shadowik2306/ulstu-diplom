from sqlalchemy import select, update, delete

from app.data.database import async_session_maker
from app.data.models import SampleModel
from app.data.repositories.MusicRepository import check_music
from app.data.schemas.SampleSchema import SampleSchema, SampleCreateSchema, SampleUpdateConnection


class SampleRepository:
    @classmethod
    async def get(cls, sample_id: int) -> SampleSchema:
        async with async_session_maker() as session:
            query = select(SampleModel).where(sample_id == SampleModel.id)
            res = await session.execute(query)

            sample_model: SampleModel = res.scalar()
            return SampleSchema.model_validate(sample_model, from_attributes=True)

    @classmethod
    async def get_all(cls, connected: bool = False, **kwargs) -> list[SampleSchema]:
        async with async_session_maker() as session:
            if connected:
                query = select(SampleModel).filter_by(**kwargs).filter(SampleModel.note_id.is_not(None))
            else:
                query = select(SampleModel).filter_by(**kwargs)
            res = await session.execute(query)

            samples_models: list[SampleModel] = res.scalars().all()
            return [SampleSchema.model_validate(sample_model, from_attributes=True) for sample_model in samples_models]


    @classmethod
    async def create_one(cls, sample: SampleCreateSchema) -> SampleSchema:
        async with async_session_maker() as session:
            new_sample = SampleModel(**sample.model_dump())

            session.add(new_sample)

            await session.commit()
            return await cls.get(new_sample.id)

    @classmethod
    async def create_many(cls, samples: list[SampleCreateSchema]) -> list[SampleSchema]:
        res = []
        for sample in samples:
            res.append(await cls.create_one(sample))
        return res

    @classmethod
    async def update_note(cls, sample_id: int, sample_update_indo: SampleUpdateConnection) -> SampleSchema:
        async with (async_session_maker() as session):
            query = update(SampleModel).where(sample_id == SampleModel.id
                                              ).values(note_id=sample_update_indo.note_id)
            await session.execute(query)
            await session.commit()

            return await cls.get(sample_id)

    @classmethod
    @check_music()
    async def delete(cls, sample_id: int) -> int:
        async with async_session_maker() as session:
            query = select(SampleModel).where(sample_id == SampleModel.id)
            res = await session.execute(query)

            sample_model = res.scalar()
            await session.delete(sample_model)
            await session.commit()

            return sample_model.id
