import copy

from src.adt.my_simple_list import MySimpleList
from src.controllers.file_controller import FilesController
from src.controllers.input_handler import InputHandler
from src.controllers.mock_up_controller import MockUpController
from src.controllers.mockup_solver_controller import MockupSolverController
from src.models.entities.mock_up import MockUp
from src.services.graphviz_service import GraphvizService
from src.services.xml_service import XMLService


class GUI:
    def __init__(self):
        print("**** Welcome User ****")
        self.my_name = "Edy Rolando Rojas González"
        self.my_id = "201730511"
        self.my_github_link = "https://github.com/edyrrg/IPC2_Proyecto2_201730511"
        self.file_controller: FilesController = None
        self.xml_service: XMLService = None
        self.mockup_controller: MockUpController = None
        self.list_of_mockups: MySimpleList = None
        self.graphviz_service: GraphvizService = None
        self.get_user_path()
        self.main_menu()

    def init_menu(self):
        if not self.file_controller.list_of_files.is_empty():
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
                    self.xml_service = XMLService(self.file_controller.path_file)
                    return
        else:
            print("No XML files found in directory", self.file_controller.directory)

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
                self.get_user_path()
            if user_input == 2:
                self.init_menu()
            if user_input == 3:
                self.mockup_manage()
            if user_input == 4:
                self.mockup_resolution_manage()
            if user_input == 5:
                self.help_me()
            if user_input == 6:
                print("Ending Program...")
                return

    def mockup_manage(self):
        if not self.xml_service:
            print("Select an xml file first...")
            return
        self.mockup_controller = MockUpController(self.xml_service)
        self.list_of_mockups = self.mockup_controller.create_list_of_mock_ups()
        while True:
            print("**** Mockup menu ****")
            print("1 ----- See list of Mockups in alphabetical order")
            print("2 ----- See Mockup configuration")
            print("3 ----- Back to Main Menu")
            user_input = InputHandler.handler_input_option(1, 3)
            if user_input == 1:
                self.see_list_of_mockups()
            if user_input == 2:
                self.see_mockup_configuration()
            if user_input == 3:
                return

    def see_list_of_mockups(self):
        if self.list_of_mockups:
            self.list_of_mockups.sort_descending()
            self.list_of_mockups.display_list()

    def see_mockup_configuration(self):
        count = 0
        print("Select Mockup to see configuration")
        for mockup in self.list_of_mockups:
            count += 1
            print(f'{count} -------------------- {mockup.name}')
        user_input = InputHandler.handler_input_option(0, self.list_of_mockups.__len__())
        tmp: MockUp = self.list_of_mockups.get_node_data_by_index(user_input)
        print(tmp.name)
        tmp.matrix_structure_build.display_list()
        print(tmp.targets_square_list_to_list_text())
        self.graphviz_service = GraphvizService("configuration_" + tmp.name)
        self.graphviz_service.matrix_list_to_graphviz(tmp.matrix_structure_build)
        self.graphviz_service.show_graphviz()

    def mockup_resolution_manage(self):
        if not self.xml_service:
            print("Select an xml file first...")
            return
        self.mockup_controller = MockUpController(self.xml_service)
        self.list_of_mockups = self.mockup_controller.create_list_of_mock_ups()
        count = 0
        print("Select Mockup to resolve")
        for mockup in self.list_of_mockups:
            count += 1
            print(f'{count} -------------------- {mockup.name}')
        print("3 -------------------- Back to Main Menu")
        user_input = InputHandler.handler_input_option(0, self.list_of_mockups.__len__() + 1)
        if user_input == 3:
            return
        tmp: MockUp = self.list_of_mockups.get_node_data_by_index(user_input)
        # print(tmp.name)
        # tmp.matrix_structure_build.display_list()
        # print(tmp.targets_square_list_to_list_text())
        mockup_build = copy.deepcopy(tmp.matrix_structure_build)
        targets_list = copy.deepcopy(tmp.target_squares_list)
        mockup_resolver_controller = MockupSolverController(mockup_build, targets_list)
        mockup_resolver_controller.resolver()
        self.graphviz_service = GraphvizService("resolve_" + tmp.name)
        self.graphviz_service.matrix_list_to_graphviz(mockup_resolver_controller.mockup_build)
        self.graphviz_service.show_graphviz()

    def help_me(self):
        print("\nHello User!")
        print(f'My name is {self.my_name}')
        print(f'My carne is {self.my_id}')
        print(f'Documentation link: {self.my_github_link}\n')

    def get_user_path(self):

        while True:
            print("Please enter path directory:")
            res_user_path = InputHandler.handler_response_user(5,
                                                               "Please enter a valid directory path...")
            self.file_controller = FilesController(res_user_path, ".xml")
            if self.file_controller.is_correct_directory_path():
                if not self.file_controller.list_of_files.is_empty():
                    print("Uploading .xml  files in directory...")
                    print("Uploaded successfully!")
                    return
                else:
                    print("No XML files found in directory", self.file_controller.directory, ", please try again.")
            else:
                print("Invalid directory path...")
