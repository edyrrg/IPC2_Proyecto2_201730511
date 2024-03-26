class File:
    def __init__(self, index, file_name):
        self.index = index
        self.file_name = file_name

    def get_index(self):
        return self.index

    def get_file_name(self):
        return self.file_name

    def __str__(self):
        return f'{self.index} -------------------- {self.file_name}'

    def __eq__(self, other):
        return self.index == other
