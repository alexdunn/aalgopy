"""Additional data structures."""
from bitarray import bitarray


def next_bit_permutation(x):
    # TODO: When the bitarray package supports shift operators, use bitarrays rather than ints
    """Given an int x, return the next lexographical bit permutation of it.

    Taken from http://graphics.stanford.edu/~seander/bithacks.html
    Examples from http://alexbowe.com/popcount-permutations/
    """
    t = (x | (x - 1)) + 1
    # This right-propogates the right-most bit:
    # Example where x = 01110
    # 01110 | 01101 = 01111
    # 01111 + 1 = 10000
    w = t | ((((t & -t) // (x & -x)) >> 1) - 1)
    # (t & -t):
    # 10000 & -10000 = 10000 & ~01111 = 10000 & 10000 = 10000
    # (x & -x) = x & ~(x - 1) isolates the rightmost bit:
    # 01110 & ~01101 = 01110 & 10010 = 00010
    # Now divide:
    # 10000 / 00010 = 01000
    # Right shift by 1:
    # 00100
    # Subtract one:
    # 00011
    # t | (everything else):
    # 10000 | 00011 = 10011
    return w


def first_permutation_of_popcount(c):
    # TODO: When the bitarray package supports shift operators, use bitarrays rather than ints
    """Return the number that is the first number of lexigraphical pop count c.

    From http://alexbowe.com/popcount-permutations/
    """
    # Example c = 3
    # 1 << 3 = 1000
    # 1000 - 1 = 0111
    return (1 << c) - 1


def binary_representation(x, padding=0):
    """Return the binary representation of the given int x as a string. If an intenger padding is provided, then it will be ensured that all returned strings have a length of at least that number by adding 0's onto the beginning of the string."""
    string_rep = ""
    if not x:
        string_rep = "0"
    while x:
        if x & 1:
            string_rep = "1" + string_rep
        else:
            string_rep = "0" + string_rep
        x = x >> 1

    while padding > len(string_rep):
        string_rep = "0" + string_rep

    return string_rep


def bit_permutation_gen(p, length):
    """A generator of all the bit permutations of the given length with the given popcount p.

    From http://alexbowe.com/popcount-permutations/
    """
    current_permutation = first_permutation = first_permutation_of_popcount(p)
    block_mask = first_permutation_of_popcount(length)

    while current_permutation >= first_permutation:
        yield current_permutation
        current_permutation = next_bit_permutation(current_permutation) & block_mask


def popcount(x):
    """Return the number of bits in the given x that are set to 1."""
    count = 0
    # Convince yourself:
    # 1101 - 1 = 1100
    # count = 1, x = 1100.  1100 - 1 = 1011
    # count = 2, x = 1000.  1000 - 1 = 0111
    # count = 3, x = 0000.
    while x:
        x &= x - 1
        count += 1
    return count


class aalgo_bitarray(bitarray):

    """A subclass of bitarray that implements right rotate."""

    def ror(self, count=1):
        """Right rotate the bits in the array.  A right rotate is the same as a right shift where if the last bit is a 1 then it is appended to the front of the resulting array."""
        # What value to append to the beginning of the new bitarray?
        for _ in range(count):
            last_value = self.pop()
            self.insert(0, last_value)
