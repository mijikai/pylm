from hamcrest import *
import collections

from pylm import m

def test_when_piped_returns_generator():
    assert_that('' | m, instance_of(collections.Iterable))

def test_generator_yields_lines_from_the_text():
    a = 'abc\nbd\n\nccc' | m
    assert_that(a, contains('abc', 'bd', '', 'ccc'))
