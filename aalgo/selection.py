"""The selection module deals with making subset selections from a given set."""

from bitarray import bitarray
from aalgo.math import number_combinations, rank_combination
from aalgo import data_structures


def all_subsets_gen(myset, size):
    """A generator for all possible subsets size n of the set myset.  This is run in constant memory."""
    if size > len(myset):
        raise ValueError("There does not exist a subset of myset that is larger than myset.")

    if size <= 0:
        raise ValueError("There is only one set of size 0, the empty set.  There are no sets of size less than 0.")

    for i in data_structures.bit_permutation_gen(size, len(myset)):
        # TODO: Converting to a string here will be unecessary when the bitarray library supports shift operators
        binary_str = data_structures.binary_representation(i, len(myset))
        subset = []
        i = 0
        for bit in binary_str:
            if bit is '1':
                subset.append(myset[i])
            i += 1
        yield subset


def lotto_ticket_set(numbers, l, k, j):
    """Heuristically determine the lottery tickets to buy such that at least one has a winning number on it.  numbers is a list of the lottery numbers (The potentially winning lottery numbers), k is the number of slots on each ticket, j is how many of the n numbers are guaranteed to be on the winning ticket, and l is the number of matching numbers necessary to win a prize.  Assume that the n potentially winning lottery numbers are consecutive integers 1...n.  This is from Chapter 1 of The Algorithm Design Manual."""
    # When writing numbers on a ticket, you only need to have l numbers chosen correctly to win a prise.  Not all of them need to be right.
    # Each valid number for the lottery 1...n may be chosen only once on a given ticket.  Order of choice does not matter.
    # We want to select the number of tickets necessary to guarantee one win with l numbers.

    if j < l:
        raise ValueError("j must not be less than l.  If it is, then we can not guarantee any winnings.  In the set of n numbers we must have at least l numbers that are guaranteed to count toward a win.")
    # j is the number of numbers that are guaranteed to be on the one single jackpot winning ticket where all numbers are correct.  l is the number of slots that must be right to win any prize, not necessarily the jackpot.

    if j > k:
        raise ValueError("j must be less than or equal to k.  It's not possible for the psychic to be sure that more numbers than the size of the ticket will appear on the ticket.")

    # Initialize the n choose l sized bit vector V to all false
    size = number_combinations(len(numbers), l)
    bit_array = bitarray(size)
    bit_array.setall(False)

    all_tickets = list(all_subsets_gen(numbers, k))

    # If the number of required correct numbers to get a cash prize is equal to the size of a ticket, then you're going to have to buy every possible ticket to guarantee a win because there is only one ticket with any kind of prize at all.
    if l == k:
        return list(all_subsets_gen(numbers, k))

    # TODO: Use simulated annealing rather than brute force to select tickets
    for i in range(size):
        for tickets_subset in all_subsets_gen(all_tickets, i + 1):
            for ticket in tickets_subset:
                # Set the bit_array to True at each position that represents an l-subset of the currently chosen ticket T
                for potentially_winning_set in all_subsets_gen(ticket, l):
                    bit_array[rank_combination(potentially_winning_set, numbers)] = True
            # The chosen tickets in tickets_subset do not cover all l-subsets, but do they cover enough such that if any ticket won, it would contain at least one of these l-subsets?
            # TODO: I shouldn't have to iterate over all tickets here.  What is a better algorithm for answering the question: Does there exist any ticket that does not share an l-subset wtih my tickets?
            satisfies = False
            for ticket in all_subsets_gen(numbers, k):  # This is the same as `for tickets in all_tickets` but I'm choosing to use the generator so that when I refactor this so that I no longer have to store a list of all the tickets, this generator can remain since it uses constant memory.
                for l_subset in all_subsets_gen(ticket, l):
                    if bit_array[rank_combination(l_subset, numbers)]:
                        satisfies = True
                        break
                    else:
                        satisfies = False
                if not satisfies:  # A ticket that does not share an l-subset with this tickets_subset was found, so this is not a winning tickets_subset
                    bit_array.setall(False)
                    break
            if satisfies:
                return tickets_subset


def equalize_money(money_spent):
    """Return the minimum amount of money that must change hands so that everyone spent the same amount of money, within one cent.  The given list money_spent is a list of how much money each person spent.

    From http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1078.  UVa Online Judge Problem 10137.
    """
    exchange = 0
    total = 0
    for money in money_spent:
        total += money

    # TODO: This is a hack.  How do I actually deal with decimal rounding properly?
    average = round(round(total / len(money_spent), 3), 2)

    for money in money_spent:
        if money > average:
            exchange += money - average

    return exchange
