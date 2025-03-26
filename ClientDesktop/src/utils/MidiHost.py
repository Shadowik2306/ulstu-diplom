import threading
import mido
import time
import sys


class MidiListener(threading.Thread):
    def __init__(self, port_name):
        super().__init__()
        self.port_name = port_name
        self.running = True
        self.subscribers = set()

    def run(self):
        with mido.open_input(self.port_name) as inport:
            print(f"Listening for MIDI messages on {self.port_name}...")
            while self.running:
                for message in inport.iter_pending():
                    if message.type == 'note_on':
                        for subscriber in self.subscribers:
                            subscriber.note_on(message.note)
                    if message.type == 'note_off':
                        for subscriber in self.subscribers:
                            subscriber.note_off(message.note)

    def stop(self):
        self.running = False

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)


class MidiHost:
    _instance = None

    def __init__(self):
        self.observed_ports = set()
        self.active_listeners = {}

    def listen_for_midi(self):
        while True:
            try:
                current_ports = set(mido.get_input_names())
            except Exception:
                continue

            new_ports = current_ports - self.observed_ports

            for port in new_ports:
                listener = MidiListener(port)
                listener.start()
                self.active_listeners[port] = listener

            disconnected_ports = self.observed_ports - current_ports

            for port in disconnected_ports:
                if port in self.active_listeners:
                    listener = self.active_listeners[port]
                    listener.stop()
                    listener.join()
                    del self.active_listeners[port]

            # Update observed ports
            self.observed_ports = current_ports

            time.sleep(1)


def midi_host_singleton_factory(_object=MidiHost()):
    return _object


if __name__ == '__main__':
    try:
        host = MidiHost()
        host.listen_for_midi()
    except KeyboardInterrupt:
        print("\nExiting MIDI host.")
        sys.exit(0)





