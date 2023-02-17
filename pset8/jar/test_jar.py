import pytest
from jar import Jar


@pytest.fixture
def jar():
    jar = Jar()
    jar.deposit(11)
    return jar


def test_str_dunder(jar):
    assert str(jar) == "🍪" * 11
    empty_jar = Jar()
    assert str(empty_jar) == ""


def test_withdraw(jar):
    jar.withdraw(1)
    assert jar.size == 10

    jar.withdraw(0)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.withdraw(-10)
    with pytest.raises(ValueError):
        jar.withdraw(11)
    with pytest.raises(ValueError):
        jar.withdraw(11)


def test_deposit(jar):
    jar.deposit(1)
    assert jar.size == 12
    jar.deposit(0)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_getters_and_setters(jar):
    assert jar.size == jar._size
    assert jar.capacity == jar._capacity


def test_constructor():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(11)
    assert jar.capacity == 11
    assert jar.size == 0
