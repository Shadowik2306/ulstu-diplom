import sys
import time

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMenuBar, QMainWindow

from src.config import settings
from src.utils.ComputerKeyboard import computer_keyboard_singleton_factory
from src.utils.PresetHost import preset_host_singleton_factory
from src.views.MusicWindow.ui_MusicWindow import Ui_MusicWindow
from src.views.MidiChannelWidget.MidiChannelWidget import MidiChannelWidget
from src.views.SingInWindow.sign_in import SignInWindow


class MusicWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MusicWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("")

        self.preset_host = preset_host_singleton_factory()
        self.update_presets()
        self.ui.PresetList.itemDoubleClicked.connect(self.preset_double_clicked)

        self.selected_device: MidiChannelWidget | None = None
        midi_channel_1 = MidiChannelWidget(
            midi_channel_id=1,
            parent=self,
            name="MIDI 1",
        )
        midi_channel_2 = MidiChannelWidget(
            midi_channel_id=2,
            parent=self,
            name="MIDI 2",
        )
        self.midi_channels = [midi_channel_1, midi_channel_2]
        self.ui.MidiChannelsLayout.addWidget(midi_channel_1)
        self.ui.MidiChannelsLayout.addWidget(midi_channel_2)
        self.midi_channel_selected: MidiChannelWidget | None = None

        self.ui.UpdatePresetsButton.clicked.connect(self.update_presets)
        self.__update_presets_view()

        self.computer_keyboard = computer_keyboard_singleton_factory()
        self.computer_keyboard_active = False
        self.ui.ComputerKeyboardButton.clicked.connect(self.computer_keyboard_button_clicked)

    def __update_presets_view(self):
        self.ui.PresetList.clear()
        self.ui.PresetList.addItems(list(self.preset_host.presets.keys()))

    def update_presets(self):
        res = self.preset_host.update()
        self.__update_presets_view()

        if res == 0:
            self.ui.UpdatePresetsButton.setStyleSheet("background-color: green")
            self.ui.UpdatePresetsButton.setText("Updated")
        else:
            self.ui.UpdatePresetsButton.setStyleSheet("background-color: red")
            self.ui.UpdatePresetsButton.setText("Some problems")

        self.ui.UpdatePresetsButton.update()

    def computer_keyboard_button_clicked(self):
        if not self.computer_keyboard_active:
            self.ui.ComputerKeyboardButton.setStyleSheet("background-color: green;")
            self.setFocus()
        else:
            self.ui.ComputerKeyboardButton.setStyleSheet("")
        self.computer_keyboard_active = not self.computer_keyboard_active

    def keyPressEvent(self, event):
        if not self.computer_keyboard_active:
            return

        if event.isAutoRepeat():
            return

        self.computer_keyboard.play_event(event.key())

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if not self.computer_keyboard_active:
            return

        if event.isAutoRepeat():
            return

        self.computer_keyboard.stop_event(event.key())

        super().keyReleaseEvent(event)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        if self.computer_keyboard_active:
            self.ui.ComputerKeyboardButton.setStyleSheet("")
            self.computer_keyboard_active = False

    def midi_channel_select(self, item):
        if self.midi_channel_selected:
            self.midi_channel_selected.deselect()
        self.midi_channel_selected = item
        self.midi_channel_selected.select()

    def preset_double_clicked(self, item):
        if self.midi_channel_selected is None:
            return
        self.midi_channel_selected.set_preset(self.preset_host.presets[item.text()])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MusicWindow()
    widget.show()
    sys.exit(app.exec())
