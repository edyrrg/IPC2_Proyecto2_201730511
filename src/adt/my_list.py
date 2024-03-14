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

    @abstractmethod
    def display_list(self):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def get_node_data_by_index(self, index):
        pass

    @abstractmethod
    def search_node_data(self, search_value):
        pass
