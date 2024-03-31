from src.adt.my_matrix_list import MyMatrixList
from src.controllers.entity_square_controller import EntitySquareController
from src.models.entities.path_square import PathSquare
from src.models.entities.wall_square import WallSquare
from src.services.xml_service import XMLService


class StructureSquareController(EntitySquareController):

    def __init__(self, xml_service: XMLService):
        super().__init__(xml_service)

    def create_entity(self, structure):
        if structure == "-":
            return PathSquare(structure)
        else:
            return WallSquare(structure)

    def create_matrix_list_structure(self, child, rows: int, columns: int):
        structure_xml_el = self.xml_service.get_child_by_parent_tag(child, "estructura")
        structure_text = (str(structure_xml_el.text).replace("\n", "")
                          .replace("\t", "")
                          .replace(" ", ""))
        my_matrix_list = MyMatrixList()
        count = 0
        for i in range(rows):
            for j in range(columns):
                tmp_structure_ = self.create_entity(structure_text[count])
                if j == 0:
                    my_matrix_list.append(tmp_structure_, new_row=True)
                    count += 1
                    continue
                my_matrix_list.append(tmp_structure_)
                count += 1
        return my_matrix_list
