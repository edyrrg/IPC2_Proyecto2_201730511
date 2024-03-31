from abc import ABC, abstractmethod


class Square(ABC):
    def __init__(self, content, is_traveled=False):
        self.__content = content
        self.__is_traveled = is_traveled

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def is_traveled(self):
        return self.__is_traveled

    @is_traveled.setter
    def is_traveled(self, value):
        self.__is_traveled = value

    def __eq__(self, other):
        return self.content == other.content

    def __ne__(self, other):
        return self.content != other.content

    @abstractmethod
    def __str__(self):
        pass
