# -*- coding: utf-8 -*-

import pytest

TEST_STRINGS = [
    ('(', 1),
    ('(()', 1),
    ('()(', 1),
    ('()', 0),
    ('(())', 0),
    ('((()))', 0),
    (')', -1),
    ('))(', -1),
    ('())', -1)
]


@pytest.mark.parametrize('string, result', TEST_STRINGS)
def test_parenthetics(parentheses_string, result):
    """Test for valid parenthetic results."""
    from proper_parenthetics import parenthetics
    assert parenthetics(parentheses_string) == result
