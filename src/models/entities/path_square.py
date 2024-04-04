from src.models.entities.square import Square


class PathSquare(Square):
    count_id = 0

    def __init__(self, content):
        PathSquare.count_id += 1
        self.__id = "PathSquare" + str(PathSquare.count_id)
        super().__init__(content)

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'{self.content}'
