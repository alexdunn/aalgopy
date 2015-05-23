"""Unit tests for the custom data structures."""

from aalgo.data_structures import next_bit_permutation, first_permutation_of_popcount, popcount, binary_representation, bit_permutation_gen, aalgo_bitarray


def test_next_bit_permutation():
    """Test that the next lexigraphical bit permutation is produced."""
    assert next_bit_permutation(7) == 11
    assert next_bit_permutation(11) == 13


def test_first_permutation_of_popcount():
    """Test that the first lexigraphical bit permutation is returned."""
    assert first_permutation_of_popcount(3) == 7
    assert first_permutation_of_popcount(4) == 15


def test_popcount():
    """Unit test for the popcount().  Does it return the correct number of 1's in the given integer."""
    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(4) == 1
    assert popcount(66) == 2
    assert popcount(63) == 6


def test_binary_representation():
    """Test the binary representation of given numbers."""
    assert binary_representation(0) == "0"
    assert binary_representation(0, 3) == "000"
    assert binary_representation(1) == "1"
    assert binary_representation(1, 0) == "1"
    assert binary_representation(1, 4) == "0001"
    assert binary_representation(2) == "10"
    assert binary_representation(3) == "11"
    assert binary_representation(47) == "101111"
    assert binary_representation(47, 8) == "00101111"


def test_bit_permutation_gen():
    """Test that all the permutations of a given number of 1's of a given length are generated correctly."""
    correct_values = ["00111", "01011", "01101", "01110", "10011", "10101", "10110", "11001", "11010", "11100"]
    i = 0
    for permutation in bit_permutation_gen(3, 5):
        assert binary_representation(permutation, 5) == correct_values[i]
        i += 1


def test_aalgo_bitarray_right_rotate():
    """Test that the right rotate function works as expected."""
    testarray = aalgo_bitarray('1011')
    aalgo_bitarray.ror(testarray, 1)
    assert testarray == aalgo_bitarray('1101')

    testarray = aalgo_bitarray('1011')
    aalgo_bitarray.ror(testarray, 2)
    assert testarray == aalgo_bitarray('1110')

    testarray = aalgo_bitarray('101100')
    aalgo_bitarray.ror(testarray, 4)
    assert testarray == aalgo_bitarray('110010')

    testarray = aalgo_bitarray('0')
    aalgo_bitarray.ror(testarray, 1)
    assert testarray == aalgo_bitarray('0')

    testarray = aalgo_bitarray('0')
    aalgo_bitarray.ror(testarray, 5)
    assert testarray == aalgo_bitarray('0')

    testarray = aalgo_bitarray('1')
    aalgo_bitarray.ror(testarray, 1)
    assert testarray == aalgo_bitarray('1')

    testarray = aalgo_bitarray('1')
    aalgo_bitarray.ror(testarray, 5)
    assert testarray == aalgo_bitarray('1')
