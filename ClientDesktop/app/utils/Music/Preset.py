import json
import time
from pathlib import Path

import numpy as np
import pygame

from app.data.repositories.SampleRepository import SampleRepository
from app.utils.Music.SoundEngine import sound_engine_singleton_factory

STATIC_PATH = Path(__file__).parent.parent.parent.parent / 'static'


class Preset:
    def __init__(
        self,
        preset_id: int
    ):
        pygame.mixer.init()
        self.preset_id = preset_id
        self.samples = {}
        self.sound_engine = sound_engine_singleton_factory()
        self.update()

    def play_note(self, midi_channel_id, note: int):
        note_convert = note % 12 + 1
        if self.samples[note_convert] is None:
            return
        print(1, midi_channel_id, note)
        self.sound_engine.add_sample(self.samples[note_convert], midi_channel_id, note)

    def stop_note(self, midi_channel_id, note: int):
        print(2, midi_channel_id, note)
        self.sound_engine.delete_sample(midi_channel_id, note)

    def update(self):
        SampleRepository.synchronize(self.preset_id)
        self.samples = {}

        for i in range(1, 13):
            sample = SampleRepository.get_sample(note_id=i, preset_id=self.preset_id)
            if sample is None:
                self.samples[i] = None
                continue
            self.samples[i] = sample.data_list


