from sqlalchemy import select

from app.data.database import async_session_maker
from app.data.models import PresetModel
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema


class PresetRepository:
    @classmethod
    async def get(cls, preset_id: int) -> PresetSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = await session.execute(query)

            preset_model: PresetModel = res.scalar()
            return PresetSchema.model_validate(preset_model, from_attributes=True)

    @classmethod
    async def get_all(cls) -> list[PresetSchema]:
        async with (async_session_maker() as session):
            query = select(PresetModel)
            res = await session.execute(query)
            presets_models = res.scalars().all()

            return [PresetSchema.model_validate(preset_model, from_attributes=True) for preset_model in presets_models]

    @classmethod
    async def create(cls, preset: PresetCreateSchema) -> PresetSchema:
        async with async_session_maker() as session:
            new_preset = PresetModel(**preset.model_dump())

            session.add(new_preset)
            await session.commit()
            await session.refresh(new_preset)

            return PresetSchema.model_validate(new_preset, from_attributes=True)
