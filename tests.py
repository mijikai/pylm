import collections

from pylm import m

def test_when_piped_returns_generator():
    assert isinstance('' | m, collections.Iterable)
