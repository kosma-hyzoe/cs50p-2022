from plates import is_valid


def test_order():
    assert not is_valid("50666")
    assert is_valid("foo666")
    assert not is_valid("fo6oo")
    assert not is_valid("3bar")
    assert not is_valid("33bar")


def test_length():
    assert not is_valid("f")
    assert not is_valid("1")
    assert is_valid("fo2")
    assert is_valid("foo3")
    assert is_valid("foo4")
    assert is_valid("foo50")
    assert is_valid("foo555")
    assert not is_valid("foo5550")


def test_punctuation():
    assert not is_valid("foo.ba")
    assert not is_valid("foo_ba")
    assert not is_valid("foo,b1")


def test_zeroes():
    assert not is_valid("cs05")
    assert not is_valid("cd0005")
    assert is_valid("cs50")
    assert not is_valid("foobar0")