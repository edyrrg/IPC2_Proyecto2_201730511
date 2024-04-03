from src.controllers.entity_square_controller import EntitySquareController
from src.models.entities.start_square import StartSquare
from src.services.xml_service import XMLService


class StartSquareController(EntitySquareController):
    def __init__(self, xml_service: XMLService):
        super().__init__(xml_service)

    def create_entity(self, child):
        input_xml_el = self.xml_service.get_child_by_parent_tag(child, "entrada")
        row = self.xml_service.get_child_by_parent_tag(input_xml_el, "fila")
        column = self.xml_service.get_child_by_parent_tag(input_xml_el, "columna")
        return StartSquare(content="/", index_y=str(row.text).strip(), index_x=str(column.text).strip())
