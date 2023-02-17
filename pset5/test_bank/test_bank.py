from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello world") == 0
    assert value("hello Mark") == 0


def test_h():
    assert value("h") == 20
    assert value("HI!") == 20
    assert value("oh hi mark") == 100


def test_else():
    assert value("foobar") == 100
    assert value("oh hi mark") == 100
    assert value("3") == 100