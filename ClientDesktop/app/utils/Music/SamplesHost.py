from pathlib import Path
import os

from app.utils.Music.Sample import Sample

class SamplesHost:
    _instance = None

    def __init__(
            self,
            path_to_samples_dir: Path = Path(__file__).parent.parent.parent.parent / "static" / "samples",
    ):
        self.path_to_samples_dir = path_to_samples_dir
        self.__initialize_system_dir()

        self.samples = {}
        self.__get_samples_dir()

        print(self.samples)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __initialize_system_dir(self):
        if self.path_to_samples_dir.exists():
            print("Samples dir exists")
            return

        self.path_to_samples_dir.mkdir(parents=True)
        print("Samples dir created")

    def __get_samples_dir(self):
        dirs = os.walk(self.path_to_samples_dir, topdown=True)

        for sample_path, _, _ in dirs:
            if Path(sample_path) == self.path_to_samples_dir:
                continue

            try:
                sample = Sample(Path(sample_path))
                self.samples[sample.name] = sample
            except Exception as e:
                continue






