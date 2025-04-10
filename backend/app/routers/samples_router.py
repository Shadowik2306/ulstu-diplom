from typing import Annotated


from arq.jobs import Job, JobStatus
from fastapi import APIRouter, Depends

from app.data.repositories.SampleRepository import SampleRepository
from app.data.schemas.MusicSchema import MusicCreateRequestSchema
from app.data.schemas.SampleSchema import SampleCreateSchema, SampleUpdateConnection
from app.data.schemas.UserSchema import UserSchema
from app.utils import auth
from app.utils.music_generaion import create_samples, delete_sample_file
import threading



router = APIRouter(
    prefix="/preset/{preset_id}/samples",
    tags=["Samples"]
)

@router.post("")
async def create_samples_for_preset_req(
        preset_id: int,
        sample_req: MusicCreateRequestSchema,
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    from app.main import redis
    await SampleRepository.check_generation_constraint(user, sample_req, preset_id)

    job = await redis.enqueue_job('create_samples_preset', preset_id, sample_req, user)
    return job.job_id


@router.get("/status/{job_id}")
async def get_sample_req_status(job_id: str):
    from app.main import redis
    j = Job(job_id, redis=redis)

    return {"status": await j.status()}


@router.delete("/status/{job_id}")
async def abort_sample_req_status(job_id: str):
    from app.main import redis
    j = Job(job_id, redis=redis)
    await j.abort()
    return {"status": await j.status()}


@router.get("")
async def get_presets_samples(preset_id: int, connected: bool = False):
    return await SampleRepository.get_all(
        connected=connected,
        preset_id=preset_id
    )


@router.patch("/{sample_id}")
async def update_sample(sample_id: int, sample_update_indo: SampleUpdateConnection):
    return await SampleRepository.update_note(sample_id, sample_update_indo)


@router.delete("/{sample_id}")
async def delete_sample(sample_id: int):
    return await SampleRepository.remove(sample_id)

