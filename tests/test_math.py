"""Test the math functions."""

from aalgo.math import number_combinations, rank_combination, unrank_combination
import pytest


def test_number_combinations():
    """Test if the correct number of choices are made for a given binomial combination."""
    assert number_combinations(5, 3) == 10
    assert number_combinations(961, 12) == 1208919326329181985658271600
    assert number_combinations(0, 0) == 1
    assert number_combinations(1, 0) == 1
    assert number_combinations(0, 1) == 0


def test_rank_combination():
    """Test that, given a combination, the correct position in its combination ordering is given."""
    assert rank_combination([1]) == 1
    assert rank_combination([1, 0]) == 0
    assert rank_combination([0, 1]) == 0
    assert rank_combination([0, 2]) == 1
    assert rank_combination([1, 2]) == 2
    assert rank_combination([0, 3]) == 3
    assert rank_combination([1, 3]) == 4
    assert rank_combination([2, 3]) == 5
    assert rank_combination([8, 6, 3, 1, 0]) == 72
    assert rank_combination([1, 6], [1, 6]) == 0
    assert rank_combination([1, 2], [1, 2, 6]) == 0
    assert rank_combination([1, 6], [1, 2, 6]) == 1
    pytest.raises(ValueError, rank_combination, [1, 2], [1])
    pytest.raises(ValueError, rank_combination, [1, 2], [1, 3])


def test_unrank_combination():
    """Test that, given a position in an n-combination, we get back the correction combination at that position."""
    assert unrank_combination(5, 72) == [0, 1, 3, 6, 8]
    assert unrank_combination(1, 1) == [1]
    assert unrank_combination(2, 0) == [0, 1]
    assert unrank_combination(2, 1) == [0, 2]
    assert unrank_combination(2, 2) == [1, 2]
    assert unrank_combination(2, 3) == [0, 3]
    assert unrank_combination(2, 4) == [1, 3]
    assert unrank_combination(2, 5) == [2, 3]
