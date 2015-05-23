"""Test the string exercises."""

from aalgo.strings import remove_duplicate_characters


def test_deduplication():
    """Test that string character deduplication works."""
    assert remove_duplicate_characters('abc') == 'abc'
    assert remove_duplicate_characters('abcc') == 'abc'
    assert remove_duplicate_characters('abca') == 'abc'
    assert remove_duplicate_characters('ccabca') == 'cab'
    assert remove_duplicate_characters('Can androids with wings eat chicken wings?') == 'Can droiswthgeck?'
