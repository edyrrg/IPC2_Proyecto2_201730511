from src.models.entities.indexed_square import IndexedSquare


class InputSquare(IndexedSquare):
    def __init__(self, content, index_x, index_y):
        super().__init__(content, index_x, index_y)
