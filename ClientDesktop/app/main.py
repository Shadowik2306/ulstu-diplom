import sys

from PySide6.QtWidgets import QApplication

from app.utils.MIDI.MidiHost import MidiHost
from app.utils.Music.SamplesHost import SamplesHost
from app.views.MainWindow.MainWindow import MainWindow
from threading import Thread
import data.database


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    SamplesHost()
    midi_host = MidiHost()

    thread = Thread(target=midi_host.listen_for_midi)
    thread.start()

    sys.exit(app.exec())