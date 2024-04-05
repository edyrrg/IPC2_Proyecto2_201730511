import copy

from src.adt.my_matrix_list import MyMatrixList
from src.adt.my_simple_list import MySimpleList
from src.adt.node import Node
from src.controllers.mock_up_controller import MockUpController
from src.models.entities.path_square import PathSquare
from src.models.entities.target_square import TargetSquare
from src.models.entities.wall_square import WallSquare
from src.services.xml_service import XMLService


class MockupSolverController:
    def __init__(self, _mockup_build: MyMatrixList, _target_square_list: MySimpleList):
        self.mockup_build: MyMatrixList = _mockup_build
        self.target_square_list: MySimpleList = _target_square_list
        self.next_to_collect: Node = self.target_square_list.head

    def resolver(self):
        # self.mockup_build.display_list()
        start_square = self.mockup_build.get_start_square()
        current_square = start_square
        # print(current_square)
        while current_square is not None and self.next_to_collect is not None:
            if isinstance(current_square.data, TargetSquare):
                self.collected_target_square(current_square)
            current_square.data.mark_traveled()
            # print(current_square)
            # current_square.data.content = "."
            current_square = self.advance_one_square(current_square)
        # self.mockup_build.display_list()

    def collected_target_square(self, current_square: Node):
        if self.next_to_collect.data.nr_order == current_square.data.nr_order:
            self.next_to_collect = self.next_to_collect.next

    def is_next_to_collect(self, current_square: Node):
        return True if self.next_to_collect.data.nr_order == current_square.data.nr_order else False

    def advance_one_square(self, node: Node):
        # Comprueba existencia de TargetSquare y avanza en esa direction
        if (node.next and isinstance(node.next.data, TargetSquare) and not node.next.data.is_traveled
                and self.is_next_to_collect(node.next)):
            return node.next
        if (node.down and isinstance(node.down.data, TargetSquare) and not node.down.data.is_traveled
                and self.is_next_to_collect(node.down)):
            return node.down
        if (node.prev and isinstance(node.prev.data, TargetSquare) and not node.prev.data.is_traveled
                and self.is_next_to_collect(node.prev)):
            return node.prev
        if (node.up and isinstance(node.up.data, TargetSquare) and not node.up.data.is_traveled
                and self.is_next_to_collect(node.up)):
            return node.up
        # Avanza
        if node.next and not isinstance(node.next.data, WallSquare) and not node.next.data.is_traveled:
            return node.next
        if node.down and not isinstance(node.down.data, WallSquare) and not node.down.data.is_traveled:
            return node.down
        if node.prev and not isinstance(node.prev.data, WallSquare) and not node.prev.data.is_traveled:
            return node.prev
        if node.up and not isinstance(node.up.data, WallSquare) and not node.up.data.is_traveled:
            return node.up
        if (isinstance(node.next.data, WallSquare) and isinstance(node.down.data, WallSquare) and
                isinstance(node.prev.data, WallSquare) and isinstance(node.up.data, WallSquare)):
            return None


if __name__ == "__main__":
    xml_handler = XMLService("../../files_xml/archivo-prueba-1.xml")
    mock_up_controller = MockUpController(xml_handler)
    tmp_mockups_list = mock_up_controller.create_list_of_mock_ups()
    mockup = tmp_mockups_list.get_node_data_by_index(2)
    mockup_build = copy.deepcopy(mockup.matrix_structure_build)
    targets_list = copy.deepcopy(mockup.target_squares_list)
    mockup_resolver_controller = MockupSolverController(mockup_build, targets_list)
    mockup_resolver_controller.resolver()
