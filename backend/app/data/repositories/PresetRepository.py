import math

from sqlalchemy import select, func

from app.data.database import async_session_maker
from app.data.models import PresetModel
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetsPageSchema
from app.data.schemas.UserSchema import UserSchema


class PresetRepository:
    @classmethod
    async def get(cls, preset_id: int) -> PresetSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = await session.execute(query)

            preset_model: PresetModel = res.scalar()
            return PresetSchema.model_validate(preset_model, from_attributes=True)

    @classmethod
    async def get_all(cls, page, size) -> PresetsPageSchema:
        async with (async_session_maker() as session):
            query = select(func.count()).select_from(PresetModel)
            res = await session.execute(query)
            total_pages = math.ceil(res.scalar() / size)

            query = select(PresetModel).limit(size).offset(page * size)
            res = await session.execute(query)
            presets_models = res.scalars().all()

            presets_page = PresetsPageSchema.model_validate({
                "presets": [PresetSchema.model_validate(preset_model, from_attributes=True) for preset_model in presets_models],
                "page": page,
                "size": size,
                "total_pages": total_pages,
            })

            return presets_page

    @classmethod
    async def create(cls, user: UserSchema, preset: PresetCreateSchema) -> PresetSchema:
        async with async_session_maker() as session:
            new_preset = PresetModel(
                **preset.model_dump(),
                user_id=user.id
            )

            session.add(new_preset)
            await session.commit()
            await session.refresh(new_preset)

            return PresetSchema.model_validate(new_preset, from_attributes=True)
