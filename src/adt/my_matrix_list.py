from src.adt.my_list import MyList
from src.adt.node import Node


class MyMatrixList(MyList):

    def __init__(self, head=None):
        super().__init__(head=head)

    def append_next(self, data):
        if not data:
            Exception('The data value cannot be empty')
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(self.head.data)
            return
        if self.head.next:
            self.head.next = new_node
            print(self.head.next.data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        print(current_node.next.data)

    def append_down(self, data):
        if not data:
            Exception('The data value cannot be empty')
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(self.head.data)
            return
        if self.head.down:
            self.head.down = new_node
            print(self.head.down.data)
            return
        current_node = self.head
        while current_node.down:
            current_node = current_node.down
        current_node.down = new_node
        print(current_node.down.data)

    def clear_list(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        pass

    def display_list(self):
        pass

    def get_node_data_by_index(self):
        pass

    def search_node_data(self, search_value):
        pass


if __name__ == '__main__':
    my_list = MyMatrixList()
    my_list.append_next(12)
    my_list.append_next(123)
    my_list.append_next(125)
    my_list.append_next(77)
    my_list.append_down(78)
    my_list.append_down(55)
    my_list.append_down(103)
    my_list.append_down(505)

