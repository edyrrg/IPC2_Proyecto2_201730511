from src.models.entities.square import Square


class WallSquare(Square):
    count_id = 0

    def __init__(self, content):
        WallSquare.count_id += 1
        self.__id = "WallSquare" + str(WallSquare.count_id)
        super().__init__(content)

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'{self.content}'
