class Target:

    def request(self) -> str:
        return "Target: default target's behavior."


class Adaptee:

    def special_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adaptor(Target, Adaptee):

    def request(self) -> str:
        return f"Adaptor :: (TRANSLATED) {self.special_request()[::1]}"


def client_code(target_obj: "Target") -> None:
    print(target_obj.request(), end="")


if __name__ == '__main__':
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.special_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adaptor = Adaptor()
    client_code(adaptor)
