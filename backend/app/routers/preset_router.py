from fastapi import APIRouter, Query, Depends

from app.data.repositories.PresetRepository import PresetRepository
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetsPageSchema
from app.data.schemas.UserSchema import UserSchema
from app.utils import auth

presets_router = APIRouter(
    prefix="/presets",
    tags=["Preset"]
)


@presets_router.get("/")
async def get_all_presets(
        page: int = Query(ge=0, default=0),
        size: int = Query(ge=1, le=100, default=100),
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page, size)
    return res


@presets_router.get("/users_presets")
async def get_users_presets(
        user: UserSchema = Depends(auth.get_current_auth_user),
        page: int = Query(ge=0, default=0),
        size: int = Query(ge=1, le=100, default=100),
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page, size, user_id=user.id)
    return res


@presets_router.post("/")
async def create_preset(
        preset: PresetCreateSchema,
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    res = await PresetRepository.create(user, preset)
    return res


preset_router = APIRouter(
    prefix="/preset/{preset_id}",
    tags=["Preset"]
)

@preset_router.get("/")
async def get_preset(preset_id: int) -> PresetSchema:
    return await PresetRepository.get(preset_id)


