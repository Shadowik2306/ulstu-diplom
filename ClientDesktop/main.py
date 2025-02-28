import sys

from PySide6.QtWidgets import QApplication

from utils.MIDI.MidiHost import MidiHost
from utils.Music.SamplesHost import SamplesHost
from views.MainWindow.MainWindow import MainWindow
from threading import Thread

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    SamplesHost()
    midi_host = MidiHost()

    thread = Thread(target=midi_host.listen_for_midi)
    thread.start()

    sys.exit(app.exec())