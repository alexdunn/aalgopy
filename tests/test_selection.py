"""Tests for the selection component."""

from aalgo.selection import all_subsets_gen, lotto_ticket_set, equalize_money
import pytest


def test_for_all_subsets():
    """Test that all the subsets of the correct size are iterated and the function applied properly."""
    test_set = [1, 2, 3, 4]
    correct_subsets = [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]
    i = 0
    for subset in all_subsets_gen(test_set, 3):
        assert correct_subsets[i] == subset
        i += 1

    test_set = [1, 2, 3, 4]
    correct_subsets = [[4], [3], [2], [1]]
    i = 0
    for subset in all_subsets_gen(test_set, 1):
        assert correct_subsets[i] == subset
        i += 1


def test_all_subsets_gen_exception1():
    """Test the generator's first assertion."""
    with pytest.raises(ValueError):
        list(all_subsets_gen([1, 2, 3], 6))


def test_all_subsets_gen_exception2():
    """Test the second assertion."""
    with pytest.raises(ValueError):
        list(all_subsets_gen([1, 2, 3], 0))


def test_lotto_ticket_set():
    """Test the selection of how many tickets need to be bought to guarantee 1 winning ticket when a psychic has narrowed down to a smaller set which numbers will definitely appear on the fully correct jackpot ticket."""
    assert lotto_ticket_set([1, 2, 3, 4, 5], 2, 3, 3) == [[1, 3, 4], [1, 2, 5]]
    assert lotto_ticket_set([1, 2, 3, 4, 5], 3, 3, 3) == [[3, 4, 5], [2, 4, 5], [2, 3, 5], [2, 3, 4], [1, 4, 5], [1, 3, 5], [1, 3, 4], [1, 2, 5], [1, 2, 4], [1, 2, 3]]
    pytest.raises(ValueError, lotto_ticket_set, [1, 2, 3, 4, 5], 4, 3, 3)
    pytest.raises(ValueError, lotto_ticket_set, [1, 2, 3, 4, 5], 3, 3, 4)
    pytest.raises(ValueError, lotto_ticket_set, [1, 2, 3, 4, 5], 3, 3, 2)
    assert lotto_ticket_set([1, 2, 4, 5], 1, 2, 2) == [[1, 4], [1, 2]]
    assert lotto_ticket_set([1, 2, 4], 1, 2, 2) == [[1, 2]]
    assert lotto_ticket_set([1, 2, 4, 5], 2, 3, 3) == [[1, 2, 4]]


def test_equalize_money():
    """Test the minimum amount of money that must exchange hands."""
    assert equalize_money([10.00, 20.00, 30.00]) == 10.00
    assert equalize_money([15.00, 15.01, 3.00, 3.01]) == 11.99
