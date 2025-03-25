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
        """Run the thread to listen for MIDI messages."""
        with mido.open_input(self.port_name) as inport:
            print(f"Listening for MIDI messages on {self.port_name}...")
            while self.running:
                for message in inport.iter_pending():
                    if message.type == 'note_on':
                        for subscriber in self.subscribers:
                            subscriber.subscribe_play_action(message.note)

    def stop(self):
        """Stop the MIDI listener's thread."""
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

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def listen_for_midi(self):
        while True:
            try:
                current_ports = set(mido.get_input_names())
            except Exception:
                continue

            # Check for new connections
            new_ports = current_ports - self.observed_ports

            for port in new_ports:
                print(f"New MIDI connection detected: {port}")
                listener = MidiListener(port)
                listener.start()
                self.active_listeners[port] = listener

            # Check for disconnected devices
            disconnected_ports = self.observed_ports - current_ports

            for port in disconnected_ports:
                print(f"MIDI connection lost: {port}")
                if port in self.active_listeners:
                    listener = self.active_listeners[port]
                    listener.stop()  # Stop the thread
                    listener.join()  # Wait for the thread to finish
                    del self.active_listeners[port]

            # Update observed ports
            self.observed_ports = current_ports

            time.sleep(1)


if __name__ == '__main__':
    try:
        host = MidiHost()
        host.listen_for_midi()
    except KeyboardInterrupt:
        print("\nExiting MIDI host.")
        sys.exit(0)





