class TestClassDemoInstance:

    value = 2

    def test_foo(self) -> None:
        TestClassDemoInstance.value += 1
        self.value = 2
        assert self.value == 2

    def test_bar(self) -> None:
        print(TestClassDemoInstance.value)
        print(self.value)
        # assert self.value == 0
