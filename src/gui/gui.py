from src.controllers.file_controller import FilesController
from src.controllers.input_handler import InputHandler


class GUI:
    def __init__(self):
        print("**** Welcome User ****")
        self.my_name = "Edy Rolando Rojas González"
        self.my_id = "201730511"
        self.my_github_link = "https://github.com/edyrrg/IPC2_Proyecto2_201730511"
        self.file_controller = self.get_user_path()
        self.init_menu()
        self.main_menu()
        self.xml_service = None

    def init_menu(self):
        print("XML Files in dir", self.file_controller.directory)
        while True:
            self.file_controller.get_list_files()
            upper_limit = self.file_controller.list_of_files.__len__() - 1
            res_user = InputHandler.handler_input_option(0, upper_limit)
            self.file_controller.set_file_by_index(res_user)
            print("Is the following XML file correct?", self.file_controller.path_file)
            print('Please enter: y(Yes) or n(No)')
            res_correct = InputHandler.handler_yorn_response_user()
            if res_correct:
                return

    def main_menu(self):
        while True:
            print("**** Main Menu ****")
            print("1 ----- Init Program")
            print("2 ----- Load an input XML file")
            print("3 ----- Mockup management")
            print("4 ----- Mockup resolution")
            print("5 ----- Help!")
            print("6 ----- Exit")
            user_input = InputHandler.handler_input_option(1, 6)
            if user_input == 1:
                self.file_controller = self.get_user_path()
            if user_input == 2:
                self.init_menu()
            if user_input == 3:
                return
            if user_input == 4:
                return
            if user_input == 5:
                self.help_me()
            if user_input == 6:
                print("Ending Program...")
                return
    def mockup_manage(self):
        pass

    def help_me(self):
        print("Hello User!")
        print(f'My name is {self.my_name}')
        print(f'My carne is {self.my_id}')
        print(f'Documentation link: {self.my_github_link}')

    @classmethod
    def get_user_path(cls):
        try:
            while True:
                print("Please enter path directory:")
                res_user_path = InputHandler.handler_response_user(5,
                                                                   "Please enter a valid directory path...")
                tmp_files_controller = FilesController(res_user_path, ".xml")
                if tmp_files_controller.is_correct_directory_path():
                    print("Uploading .xml  files in directory...")
                    print("Uploaded successfully!")
                    return tmp_files_controller
                print("Invalid directory path...")
        except Exception as e:
            print(e)
