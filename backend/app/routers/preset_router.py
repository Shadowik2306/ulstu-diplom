from fastapi import APIRouter, Query

from app.data.repositories.PresetRepository import PresetRepository
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetsPageSchema

router = APIRouter(
    prefix="/presets",
    tags=["Preset"]
)


@router.get("/{preset_id}")
async def get_preset(preset_id: int) -> PresetSchema:
    return await PresetRepository.get(preset_id)


@router.get("/")
async def get_all_presets(
    page: int = Query(ge=0, default=0),
    size: int = Query(ge=1, le=100, default=100),
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page, size)
    return res


@router.post("/")
async def create_preset(preset: PresetCreateSchema):
    res = await PresetRepository.create(preset)
    return res


