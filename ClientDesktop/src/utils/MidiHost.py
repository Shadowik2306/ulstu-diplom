import rtmidi
from rtmidi.midiutil import open_midiinput


class MidiDevice:

    def __init__(self, port_num, midi_in):
        self.midi_in, port_name = open_midiinput(port_num)
        self.midi_in.set_callback(self.callback)
        self.__subscribers = set()

    def __del__(self):
        del self.midi_in

    def callback(self, event, data=None):
        message, deltatime = event
        status = message[0]

        if status & 0xF0 == 0x90:  # note_on
            note, velocity = message[1], message[2]
            # print(f"Note On: {note}, Velocity: {velocity}")
            for subscriber in self.__subscribers:
                subscriber.note_on(note)
        elif status & 0xF0 == 0x80:  # note_off
            note, velocity = message[1], message[2]
            # print(f"Note Off: {note}, Velocity: {velocity}")

    def add_subscriber(self, subscriber):
        self.__subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.__subscribers.remove(subscriber)

class MidiHost:
    last_midi_ports = []
    midi_ports = {}

    @classmethod
    def update_midi_ports(cls):
        midi_in = rtmidi.MidiIn()

        try:
            ports = midi_in.get_ports()
        except Exception as e:
            print(f"Some problems")
            return

        for port_id, port_name in enumerate(ports):
            if port_id < len(cls.last_midi_ports):
                if port_name != cls.last_midi_ports[port_id]:
                    del cls.midi_ports[cls.last_midi_ports[port_id]]
                    print(f"Device disconnected {port_name}")
                else:
                    continue

            print(f"Device connected {port_name}")
            cls.midi_ports[port_name] = MidiDevice(port_id, midi_in)

        for undefined_ports_name in cls.last_midi_ports[len(ports):]:
            del cls.midi_ports[undefined_ports_name]
            print(f"Device disconnected {undefined_ports_name}")

        cls.last_midi_ports = ports

        return ports



if __name__ == '__main__':
    import time
    while True:
        MidiHost.update_midi_ports()
        time.sleep(1)
