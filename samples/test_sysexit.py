import pytest


def foo() -> None:
    raise SystemExit(-1)


def bar() -> None:
    raise ExceptionGroup(
        "Exception Group Message",
        [
            RuntimeError(),
        ])


def test_foo() -> None:
    with pytest.raises(SystemExit) as exec_info:
        foo()


def test_bar() -> None:
    with pytest.raises(ExceptionGroup) as exec_info:
        bar()

    # assert exception group message
    assert exec_info.value.args[0] == "Exception Group Message"

    assert exec_info.group_contains(RuntimeError)
    assert not exec_info.group_contains(ValueError)