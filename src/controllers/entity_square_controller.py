from abc import ABC, abstractmethod

from src.services.xml_service import XMLService


class EntitySquareController(ABC):
    def __init__(self, xml_service: XMLService):
        self.__xml_service = xml_service

    @property
    def xml_service(self):
        return self.__xml_service

    @xml_service.setter
    def xml_service(self, value):
        self.__xml_service = value

    @abstractmethod
    def create_entity(self, child):
        pass
