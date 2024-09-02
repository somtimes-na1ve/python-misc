class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        self.value = 1

    def business_logic(self):
        self.value += 1
        print(self.value)


if __name__ == '__main__':
    singleton1 = Singleton()
    singleton2 = Singleton()

    assert singleton1 is singleton2
    assert id(singleton1) == id(singleton2)

    singleton1.business_logic()
    singleton2.value = -1

    singleton2.business_logic()
