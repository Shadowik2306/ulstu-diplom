import os
from pathlib import Path

import requests
from sqlalchemy import select, update, delete

from src.config import settings
from src.data.database import session_maker
from src.data.models import SampleModel
from src.data.schemas.SampleSchema import SampleSchema, SampleSchemaServer

import soundfile as sf
import numpy as np

URL_PATH_SAMPLES = "/preset/{preset_id}/samples/"
URL_DOWNLOAD_SAMPLE = "/files/{file_name}"
STATIC_PATH = Path(__file__).parent.parent.parent.parent / "static"


def parse_sample(sample_file_name):
    file = sf.SoundFile(sample_file_name)

    file_freq = sf.read(sample_file_name, dtype='float32')[0]

    return file_freq


def download_and_parse_sample(sample_name):
    response = requests.get(settings.server_url + f"{URL_DOWNLOAD_SAMPLE.format(file_name=sample_name)}")
    file_path = sample_name
    with open(file_path, "wb") as file:
        file.write(response.content)

    parsed_sample = parse_sample(file_path)
    os.remove(file_path)
    return parsed_sample


class SampleRepository:
    @classmethod
    def synchronize(cls, preset_id: int):
        response = requests.get(settings.server_url + URL_PATH_SAMPLES.format(preset_id=preset_id), headers={
            "Accept": "application/json",
        }, params={
            "connected": True
        })

        if response.status_code != 200:
            print("Something went wrong")
            return

        presets_connected_samples = [SampleSchemaServer.model_validate(sample) for sample in response.json()]

        with session_maker() as session:
            query = select(SampleModel).filter(SampleModel.preset_id == preset_id).filter(SampleModel.id.notin_([sample.id for sample in presets_connected_samples]))
            res = session.execute(query)

            samples_not_exist = res.scalars().all()

            for sample_unused in samples_not_exist:
                session.delete(sample_unused)
                session.commit()

            for global_sample in presets_connected_samples:
                query = select(SampleModel).where(global_sample.id == SampleModel.id)
                res = session.execute(query)

                sample_old: SampleModel = res.scalar()
                if sample_old is None:
                    parsed_sample = download_and_parse_sample(global_sample.music_url)
                    sample_new = SampleModel(
                        id=global_sample.id,
                        preset_id=global_sample.preset_id,
                        note_id=global_sample.note_id,
                    )
                    sample_new.set_data(parsed_sample)
                    session.add(sample_new)
                else:
                    sample_old.note_id = global_sample.note_id

                session.commit()

    @classmethod
    def get_sample(cls, **kwargs):
        with session_maker() as session:
            query = select(SampleModel).filter_by(**kwargs)

            res = session.execute(query)
            sample = res.scalar()
            if sample is None:
                return None
            return SampleSchema.model_validate(sample, from_attributes=True)