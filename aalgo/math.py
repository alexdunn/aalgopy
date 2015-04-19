"""Common math functions."""

from operator import mul
from fractions import Fraction
from functools import reduce


# If you want to do this in production code, use sympy.binomial, which is exponentially faster
def number_combinations(n, k):
    """Return the value of the binomial n choose k."""
    # n choose k = (n^k)/(k!)
    fractions = (Fraction(n - i, i + 1) for i in range(k))
    return int(reduce(mul, fractions, 1))


def rank_combination(combination, valid_numbers=None):
    """Take a list of numbers that is a combination and return that combination's rank if it were in an array of ordered combinations.  Rank position starts at 0.  This is useful for mapping combinations to a bit array.  This algorithm assumes that the numbers your combination have to choose from are consecutive.  That is, if you provide the combination {1, 2, 6} then this algorithm assumes that this combination is from a 7 choose 3 combination set where 0, 1, 2, 3, 4, 5, 6 are the available numbers.  If that is not the case, then pass the value n = number of numbers your combination set has to choose from."""
    if valid_numbers is not None:
        if len(valid_numbers) < len(combination):
            raise ValueError("valid_numbers can not be smaller than the given combination.  That makes no sense.  There must be enough numbers to choose to create your combination.")

    # smallest to highest
    combination = sorted(combination)  # You could use your C++ insertion sort here
    if valid_numbers is not None:
        valid_numbers = sorted(valid_numbers)

    i = 1
    rank = 0
    for c in combination:
        if valid_numbers is not None:  # Replace c with the number it would be if it were in a consecutive combination set 0...c
            c = valid_numbers.index(c)
        rank += number_combinations(c, i)
        i += 1
    return rank


def unrank_combination(n, j):
    """Return the list of ints that is at position j of the ordered n-combination."""
    result = []
    m = n
    while j > 0:  # j will be exhausted as the sum of combinations found will end up equally j
        i = m - 1
        val = 0
        while True:
            test_val = number_combinations(i, m)
            if test_val <= j:
                val = test_val
            else:
                break
            i += 1
        result.insert(0, i - 1)
        j = j - val
        m = m - 1

    # The remainder
    while len(result) < n:
        i = n - len(result)
        result.insert(0, i - 1)

    return result
