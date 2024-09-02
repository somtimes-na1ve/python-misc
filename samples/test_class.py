class TestClass:

    def test_foo(self) -> None:
        x = "this"
        assert "h" in x

    def test_bar(self) -> None:
        x = "hello"
        assert hasattr(x, "find")
