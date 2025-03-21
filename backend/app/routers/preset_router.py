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
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=100),
        text: str = "%",
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page - 1, size, text=text)
    return res


@presets_router.get("/users_presets")
async def get_users_presets(
        user: UserSchema = Depends(auth.get_current_auth_user),
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=100),
        text: str = "",
) -> PresetsPageSchema:
    res = await PresetRepository.get_all(page - 1, size, show_unsaved=True, user_id=user.id, text=text)
    return res


@presets_router.get("/favorites")
async def get_user_favorites(
        user: UserSchema = Depends(auth.get_current_auth_user),
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=100),
        text: str = "",
):
    res = await PresetRepository.get_favorites(user, page, size, text)
    return res


@presets_router.get("/last")
async def get_last_presets():
    res = await PresetRepository.get_last_presets()
    return res


@presets_router.get("/most_liked")
async def get_most_liked_presets():
    res = await PresetRepository.get_most_liked_presets()
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
    res = await PresetRepository.create_or_get_unsaved(user, preset)
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


@preset_router.get("/like")
async def get_liked_preset(
        preset_id: int,
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    res = await PresetRepository.is_user_favorite(user, preset_id)
    return res


@preset_router.patch("/like")
async def set_liked_preset(
        preset_id: int,
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    res = await PresetRepository.xor_favorites(user, preset_id)
    return res


@preset_router.delete("/")
async def delete_preset(
        preset_id: int,
        user: UserSchema = Depends(auth.get_current_auth_user),
):
    return await PresetRepository.remove(user, preset_id)