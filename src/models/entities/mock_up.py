import copy

from src.adt.my_matrix_list import MyMatrixList


class MockUp:
    def __init__(self, name, rows, columns, start_square=None, target_squares_list=None,
                 matrix_structure_squares: MyMatrixList = None):
        self.__name = name
        self.__rows = rows
        self.__columns = columns
        self.__start_square = start_square
        self.__target_squares_list = target_squares_list
        self.__matrix_structure_squares = matrix_structure_squares
        self.__matrix_structure_build = self.build_mock_up_structure()

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
    def target_squares_list(self):
        return self.__target_squares_list

    @property
    def matrix_structure(self):
        return self.__matrix_structure_squares

    @property
    def matrix_structure_build(self):
        return self.__matrix_structure_build

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

    @target_squares_list.setter
    def target_squares_list(self, value):
        self.__target_squares_list = value

    @matrix_structure.setter
    def matrix_structure(self, value):
        self.__matrix_structure_squares = value

    @matrix_structure_build.setter
    def matrix_structure_build(self, value):
        self.__matrix_structure_build = value

    def __str__(self):
        return (f'Nombre: {self.name}\n'
                f'Fila: {self.rows}\n'
                f'Columna: {self.columns}\n'
                f'{self.start_square.show()}\n'
                f'{self.targets_square_list_to_list_text()}'
                f'Estructura:\n'
                f'{self.matrix_structure.to_str()}')

    def targets_square_list_to_list_text(self):
        tmp_text_list = "Targets Squares List:\n"
        for target in self.target_squares_list:
            tmp_text_list += f"\tnr order={target.nr_order} " + target.show() + "\n"

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

    def build_mock_up_structure(self):
        matrix_list = self.matrix_structure
        tmp_matrix_structure_list = copy.deepcopy(matrix_list)
        xi = int(self.start_square.index_x) + 1
        yi = int(self.start_square.index_y) + 1
        tmp_matrix_structure_list.update_node_data_by_index(xi=xi, yi=yi, value=self.start_square)
        for target in self.target_squares_list:
            target_xi = int(target.index_x) + 1
            target_yi = int(target.index_y) + 1
            tmp_matrix_structure_list.update_node_data_by_index(xi=target_xi, yi=target_yi, value=target)
        return tmp_matrix_structure_list
