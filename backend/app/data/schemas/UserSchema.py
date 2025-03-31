from pydantic import BaseModel, Field
from datetime import date


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
    subscription_to: date | None

    @property
    def is_subscribed(self) -> bool:
        return self.subscription_to > date.today() if self.subscription_to else False



class UserLoginSchema(BaseModel):
    email: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int = Field(..., validation_alias='id')
    username: str
    subscription_to: date
    is_subscribed: bool
