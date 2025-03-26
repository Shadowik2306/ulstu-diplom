from pathlib import Path
import os
import requests

from app.config import settings
from app.data.repositories.PresetRepository import PresetRepository
from app.utils.Music.Preset import Preset


class PresetHost:
    _instance = None

    def __init__(
            self,
    ):
        self.presets = {}
        self.update()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def update(self):
        PresetRepository.synchronize()
        self.presets = {preset.name: Preset(preset.id) for preset in PresetRepository.get_all()}





