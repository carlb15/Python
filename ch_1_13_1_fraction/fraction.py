"""Fraction class."""


def gcd(m, n):
    """Compute the GCD of m & n."""
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn

    return n


class Fraction:
    """Fraction class."""

    def __init__(self, top, bottom):
        """Initialization of the numerator and denominator."""
        if isinstance(top, int) and isinstance(bottom, int):
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common
        else:
            raise ValueError("Fraction must have an integer numerator and \
                              denominator.")

    def __str__(self):
        """String overloading for printing."""
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        """Repr overloading."""
        return "%s(%r, %r)" % (self.__class__, self.num, self.den)

    def show(self):
        """Show method for printing."""
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        """Overloaded add method for adding fractions."""
        newnum = self.num * otherfraction.den + self.den * otherfraction.num

        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __radd__(self, other):
        """Overloaded reverse add 1 + X."""
        if not isinstance(other, int):
            raise ValueError("Fractions can only be added with integers.")

        otherNum = other * self.den

        newnum = self.num + otherNum
        common = gcd(newnum, self.den)

        return Fraction(newnum // common, self.den // common)

    def __iadd__(self, other):
        """Overloading iadd for sum()."""
        otherNum = other * self.den

        newnum = self.num + otherNum
        common = gcd(newnum, self.den)

        return Fraction(newnum // common, self.den // common)

    def __eq__(self, other):
        """Overloading equal to for comparing fractions."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        """Overloading multiplication."""
        num = self.num * other.num
        den = self.den * other.den

        common = gcd(num, den)

        return Fraction(num // common, den // common)

    def __truediv__(self, other):
        """Overloading true division."""
        num = self.num * other.den
        den = self.den * other.num

        common = gcd(num, den)

        return Fraction(num // common, den // common)

    def __sub__(self, other):
        """Overloading subtraction."""
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den

        common = gcd(num, den)

        return Fraction(num // common, den // common)

    def __gt__(self, other):
        """Overloading greater than."""
        return (self.num * other.den) > (other.num * self.den)

    def __ge__(self, other):
        """Overloading greater than or equal to."""
        return (self.num * other.den) >= (other.num * self.den)

    def __lt__(self, other):
        """Overloading less than."""
        return (self.num * other.den) < (other.num * self.den)

    def __le__(self, other):
        """Overloading less than or equal to."""
        return (self.num * other.den) <= (other.num * self.den)

    def __ne__(self, other):
        """Overloading not equal to."""
        return (self.num != other.num) or (self.den != other.den)

    def getNum(self):
        """Get the numerator of the fraction."""
        return self.num

    def getDen(self):
        """Get the denominator of the fraction."""
        return self.den


x = Fraction(1, 3)
y = Fraction(2, 3)

print(x + y)
print(x == y)
print(x * y)
print(x / y)
print(x - y)
print(y - x)
print(x > y)
print(x < y)
print(x.getNum())
print(x.getDen())
print(y.getNum())
print(y.getDen())
print(x >= y)
print(y <= x)
print(x != y)
print(1 + x)
x += 1
print(x)
print(sum([x, y]))
print(repr(x))
