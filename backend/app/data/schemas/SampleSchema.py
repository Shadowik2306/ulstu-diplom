from pydantic import BaseModel


class SampleSchema(BaseModel):
    id: int
    name: str
    music_url: str


class SampleCreateSchema(BaseModel):
    name: str
    music_url: str
    preset_id: int


class SampleCreateRequestSchema(BaseModel):
    text_request: str
    count: int

