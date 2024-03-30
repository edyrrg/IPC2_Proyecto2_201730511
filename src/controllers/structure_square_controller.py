from src.controllers.entity_square_controller import EntitySquareController
from src.services.xml_service import XMLService


class StructureSquareController(EntitySquareController):

    def __init__(self, xml_service: XMLService):
        super().__init__(xml_service)

    def create_entity(self, child):
        pass
