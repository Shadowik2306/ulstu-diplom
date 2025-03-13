from typing import Annotated

from fastapi import APIRouter, Depends

from app.data.repositories.SampleRepository import SampleRepository
from app.data.schemas.SampleSchema import SampleCreateSchema, SampleUpdateConnection
from app.utils.music_generaion import create_samples, delete_sample_file

router = APIRouter(
    prefix="/preset/{preset_id}/samples",
    tags=["Samples"]
)


@router.post("/")
async def create_samples_for_preset(
        preset_id: int,
        samples: Annotated[list[SampleCreateSchema], Depends(create_samples)]
):
    return await SampleRepository.create_many(samples)


@router.get("/")
async def get_presets_samples(preset_id: int, connected: bool = False):
    return await SampleRepository.get_all(
        connected=connected,
        preset_id=preset_id
    )


@router.patch("/{sample_id}")
async def update_preset(sample_id: int, sample_update_indo: SampleUpdateConnection):
    return await SampleRepository.update_note(sample_id, sample_update_indo)


@router.delete("/{sample_id}")
async def delete_preset(sample_id: int):
    return await SampleRepository.delete(sample_id)

