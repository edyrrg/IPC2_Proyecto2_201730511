from src.adt.my_simple_list import MySimpleList
from src.controllers.start_square_controller import StartSquareController
from src.controllers.structure_square_controller import StructureSquareController
from src.controllers.target_square_controller import TargetSquareController
from src.models.entities.mock_up import MockUp
from src.services.xml_service import XMLService


class MockUpController:
    def __init__(self, xml_service: XMLService):
        self.xml_service = xml_service
        self.start_square_controller = StartSquareController(self.xml_service)
        self.target_square_controller = TargetSquareController(self.xml_service)
        self.structure_square_controller = StructureSquareController(self.xml_service)

    def get_text_to_xml_element(self, child, tag):
        child_to_text = self.xml_service.get_child_by_parent_tag(child, tag)
        return str(child_to_text.text).strip()

    def create_list_of_mock_ups(self):
        mock_ups = self.xml_service.get_parent("maquetas")
        my_simple_list = MySimpleList()
        for child in mock_ups:
            name = self.get_text_to_xml_element(child, "nombre")
            rows = self.get_text_to_xml_element(child, "filas")
            columns = self.get_text_to_xml_element(child, "columnas")
            start_square = self.start_square_controller.create_entity(child)
            targets_square_list = self.target_square_controller.create_list_of_targets_square(child)
            tmp_mock_up = self.create_entity(name, rows, columns, start_square, targets_square_list)

            my_simple_list.append(tmp_mock_up)
        return my_simple_list

    @classmethod
    def create_entity(cls, name, rows, columns, start_square, targets_square_list):
        return MockUp(name, rows, columns, start_square, targets_square_list)


if __name__ == '__main__':
    xml_handler = XMLService("../../enter_files_xml/archivo-prueba-1.xml")
    mock_up_controller = MockUpController(xml_handler)
    tmp_mock_ups = mock_up_controller.create_list_of_mock_ups()
    tmp_mock_ups.display_list()
    sorted_mock_ups = sorted(tmp_mock_ups)
    for mock_up in sorted_mock_ups:
        print(mock_up)
