from fastapi import APIRouter, Query, Depends

from app.data.repositories.PresetRepository import PresetRepository
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetsPageSchema, PresetUpdateSchema
from app.data.schemas.UserSchema import UserSchema
from app.utils import auth

presets_router = APIRouter(
    prefix="/presets",
    tags=["Preset"]
)


@presets_router.get("/")
async def get_all_presets(
        page: int = Query(ge=1, default=0),
        size: int = Query(ge=1, le=100, default=100),
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page - 1, size)
    return res


@presets_router.get("/users_presets")
async def get_users_presets(
        user: UserSchema = Depends(auth.get_current_auth_user),
        page: int = Query(ge=1, default=0),
        size: int = Query(ge=1, le=100, default=100),
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page - 1, size, user_id=user.id)
    return res


@presets_router.post("/")
async def create_preset(
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    from random import choice
    preset = PresetCreateSchema(
        name="",
        color=choice([
            "#B8F3B2",
            "#F5C1DE",
            "#A8E0EA",
            "#F59B9B",
            "#F7D18F",
            "#C9A8F9",
            "#FCFDAB",
            "#E8DCC3",
            "#567853",
            "#70A7F3",
            "#C791A3",
            "#DDD96F"
        ])
    )
    res = await PresetRepository.create(user, preset)
    return res


preset_router = APIRouter(
    prefix="/preset/{preset_id}",
    tags=["Preset"]
)


@preset_router.get("/")
async def get_preset(preset_id: int) -> PresetSchema:
    return await PresetRepository.get(preset_id)


@preset_router.patch("/")
async def update_preset(
        preset_id: int,
        preset_update_info: PresetUpdateSchema,
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    return await PresetRepository.update(user, preset_id, preset_update_info)