from datetime import datetime, timedelta, timezone

import jwt
import bcrypt
from fastapi import Depends, HTTPException
from jwt import InvalidTokenError
from starlette import status

from app.config import jwt_settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.data.repositories.UserRepository import JwtBlackListRepository, UserRepository
from app.data.schemas.UserSchema import UserSchema

http_bearer = HTTPBearer()


def encode_jwt(
        payload: dict,
        private_key: str = jwt_settings.private_key_path.read_text(),
        algorithm: str = jwt_settings.algorithm,
):
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)

    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
        token: str,
        public_key: str = jwt_settings.public_key_path.read_text(),
        algorithm: str = jwt_settings.algorithm
):
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )
    return decoded


def hash_password(
        password: str
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
        password: str,
        hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password
    )


async def get_current_auth_user_token(
    token: HTTPAuthorizationCredentials = Depends(http_bearer)
):
    if await JwtBlackListRepository.is_exist(token.credentials):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authenticated",
        )
    return token.credentials


async def get_current_token_payload_user(
        token: str = Depends(get_current_auth_user_token),
) -> UserSchema:
    try:
        payload = decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return payload


async def get_current_auth_user(
        payload: dict = Depends(get_current_token_payload_user),
) -> UserSchema:
    user: UserSchema | None = await UserRepository.get_one(payload['sub'])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user

