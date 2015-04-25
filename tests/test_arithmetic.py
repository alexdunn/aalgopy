"""Test the arithmetic functions."""

from aalgo import arithmetic


def test_multiplication_game():
    """Test if the correct winner is found."""
    assert arithmetic.multiplication_game(1) == True
    assert arithmetic.multiplication_game(162) == True
    assert arithmetic.multiplication_game(17) == False
    assert arithmetic.multiplication_game(34012226) == True

    expected = True
    input_value = 0
    with open("/Users/admin/Desktop/outputs.txt") as file:
        for line in file:
            input_value += 1
            if line.replace('\n', '') == "Stan wins.":
                print("Stan expected to win")
                expected = True
            else:
                print("Ollie expected to win")
                expected = False
            print("input_value = {}" .format(str(input_value)))
            assert arithmetic.multiplication_game(input_value) == expected
