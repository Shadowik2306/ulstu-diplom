import asyncio
import functools
from http import HTTPStatus

from sqlalchemy import select, update, delete, func
from fastapi import HTTPException
from starlette.concurrency import run_in_threadpool

from app.data.database import async_session_maker
from app.data.models import SampleModel, PresetModel
from app.data.repositories.MusicRepository import check_music, MusicRepository
from app.data.repositories.UserRequestsRepository import UserRequestsRepository, check_user_requests_constraint
from app.data.schemas.MusicSchema import MusicCreateRequestSchema, MusicCreateSchema
from app.data.schemas.SampleSchema import SampleSchema, SampleCreateSchema, SampleUpdateConnection
from app.data.schemas.UserSchema import UserSchema

from app.config import SubscriptionConstraint
from app.utils.AudioLDM2Generator import AudioLDM2Generator

from app.utils.music_generaion import create_samples


def check_user_sample_constraint():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            if len(args) <= 2:
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
                request = args[2]
                if type(request) is not MusicCreateRequestSchema:
                    raise HTTPException(
                        status_code=HTTPStatus.BAD_REQUEST,
                        detail="Something went wrong"
                    )
                request: MusicCreateRequestSchema

                res = await SampleRepository.get_users_samples_count(user)
                if SubscriptionConstraint().max_requests_count - res <= 0:
                    raise HTTPException(
                        status_code=403,
                        detail="You have reached the maximum number of available samples"
                    )

            res = await func(*args, **kwargs)
            return res

        return wrapped

    return wrapper


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
    async def __create_one(cls, sample: SampleCreateSchema) -> SampleSchema:
        async with async_session_maker() as session:
            new_sample = SampleModel(**sample.model_dump())

            session.add(new_sample)

            await session.commit()
            return await cls.get(new_sample.id)

    @classmethod
    @check_user_requests_constraint()
    @check_user_sample_constraint()
    async def check_generation_constraint(
            cls,
            user: UserSchema,
            sample_req: MusicCreateRequestSchema,
            preset_id: int,):
        await UserRequestsRepository().add_one(user, sample_req)
        return True

    @classmethod
    @check_user_requests_constraint()
    @check_user_sample_constraint()
    async def create_many(
            cls,
            user: UserSchema,
            sample_req: MusicCreateRequestSchema,
            preset_id: int,
    ) -> list[SampleSchema]:
        new_samples_name: list[SampleCreateSchema] = \
            await asyncio.to_thread(AudioLDM2Generator().create_samples, sample_req)

        samples = []
        for sample_name in new_samples_name:
            music_model = await MusicRepository().create(MusicCreateSchema(
                music_url=sample_name
            ))

            samples.append(SampleCreateSchema(
                name=f"{sample_req.text_request}",
                music_id=music_model.id,
                preset_id=preset_id,
            ))

        for sample in samples:
            await cls.__create_one(sample)

        print(new_samples_name)
        return []

    @classmethod
    async def update_note(cls, sample_id: int, sample_update_info: SampleUpdateConnection) -> SampleSchema:
        async with (async_session_maker() as session):
            query = update(SampleModel).where(sample_id == SampleModel.id
                                              ).values(note_id=sample_update_info.note_id)
            await session.execute(query)
            await session.commit()

            return await cls.get(sample_id)

    @classmethod
    @check_music()
    async def remove(cls, sample_id: int) -> int:
        async with async_session_maker() as session:
            query = select(SampleModel).where(sample_id == SampleModel.id)
            res = await session.execute(query)

            sample_model = res.scalar()
            await session.delete(sample_model)
            await session.commit()

            return sample_model.id

    @classmethod
    async def get_users_samples_count(cls, user: UserSchema) -> int:
        async with async_session_maker() as session:
            query = select(func.count()).select_from(SampleModel).join(PresetModel).filter(user.id == PresetModel.user_id)
            res = await session.execute(query)
            user_samples_count: int = res.scalar()

            return user_samples_count



