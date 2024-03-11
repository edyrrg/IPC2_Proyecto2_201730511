from abc import ABC


class MyList(ABC):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
