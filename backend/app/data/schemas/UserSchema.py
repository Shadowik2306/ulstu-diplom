from pydantic import BaseModel


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
