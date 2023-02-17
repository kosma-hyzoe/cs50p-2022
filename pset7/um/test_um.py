from um import count


def test_um_as_as_substrings():
    assert not count("umbro")
    assert not count("bum")
    assert not count(" umbro")
    assert not count("bum!")


def test_several_ums():
    assert count("um, bum, um, um?") == 3
    assert count("mum, um. um! um, um") == 4
    assert count("bum um, um... mum") == 2



def test_other_variants():
    assert not count("1")
    assert count("uM UM Um") == 3
    assert count("um, UM um?") == 3
