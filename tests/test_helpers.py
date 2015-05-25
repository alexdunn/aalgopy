"""Helper methods for testing."""


def number_close_to(number, target, delta):
    """Assert that the given number is within target +/- delta."""
    assert number < target + delta
    assert number > target - delta
