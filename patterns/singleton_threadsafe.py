from threading import Lock, Thread

from pytest_cov.plugin import validate_fail_under


class SingletonMeta(type):

    _instances = {}

    _mutex: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._mutex:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

            return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        print(self.value)


def do_something(value: str) -> None:
    obj = Singleton(value)
    obj.some_business_logic()


if __name__ == '__main__':
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=do_something, args=("FOO",))
    process2 = Thread(target=do_something, args=("BAR",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
