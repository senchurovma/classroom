class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    # def __setattr__(self, key, value):

    
    @classmethod
    def validate(self, num, den):
        if isinstance(num, int) and isinstance(den, int):
            if den == 0:
                raise ArithmeticError('>0')
            else:
                raise ValueError('целые числа')


    @property
    def value(self):
        return round(self.num / self.den, 3)
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)
    
    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)
    
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    
    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num) if other.num else ValueError("нельзя делить на ноль")


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)  # 5/4
print(f1 - f2)  # -1/4
print(f1 * f2)  # 3/8
print(f1 / f2)  # 2/3
print(f1.value) # 0.5