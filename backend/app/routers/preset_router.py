from typing import Annotated

from fastapi import APIRouter, Depends

from app.data.repositories.PresetRepository import PresetRepository
from app.data.repositories.SampleRepository import SampleRepository
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema
from app.data.schemas.SampleSchema import SampleCreateSchema, SampleCreateRequestSchema
from app.utils.music_generaion import create_samples

router = APIRouter(
    prefix="/preset",
    tags=["Preset"]
)


@router.get("/{preset_id}")
async def get_preset(preset_id: int) -> PresetSchema:
    return await PresetRepository.get(preset_id)


@router.post("/")
async def create_preset(preset: PresetCreateSchema):
    res = await PresetRepository.create(preset)
    return res


@router.post("/{preset_id}")
async def create_samples_for_preset(
        preset_id: int,
        samples: Annotated[list[SampleCreateSchema], Depends(create_samples)]
):
    return await SampleRepository.create_many(samples)