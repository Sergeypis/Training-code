from typing import Any


class Queue:
    """
    Класс Очередь.
    Реализует подход к хранению данных по принципу «Первый вошёл – первый ушел»
    """

    def __init__(self) -> None:
        """Создается пустая очередь"""
        self.queue = []

    def push(self, item: Any) -> None:
        """Добавляет элемент в конец очереди"""
        self.queue.append(item)

    def pop(self) -> Any:
        """Извлекает первый элемент из очереди"""
        return self.queue.pop(0) if not self.is_empty() else "Queue is Empty!"

    def is_empty(self) -> bool:
        """Проверят очередь на пустоту"""
        return True if not self.queue else False


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")  # 0123456789

print()

queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())  # Hello,
                        # world!