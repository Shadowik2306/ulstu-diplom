from pydantic import BaseModel


class MusicSchema(BaseModel):
    id: int
    music_url: str


class MusicCreateRequestSchema(BaseModel):
    text_request: str
    count: int


class MusicCreateSchema(BaseModel):
    music_url: str


class MusicDeleteSchema(BaseModel):
    note_id: int | None = None