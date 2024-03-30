class MockUp:
    def __init__(self, name, rows, columns, start_square=None, targets_square_list=None):
        self.__name = name
        self.__rows = rows
        self.__columns = columns
        self.__start_square = start_square
        self.__targets_square_list = targets_square_list

    @property
    def name(self):
        return self.__name

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    @property
    def start_square(self):
        return self.__start_square

    @property
    def targets_square_list(self):
        return self.__targets_square_list

    @name.setter
    def name(self, value):
        self.__name = value

    @rows.setter
    def rows(self, value):
        self.__rows = value

    @columns.setter
    def columns(self, value):
        self.__columns = value

    @start_square.setter
    def start_square(self, value):
        self.__start_square = value

    @targets_square_list.setter
    def targets_square(self, value):
        self.__targets_square_list = value

    def __str__(self):
        return (f'{self.name}, {self.rows}, {self.columns}\n'
                f'{self.start_square}\n'
                f'{self.targets_square_list_to_list_text()}')

    def targets_square_list_to_list_text(self):
        tmp_text_list = "Targets Squares List:\n"
        for target in self.targets_square_list:
            tmp_text_list += "\t" + target.__str__() + "\n"

        return tmp_text_list

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name
