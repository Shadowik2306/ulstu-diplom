from pydantic import BaseModel


class SampleSchema(BaseModel):
    id: int
    music_url: str
    preset_id: int
    note_id: int


class SampleCreateSchema(BaseModel):
    music_url: str
    preset_id: int




