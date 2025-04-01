import datetime

from sqlalchemy import select, update

from app.data.database import async_session_maker
from app.data.models import UserModel, JwtBlackListModel
from app.data.schemas.UserSchema import UserAddSchema, UserSchema


class UserRepository:
    @classmethod
    async def add_one(cls, user: UserAddSchema):
        async with async_session_maker() as session:
            user_dict = user.model_dump()
            user = UserModel(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return UserSchema.model_validate(user, from_attributes=True)

    @classmethod
    async def get_by_email(cls, email):
        async with async_session_maker() as session:
            query = select(UserModel).where(email == UserModel.email)
            res = await session.execute(query)
            user_model: UserModel = res.scalars().first()
            return user_model

    @classmethod
    async def get_one(cls, id):
        async with (async_session_maker() as session):
            query = select(UserModel).where(id == UserModel.id)
            res = await session.execute(query)
            user_model: UserModel = res.scalars().first()
            return UserSchema.model_validate(user_model, from_attributes=True)

    @classmethod
    async def set_subscribe(cls, user: UserSchema):
        async with async_session_maker() as session:
            query = select(UserModel).where(user.id == UserModel.id)
            res = await session.execute(query)
            user = res.scalar()

            user.subscription_to = datetime.date.today() + datetime.timedelta(days=31)

            await session.commit()
            return UserSchema.model_validate(user, from_attributes=True)


class JwtBlackListRepository:
    @classmethod
    async def add_one(cls, token_payload: str):
        async with async_session_maker() as session:
            token = JwtBlackListModel(token=token_payload)
            session.add(token)
            await session.flush()
            await session.commit()
            return token.id

    @classmethod
    async def is_exist(cls, token_payload: str):
        async with async_session_maker() as session:
            query = select(JwtBlackListModel).where(token_payload == JwtBlackListModel.token)
            res = await session.execute(query)
            return res.first() is not None
