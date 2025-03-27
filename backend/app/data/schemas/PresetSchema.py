from pydantic import BaseModel
from app.data.schemas.SampleSchema import SampleSchema
from app.data.schemas.Schema import PaginationSchema


class PresetSchema(BaseModel):
    id: int
    user_id: int
    name: str
    color: str


class PresetAndSamplesSchema(PresetSchema):
    samples: list["SampleSchema"]


class PresetsPageSchema(PaginationSchema):
    presets: list[PresetSchema]


class PresetCreateSchema(BaseModel):
    name: str
    color: str


class PresetUpdateSchema(BaseModel):
    name: str

