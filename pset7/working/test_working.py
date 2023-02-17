import pytest
from working import convert


def test_impossible_hours():
    with pytest.raises(ValueError):
        convert("19 PM to 11 AM")
    with pytest.raises(ValueError):
        convert("29 AM to 3 PM")


def test_valid_hours():
    assert convert("3 PM to 1 AM") == "15:00 to 01:00"


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("foo PM to bar AM")
    with pytest.raises(ValueError):
        convert("3 PM 2 AM")
