"""Super simple problems."""


def fizz_buzz():
    """Print the numbers 1 to 100 but print "Fizz" for multiples of three and "Buzz" for multiples of 5 and "FizzBuzz" for multiples of both 3 and 5.  This is from http://c2.com/cgi/wiki?FizzBuzzTest."""
    result = []
    for i in range(1, 101):
        three_multiple = False
        if i % 3 == 0:
            three_multiple = True
        if i % 5 == 0:
            if three_multiple:
                result.append('FizzBuzz')
            else:
                result.append('Buzz')
        elif three_multiple:
            result.append('Fizz')
        else:
            result.append(str(i))
    return result
