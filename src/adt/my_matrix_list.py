from src.adt.my_list import MyList
from src.adt.node import Node
from src.services.matrix_service import MatrixService


class MyMatrixList(MyList):

    def __init__(self, head=None):
        super().__init__(head=head)

    def append(self, data, new_row=False):
        if not data:
            raise Exception('The data value cannot be empty')
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_row = self.get_last_row()
        if new_row:
            while current_row.down:
                current_row = current_row.down
            MatrixService.connect_vertical_nodes(node_up=current_row, node_down=new_node)
            return
        if current_row.up:
            previous_row = current_row.up
            while current_row.next:
                current_row = current_row.next
                previous_row = previous_row.next
            MatrixService.connect_horizontal_nodes(node_prev=current_row, node_next=new_node)
            MatrixService.connect_vertical_nodes(node_up=previous_row.next, node_down=new_node)
            return
        while current_row.next:
            current_row = current_row.next
        MatrixService.connect_horizontal_nodes(node_prev=current_row, node_next=new_node)

    def get_last_row(self):
        if not self.head:
            raise Exception('The matrix list is empty')
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
            raise Exception('The matrix list is empty, cannot display it')

        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                if current_column.next:
                    print(current_column.data, end=' ')
                if not current_column.next:
                    print(current_column.data, end='')
                current_column = current_column.next
            print()
            current_row = current_row.down

    def get_node_by_index(self, xi, yi):
        if xi <= 0 or yi <= 0:
            raise IndexError("Index must be greater than zero")
        if self.is_empty():
            raise Exception("The matrix list is empty, cannot display it")
        if self.head and xi == 1 and yi == 1:
            return self.head
        count_x = 1
        count_y = 1
        current_node = self.head
        if self.head and xi == 1 and yi > 1:
            while current_node and count_y < yi:
                count_y += 1
                current_node = current_node.down
                if count_y == yi:
                    return current_node
                if current_node.down is None:
                    raise IndexError("Not enough elements in vertical direction...")
        if self.head and yi == 1 and xi > 1:
            while current_node and count_x < xi:
                count_x += 1
                current_node = current_node.next
                if count_x == xi:
                    return current_node
                if current_node.next is None:
                    raise IndexError("Not enough elements in horizontal direction...")
        while current_node.next and count_x < xi:
            count_x += 1
            current_node = current_node.next
            if count_x == xi:
                while current_node.down and count_y < yi:
                    count_y += 1
                    current_node = current_node.down
                    if count_y == yi:
                        return current_node
                    if current_node.down is None:
                        raise IndexError("Not enough elements in vertical direction...")
            if current_node.next is None:
                raise IndexError("Not enough elements in horizontal direction...")

    def get_node_data_by_index(self, xi, yi):
        if xi <= 0 or yi <= 0:
            raise IndexError("Index must be greater than zero")
        if self.is_empty():
            raise Exception("The matrix list is empty, cannot display it")
        if self.head and xi == 1 and yi == 1:
            return self.head.data
        count_x = 1
        count_y = 1
        current_node = self.head
        if self.head and xi == 1 and yi > 1:
            while current_node and count_y < yi:
                count_y += 1
                current_node = current_node.down
                if count_y == yi:
                    return current_node.data
                if current_node.down is None:
                    raise IndexError("Not enough elements in vertical direction...")
        if self.head and yi == 1 and xi > 1:
            while current_node and count_x < xi:
                count_x += 1
                current_node = current_node.next
                if count_x == xi:
                    return current_node.data
                if current_node.next is None:
                    raise IndexError("Not enough elements in horizontal direction...")
        while current_node.next and count_x < xi:
            count_x += 1
            current_node = current_node.next
            if count_x == xi:
                while current_node.down and count_y < yi:
                    count_y += 1
                    current_node = current_node.down
                    if count_y == yi:
                        return current_node.data
                    if current_node.down is None:
                        raise IndexError("Not enough elements in vertical direction...")
            if current_node.next is None:
                raise IndexError("Not enough elements in horizontal direction...")

    def search_node_data(self, search_value):
        if not self.head:
            raise Exception('The matrix list is empty, cannot display it')

        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                if current_column.__eq__(search_value):
                    return current_column
                current_column = current_column.next
            current_row = current_row.down
        return None

    def update_node_data_by_index(self, xi, yi, value):
        if xi <= 0 or yi <= 0 or not value:
            raise IndexError("Index must be greater than zero or value is None")
        if self.is_empty():
            raise Exception("The matrix list is empty, cannot display it")
        if self.head and xi == 1 and yi == 1:
            self.head.data = value
        count_x = 1
        count_y = 1
        current_node = self.head
        if self.head and xi == 1 and yi > 1:
            while current_node and count_y < yi:
                count_y += 1
                current_node = current_node.down
                if count_y == yi:
                    current_node.data = value
                if current_node.down is None:
                    raise IndexError("Not enough elements in vertical direction...")
        if self.head and yi == 1 and xi > 1:
            while current_node and count_x < xi:
                count_x += 1
                current_node = current_node.next
                if count_x == xi:
                    current_node = value
                if current_node.next is None:
                    raise IndexError("Not enough elements in horizontal direction...")
        while current_node.next and count_x < xi:
            count_x += 1
            current_node = current_node.next
            if count_x == xi:
                while current_node.down and count_y < yi:
                    count_y += 1
                    current_node = current_node.down
                    if count_y == yi:
                        current_node.data = value
                        return
                    if current_node.down is None:
                        raise IndexError("Not enough elements in vertical direction...")
            if current_node.next is None:
                raise IndexError("Not enough elements in horizontal direction...")


if __name__ == '__main__':
    patron1 = "**********-*-*---**-*-*-*-**---*-*-**-*-*-*-**-*-*-*-**-*---*-**-*-*-*-**-*-*---**********"
    patron2 = "132456789"
    my_matrix_list = MyMatrixList()
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 0:
                my_matrix_list.append(patron2[count], new_row=True)
                count += 1
                continue
            my_matrix_list.append(patron2[count])
            count += 1
    my_matrix_list.display_list()
    print(my_matrix_list.get_node_data_by_index(xi=1, yi=3))
    print(my_matrix_list.search_node_data("9"))
    my_matrix_list.update_node_data_by_index(2, 2, "6")
    my_matrix_list.display_list()
    print(my_matrix_list.get_node_data_by_index(2, 2))
