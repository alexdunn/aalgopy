"""Arithmetic problems."""


def multiplication_game(goal):
    """With perfect play, return whether player 1 or player 2 would win in a game where the first player chooses a number 2-9 inclusive and multiplies with a number chosen by the second player going back and forth until the winner is the first player to reach a result greater or equal to the given integer `goal`.

    This is UVa Programming Challenges Online Judge 847.  This is from chapter 2 of The Algorithm Design Manual.
    """
    # Player 1 must win for value 1
    if goal == 1:
        return True

    # Assume that player 1 must win under optimal play.  This means player 1 should always choose 9 (make it take as few plays as possible) and player 2 should always choose 2 (make it take as many plays as possible).  If player 1 wins under this assumption, there is nothing player 2 can do to prevent this win because player 2 is already choosing the lowest numbers possible.  Under this assumption, any solution where player 2 wins is the optimal solution only if it has length less than the first solution where player 1 wins.  If it's the same length or shorter, player 1 could simply make some choices less than 9 to deny player 2 her/his win.
    current_value = 1
    first_players_turn = True  # True for player 1 and False for player 2
    while current_value < goal:
        if first_players_turn:
            current_value *= 9
            first_players_turn = False
        else:
            current_value *= 2
            first_players_turn = True

    # If the assumption that player 1 must win finds player 2 winning first, then player 2 is going to win under optimal play.
    if first_players_turn:  # player 2 winning will set player 1 as the current player
        return False
    else:
        return True
