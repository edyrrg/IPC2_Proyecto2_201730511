import xml.etree.ElementTree as et


class XMLService:
    def __init__(self, path):
        self.path = path
        self.ET = self.create_et()
        self.root = self.get_root()

    def create_et(self):
        return et.parse(self.path)

    def get_root(self):
        return self.ET.getroot()

    def get_parent(self, tag):
        return self.root.find(tag)

    @staticmethod
    def get_child_by_parent_tag(parent, tag):
        return parent.find(tag)


if __name__ == '__main__':
    xml = XMLService('../../files_xml/archivo-prueba-1.xml')
    maquetas = xml.get_parent("maquetas")
    print(maquetas)
    for el in maquetas:
        print(el)
        print(xml.get_child_by_parent_tag(el, "nombre"))
        for child in el:
            print(child.tag)
