"""Unit tests for the custom data structures."""

from aalgo import data_structures


def test_next_bit_permutation():
    """Test that the next lexigraphical bit permutation is produced."""
    assert data_structures.next_bit_permutation(7) == 11
    assert data_structures.next_bit_permutation(11) == 13


def test_first_permutation_of_popcount():
    """Test that the first lexigraphical bit permutation is returned."""
    assert data_structures.first_permutation_of_popcount(3) == 7
    assert data_structures.first_permutation_of_popcount(4) == 15


def test_popcount():
    """Unit test for the popcount().  Does it return the correct number of 1's in the given integer."""
    assert data_structures.popcount(0) == 0
    assert data_structures.popcount(1) == 1
    assert data_structures.popcount(4) == 1
    assert data_structures.popcount(66) == 2
    assert data_structures.popcount(63) == 6


def test_binary_representation():
    """Test the binary representation of given numbers."""
    assert data_structures.binary_representation(0) == "0"
    assert data_structures.binary_representation(0, 3) == "000"
    assert data_structures.binary_representation(1) == "1"
    assert data_structures.binary_representation(1, 0) == "1"
    assert data_structures.binary_representation(1, 4) == "0001"
    assert data_structures.binary_representation(2) == "10"
    assert data_structures.binary_representation(3) == "11"
    assert data_structures.binary_representation(47) == "101111"
    assert data_structures.binary_representation(47, 8) == "00101111"


def test_bit_permutation_gen():
    """Test that all the permutations of a given number of 1's of a given length are generated correctly."""
    correct_values = ["00111", "01011", "01101", "01110", "10011", "10101", "10110", "11001", "11010", "11100"]
    i = 0
    for permutation in data_structures.bit_permutation_gen(3, 5):
        assert data_structures.binary_representation(permutation, 5) == correct_values[i]
        i += 1


def test_aalgo_bitarray_right_rotate():
    """Test that the right rotate function works as expected."""
    testarray = data_structures.aalgo_bitarray('1011')
    data_structures.aalgo_bitarray.ror(testarray, 1)
    assert testarray == data_structures.aalgo_bitarray('1101')

    testarray = data_structures.aalgo_bitarray('1011')
    data_structures.aalgo_bitarray.ror(testarray, 2)
    assert testarray == data_structures.aalgo_bitarray('1110')

    testarray = data_structures.aalgo_bitarray('101100')
    data_structures.aalgo_bitarray.ror(testarray, 4)
    assert testarray == data_structures.aalgo_bitarray('110010')

    testarray = data_structures.aalgo_bitarray('0')
    data_structures.aalgo_bitarray.ror(testarray, 1)
    assert testarray == data_structures.aalgo_bitarray('0')

    testarray = data_structures.aalgo_bitarray('0')
    data_structures.aalgo_bitarray.ror(testarray, 5)
    assert testarray == data_structures.aalgo_bitarray('0')

    testarray = data_structures.aalgo_bitarray('1')
    data_structures.aalgo_bitarray.ror(testarray, 1)
    assert testarray == data_structures.aalgo_bitarray('1')

    testarray = data_structures.aalgo_bitarray('1')
    data_structures.aalgo_bitarray.ror(testarray, 5)
    assert testarray == data_structures.aalgo_bitarray('1')
