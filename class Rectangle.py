from typing import Tuple, Union


class Rectangle:
    """Описывается класс Прямоугольник"""
    
    def __init__(self, corner1, corner2):
        self._corner1 = None
        self._corner2 = None
        self._x0 = None
        self._y0 = None
        self._width = None
        self._height = None
        self.validation_init(corner1, corner2)
        self.set_0_pos(self._corner1, self._corner2)
        self.set_size(self._corner1, self._corner2)

    def validation_init(self, corner1: Tuple[float, ...], corner2: Tuple[float, ...]) -> None:
        """
        Проверяет значения координат на валидность
        
        :param corner1: Кортеж координат первого угла фигуры
        :param corner2: Кортеж координат второго угла фигуры
        :raise TypeError: Вызов исключения, если введен невертый тип координат
        :return: None, либо ошибка TypeError.
        """

        if (not isinstance(corner1[0], float)) or (not isinstance(corner1[1], float)):
            raise TypeError(f"Не верный тип данных 'corner1' - {type(corner1)}")
        if (not isinstance(corner2[0], float)) or (not isinstance(corner2[1], float)):
            raise TypeError(f"Не верный тип данных 'corner2' - {type(corner2)}")
        self._corner1 = corner1
        self._corner2 = corner2
    
    def set_0_pos(self, corner1: tuple, corner2: tuple) -> tuple:
        """Расчитывает координаты левого верхнего угла по входным данным
        :param corner1: Координата одного угла
        :param corner2: Координата второго противоположного угла
        :return: Кортежс координатами левого верхнего угла
        """
        self._x0 = round(min(corner1[0], corner2[0]), 2)
        self._y0 = round(max(corner1[1], corner2[1]), 2)
        return self._x0, self._y0
    
    def perimeter(self) -> float:
        """
        Вычисляет периметр фигуры

        :return: Округленное до сотых значение периметра
        """
        w, h = self.get_size()
        return round(2 * (w + h), 2)
        
    def area(self) -> float:
        """
        Вычисляет площадь фигуры

        :return: Округленное до сотых значение пплощади
        """
        w, h = self.get_size()
        return round(w * h, 2)

    def get_pos(self) -> tuple:
        """Возвращает координаты верхнего левого угла в виде кортежа
        :return: Кортеж с координатами левого верхнего угла
        """
        return round(self._x0, 2), round(self._y0, 2)
        
    def set_size(self, corner1: tuple, corner2: tuple) -> None:
        """
        Устанавливает размеры фигуры исходя из входных данных
        :param corner1: Координата одного угла
        :param corner2: Координата второго противоположного угла
        :return: None
        """
        x1, y1 = corner1
        x2, y2 = corner2
        self._width = round(abs(x1 - x2), 2)
        self._height = round(abs(y1 - y2), 2)

    def get_size(self) -> tuple:
        """Возвращает размеры в виде кортежа"""
        return self._width, self._height

    def move(self, dx: Union[float, int], dy: Union[float, int]) -> None:
        """Изменяет положение на заданные значения"""
        if not isinstance(dx, (int, float)):
            raise TypeError("Неверный тип координат в move")
        if not isinstance(dy, (int, float)):
            raise TypeError("Неверный тип координат в move")
        
        self._x0 += dx
        self._y0 += dy

    def resize(self, width: Union[float, int], height: Union[float, int]) -> None:
        """Изменяет размер (положение верхнего левого угла остаётся неизменным)"""
        if not isinstance(width, (int, float)):
            raise TypeError("Неверный тип координат в resize")
        if not isinstance(height, (int, float)):
            raise TypeError("Неверный тип координат в resize")
        
        self._width = round(width, 2)
        self._height = round(height, 2)
        
    def turn(self):
        """Поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра"""
        diff = (self._width - self._height) / 2
        self.move(diff, diff)
        self._width, self._height = self._height, self._width
        
    def scale(self, factor: Union[float, int]) -> None:
        """Изменяет размер в указанное количество раз, тоже относительно центра
        :param factor: Коеффициент изменения размера фигуры
        :return: None
        """
        if not isinstance(factor, (int, float)):
            raise TypeError("Неверный тип координат в factor")
        
        # self._width *= factor
        # self._height *= factor
        # self._x0 *= factor
        # self._y0 *= factor
        dx = round((self._width * (factor - 1)), 2)
        dy = round((self._height * (factor - 1)), 2)
        self.move(-dx / 2, dy / 2)
        self.resize(self._width * factor, self._height * factor)
        
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
assert rect.get_pos() == (3.2, 3.14)
assert rect.get_size() ==  (4.32, 7.44)
rect.move(1.32, -5)
assert rect.get_pos() == (4.52, -1.86)
assert rect.get_size() ==  (4.32, 7.44)

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
assert rect.get_pos() == (3.2, 3.14)
assert rect.get_size() ==  (4.32, 7.44)
rect.resize(23.5, 11.3)
assert rect.get_pos() == (3.2, 3.14)
assert rect.get_size() ==  (23.5, 11.3)

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
assert rect.get_pos() == (-3.14, 2.71)
assert rect.get_size() ==  (6.28, 5.42)
rect.turn()
assert rect.get_pos() == (-2.71, 3.14)
assert rect.get_size() ==  (5.42, 6.28)

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
assert rect.get_pos() == (-3.14, 2.71)
assert rect.get_size() ==  (6.28, 5.42)
rect.scale(2.0)
assert rect.get_pos() == (-6.28, 5.42)
assert rect.get_size() ==  (12.56, 10.84)
