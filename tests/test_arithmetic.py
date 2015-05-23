"""Test the arithmetic functions."""

from aalgo.arithmetic import multiplication_game


def test_multiplication_game():
    """Test if the correct winner is found."""
    assert multiplication_game(1) == True
    assert multiplication_game(162) == True
    assert multiplication_game(17) == False
    assert multiplication_game(34012226) == True
