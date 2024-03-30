from src.adt.my_simple_list import MySimpleList
from src.controllers.entity_square_controller import EntitySquareController
from src.models.entities.target_square import TargetSquare
from src.services.xml_service import XMLService


class TargetSquareController(EntitySquareController):

    def __init__(self, xml_service: XMLService):
        super().__init__(xml_service)

    def create_entity(self, child):
        name = self.xml_service.get_child_by_parent_tag(child, "nombre")
        row = self.xml_service.get_child_by_parent_tag(child, "fila")
        column = self.xml_service.get_child_by_parent_tag(child, "columna")
        return TargetSquare(content=str(name.text).strip(), index_x=str(row.text).strip(),
                            index_y=str(column.text).strip())

    def list_of_targets_square(self, target_parent):
        targets_children = self.xml_service.get_child_by_parent_tag(target_parent, "objetivos")
        my_simple_list = MySimpleList()
        index_target_square_count = 0
        for child in targets_children:
            index_target_square_count += 1
            tmp_target_square = self.create_entity(child)
            tmp_target_square.nr_order = index_target_square_count
            my_simple_list.append(tmp_target_square)
        return my_simple_list
