import stdio
import sys


class Rational:
    """
    Represents a rational number.
    """

    def __init__(self, x, y=1):
        """
        Constructs a new rational given its numerator and
        denominator.
        """

        ...
        
    def __add__(self, other):
        """
        Returns the sum of self and other.
        """

        ...
        
    def __sub__(self, other):
        """
        Returns the difference of self and other.
        """

        ...
        
    def __mul__(self, other):
        """
        Returns the product of self and other.
        """

        ...

    def __abs__(self):
        """
        Return the absolute value of self.
        """

        ...

    def __str__(self):
        """
        Returns a string representation of self.
        """

        a, b = self._x, self._y
        if a == 0 or b == 1:
            return str(a)
        if b < 0:
            a *= -1
            b *= -1
        return str(a) + '/' + str(b)

    def _gcd(self, p, q):
        """
        Return the GCD of p and q.
        """

        return p if q == 0 else self._gcd(q, p % q)


# Test client [DO NOT EDIT].
def _main():
    n = int(sys.argv[1])
    total = Rational(0)
    sign = Rational(1)
    for i in range(1, n + 1):
        total += sign * Rational(1, 2 * i - 1)
        sign *= Rational(-1)
    stdio.writeln(4.0 * total._x / total._y)


if __name__ == '__main__':
    _main()
