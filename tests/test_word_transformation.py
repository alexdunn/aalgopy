"""Test the fizzbuzz functions."""

from aalgo.word_transformation import transform_word


def test_word_transformation():
    assert transform_word("cat", "dog") == ['cat', 'cag', 'cog', 'dog']
    assert transform_word("cat", "bed") == ['cat', 'bat', 'bad', 'bed']
    assert transform_word("here", "cant") == ['here', 'cere', 'care', 'cane', 'cant']
    assert transform_word("gym", "cup") == ['gym', 'gum', 'cum', 'cup']
    assert transform_word("tart", "aero") == ['tart', 'cart', 'caro', 'cero', 'aero']
    assert 1 == 1
