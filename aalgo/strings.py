"""String exercises."""


def remove_duplicate_characters(string):
    """Given a string, return that string where only the first occurence of each character is preserved."""
    encountered_chars = []
    result = string
    i = 0
    for char in string:
        if char in encountered_chars:
            result = result[:i] + result[i + 1:]
            i -= 1
        else:
            encountered_chars.append(char)
        i += 1
    return result
