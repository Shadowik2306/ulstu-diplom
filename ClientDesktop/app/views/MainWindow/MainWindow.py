import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget

from app.utils.MIDI.ComputerKeyboard import ComputerKeyboard
from app.utils.Music.PresetHost import PresetHost
from app.views.MainWindow.ui_MainWindow import Ui_MainWindow
from app.views.DeviceWidget.DeviceWidget import DeviceWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("")

        self.preset_host = PresetHost()
        self.selected_device: DeviceWidget | None = None

        self.computer_keyboard_active = False
        self.ui.ComputerKeyboardButton.clicked.connect(self.computer_keyboard_clicked)
        self.ui.addPresetButton.clicked.connect(self.update_button)

        midi_1 = DeviceWidget(
            device_id=0,
            name="MIDI 1",
        )

        midi_2 = DeviceWidget(
            device_id=1,
            name="MIDI 2",
        )

        self.widgets = [midi_1, midi_2]

        self.ui.channels_layout.addWidget(midi_1)
        self.ui.channels_layout.addWidget(midi_2)

        self.__load_items()
        self.ui.SoundsWidget.itemDoubleClicked.connect(self.sample_double_clicked)

        self.setFocus()

    def __load_items(self):
        self.ui.SoundsWidget.clear()
        self.ui.SoundsWidget.addItems(
            [preset for preset in self.preset_host.presets.keys()]
        )

    def widget_clicked(self, clicked_widget):
        for i, widget in enumerate(self.widgets):
            if clicked_widget == widget:
                self.selected_device = clicked_widget
            widget.widget_deselect()

        clicked_widget.widget_selected()

    def sample_double_clicked(self, item):
        if not self.selected_device:
            return
        self.selected_device.set_sample(item.text())

    def computer_keyboard_clicked(self, clicked_widget):
        if not self.computer_keyboard_active:
            self.ui.ComputerKeyboardButton.setStyleSheet("background-color: green;")
            self.setFocus()
        else:
            self.ui.ComputerKeyboardButton.setStyleSheet("")
        self.computer_keyboard_active = not self.computer_keyboard_active

    def keyPressEvent(self, event):
        if not self.computer_keyboard_active:
            return

        keyboard_to_midi = {
            Qt.Key.Key_A: 60,  # C4
            Qt.Key.Key_S: 62,  # D4
            Qt.Key.Key_D: 64,  # E4
            Qt.Key.Key_F: 65,  # F4
            Qt.Key.Key_G: 67,  # G4
            Qt.Key.Key_H: 69,  # A4
            Qt.Key.Key_J: 71,  # B4
            Qt.Key.Key_K: 72,  # C5
            Qt.Key.Key_L: 74   # D5
        }

        if event.key() in keyboard_to_midi:
            ComputerKeyboard.event(keyboard_to_midi[event.key()])
            print(keyboard_to_midi[event.key()])
            return

        super().keyPressEvent(event)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        if self.computer_keyboard_active:
            self.ui.ComputerKeyboardButton.setStyleSheet("")
            self.computer_keyboard_active = False

    def update_button(self):
        self.preset_host.update()
        self.ui.SoundsWidget.clear()
        new_presets = [preset for preset in self.preset_host.presets.keys()]
        self.ui.SoundsWidget.addItems(
            new_presets
        )

        for widget in self.widgets:
            if widget.sample_name not in new_presets:
                widget.remove_sample()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
