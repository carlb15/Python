def gcd(m,n):
  while m % n != 0:
    oldm = m
    oldn = n

    m = oldn
    n = oldm % oldn
  return n

class Fraction:
  def __init__(self, top, bottom):
    if isinstance(top, int) and isinstance(bottom, int):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common
    else:
        raise ValueError("Fraction must have an integer numerator and denominator.")

  def __str__(self):
    return str(self.num)+"/"+str(self.den)

  def show(self):
    print(self.num,"/",self.den)

  def __add__(self,otherfraction):
    newnum = self.num * otherfraction.den + \
             self.den * otherfraction.num

    newden = self.den * otherfraction.den
    common = gcd(newnum, newden)

    return Fraction(newnum//common,newden//common)

  def __radd__(self, other):
      otherNum = other * self.den

      newnum = self.num + otherNum
      common = gcd(newnum, self.den)

      return Fraction(newnum // common, self.den // common)

  def __iadd__(self, other):
      otherNum = other * self.den

      newnum = self.num + otherNum
      common = gcd(newnum, self.den)

      return Fraction(newnum // common, self.den // common)

  def __eq__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den

    return firstnum == secondnum

  def __mul__(self, other):
    num = self.num * other.num
    den = self.den * other.den

    common = gcd(num, den)

    return Fraction(num // common, den // common)

  def __truediv__(self, other):
    num = self.num * other.den
    den = self.den * other.num

    common = gcd(num, den)

    return Fraction(num // common, den // common)

  def __sub__(self, other):
    num = self.num * other.den - \
          other.num * self.den

    den = self.den * other.den

    common = gcd (num, den)

    return Fraction(num // common, den // common)

  def __gt__(self, other):
    return (self.num * other.den) > (other.num * self.den)

  def __ge__(self, other):
    return (self.num * other.den) >= (other.num * self.den)

  def __lt__(self, other):
    return (self.num * other.den) < (other.num * self.den)

  def __le__(self, other):
    return (self.num * other.den) <= (other.num * self.den)

  def __ne__(self, other):
    return (self.num != other.num) or (self.den != other.den)

  def getNum(self):
      return self.num

  def getDen(self):
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
