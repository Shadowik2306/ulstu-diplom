import json
import time
from pathlib import Path

import numpy as np
import pygame

from app.data.repositories.SampleRepository import SampleRepository
from app.utils.Music.SoundEngine import SoundEngine

STATIC_PATH = Path(__file__).parent.parent.parent.parent / 'static'

i = 0
class Preset:
    def __init__(
        self,
        preset_id: int
    ):
        pygame.mixer.init()
        self.preset_id = preset_id
        self.samples = {}
        self.sound_engine = SoundEngine()
        self.update()
        self.i = 0

    def play_note(self, note: int, volume: float):
        if self.samples[note] is None:
            return
        # sound_file = self.samples[note]
        # sound_file.set_volume(volume)
        # sound_file.play()
        self.i += 1
        self.sound_engine.add_sample(self.samples[note], self.i)


    def download_music_file(self, music_path: Path):
        pass

    def update(self):
        SampleRepository.synchronize(self.preset_id)
        self.samples = {}

        for i in range(1, 13):
            sample = SampleRepository.get_sample(note_id=i, preset_id=self.preset_id)
            if sample is None:
                self.samples[i] = None
                continue
            self.samples[i] = sample.data_list


