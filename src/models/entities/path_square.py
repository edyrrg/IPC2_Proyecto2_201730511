from src.models.entities.square import Square


class PathSquare(Square):

    def __init__(self, content):
        super().__init__(content)

    def __str__(self):
        return f'PathSquare {self.content}'
