from numb3rs import validate


def test_numbers_separated_by_dots_properly():
    assert not validate("666.102.22.134")
    assert validate("1.1.1.1")
    assert not validate("123.555.442.355")


def test_other_cases():
    assert not validate("..0.0.0.0")
    assert not validate("0.foo.0.bar")
    assert not validate("0..0.1.2")
    assert not validate("foobar")
    assert not validate("0.0.1.0..")


