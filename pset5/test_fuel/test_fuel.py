import pytest

from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("foobar")
    assert convert("4/4") == 100
    assert convert("0/1") == 0


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(-1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"