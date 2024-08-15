from __future__ import annotations  # Отложенное исполнение
from typing import Self


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def move(self, x, y) -> None:
        self.x += x
        self.y += y

    def length(self, coord: Point) -> float:
        return round((((self.x - coord.x) ** 2) + ((self.y - coord.y) ** 2)) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                super().__init__(0, 0)  # Инициализация без параметров
            case 1:
                super().__init__(*args[0])  # Инициализация с одним параметром, кортеж координат
            case 2:
                super().__init__(*args)  # Инициализация с двумя координатами

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    # Реализация оператора "+", (point + (2, -3))
    def __add__(self, other) -> PatchedPoint:
        return self.__class__(self.x + other[0], self.y + other[1])

    # Реализация оператора "+=", (first_point += (7, 3))
    def __iadd__(self, other) -> Self:
        self.move(*other)
        return self


# point = PatchedPoint((2,7))
# print(point.x, point.y)
# print(repr(point))

point = PatchedPoint()
print(point)
new_point = point + (2, -3)  # создаётся новая точка, которая отличается от изначальной на заданное кортежем расстояние по осям x и y.
print(point, new_point, point is new_point)  # (0, 0) PatchedPoint(2, -3) False

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)  # Производится перемещение изначальной точки
print(first_point, second_point, first_point is second_point)  # (9, -4) (9, -4) True


