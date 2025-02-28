import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget

from utils.MIDI.ComputerKeyboard import ComputerKeyboard
from utils.MIDI.MidiHost import MidiHost
from utils.Music.SamplesHost import SamplesHost
from .ui_DeviceWidget import Ui_DeviceWidget


class DeviceWidget(QWidget):
    def __init__(
            self,
            name=None,
            parent=None
    ):
        super().__init__(parent)
        self.ui = Ui_DeviceWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("")

        self.is_muted = False
        self.is_enabled = False

        self.sample_host = SamplesHost()

        self.sample = None
        self.ui.PresetNameLabel.setText("No Sample")
        self.ui.RemovePresetButton.disabled = True
        self.ui.RemovePresetButton.setStyleSheet("")
        self.ui.RemovePresetButton.clicked.connect(self.remove_sample)

        self.current_subscription = None
        self.device_list = []

        if name is not None:
            self.ui.WidgetNameLabel.setText(name)

        self.ui.MuteButton.clicked.connect(self.mute_clicked)
        self.ui.EnableButton.clicked.connect(self.enable_clicked)

        self.ui.DevicesBox.currentIndexChanged.connect(self.new_device_chosen)

        self.midihost = MidiHost()
        self.timer = QTimer()
        self.timer.timeout.connect(self.midihost_check)
        self.timer.start(3000)


    def widget_selected(self):
        self.ui.border.setStyleSheet("background-color: white")

    def widget_deselect(self):
        self.ui.border.setStyleSheet("background-color: rgb(125, 128, 128)")

    def mute_clicked(self):
        if not self.is_muted:
            self.ui.MuteButton.setText("Unmute")
            self.ui.MuteButton.setStyleSheet("background-color: red")
        else:
            self.ui.MuteButton.setText("Mute")
            self.ui.MuteButton.setStyleSheet("")
        self.is_muted = not self.is_muted

    def enable_clicked(self):
        if not self.is_enabled:
            self.ui.EnableButton.setText("Disable")
            self.ui.EnableButton.setStyleSheet("background-color: green")
        else:
            self.ui.EnableButton.setText("Enable")
            self.ui.EnableButton.setStyleSheet("")
        self.is_enabled = not self.is_enabled

    def mousePressEvent(self, event):
        self.parent().widget_clicked(self)
        super().mousePressEvent(event)

    def set_sample(self, preset):
        self.sample = self.sample_host.samples[preset]

        self.ui.PresetNameLabel.setText(preset)
        self.ui.RemovePresetButton.setStyleSheet("background-color: red")
        self.ui.RemovePresetButton.disabled = False

    def remove_sample(self):
        self.sample = None

        self.ui.PresetNameLabel.setText("No Sample")
        self.ui.RemovePresetButton.setStyleSheet("")
        self.ui.RemovePresetButton.disabled = True

    def new_device_chosen(self, index):
        selected_item = self.ui.DevicesBox.currentText()

        if self.current_subscription is not None:
            self.current_subscription.remove_subscriber(self)
            self.current_subscription = None

        if selected_item == "No Device" or selected_item == "":
            return

        if selected_item == "Computer Keyboard":
            self.current_subscription = ComputerKeyboard
            ComputerKeyboard.add_subscriber(self)
            return

        self.current_subscription = self.midihost.active_listeners[selected_item]
        self.current_subscription.add_subscriber(self)

    def subscribe_action(self, num):
        if not self.sample or not self.is_enabled:
            return
        volume = self.ui.VolumeSlider.value() / 100 if not self.is_muted else 0
        self.sample.play_note_by_num(num, volume)


    def midihost_check(self):
        new_devices = list(self.midihost.active_listeners.keys())

        if self.device_list != new_devices:
            self.ui.DevicesBox.clear()
            self.ui.DevicesBox.addItems(["No Device", "Computer Keyboard"])
            self.ui.DevicesBox.addItems(list(new_devices))
            self.ui.DevicesBox.setCurrentIndex(0)
            self.device_list = new_devices



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DeviceWidget()
    widget.show()
    sys.exit(app.exec())
