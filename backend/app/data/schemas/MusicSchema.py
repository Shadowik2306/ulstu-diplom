from pydantic import BaseModel, Field


class MusicSchema(BaseModel):
    id: int
    music_url: str


class MusicCreateRequestSchema(BaseModel):
    text_request: str
    negative_prompt: str = Field(default="Low quality.")
    audio_length_in_s: int = Field(default=5)
    num_inference_steps: int = Field(default=200)
    num_waveforms_per_prompt: int = Field(default=3)
    count: int = Field(default=1)


class MusicCreateSchema(BaseModel):
    music_url: str


class MusicDeleteSchema(BaseModel):
    note_id: int | None = None