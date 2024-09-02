def func(x: int) -> int:
    return x + 1


def test_success() -> None:
    assert func(3) == 4


def test_not_equal() -> None:
    assert func(3) != 5
