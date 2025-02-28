from fastapi import APIRouter

from app.data.repositories.PresetRepository import PresetRepository
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema

router = APIRouter(
    prefix="/presets",
    tags=["Preset"]
)


@router.get("/{preset_id}")
async def get_preset(preset_id: int) -> PresetSchema:
    return await PresetRepository.get(preset_id)


@router.post("/")
async def create_preset(preset: PresetCreateSchema):
    res = await PresetRepository.create(preset)
    return res

