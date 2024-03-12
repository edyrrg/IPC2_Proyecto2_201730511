from abc import ABC, abstractmethod

from src.adt.node import Node


class MyList(ABC):
    def __init__(self, head=None):
        self.head = head

    @abstractmethod
    def append(self, data):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    # @abstractmethod
    # def search(self, data):
        # pass
