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
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def append_down(self, data):
        if not data:
            Exception('The data value cannot be empty')
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.down:
            current_node = current_node.down
        current_node.down = new_node
        new_node.up = current_node

    def append_column(self, data, row):
        if not data:
            Exception('The data value cannot be empty')
            return
        new_node = Node(data)
        current_row = row
        while current_row.next:
            current_row = current_row.next
        current_row.next = Node(data)
        new_node.prev = current_row

    def get_last_row(self):
        if not self.head:
            return
        current_down = self.head
        while current_down.down:
            current_down = current_down.down
        return current_down

    def clear_list(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        pass

    def display_list(self):
        if not self.head:
            raise Exception('The matrix list is empty')

        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                print(current_column.data, end=' ')
                current_column = current_column.next
            print()
            current_row = current_row.down

    def get_node_data_by_index(self):
        pass

    def search_node_data(self, search_value):
        pass


if __name__ == '__main__':
    patron1 = "**********-*-*---**-*-*-*-**---*-*-**-*-*-*-**-*-*-*-**-*---*-**-*-*-*-**-*-*---**********"
    patron2 = "123456789123456789123456789"
    my_matrix_list = MyMatrixList()
    for i in range(5):
        my_matrix_list.append_next(patron2[i])
    my_matrix_list.append_down(patron2[5])
    my_matrix_list.display_list()
    curr_row = my_matrix_list.get_last_row()
    print(curr_row.data)
    for i in range(6, 10):
        my_matrix_list.append_column(data=patron2[i], row=curr_row)
    my_matrix_list.display_list()
    curr_row = my_matrix_list.get_last_row()
    print(curr_row.up.data)





