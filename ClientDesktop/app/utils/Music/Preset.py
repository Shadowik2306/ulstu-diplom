import json
from pathlib import Path
import pygame

from app.data.repositories.SampleRepository import SampleRepository

STATIC_PATH = Path(__file__).parent.parent.parent.parent / 'static'

class Preset:
    def __init__(
        self,
        preset_id: int
    ):
        pygame.mixer.init()
        self.preset_id = preset_id
        self.samples = {}
        self.update()

    def play_note(self, note: int, volume: float):
        if self.samples[note] is None:
            return
        sound_file = self.samples[note]
        sound_file.set_volume(volume)
        sound_file.play()

    def download_music_file(self, music_path: Path):
        pass

    def update(self):
        SampleRepository.synchronize(self.preset_id)
        self.samples = {}

        for i in range(1, 13):
            sample = SampleRepository.get_sample(note_id=i, preset_id=self.preset_id)
            if sample is None or not (STATIC_PATH / sample.music_url).is_file():
                self.samples[i] = None
                continue
            self.samples[i] = pygame.mixer.Sound(STATIC_PATH / sample.music_url)


