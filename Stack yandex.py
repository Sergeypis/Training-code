from typing import Any


class Stack:
    """
    Класс Стек.
    Реализует подход к хранению данных по прин "Последний пришёл – первый ушёл"
    """

    def __init__(self) -> None:
        """Создается пустой стек"""
        self.stack = []

    def push(self, item: Any) -> None:
        """Добавляет элемент в конец стека"""
        self.stack.append(item)

    def pop(self) -> Any:
        """Извлекает первый элемент из стека"""
        return self.stack.pop() if not self.is_empty() else "Stack is Empty!"

    def is_empty(self) -> bool:
        """Проверят стек на пустоту"""
        return True if not self.stack else False


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")  # 9 8 7 6 5 4 3 2 1 0

print()

stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())  # world!
                        # Hello,