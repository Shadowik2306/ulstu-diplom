
class ComputerKeyboard:
    subscribers = set()

    @classmethod
    def add_subscriber(cls, subscriber):
        cls.subscribers.add(subscriber)

    @classmethod
    def remove_subscriber(cls, subscriber):
        cls.subscribers.remove(subscriber)

    @classmethod
    def event(cls, num):
        for subscriber in cls.subscribers:
            subscriber.subscribe_action(num)
