
class ComputerKeyboard:
    subscribers = set()

    @classmethod
    def add_subscriber(cls, subscriber):
        cls.subscribers.add(subscriber)

    @classmethod
    def remove_subscriber(cls, subscriber):
        cls.subscribers.remove(subscriber)

    @classmethod
    def play_event(cls, num):
        for subscriber in cls.subscribers:
            subscriber.subscribe_play_action(num)

    @classmethod
    def stop_event(cls, num):
        for subscriber in cls.subscribers:
            subscriber.subscribe_stop_action(num)
