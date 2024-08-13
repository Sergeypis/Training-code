"""
Игра шашки

Объекты класса Checkers при инициализации строят игральную доску со стандартным распределением клеток

Объекты класса Cell при инициализации принимают одно из трех состояний:
W — белая шашка, B — чёрная шашка, X — пустая клетка, а также обладают методом status()
возвращающим заложенное в ней состояние.

Координаты клеток описываются строками вида PQ, где:
P — столбец игральной доски, одна из заглавных латинских букв: ABCDEFGH;
Q — строка игральной доски, одна из цифр: 12345678.
"""

class Checkers:
    """Класс - игровое поле"""
    def __init__(self) -> None:
        self.game_field = dict() 
        self.init_field()
        
    def init_field(self):
        for x, char in enumerate('ABCDEFGH', 1):
            for num in '87654321':
                if (x%2 and num == '7') or (not x%2 and num in '68'):
                    obj = 'B'
                elif (not x%2 and num == '2') or (x%2 and num in '13'):
                    obj = 'W'
                else:
                    obj = 'x'
                self.game_field[char + num] = Cell(obj)

    def move(self, f, t):
        """Перемещает шашку из позиции f в позицию t"""
        self.game_field[t] = Cell(self.get_cell(f).status())
        self.game_field[f] = Cell('x')

    def get_cell(self, p: str):
        """Возвращает объект «клетка» в позиции p"""
        return self.game_field.get(p)

class Cell:
    """Класс - клетка на поле"""
    def __init__(self, state) -> None:
        self.state = state

    def status(self) -> str:
        """Возвращает состояние клетки"""
        return self.state


checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()

print() 

checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()
    