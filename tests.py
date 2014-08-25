from hamcrest import *
import collections

from pylm import m

def test_when_piped_returns_generator():
    assert_that('' | m, instance_of(collections.Iterable))
