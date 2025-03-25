import sys

from PySide6.QtWidgets import QApplication

from app.data.repositories.NoteRepository import NoteRepository
from app.utils.MIDI.MidiHost import MidiHost
from app.utils.Music.PresetHost import PresetHost
from app.views.MainWindow.MainWindow import MainWindow
from threading import Thread

from app.utils.Music.SoundEngine import SoundEngine


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    PresetHost()

    NoteRepository.initialize_table()

    midi_host = MidiHost()
    midi_host_thread = Thread(target=midi_host.listen_for_midi)
    midi_host_thread.start()

    sound_engine = SoundEngine()
    sound_engine_thread = Thread(target=sound_engine.main_cycle)
    sound_engine_thread.start()

    sys.exit(app.exec())