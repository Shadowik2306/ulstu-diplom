import requests
from sqlalchemy import select, delete

from app.data.database import session_maker
from app.data.models import PresetModel
from app.data.schemas.PresetSchema import PresetSchema, PresetCreateSchema, PresetSchemaSync
from app.config import settings

URL_PATH_PRESET = "/presets"

class PresetRepository:
    @classmethod
    def get(cls, preset_id: int) -> PresetSchema:
        with session_maker() as session:
            query = select(PresetModel).where(preset_id == PresetModel.id)
            res = session.execute(query)

            preset_model: PresetModel = res.scalar()
            return PresetSchema.model_validate(preset_model, from_attributes=True)

    @classmethod
    def get_all(cls) -> list[PresetSchema]:
        with session_maker() as session:
            query = select(PresetModel)
            res = session.execute(query)
            presets_models = res.scalars().all()

            return [PresetSchema.model_validate(preset_model, from_attributes=True) for preset_model in presets_models]

    @classmethod
    def synchronize(cls):
        response = requests.get(settings.server_url + URL_PATH_PRESET, headers={
            "Accept": "application/json",
        })

        if response.status_code != 200:
            raise Exception("Something went wrong")

        global_presets = [PresetSchemaSync.model_validate(preset) for preset in response.json()]

        with session_maker() as session:
            query = delete(PresetModel).filter(PresetModel.id.notin_([preset.id for preset in global_presets]))
            session.execute(query)
            session.commit()

            for preset in global_presets:
                query = select(PresetModel).where(preset.id == PresetModel.id)
                res = session.execute(query)

                preset_model: PresetModel = res.scalar()
                if preset_model is None:
                    new_preset = PresetModel(**preset.model_dump())
                    session.add(new_preset)
                else:
                    preset_model.name = preset.name

                session.commit()







