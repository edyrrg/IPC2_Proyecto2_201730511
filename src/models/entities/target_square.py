from src.models.entities.indexed_square import IndexedSquare


class TargetSquare(IndexedSquare):
    def __init__(self, content, index_x, index_y, nr_order=None):
        super().__init__(content, index_x, index_y)
        self.__nr_order = nr_order

    @property
    def nr_order(self):
        return self.__nr_order

    @nr_order.setter
    def nr_order(self, value):
        self.__nr_order = value

    def __str__(self):
        return f'TargetSquare {self.nr_order}, {self.content}, {self.index_x}, {self.index_y}'


if __name__ == '__main__':
    target_square = TargetSquare(1, "B", 2, 1)
    print(target_square)
