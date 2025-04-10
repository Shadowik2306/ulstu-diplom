import functools
import math
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select, func, and_
from sqlalchemy.orm import session
from starlette import status

from app.config import SubscriptionConstraint
from app.data.database import async_session_maker
from app.data.models import PresetModel, UserModel, UserFavorites, SampleModel
from app.data.repositories.MusicRepository import check_music
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetsPageSchema, PresetUpdateSchema, \
    PresetAndSamplesSchema
from app.data.schemas.UserSchema import UserSchema


def check_user_presets_constraint():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            if len(args) <= 1:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail="Something went wrong"
                )

            user = args[1]
            if type(user) is not UserSchema:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail="Something went wrong"
                )
            user: UserSchema

            if not user.is_subscribed:
                res = await PresetRepository().count_users_preset(user)
                if SubscriptionConstraint().max_preset_count <= res:
                    raise HTTPException(
                        status_code=403,
                        detail="You have reached the maximum number of presets"
                    )

            res = await func(*args, **kwargs)
            return res

        return wrapped

    return wrapper


class PresetRepository:
    @classmethod
    async def get(cls, preset_id: int) -> PresetAndSamplesSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = await session.execute(query)

            preset_model: PresetModel = res.scalar()
            return PresetAndSamplesSchema.model_validate(preset_model, from_attributes=True)

    @classmethod
    async def get_all(
            cls,
            page,
            size,
            show_unsaved=False,
            text="",
            **kwargs
    ) -> PresetsPageSchema:
        async with (async_session_maker() as session):
            query = select(func.count()).select_from(PresetModel).where(
                func.upper(PresetModel.name).like(f'%{text.upper()}%')
            ).filter_by(**kwargs)
            if not show_unsaved:
                query = query.filter(PresetModel.name != '')

            res = await session.execute(query)
            total_pages = math.ceil(res.scalar() / size)

            query = select(PresetModel).where(
                func.upper(PresetModel.name).like(f'%{text.upper()}%')
            ).filter_by(**kwargs).limit(size).offset(page * size)

            if not show_unsaved:
                query = query.filter(PresetModel.name != '')
            res = await session.execute(query)
            presets_models = res.scalars().all()

            presets_page = PresetsPageSchema.model_validate({
                "presets": [PresetSchema.model_validate(preset_model, from_attributes=True) for preset_model in
                            presets_models],
                "page": page,
                "size": size,
                "total_pages": total_pages,
            })

            return presets_page

    @classmethod
    async def get_favorites(cls, user: UserSchema, page, size, text="") -> PresetsPageSchema:
        async with async_session_maker() as session:

            query = select(UserModel).where(user.id == UserModel.id)
            res = await session.execute(query)

            user_model: UserModel = res.scalar()
            if text:
                data = [preset for preset in user_model.favorites if text.upper() in preset.name.upper()]
            else:
                data = user_model.favorites

            return PresetsPageSchema.model_validate({
                "presets":
                    [PresetSchema.model_validate(preset, from_attributes=True) for preset in data][
                    size * (page - 1):size * (page - 1) + size],
                "page": page,
                "size": size,
                "total_pages": len(data),
            })

    @classmethod
    async def is_user_favorite(cls, user: UserSchema, preset_id: int) -> bool:
        async with async_session_maker() as session:
            query = select(UserFavorites).where(
                and_(UserFavorites.user_id == user.id, UserFavorites.preset_id == preset_id)
            )
            res = await session.execute(query)
            obj = res.scalar()

            return obj is not None

    @classmethod
    async def xor_favorites(cls, user: UserSchema, preset_id: int):
        async with async_session_maker() as session:
            query = select(UserFavorites).where(
                and_(UserFavorites.user_id == user.id, UserFavorites.preset_id == preset_id)
            )
            res = await session.execute(query)
            obj = res.scalar()

            if obj:
                await session.delete(obj)
            else:
                new_obj = UserFavorites(user_id=user.id, preset_id=preset_id)
                session.add(new_obj)

            await session.commit()
            return

    @classmethod
    @check_user_presets_constraint()
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
    @check_user_presets_constraint()
    async def clone_preset(cls, user: UserSchema, preset_id: int) -> PresetSchema:
        async with async_session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = await session.execute(query)
            original_preset = res.scalar()

            new_preset = PresetModel(
                user_id=user.id,
                name=original_preset.name,
                color=original_preset.color
            )

            for samples in original_preset.samples:
                new_sample = SampleModel(
                    name=samples.name,
                    music_id=samples.music_id,
                    note_id=samples.note_id
                )
                new_preset.samples.append(new_sample)

            session.add(new_preset)

            await session.commit()

            return PresetSchema.model_validate(new_preset, from_attributes=True)

    @classmethod
    async def get_last_presets(cls) -> list[PresetSchema]:
        async with async_session_maker() as session:
            query = select(PresetModel).filter(
                PresetModel.name != ''
            ).order_by(PresetModel.created_at).limit(9)
            res = await session.execute(query)

            last_presets = res.scalars().all()

            return [PresetSchema.model_validate(preset, from_attributes=True) for preset in last_presets]

    @classmethod
    async def get_most_liked_presets(cls) -> list[PresetSchema]:
        async with (async_session_maker() as session):
            query = select(
                PresetModel, func.count(UserFavorites.user_id)
            ).join(
                UserFavorites, PresetModel.id == UserFavorites.preset_id, isouter=True
            ).filter(
                PresetModel.name != ''
            ).group_by(
                PresetModel.id
            ).order_by(
                func.count(UserFavorites.user_id).desc()
            ).limit(9)

            res = await session.execute(query)
            most_liked_presets = res.scalars().all()

            return [PresetSchema.model_validate(preset, from_attributes=True) for preset in most_liked_presets]

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
            await session.flush()
            await session.commit()

            return PresetSchema.model_validate(preset, from_attributes=True)

    @classmethod
    async def count_users_preset(cls, user: UserSchema) -> int:
        async with async_session_maker() as session:
            query = select(func.count()).select_from(PresetModel).filter(user.id == PresetModel.user_id)
            res = await session.execute(query)
            return res.scalar()
