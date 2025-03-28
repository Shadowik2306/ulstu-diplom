from src.data.repositories.PresetRepository import PresetRepository
from src.data.repositories.SampleRepository import SampleRepository
from src.data.schemas.PresetSchema import PresetSchema


class Preset:
    def __init__(self, preset_info: PresetSchema):
        self.id = preset_info.id
        self.name = preset_info.name
        self.samples = {}
        self.update()

    def update(self):
        SampleRepository.synchronize(preset_id=self.id)
        self.samples = {}

        for i in range(1, 13):
            sample = SampleRepository.get_sample(note_id=i, preset_id=self.id)
            if sample is None:
                self.samples[i] = None
                continue
            self.samples[i] = sample.data_list

    def get_sample_sound(self, note):
        note_convert = note % 12 + 1
        if self.samples[note_convert] is None:
            return
        return self.samples[note_convert]


class PresetHost:
    _instance = None

    def __init__(self):
        self.presets: dict[str, Preset] = {}
        self.update()

    def update(self):
        res = PresetRepository().synchronize()
        self.presets = {
            preset_info.name: Preset(preset_info)
            for preset_info in PresetRepository.get_all()
        }
        return res


def preset_host_singleton_factory(_object=PresetHost()):
    return _object









