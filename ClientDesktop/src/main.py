import sys

from PySide6.QtWidgets import QApplication

from src.config import settings
from src.data.models import CustomBaseModel
from src.data.database import engine

CustomBaseModel.metadata.create_all(engine)

from src.utils.SoundEngine import sound_engine_singleton_factory
from src.views.MainWindow import MainWindow

import sounddevice as sd


if __name__ == '__main__':
    sound_engine = sound_engine_singleton_factory()

    with sd.OutputStream(callback=sound_engine.callback, samplerate=16000, channels=1):
        app = QApplication(sys.argv)
        app.setApplicationName("MyQtApp")
        widget = MainWindow()
        widget.setWindowTitle("Tinkling App")

        if settings.jwt_secret_key:
            widget.show()
        else:
            sys.exit()
        sys.exit(app.exec())
