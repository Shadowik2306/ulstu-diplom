import json
from pathlib import Path
import pygame
from schema import Schema, SchemaError

SAMPLE_CONFIG_SCHEMA = Schema({
    'name': str,
    "notes": {
        "a": str,
        "b": str,
        "b#": str,
        "c": str,
        "c#": str,
        "d": str,
        "e": str,
        "e#": str,
        "f": str,
        "f#": str,
        "g": str,
        "g#": str
      }
})


class Sample:
    def __init__(
        self,
        path_to_dir: Path
    ):
        pygame.mixer.init()
        self.path_to_dir = path_to_dir
        self.config_file_path = self.path_to_dir / "sample.json"

        self.__check_sample_dir()

        self.sound_objects = {}
        self.__load_notes()

    def __check_sample_dir(self):
        if not self.config_file_path.exists():
            raise NotADirectoryError("Sample directory is not sample dir")

        with open(self.config_file_path) as json_file:
            data = json.load(json_file)

        if not SAMPLE_CONFIG_SCHEMA.is_valid(data):
            raise SchemaError("Config file is not valid json")

        self.name = data["name"]
        self.notes = data["notes"]

    def __load_notes(self):
        for note in self.notes.keys():
            filename = Path(self.path_to_dir) / self.notes[note]
            self.sound_objects[note] = pygame.mixer.Sound(str(filename))

    def play_note(self, note: str, volume: float):
        sound_file = self.sound_objects[note]
        sound_file.set_volume(volume)
        sound_file.play()

    def play_note_by_num(self, num: int, volume: float):
        notes = ["a", "b", "b#", "c", "c#" ,"d", "e", "e#", "f", "f#", "g", "g#"]
        self.play_note(notes[num % len(notes)], volume)

