from src.models.entities.indexed_square import IndexedSquare


class StartSquare(IndexedSquare):
    def __init__(self, content, index_x, index_y):
        super().__init__(content, index_x, index_y)

    def __str__(self):
        return f'{self.content}'


if __name__ == '__main__':
    start_square = StartSquare("+", 1, 2)
    print(start_square)
