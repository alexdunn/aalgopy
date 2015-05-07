"""Test the arithmetic functions."""

from aalgo import arithmetic


def test_multiplication_game():
    """Test if the correct winner is found."""
    assert arithmetic.multiplication_game(1) == True
    assert arithmetic.multiplication_game(162) == True
    assert arithmetic.multiplication_game(17) == False
    assert arithmetic.multiplication_game(34012226) == True

