from src.models.entities.indexed_square import IndexedSquare


class StartSquare(IndexedSquare):
    count_id = 0

    def __init__(self, content, index_x, index_y):
        StartSquare.count_id += 1
        self.__id = "StartSquare" + str(StartSquare.count_id)
        super().__init__(content, index_x, index_y)

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'{self.content}'

    def show(self):
        return f'StartSquare={self.content}, x={self.index_x}, y={self.index_y}'


if __name__ == '__main__':
    start_square = StartSquare("+", 1, 2)
    print(start_square)
