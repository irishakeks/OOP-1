# класс Node для определения элемента списка
class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev