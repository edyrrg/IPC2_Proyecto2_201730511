from abc import ABC


class Square(ABC):
    def __init__(self, content, is_traveled=False):
        self.content = content
        self.is_traveled = is_traveled

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, value):
        self.content = value

    @property
    def is_traveled(self):
        return self.is_traveled

    @is_traveled.setter
    def is_traveled(self, value):
        self.is_traveled = value

    def __eq__(self, other):
        return self.content == other.content

    def __ne__(self, other):
        return self.content != other.content

    def __str__(self):
        return self.content
