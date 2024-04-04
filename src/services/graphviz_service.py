import graphviz

from src.adt.my_matrix_list import MyMatrixList
from src.adt.node import Node
from src.controllers.mock_up_controller import MockUpController
from src.models.entities.path_square import PathSquare
from src.models.entities.start_square import StartSquare
from src.models.entities.target_square import TargetSquare
from src.models.entities.wall_square import WallSquare
from src.services.xml_service import XMLService


class GraphvizService:
    def __init__(self, name):
        self.name = name
        self.graph = graphviz.Digraph(name=f'{self.name}',
                                      filename=f'{self.name}',
                                      comment=f'The Graph to MockUp: {self.name}',
                                      directory='../../graphviz_render/')
        self.graph.attr(rankdir='LR')
        self.graph.attr('edge', arrowhead='none')
        # self.graph.node("Hello", shape='circle', style='filled', color='brown')
        # self.graph.node("World", shape='box', style='filled', color='green')
        # self.graph.edge("Hello", "World")

    def matrix_list_to_graphviz(self, matrix_list: MyMatrixList):
        for node in reversed(matrix_list):
            self.node_to_graphviz(node)

    def node_to_graphviz(self, node: Node):
        if isinstance(node.data, PathSquare):
            self.graph.node(node.data.id, label=f"{node.data}", shape='box', style="dotted", color='black')
        if isinstance(node.data, WallSquare):
            self.graph.node(node.data.id, label=f"{node.data}", shape='box', style='filled', color='brown')
        if isinstance(node.data, StartSquare):
            self.graph.node(node.data.id, label=f"{node.data}", shape='box', style='filled', color='green')
        if isinstance(node.data, TargetSquare):
            self.graph.node(node.data.id, label=f"Nr.O_{node.data.nr_order}\n{node.data}", shape='box', style='filled', color='yellow')
        if node.next:
            self.graph.edge(node.data.id, node.next.data.id)

    def show_graphviz(self):
        self.graph.view()


if __name__ == '__main__':
    xml_handler = XMLService("../../files_xml/archivo-prueba-2.xml")
    mock_up_controller = MockUpController(xml_handler)
    tmp_mock_ups = mock_up_controller.create_list_of_mock_ups()
    # tmp_mock_ups.display_list()
    matrix = tmp_mock_ups.get_node_data_by_index(2)
    #matrix.matrix_structure.display_list()
    matrix.matrix_structure_build.display_list()
    graphviz_service = GraphvizService('configuration_' + matrix.name)
    #graphviz_service.matrix_list_to_graphviz(matrix.matrix_structure)
    graphviz_service.matrix_list_to_graphviz(matrix.matrix_structure_build)
    graphviz_service.show_graphviz()
