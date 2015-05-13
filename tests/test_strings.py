"""Test the string exercises."""

from aalgo import strings


def test_deduplication():
    """Test that string character deduplication works."""
    assert strings.remove_duplicate_characters('abc') == 'abc'
    assert strings.remove_duplicate_characters('abcc') == 'abc'
    assert strings.remove_duplicate_characters('abca') == 'abc'
    assert strings.remove_duplicate_characters('ccabca') == 'cab'
    assert strings.remove_duplicate_characters('Can androids with wings eat chicken wings?') == 'Can droiswthgeck?'
