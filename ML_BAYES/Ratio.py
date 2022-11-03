from math import gcd


class Ratio:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return "(" + str(self.num) + "/" + str(self.den) + ")"

    def __repr__(self):
        return self.__str__()

    def is_one(self):
        return self.num == self.den

    def __add__(self, other):
        if isinstance(other, Ratio):
            return Ratio(self.num * other.den + other.num * self.den, self.den * other.den)
        elif isinstance(other, int):
            return Ratio(self.num + other * self.den, self.den)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Ratio):
            return Ratio(self.num * other.num, self.den * other.den)
        elif isinstance(other, int):
            return Ratio(self.num * other, self.den)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Ratio(-self.num, self.den)

    def __truediv__(self, other):
        return self * other.get_inverse()

    def __div__(self, other):
        return self.__truediv__(other)

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __pow__(self, power, modulo=None):
        return Ratio(self.num ** power, self.den ** power)

    def get_inverse(self):
        return Ratio(self.den, self.num)

    def simplify(self):
        greates_common_divisor = gcd(self.num, self.den)
        self.num = self.num // greates_common_divisor
        self.den = self.den // greates_common_divisor

    def get_simplified(self):
        new_ratio = Ratio(self.num, self.den)
        new_ratio.simplify()
        return new_ratio
