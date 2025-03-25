import pickle
from pydantic import BaseModel


class SampleSchemaServer(BaseModel):
    id: int
    preset_id: int
    note_id: int
    music_url: str


class SampleSchema(BaseModel):
    id: int
    preset_id: int
    note_id: int
    data: bytes

    @property
    def data_list(self):
        return pickle.loads(self.data)



