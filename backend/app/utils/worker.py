from arq import create_pool
from arq.connections import RedisSettings, ArqRedis
from fastapi import Depends

from app.config import REDIS_HOST
from app.data.repositories.SampleRepository import SampleRepository
from app.data.schemas.MusicSchema import MusicCreateRequestSchema
from app.data.schemas.UserSchema import UserSchema
from app.utils import auth

REDIS_SETTINGS = RedisSettings(
    host=REDIS_HOST
)


async def create_samples_preset(
    ctx,
    preset_id: int,
    sample_req: MusicCreateRequestSchema,
    user: UserSchema = Depends(auth.get_current_auth_user)
):

    res = await SampleRepository.create_many(user, sample_req, preset_id)
    return res


class WorkerSettings:
    functions = [create_samples_preset]
    redis_settings = REDIS_SETTINGS
    max_jobs = 5




