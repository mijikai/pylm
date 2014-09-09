from hamcrest import *
import collections
import pytest

from pylm import m

def test_when_piped_returns_generator():
    assert_that('' | m, instance_of(collections.Iterable))

def test_generator_yields_lines_from_the_text():
    a = 'abc\nbd\n\nccc' | m
    assert_that(a, contains('abc', 'bd', '', 'ccc'))

def test_retrieve_a_character_with_index_for_all_lines():
    text = 'ajkw\nbfkad\noak#2'
    assert_that(text | m[0], contains('a', 'b', 'o'))
    assert_that(text | m[3], contains('w', 'a', '#'))

@pytest.skip
def test_append_characters_to_each_other():
    assert_that('abc\nxyz' | m[0] + m[-1], contains('ac', 'xz'))
    assert_that('abc\ndef\nghi' | m[-1] + m[1], contains('cb', 'fe', 'ih'))

@pytest.skip
def test_select_range_of_characters_from_line():
    assert_that('thequickbrownfox\njumpsoverthelazy' | m[2:7],
            contains('equic', 'mpsov'))

@pytest.skip
def test_select_range_of_characters_from_line_with_step():
    assert_that('thequickbrownfox\njumpsoverthelazy' | m[2:7:2],
            contains('euc', 'msv'))
