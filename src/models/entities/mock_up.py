class MockUp:
    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns

    @property
    def name(self):
        return self.name

    @property
    def rows(self):
        return self.rows

    @property
    def columns(self):
        return self.columns

    @name.setter
    def name(self, value):
        self._name = value

    @rows.setter
    def rows(self, value):
        self._rows = value

    @columns.setter
    def columns(self, value):
        self._columns = value

    def __str__(self):
        return f'{self._name}, {self._rows}, {self._columns}'

    def __eq__(self, other):
        return self._name == other.name

    def __ne__(self, other):
        return self._name != other.name

    def __lt__(self, other):
        return self._name < other.name

    def __le__(self, other):
        return self._name <= other.name

    def __gt__(self, other):
        return self._name > other.name

    def __ge__(self, other):
        return self._name >= other.name
