from src.controllers.file_controller import FilesController


class GUI:
    def __init__(self):
        self.path = self.get_input_user_path()
        self.file_controller = FilesController()
        self.init_main()

    def init_main(self):
        pass

    def get_input_user_path(self):
        pass
