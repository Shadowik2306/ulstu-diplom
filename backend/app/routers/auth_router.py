from fastapi import APIRouter, Depends

from app.data.repositories.UserRepository import UserRepository, JwtBlackListRepository
from app.data.schemas.UserSchema import UserRegisterSchema, UserAddSchema
from app.utils import auth

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


def create_user(
    user: UserRegisterSchema,
):
    user_dict = user.model_dump()
    user_dict['password'] = auth.hash_password(user_dict['password'])
    return UserAddSchema(**user_dict)


@router.post("/SignUp", description="# Регистрация нового аккаунта")
async def sign_up(
        user: UserAddSchema = Depends(create_user)
):
    res = await UserRepository.add_one(user)
    return res


@router.post("/SingOut", description="# Выход из аккаунта")
async def sign_out(
        jwt_token: str = Depends(auth.get_current_auth_user_token)
):
    await JwtBlackListRepository().add_one(jwt_token)
    return {
        "status": "success",
        "detail": "You have successfully logged out.",
    }