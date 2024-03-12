from src.adt.my_list import MyList
from src.adt.node import Node


class MySimpleList(MyList):

    def __init__(self, head=None):
        super().__init__(head=head)

    def append(self, data):
        if not data:
            Exception('The data value cannot be empty')
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return new_node.data
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return new_node.data

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        if self.is_empty():
            print('The simple list is empty')
            return
        count = 0
        current_node = self.head
        while current_node.next:
            count += 1
            current_node = current_node.next
        return count


if __name__ == '__main__':
    my_simple_list = MySimpleList()
    print(my_simple_list.head)
    print(my_simple_list.append(1))
    print(my_simple_list.append(2))
