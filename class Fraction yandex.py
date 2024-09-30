import re


class Fraction:
    """Класс реализует правильную рациональную дробь"""

    def __init__(self, *args):
        self.__num = None  # Числитель
        self.__den = None  # Знаменатель
        self.__init_validation(args)

    def __init_validation(self, args) -> None:
        """
        Реализует возможность инициализации дроби с помощью двух целых чисел и строки.
        Производит валидацию входных значений. Сокращает дробь при необходимости.
        """
        match len(args):
            case 1:
                fraction_string = args[0]
                if not isinstance(fraction_string, str):
                    raise TypeError("Error type")
                if not re.fullmatch(r'[-+]?\d+/[-+]?\d+', fraction_string):
                    raise ValueError("Error value")
                self.__num, self.__den = [int(num) for num in fraction_string.split('/')]

            case 2:
                if not (isinstance(args[0], int) and isinstance(args[1], int)):
                    raise TypeError("Error type")
                self.__num, self.__den = args
        self.__reduction()

    def __nod(self, a, b) -> int:
        """Вычисляет наибольший общий делитель"""
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> tuple:
        """Сокращает дробь при необходимости"""
        nod = self.__nod(self.__num, self.__den)
        self.__num //= nod
        self.__den //= nod

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)

    def numerator(self, number=None) -> int:
        """
        Возвращает значение числителя.
        Изменяет значение числителя и производит сокращение дроби, если это необходимо
        """
        if number is not None:
            if not isinstance(number, int):
                raise TypeError("Error type")
            self.__num = number * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, number=None) -> int:
        """
        Возвращает значение знаменателя.
        Изменяет значение знаменателя и производит сокращение дроби, если необходимо
        """
        if number is not None:
            if not isinstance(number, int):
                raise TypeError("Error type")
            self.__den = number
            self.__reduction()
        return abs(self.__den)

    def __sign(self) -> int:
        """Возвращает текущий знак дроби"""
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> "Fraction":
        """Меняет знак дроби. Математическое отрицание"""
        return Fraction(-self.__num, self.__den)

    def __add__(self, other: "Fraction") -> "Fraction":
        """Складывает две дроби и возвращает новую дробь"""
        new = Fraction(1, 1)
        new.__num = (self.__num * other.__den) + (other.__num * self.__den)
        new.__den = self.__den * other.__den
        new.__reduction()
        return new

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Вычитает дроби и возвращает новую дробь"""
        new = Fraction(1, 1)
        new.__num = (self.__num * other.__den) - (other.__num * self.__den)
        new.__den = self.__den * other.__den
        new.__reduction()
        return new

    def __isub__(self, other: "Fraction") -> "Fraction":
        """Вычитает дроби и изменяет левую дробь"""
        self.__num = (self.__num * other.__den) - (other.__num * self.__den)
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __iadd__(self, other: "Fraction") -> "Fraction":
        """Складывает дроби и изменяет левую дробь"""
        self.__num = (self.__num * other.__den) + (other.__num * self.__den)
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Умножает дробь, результат в новую дробь"""
        new = Fraction(1, 1)
        new.__num = self.__num * other.__num
        new.__den = self.__den * other.__den
        new.__reduction()
        return new

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Делит дроби, результат в новую дробь"""
        new = Fraction(self.__num, self.__den)
        new.__reduction()
        return new.__mul__(other.reverse())

    def __imul__(self, other: "Fraction") -> "Fraction":
        """Умножает дробь, результат в левую дробь"""
        self.__num = self.__num * other.__num
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __itruediv__(self, other: "Fraction") -> "Fraction":
        """Делит дроби, результат в левую дробь"""
        return self.__imul__(other.reverse())

    def reverse(self) -> "Fraction":
        """Переворачивает дробь"""
        return Fraction(self.__den, self.__num)

    def __str__(self):
        """Возвращает строковое представление дроби в формате <числитель>/<знаменатель>"""
        return f"{self.__num}/{self.__den}"

    def __repr__(self):
        """Возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>)"""
        return f"{__class__.__name__}('{self.__num}/{self.__den}')"


fraction = Fraction("-3/210")
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(-2)
print(fraction, repr(fraction))
print(fraction.numerator(), fraction.denominator())

print()

a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())

print("\nДроби 3.0")
a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)  # 1/3 1/2 5/6 False False

a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)  # 1/8 1/4 1/4 True

print("\nДроби 4.0")
a = Fraction(1, 3)
b = Fraction(1, 2)
c = a * b
print(a, b, c, a is c, b is c)  # 1/3 1/2 1/6 False False

a = Fraction(1, 3)
c = b = Fraction(2, 1).reverse()
b /= a
print(a, b, c, b is c)  # 1/3 3/2 3/2 True