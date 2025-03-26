import sys
from threading import Thread

from PySide6.QtWidgets import QApplication

from src.utils.MidiHost import midi_host_singleton_factory
from src.utils.SoundEngine import sound_engine_singleton_factory
from src.views.MainWindow.MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    midi_host = midi_host_singleton_factory()
    midi_host_thread = Thread(target=midi_host.listen_for_midi)
    midi_host_thread.start()

    sound_engine = sound_engine_singleton_factory()
    sound_engine_thread = Thread(target=sound_engine.main_cycle)
    sound_engine_thread.start()

    sys.exit(app.exec())