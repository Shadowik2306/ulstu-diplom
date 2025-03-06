import os
from pathlib import Path

import requests
from sqlalchemy import select, update, delete

from app.config import settings
from app.data.database import session_maker
from app.data.models import SampleModel
from app.data.schemas.SampleSchema import SampleSchema

URL_PATH_SAMPLES = "/presets/{preset_id}/samples/"
URL_DOWNLOAD_SAMPLE = "/files/{file_name}"
STATIC_PATH = Path(__file__).parent.parent.parent.parent / "static"


def download_sample(sample_name):
    response = requests.get(settings.server_url + f"{URL_DOWNLOAD_SAMPLE.format(file_name=sample_name)}")
    with open(STATIC_PATH / sample_name, "wb") as file:
        file.write(response.content)


def delete_sample(sample_name):
    os.remove(STATIC_PATH / sample_name)


class SampleRepository:
    @classmethod
    def synchronize(cls, preset_id: int) -> SampleSchema:
        response = requests.get(settings.server_url + URL_PATH_SAMPLES.format(preset_id=preset_id), headers={
            "Accept": "application/json",
        }, params={
            "connected": True
        })

        if response.status_code != 200:
            raise Exception("Something went wrong")

        presets_connected_samples = [SampleSchema.model_validate(sample) for sample in response.json()]

        with session_maker() as session:
            query = select(SampleModel).filter(SampleModel.id.notin_([sample.id for sample in presets_connected_samples]))
            res = session.execute(query)

            samples_not_exist = res.scalars().all()

            for sample_unused in samples_not_exist:
                delete_sample(sample_unused.music_url)
                session.delete(sample_unused)
                session.commit()


            for global_sample in presets_connected_samples:
                query = select(SampleModel).where(global_sample.id == SampleModel.id)
                res = session.execute(query)

                sample_old: SampleModel = res.scalar()
                if sample_old is None:
                    sample_new = SampleModel(**global_sample.model_dump())
                    download_sample(sample_new.music_url)
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