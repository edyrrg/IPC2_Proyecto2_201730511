from abc import ABC, abstractmethod


class MyList(ABC):
    def __init__(self, head=None):
        self.head = head

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def display_list(self):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def search_node_data(self, search_value):
        pass
