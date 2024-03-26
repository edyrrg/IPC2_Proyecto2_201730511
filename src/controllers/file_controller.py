from pathlib import Path

from src.adt.my_simple_list import MySimpleList
from src.models.file import File


class FilesController:
    def __init__(self, path, extension):
        try:
            self.directory = Path(path)
            if not self.directory.exists():
                raise Exception('Directory does not exist')
            self.list_of_files = self.get_list_files_in_dir(extension=extension)
        except Exception as err:
            print(err)
        self.file = None
        self.path_file = None

    def get_list_files_in_dir(self, extension):
        list_of_files = MySimpleList()
        count = 0
        for _file in self.directory.iterdir():
            if _file.is_file() and _file.suffix == extension:
                list_of_files.append(File(index=count, file_name=_file.name))
                count += 1
        return list_of_files

    def set_file_by_index(self, index_selection_file):
        _file = self.list_of_files.search(index_selection_file)
        if _file:
            self.file = _file
            self.build_path_file()
        else:
            raise Exception('File not found')

    def build_path_file(self):
        self.path_file = self.directory.__str__() + "/" + self.file.get_file_name()

    def get_path_file(self):
        return self.path_file

    def set_path(self, new_directory_path):
        self.directory = new_directory_path

    def is_path_file_correct(self):
        return True if Path(self.path_file).exists() and Path(self.path_file).is_file() else False


if __name__ == "__main__":
    controller = FilesController('../../enter_files_xml/', '.xml')
    controller.list_of_files.display_list()
    controller.set_file_by_index(1)
    print(controller.get_path_file())
    print(f'Path file is correct?: {controller.is_path_file_correct()}')
