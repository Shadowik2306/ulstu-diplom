from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.data.repositories.UserRepository import UserRepository, JwtBlackListRepository
from app.data.schemas.UserSchema import UserRegisterSchema, UserAddSchema, UserSchema, UserLoginSchema, TokenSchema, \
    TokenPayload
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


@router.post("/sign_up", description="# Регистрация нового аккаунта")
async def sign_up(
        user: UserAddSchema = Depends(create_user)
):
    res = await UserRepository.add_one(user)
    return res


async def validate_auth_user(
        user_login: UserLoginSchema,
):
    if not (user := await UserRepository().get_by_email(user_login.email)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    if not auth.validate_password(
        password=user_login.password,
        hashed_password=user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    return UserSchema.model_validate(user, from_attributes=True)


@router.post("/sing_in", description="# Получение новой пары jwt пользователя")
async def sign_in(
    user: UserSchema = Depends(validate_auth_user)
):
    jwt_payload = TokenPayload(**user.model_dump()).model_dump()
    token = auth.encode_jwt(jwt_payload)
    return TokenSchema(
        access_token=token,
        token_type="Bearer",
    )


@router.post("/sing_out", description="# Выход из аккаунта")
async def sign_out(
        jwt_token: str = Depends(auth.get_current_auth_user_token)
):
    await JwtBlackListRepository().add_one(jwt_token)
    return {
        "status": "success",
        "detail": "You have successfully logged out.",
    }