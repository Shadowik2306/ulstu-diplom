import math
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.orm import session
from starlette import status

from app.data.database import async_session_maker
from app.data.models import PresetModel
from app.data.repositories.MusicRepository import check_music
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetsPageSchema, PresetUpdateSchema
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
    async def get_all(cls, page, size, show_unsaved=False, **kwargs) -> PresetsPageSchema:
        async with (async_session_maker() as session):
            query = select(func.count()).select_from(PresetModel).filter_by(**kwargs)
            if not show_unsaved:
                query = query.filter(PresetModel.name != '')

            res = await session.execute(query)
            total_pages = math.ceil(res.scalar() / size)

            query = select(PresetModel).filter_by(**kwargs).limit(size).offset(page * size)
            if not show_unsaved:
                query = query.filter(PresetModel.name != '')
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
    async def create_or_get_unsaved(cls, user: UserSchema, new_preset_data: PresetCreateSchema) -> PresetSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where("" == PresetModel.name).where(user.id == PresetModel.user_id)
            res = await session.execute(query)
            preset = res.scalar()

            if preset:
                return PresetSchema.model_validate(preset, from_attributes=True)

            new_preset = PresetModel(
                **new_preset_data.model_dump(),
                user_id=user.id
            )

            session.add(new_preset)
            await session.commit()
            await session.refresh(new_preset)

            return PresetSchema.model_validate(new_preset, from_attributes=True)

    @classmethod
    async def update(cls, user: UserSchema, preset_id: int, new_preset: PresetUpdateSchema) -> PresetSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = await session.execute(query)
            preset = res.scalar()

            if preset.user_id != user.id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You do not have permission to perform this operation."
                )

            preset.name = new_preset.name
            await session.commit()

            return PresetSchema.model_validate(preset, from_attributes=True)

    @classmethod
    @check_music()
    async def remove(cls, user: UserSchema, preset_id: int) -> PresetSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = await session.execute(query)
            preset = res.scalar()

            if preset.user_id != user.id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You do not have permission to perform this operation."
                )

            await session.delete(preset)
            await session.commit()

            return PresetSchema.model_validate(preset, from_attributes=True)