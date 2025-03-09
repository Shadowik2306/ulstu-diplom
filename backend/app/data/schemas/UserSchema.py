from pydantic import BaseModel, Field


class UserRegisterSchema(BaseModel):
    username: str
    email: str
    password: str


class UserAddSchema(BaseModel):
    username: str
    email: str
    password: bytes


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: bytes


class UserLoginSchema(BaseModel):
    email: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int = Field(..., validation_alias='id')
    username: str
