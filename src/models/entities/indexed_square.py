from src.models.entities.square import Square


class IndexedSquare(Square):
    def __init__(self, content, index_x, index_y):
        super().__init__(content)
        self.index_x = index_x
        self.index_y = index_y

    @property
    def index_x(self):
        return self.index_x

    @index_x.setter
    def index_x(self, value):
        self.index_x = value

    @property
    def index_y(self):
        return self.index_y

    @index_y.setter
    def index_y(self, value):
        self.index_y = value
