from datetime import datetime, timedelta, timezone

import jwt
import bcrypt

from app.config import jwt_settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


http_bearer = HTTPBearer()


def encode_jwt(
        payload: dict,
        private_key: str = jwt_settings.private_key_path.read_text(),
        algorithm: str = jwt_settings.algorithm,
        expire_minutes: int = jwt_settings.access_token_expires_minutes,
        expire_timedelta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
        token: str | bytes,
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
