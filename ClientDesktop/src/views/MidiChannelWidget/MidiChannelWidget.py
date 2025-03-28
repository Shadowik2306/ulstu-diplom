import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget

from src.utils.ComputerKeyboard import computer_keyboard_singleton_factory
from src.utils.MidiHost import MidiHost
from src.utils.PresetHost import Preset
from src.utils.SoundEngine import sound_engine_singleton_factory
from src.views.MidiChannelWidget.ui_Midi_ChannelWidget import Ui_MidiChannelWidget


class MidiChannelWidget(QWidget):
    def __init__(
            self,
            midi_channel_id,
            parent=None,
            name=None,
    ):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_MidiChannelWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("")

        if name is not None:
            self.ui.WidgetNameLabel.setText(name)

        self.__preset: Preset | None = None
        self.ui.RemovePresetButton.disabled = True
        self.ui.RemovePresetButton.setStyleSheet("")
        self.ui.RemovePresetButton.clicked.connect(self.remove_preset)

        self.computer_keyboard = computer_keyboard_singleton_factory()
        self.current_subscription = None
        self.device_list = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.midi_host_update)
        self.timer.start(3000)
        self.ui.DevicesBox.currentIndexChanged.connect(self.new_device_chosen)

        self.ui.MuteButton.clicked.connect(self.mute_clicked)
        self.is_muted = False

        self.ui.EnableButton.clicked.connect(self.enable_clicked)
        self.is_enabled = False

        self.id = midi_channel_id
        self.sound_engine = sound_engine_singleton_factory()
        self.sound_engine.add_midi_channel(midi_channel_id, self.ui.VolumeSlider.value())
        self.ui.VolumeSlider.valueChanged.connect(self.volume_changed)

    def set_preset(self, preset: Preset):
        self.__preset = preset
        self.ui.PresetNameLabel.setText(preset.name)

        self.ui.RemovePresetButton.setStyleSheet("background-color: red")
        self.ui.RemovePresetButton.disabled = False

    def remove_preset(self):
        self.__preset = None

        self.ui.PresetNameLabel.setText("No Sample")
        self.ui.RemovePresetButton.setStyleSheet("")
        self.ui.RemovePresetButton.disabled = True

    def mousePressEvent(self, event):
        self.parent.midi_channel_select(self)

    def deselect(self):
        self.ui.border.setStyleSheet("background-color: rgb(125, 128, 128)")

    def select(self):
        self.ui.border.setStyleSheet("background-color: white")

    def mute_clicked(self):
        if not self.is_muted:
            self.ui.MuteButton.setText("Unmute")
            self.ui.MuteButton.setStyleSheet("background-color: red")
            self.sound_engine.update_midi_channel(self.id, 0)
        else:
            self.ui.MuteButton.setText("Mute")
            self.ui.MuteButton.setStyleSheet("")
            self.sound_engine.update_midi_channel(self.id, self.ui.VolumeSlider.value())

        self.is_muted = not self.is_muted

    def volume_changed(self):
        if self.is_muted:
            return
        self.sound_engine.update_midi_channel(
            self.id, self.ui.VolumeSlider.value()
        )

    def enable_clicked(self):
        if not self.is_enabled:
            self.ui.EnableButton.setText("Disable")
            self.ui.EnableButton.setStyleSheet("background-color: green")
        else:
            self.ui.EnableButton.setText("Enable")
            self.ui.EnableButton.setStyleSheet("")
        self.is_enabled = not self.is_enabled

    def midi_host_update(self):
        MidiHost.update_midi_ports()
        new_devices = list(MidiHost.midi_ports)

        if self.device_list != new_devices:
            self.ui.DevicesBox.clear()
            self.ui.DevicesBox.addItems(["No Device", "Computer Keyboard"])
            self.ui.DevicesBox.addItems(list(new_devices))
            self.ui.DevicesBox.setCurrentIndex(0)
            self.device_list = new_devices

    def new_device_chosen(self):
        selected_item = self.ui.DevicesBox.currentText()

        if self.current_subscription is not None:
            self.current_subscription.remove_subscriber(self)
            self.current_subscription = None

        if selected_item == "No Device" or selected_item == "":
            return

        if selected_item == "Computer Keyboard":
            self.current_subscription = self.computer_keyboard
            self.computer_keyboard.add_subscriber(self)
            return

        self.current_subscription = MidiHost.midi_ports[selected_item]
        self.current_subscription.add_subscriber(self)

    def note_on(self, note):
        if self.__preset is None or not self.is_enabled:
            return
        data = self.__preset.get_sample_sound(note)
        self.sound_engine.add_sound(
            midi_channel_id=self.id,
            note=note,
            data=data,
        )

    def note_off(self, note):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MidiChannelWidget()
    widget.show()
    sys.exit(app.exec())
