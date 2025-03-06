import sys

from PySide6.QtWidgets import QApplication

from app.data.repositories.NoteRepository import NoteRepository
from app.utils.MIDI.MidiHost import MidiHost
from app.utils.Music.PresetHost import PresetHost
from app.views.MainWindow.MainWindow import MainWindow
from threading import Thread


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    PresetHost()
    midi_host = MidiHost()

    NoteRepository.initialize_table()

    thread = Thread(target=midi_host.listen_for_midi)
    thread.start()

    sys.exit(app.exec())