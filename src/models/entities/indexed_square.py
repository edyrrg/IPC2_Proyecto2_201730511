from abc import ABC

from src.models.entities.square import Square


class IndexedSquare(Square, ABC):
    def __init__(self, content, index_x, index_y):
        super().__init__(content)
        self.__index_x = index_x
        self.__index_y = index_y

    @property
    def index_x(self):
        return self.__index_x

    @index_x.setter
    def index_x(self, value):
        self.__index_x = value

    @property
    def index_y(self):
        return self.__index_y

    @index_y.setter
    def index_y(self, value):
        self.__index_y = value


if __name__ == '__main__':
    indexed_square = IndexedSquare(content="b", index_x=1, index_y=2)
    print(indexed_square)
