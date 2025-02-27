from sqlalchemy import select

from app.data.database import async_session_maker
from app.data.models import SampleModel
from app.data.schemas.SampleSchema import SampleSchema, SampleCreateSchema


class SampleRepository:
    @classmethod
    async def get(cls, sample_id: int) -> SampleSchema:
        async with async_session_maker() as session:
            query = select(SampleModel).where(sample_id == SampleModel.id)
            res = await session.execute(query)

            # TODO Just checking the difference
            print(res.scalar())
            print(res.first())

            preset_model: SampleModel = res.scalar()
            return SampleSchema.model_validate(preset_model, from_attributes=True)

    @classmethod
    async def create_one(cls, sample: SampleCreateSchema) -> SampleSchema:
        async with async_session_maker() as session:
            new_sample = SampleModel(**sample.model_dump())

            session.add(new_sample)
            await session.commit()
            return SampleSchema.model_validate(new_sample, from_attributes=True)

    @classmethod
    async def create_many(cls, samples: list[SampleCreateSchema]) -> list[SampleSchema]:
        res = []
        for sample in samples:
            res.append(await cls.create_one(sample))
        return res
