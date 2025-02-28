from pydantic import BaseModel

from app.data.schemas.SampleSchema import SampleSchema


class PresetSchema(BaseModel):
    id: int
    name: str
    samples: list["SampleSchema"]


class PresetCreateSchema(BaseModel):
    name: str


