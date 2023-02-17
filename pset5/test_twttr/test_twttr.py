from twttr import shorten
from typing import NamedTuple

def test_with_numbers():
    assert shorten("foobar1") == "fbr1"


def test_lowercase():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("aeiou") == ""


def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("AEIOU") == ""


def test_novowels():
    assert shorten("tst n vwls") == "tst n vwls"

def test_punctuation():
    assert shorten("foobar!") == "fbr!"
    assert shorten("foo.bar") == "f.br"
