import functools
from http import HTTPStatus

from sqlalchemy import select, func
from fastapi import HTTPException
import datetime

from app.data.database import async_session_maker
from app.data.models import UserRequestsModel
from app.data.schemas.MusicSchema import MusicCreateRequestSchema
from app.data.schemas.UserSchema import UserSchema
from app.config import SubscriptionConstraint


class UserRequestsRepository:
    @classmethod
    async def add_one(cls, user: UserSchema, music_req: MusicCreateRequestSchema):
        async with async_session_maker() as session:
            new_req = UserRequestsModel(
                user_id=user.id,
                request=music_req.text_request
            )

            session.add(new_req)
            await session.commit()

    @classmethod
    async def count_user_requests_today(cls, user: UserSchema):
        async with async_session_maker() as session:
            query = select(func.count()).select_from(UserRequestsModel).filter_by(user_id=user.id,
                                                                                  created_at=datetime.date.today())
            res = await session.execute(query)
            count_req = res.scalar()

            return count_req


def check_user_requests_constraint():
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
                res = await UserRequestsRepository.count_user_requests_today(user)
                if SubscriptionConstraint().max_requests_count <= res:
                    raise HTTPException(
                        status_code=403,
                        detail="You have reached the maximum number of requests for today"
                    )

            res = await func(*args, **kwargs)
            return res

        return wrapped

    return wrapper

