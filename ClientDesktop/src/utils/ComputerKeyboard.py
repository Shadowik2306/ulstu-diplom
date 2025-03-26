
num_to_notes = {
    65: 60,
    83: 62,
    68: 64,
    70: 65,
    71: 67,
    74: 71,
    75: 72,
    76: 74
}


class ComputerKeyboard:
    def __init__(self):
        self.subscribers = set()

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def play_event(self, num):
        if num not in num_to_notes:
            return

        for subscriber in self.subscribers:
            subscriber.note_on(num_to_notes[num])

    def stop_event(self, num):
        if num not in num_to_notes:
            return
        for subscriber in self.subscribers:
            subscriber.note_off(num_to_notes[num])


def computer_keyboard_singleton_factory(_object=ComputerKeyboard()):
    return _object
