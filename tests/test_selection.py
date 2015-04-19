"""Tests for the selection component."""

from aalgo import selection
import pytest


def test_for_all_subsets():
    """Test that all the subsets of the correct size are iterated and the function applied properly."""
    test_set = [1, 2, 3, 4]
    correct_subsets = [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]
    i = 0
    for subset in selection.all_subsets_gen(test_set, 3):
        assert correct_subsets[i] == subset
        i += 1

    test_set = [1, 2, 3, 4]
    correct_subsets = [[4], [3], [2], [1]]
    i = 0
    for subset in selection.all_subsets_gen(test_set, 1):
        assert correct_subsets[i] == subset
        i += 1

    # TODO: Figure out how to unit test an exception on a generator with pytest
    #pytest.raises(ValueError, list(selection.all_subsets_gen([1, 2, 3], 6)))


def test_lottoTicketSelection():
    """Test the selection of how many tickets need to be bought to guarantee 1 winning ticket when a psychic has narrowed down to a smaller set which numbers will definitely appear on the fully correct jackpot ticket."""
    assert selection.LottoTicketSet([1, 2, 3, 4, 5], 2, 3, 3) == [[1, 3, 4], [1, 2, 5]]
    assert selection.LottoTicketSet([1, 2, 3, 4, 5], 3, 3, 3) == [[3, 4, 5], [2, 4, 5], [2, 3, 5], [2, 3, 4], [1, 4, 5], [1, 3, 5], [1, 3, 4], [1, 2, 5], [1, 2, 4], [1, 2, 3]]
    pytest.raises(ValueError, selection.LottoTicketSet, [1, 2, 3, 4, 5], 4, 3, 3)
    pytest.raises(ValueError, selection.LottoTicketSet, [1, 2, 3, 4, 5], 3, 3, 4)
    pytest.raises(ValueError, selection.LottoTicketSet, [1, 2, 3, 4, 5], 3, 3, 2)
    assert selection.LottoTicketSet([1, 2, 4, 5], 1, 2, 2) == [[1, 4], [1, 2]]
    assert selection.LottoTicketSet([1, 2, 4], 1, 2, 2) == [[1, 2]]
    assert selection.LottoTicketSet([1, 2, 4, 5], 2, 3, 3) == [[1, 2, 4]]
